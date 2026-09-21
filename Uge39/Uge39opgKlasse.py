#Lav en dictionary med animals
animals = {
    "cat": "Fie",
    "dog": "Doggy",
    "bird": "Tweetie"
}
print(animals["cat"])

#get på dict's
dyr = animals.get("bird", "NotFound")
print(f"Fundet: {dyr}")

dyr = animals.get("fish", "NotFound")
print(f"Fundet: {dyr}")
#Looping
for key, value in animals.items():
    print(f"{key}: {value}")

#Set

for key, value in animals.items():
    print(f"Tilføjet: {key}: {value}")
