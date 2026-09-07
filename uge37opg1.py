#Opgaver på klassen
#En regning på en restaurant skal deles i tre lige store dele inkl drikkepenge.
#Skriv Total
#Skriv drikkepenge på 15%
#Skriv Totalen
#Hver del personerne skal af med.
"""totalnette = float()
drikkepenge = float(0.15)
antalpersoner = int
total = float
drikkepenge+=1
total = totalnette * drikkepenge
anpart = total / antalpersoner
"""

guest1 = input("Indtast navnet på den første gæst?")
#debug
print("Første gæst hedder", guest1)
guest2 = input("Indtast navnet på den anden gæst?")
#debug
print("Anden gæst hedder", guest2)
guest3 = input("Indtast navnet på den tredje gæst?")
#debug
print("Tredje gæst hedder", guest3)
bill = input("Indtast regningens total?")
bill = float(bill)
print("Regningen er", bill)
print("Indtast drikkepengene som procent")
drikp = input("Drikkepenge % er")
drikp = int(drikp)
print("Drikkepenge i procenter er", drikp)
tip = bill * (drikp/100)
print("Drikkepengene udgør dette af regningr", tip)
total_amount = bill + tip
print("Regningen er", total_amount)
guest_amount = total_amount / 3
print("Hver gæst skal betale", round(guest_amount, 2))



