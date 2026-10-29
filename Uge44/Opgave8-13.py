#Kopi af opgaven fra bogen - modificeret til at indeholde min info
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    input: first - the first name of the user
           last - the last name of the user
           user_info - additional information about the user

    output: user_info - a dictionary containing all the information about the user
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Klaus', 'Hviid', lokation='Varde', hardyr='To katte', borsammenmed='Sanne')
print(user_profile)