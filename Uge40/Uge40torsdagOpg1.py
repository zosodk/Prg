#OPGAVE 1 – KONTROL AF LOGIN-FORSØG
#Programmet skal blive ved med at spørge, indtil brugeren skriver:
#quit
#Eksempel:
#Enter number of failed logins or quit: 2
#2 failed login attempts
#Enter number of failed logins or quit: 7
#Warning: Many failed login attempts
#Enter number of failed logins or quit: quit
#Program stopped
#Programmet skal kontrollere brugerens input.
#Kun heltal mellem 0 og 20 er gyldige.
#Hvis brugeren skriver tekst i stedet for et tal, skal programmet skrive:
#Invalid input
#Hvis brugeren skriver et tal mindre end 0 eller større end 20, skal programmet skrive:
#Number must be between 0 and 20
#Hvis tallet er 5 eller højere, skal programmet skrive en advarsel:
#Warning: Many failed login attempts
#Ellers udskrives antallet af login-forsøg.

while True:
    console = input("Enter number of failed login attempts: ")
    if console.lower() == "quit":
        break
    if console.isdigit():
        console = int(console)
        if console >= 0 and console <= 20:
            print(f"Valid input: {console}")
        else:
            print(f"Number out of range (0-20): {console}")
    else:
        print(f"Not a number: {console}")
print(f"You chose to quit the program with: {console}")


