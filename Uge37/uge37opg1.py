#Opgaver på klassen
#En regning på en restaurant skal deles i tre lige store dele inkl drikkepenge.
# Hent input og konverter med det samme
people = int(input("Hvor mange personer er I?: "))
total_price = float(input("Hvad er den samlede pris?: "))
percent_of_tip = float(input("Indtast drikkepenge i procent (%): "))

# Beregn det hele
amount_to_tip = total_price * (percent_of_tip / 100)
total_inc_tip = total_price + amount_to_tip
tip_per_guest = amount_to_tip / people
per_guest = total_inc_tip / people

# Byg listen med input og en for løkke med range på antallet af gæster
names = [input(f"Indtast navnet på gæst {i+1}: ") for i in range(people)]

# Udskriv resultater med 2 decimaler
print(f"\nRegningen lyder på: {total_price:.2f} kr.")
print(f"Samlede drikkepenge: {amount_to_tip:.2f} kr.")
print(f"Drikkepenge pr. gæst: {tip_per_guest:.2f} kr.")
print(f"Samlet beløb inkl. drikkepenge: {total_inc_tip:.2f} kr.\n")

#Skriv beløb pr navn
for name in names:
    print(f"{name} skal betale: {per_guest:.2f} kr.")



