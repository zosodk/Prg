#En firewall tillader kun trafik til bestemte porte.
#Gem de tilladte porte i en tuple:
#allowed_ports = (22, 80, 443)
#Lav en variabel:
#port = 443
#Undersøg med if og in, om port findes i allowed_ports.
#Programmet skal udskrive enten:
#Port is allowed
#eller:
#Port is blocked
#Afprøv programmet med:
#22 #25 #80 #443 #8080
#Ekstra: Lad brugeren indtaste portnummeret med input().
allowed_ports = (22, 80, 443)
allowedport = 443
for port in allowed_ports:
    if allowedport not in allowed_ports:
        print(f"Port {allowedport} is not allowed")
    else:
        print(f"Port {allowedport} is allowed")
        break
