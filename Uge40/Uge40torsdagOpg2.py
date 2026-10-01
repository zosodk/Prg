#OPGAVE 2 – KONTROL AF PORTNUMRE
#Et portnummer i TCP/IP kan være mellem 1 og 65535.
#Lav et program, som gentagne gange spørger brugeren:
#Enter port number or quit:
#Programmet skal stoppe, når brugeren skriver:
#quit
#Kontrollér først, om input er et tal.
#Hvis det ikke er et tal, udskrives:
#Invalid input
#Hvis det er et tal, skal det konverteres til int.
#Kontrollér derefter, om tallet ligger mellem 1 og 65535.
#Hvis det ikke gør, udskrives:
#Invalid port number
#Opret denne tuple:
#common_ports = (22, 80, 443)
#Hvis det indtastede portnummer findes i common_ports, skal programmet skrive:
#Common port
#Ellers skal programmet skrive:
#Other valid port
common_ports = (22, 80, 443)
while True:
    console = input("Enter port number between 1-65535 or quit: ")
    if console.lower() == "quit":
        break
    if console.isdigit():
        console = int(console)
        if console >= 1 and console <= 65535:
            #print(f"Valid portnumber: {console}")
            if console not in common_ports:
                print(f"Other port number: {console}")
            else:
                print(f"Common port number: {console}")
        else:
            print(f"Port number out of range (1-65535): {console}")
    else:
        print(f"Not a port number: {console}")
print(f"You chose to quit the program with: {console}")