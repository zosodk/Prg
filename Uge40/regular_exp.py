import re

def valider_email(email):
    # Matcher typiske email-formater (f.eks. navn@domæne.dk)
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(pattern, email))

def valider_dansk_telefonnummer(telefon):
    # Matcher præcis 8 tal
    pattern = r"^[0-9]{8}$"
    return bool(re.fullmatch(pattern, telefon))

def valider_postnummer(postnr):
    # Matcher præcis 4 tal (danske postnumre)
    pattern = r"^[0-9]{4}$"
    return bool(re.fullmatch(pattern, postnr))

def valider_adgangskode(password):
    # Mindst 8 tegn: mindst ét lille bogstav, ét stort bogstav og ét tal
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.fullmatch(pattern, password))

# Test af funktionerne
print(valider_email("bruger@eksempel.dk"))      # True
print(valider_email("ugyldig-email@.dk"))       # False

print(valider_dansk_telefonnummer("12345678"))  # True
print(valider_dansk_telefonnummer("12 34 56"))  # False (mellemrum er ikke tilladt i regex'en)

print(valider_adgangskode("Kodeord123"))        # True
print(valider_adgangskode("kodeord"))           # False (mangler stort bogstav og tal)