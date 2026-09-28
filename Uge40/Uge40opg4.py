#Vi kan repræsentere en simpel sikkerhedshændelse med en tuple:
#event = ("192.168.1.25", "failed_login", 5)
#Tuplen indeholder:
#IP-adresse
#Type af hændelse
#Antal forsøg
#Udskriv de tre værdier hver for sig.
#Lav derefter en betingelse:
#Hvis event[1] er "failed_login" og event[2] er mindst 3, skal programmet udskrive:
#Warning: Multiple failed login attempts
#Ekstra: Udskriv også den IP-adresse advarslen kommer fra.

event = ("192.168.1.25", "failed_login", 5)
for dimser in event:
    print(dimser)
if event[1] == "failed_login" and event[2] >= 3:
    print(f"Warning: Multiple failed login attempts from {event[0]}")