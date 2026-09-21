#"Dyrepark"

animals_in_park = [
    {
        "mammal": True,
        "species": "African Lion",
        "age": 4,
        "birthplace": "Africa",
        "vaccinated": True
    },
    {
        "mammal": True,
        "species": "Zebra",
        "age": 2,
        "birthplace": "Africa",
        "vaccinated": False
    },
    {
        "mammal": True,
        "species": "Giraffe",
        "age": 5,
        "birthplace": "Africa",
        "vaccinated": True
    },
    {
        "mammal": True,
        "species": "Elephant",
        "age": 10,
        "birthplace": "Africa",
        "vaccinated": True
    },
]
print(animals_in_park)
for animal in animals_in_park:
    print(f"Animals in the list: \n{animal['species']}")
    print(f" Mammal: {animal["mammal"]}\n Age:{animal["age"]}")