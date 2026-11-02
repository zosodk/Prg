import matplotlib.pyplot as plt
filename = "animal_counts_large.csv"

animals = []
amounts = []

with open(filename, "r", encoding="utf-8") as fil:
    # Springer header-linjen over:
    next(fil)

    for line in fil:
        # Fjerner linjeskift og splitter ved komma
        parts = line.strip().split(",")
        if parts:
            animals.append(parts[0].strip())
            amounts.append(int(parts[1].strip()))

plt.pie(amounts, labels=animals,autopct="%1.1f%%", shadow=False, startangle=90)
plt.title("Animals")
#plt.xlabel("Animals")
#plt.ylabel("Amount")
#plt.scatter(animals, amounts)
#plt.bar(animals, amounts)
#plt.hist(amounts)
plt.show()

