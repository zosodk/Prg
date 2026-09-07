countries = ["Germany", "France", "Italy","Spain","Portugal"]
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
    break
else :
    print("Ingen lande i listen!")
