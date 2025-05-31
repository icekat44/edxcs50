# Create my own function called Hello

def main():
    name = input("What's your name? ").strip().title()
    hello(name)

# Define Hello function
def hello(to="World"):
    print("Hello,", to)


main()