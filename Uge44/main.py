from functions import connect_to_db, create_table, insert_student, fetch_all_students

def main():
    # 1. Forbind til databasen
    conn = connect_to_db("students.db")

    if conn:
        # 2. Sørg for at tabellen eksisterer
        create_table(conn)

        # 3. Indsæt en test-elev (hvis du vil prøve det)
        # Fjern '#' for at aktivere denne linje
        insert_student(conn, "Anders Jensen", 20, 8.5)

        # 4. Hent alle elever
        students = fetch_all_students(conn)

        print("\nListe over alle studerende:")
        for student in students:
            print(f"ID: {student[0]} | Navn: {student[1]} | Alder: {student[2]} | Karakter: {student[3]}")

        # Luk forbindelsen når vi er færdige
        conn.close()
    else:
        print("Kunne ikke oprette forbindelse.")

if __name__ == "__main__":
    main()
