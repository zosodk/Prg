current_users = ['man', 'tir', 'ons', 'tor', 'fre']
new_users = ['mand', 'tirs', 'ons', 'tors', 'fre']
index = 0

for index in range(len(current_users)):
    for user in new_users:
        if user == current_users[index]:
            print(f"Brugeren {user} findes i listen!")

# simplificeringsforslag
beskeder = [f"Brugeren {user} findes i listen!" for user in new_users if user in current_users]

print('\n'.join(beskeder))