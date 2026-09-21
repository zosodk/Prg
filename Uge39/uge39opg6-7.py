#6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
#two new dictionaries representing different people, and store all three dictionar-
#ies in a list called people. Loop through your list of people. As you loop through
#the list, print everything you know about each person.

#6-1.
# Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each piece
#of information stored in your dictionary.

people = [
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

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()