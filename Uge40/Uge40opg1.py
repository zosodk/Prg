#Opgave 1 Byer
#Lav en liste med mindst 8 forskellige byer.
#Brug slices til at udskrive:
#De første tre byer
#De sidste tre byer
#Tre byer fra midten
#Lav derefter et loop som kun gennemløber de første fire byer.
#Udskriv: I would like to visit Esbjerg
#for hver af de fire byer. (Det med gult skal jo skiftes ud for hver by

byer = ["Varde", "Esbjerg", "Bramming", "Ribe", "Guldager", "Tarp", "Jerne", "Hjerting"]
print(byer[0:3])
print()
print(byer[-3:])
print()
print(byer[3:6])
for by in byer[0:4]:
    print(f"I would like to visit {by}")