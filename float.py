# Make a calculator that also uses floats
# Declare variables
# x = input("What's x? ")
# y = input("What's y? ")
# x = int(input("WHat's x? "))
# y = int(input("What's y? "))
x = float(input("WHat's x? "))
y = float(input("What's y? "))

# z = int(x) + int(y)

# Print output
# print(z)
# Use round to take care of really large numbers
# z = round(x + y)
# z  = round(x / y, 2)
z = x / y

# Add commas to longer numbers
# print(f"{z:,}")

# print(x + y)
print(f"{z:.2f}")