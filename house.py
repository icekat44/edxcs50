name = input("What's your name? ")
# Included comments only to show progression of learning process
# ordinarily would not include all of the below.
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
#    case "Hermione":
#        print("Griffindor")
#    case "Ron":
#        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who??")

# if name == "Harry":
#     print("Griffindor")
# elif name == "Hermione":
#     print("Griffindor")
# elif name == "Ron":
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?!!?")