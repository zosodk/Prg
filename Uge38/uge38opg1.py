# Opgave 5.3, 5.4, 5.5
#alien_color = "blue"
#print("You have been spotted!")
#if alien_color == "green":
#    print("You have earned 5 points!")
#elif alien_color == "yellow":
#    print("You have earned 10 points!")
#else:
#    print("You have earned 15 points!")
#print("The End!")
alien_color = "farve"
while alien_color !=" " or alien_color != "stop":
    alien_color = input("Type a color:\n")
    alien_color = alien_color.lower()

    match alien_color:
        case "green":
            print("You have earned 5 points!")
        case "yellow":
            print("You have earned 10 points!")
        case "red":
            print("You have earned 15 points!")
        case "blue" | "purple":
            print("You have earned 20 points!")
        case "stop":
            break
        case _:
            print("You have earned 0 points!")