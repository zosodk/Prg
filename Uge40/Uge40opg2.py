#En IPv4-adresse består af fire tal.
#Opret IP-adressen 192.168.1.25 som en tuple:
#ip = (192, 168, 1, 25)
#Udskriv hele tuplen.
#Udskriv kun det første tal.
#Udskriv kun det sidste tal.
#Brug et for-loop til at udskrive alle fire tal.
#Prøv til sidst:
#ip[3] = 30 Hvad sker der? Forklar hvorfor.

ip = (192, 168, 1, 25)
print(ip)
print()
print(ip[0])
print()
print(ip[-1])
print()
print()
for octet in ip:
    print(octet)
#ip[3] = 30 ikke tilladt - immuterbar

