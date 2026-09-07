with open("uge37extraleg.txt", 'w') as fil:
    fil.write("Sanne, Danmark\n")
    fil.write("Klaus, Danmark\n")
    fil.close()
with open("uge37extraleg.txt", 'r') as fil:
    linjer = [linje.strip() for linje in fil.readlines()]
print(linjer)