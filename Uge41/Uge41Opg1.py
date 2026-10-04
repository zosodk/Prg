import sqlite3
from pathlib import Path

# Definér filnavnet for SQLite-databasen (den gemmes i samme mappe som scriptet)
DB_FILE = "min_database.db"


def main():
  # 1. Opret forbindelse til databasen (hvis filen ikke findes, oprettes den automatisk)
  conn = sqlite3.connect(DB_FILE)

  # Sørg for at rækker returneres som dictionaries (nøgle-værdi par) i stedet for tupler
  conn.row_factory = sqlite3.Row

  # Opret en cursor til at udføre SQL-kommandoer
  cursor = conn.cursor()

  # 2. Opret tabeller (bruger 'IF NOT EXISTS' så scriptet kan køres flere gange)
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS kunder (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            navn TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordrer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kunde_id INTEGER,
            produkt TEXT NOT NULL,
            pris REAL,
            FOREIGN KEY (kunde_id) REFERENCES kunder (id)
        )
    """)

  # 3. Indsæt lidt data (bruger 'OR IGNORE' for at undgå fejl, hvis de allerede findes)
  cursor.execute(
      "INSERT OR IGNORE INTO kunder (navn, email) VALUES (?, ?)",
      ("Anna Hansen", "anna@example.com"),
  )
  cursor.execute(
      "INSERT OR IGNORE INTO kunder (navn, email) VALUES (?, ?)",
      ("Lars Jensen", "lars@example.com"),
  )

  # Hent kunde-id'erne til brug i ordrer
  cursor.execute("SELECT id, navn FROM kunder")
  kunder = cursor.fetchall()

  # Indsæt test-ordrer baseret på hvem der findes
  for kunde in kunder:
    if kunde["navn"] == "Anna Hansen":
      cursor.execute(
          "INSERT INTO ordrer (kunde_id, produkt, pris) VALUES (?, ?, ?)",
          (kunde["id"], "Mekanisk Tastatur", 799.00),
      )
      cursor.execute(
          "INSERT INTO ordrer (kunde_id, produkt, pris) VALUES (?, ?, ?)",
          (kunde["id"], "Trådløs Mus", 349.50),
      )
    elif kunde["navn"] == "Lars Jensen":
      cursor.execute(
          "INSERT INTO ordrer (kunde_id, produkt, pris) VALUES (?, ?, ?)",
          (kunde["id"], "Skærm 27\"", 2299.00),
      )

  # Husk at gemme (commit) ændringer til databasen
  conn.commit()

  # 4. Udvælg data og put det i en liste af dictionaries (ved hjælp af et JOIN)
  cursor.execute("""
        SELECT kunder.navn, kunder.email, ordrer.produkt, ordrer.pris
        FROM ordrer
        JOIN kunder ON ordrer.kunde_id = kunder.id
    """)

  # fetchall() henter alle rækker. Fordi vi satte row_factory, kan vi slå op med kolonnenavn.
  rækker = cursor.fetchall()
  ordrer_liste = []

  for række in rækker:
    # Konverter hver sqlite3.Row til en helt almindelig Python dictionary
    ordrer_liste.append({
        "kunde": række["navn"],
        "email": række["email"],
        "produkt": række["produkt"],
        "pris": række["pris"],
    })

  # 5. Luk forbindelsen pænt, når vi er færdige
  conn.close()

  # 6. Skriv resultatet ud på skærmen
  print("--- Hentede data fra SQLite-databasen ---")
  for i, ordre in enumerate(ordrer_liste, 1):
    print(
        f"Ordre {i}: {ordre['kunde']} ({ordre['email']}) købte"
        f" '{ordre['produkt']}' for {ordre['pris']} kr."
    )


if __name__ == "__main__":
  main()