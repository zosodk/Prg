#6-1.
# Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each piece
#of information stored in your dictionary.

#Dictionary
poi = {
    "first_name": "Susanne",
    "last_name": "Schmidt",
    "age": 53,
    "city": "Varde"
}
for key, value in poi.items():
    print(f"{key}: {value}")
print("Opgave 6.1 slut - begynder liste med personer:\n")
#
persons = [
    {
        "first_name": "Susanne",
        "last_name": "Schmidt",
        "age": 53,
        "city": "Varde"
    },
    {
        "first_name": "Jens",
        "last_name": "Hansen",
        "age": 45,
        "city": "København"
    },
    {
        "first_name": "Lise",
        "last_name": "Andersen",
        "age": 32,
        "city": "Roskilde"
    }
]

for person in persons:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()