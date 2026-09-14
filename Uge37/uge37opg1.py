#Opgaver på klassen
# En regning på en restaurant skal deles i tre lige store dele inkl drikkepenge.

# Hent input og konverter med det samme
antal_personer = int(input("Hvor mange personer er I?: "))
samlet_pris = float(input("Hvad er den samlede pris?: "))
drikkepenge_procent = float(input("Indtast drikkepenge i procent (%): "))

# Beregn det hele
drikkepenge_beloeb = samlet_pris * (drikkepenge_procent / 100)
samlet_inkl_drikkepenge = samlet_pris + drikkepenge_beloeb
drikkepenge_pr_gaest = drikkepenge_beloeb / antal_personer
beloeb_pr_gaest = samlet_inkl_drikkepenge / antal_personer

# Byg listen med input og en for løkke med range på antallet af gæster
navne = [input(f"Indtast navnet på gæst {i+1}: ") for i in range(antal_personer)]

# Udskriv resultater med 2 decimaler
print(f"\nRegningen lyder på: {samlet_pris:.2f} kr.")
print(f"Samlede drikkepenge: {drikkepenge_beloeb:.2f} kr.")
print(f"Drikkepenge pr. gæst: {drikkepenge_pr_gaest:.2f} kr.")
print(f"Samlet beløb inkl. drikkepenge: {samlet_inkl_drikkepenge:.2f} kr.\n")

# Skriv beløb pr navn
for navn in navne:
    print(f"{navn} skal betale: {beloeb_pr_gaest:.2f} kr.")


