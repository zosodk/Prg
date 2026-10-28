#Brugt pizza funktionen fra bogen og omdøbt den til sandwich

def make_sandwich(*ingredients):
    """Print the list of ingredients that have been requested."""
    print(f"The sandwich is made with:")
    for ingredient in ingredients:
        print(f"    Ingredient: {ingredient.title()}")
make_sandwich('ham')
make_sandwich('ham', 'cheese', 'onions')
make_sandwich('chicken', 'bacon', 'lettuce')