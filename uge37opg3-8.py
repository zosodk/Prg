countries = ["Germany", "France", "Italy","Spain","Portugal"]
persons = ["John", "Jane", "Bob", "Sue", "Allen"]
while len(countries) > 0:
    #print(countries[0:3])
    print("Lande soom indskrevet på listen: ")
    print(countries)
    print("Lande sorteret i udskrift:")
    print(sorted(countries))
    print("Lande som indskrevet på listen:")
    print(countries)
    print("Lande i listen i omvendt orden: ")
    countries.reverse()
    print(countries)
    print("Lande i listen i korrekt orden igen: ")
    countries.reverse()
    print(countries)
    print("Lande alfabetisk sorteret: ")
    countries.sort()
    print(countries)
    print("Lande omvendt alfabetisk sorteret: ")
    countries.sort(reverse=True)
    print(countries)
    for land in countries:
        if land == "France":
            print("France er i listen inde i if sætningen under gennemløb i en for løkke!")
        print ("Lande i listen inde i for løkken: ")
        print(countries)
    personer_lande = [list(par) for par in zip(persons, countries)]
    for i in range(len(personer_lande)):
        print (personer_lande[i][0] + " bor i " + personer_lande[i][1] + "!")

    break

else :
    print("Ingen lande i listen!")
