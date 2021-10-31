PrimaryColors = set(["red", "blue","yellow"])

color = input("Type the color to see whethe it is a Primary one")

if color.lower() in PrimaryColors:
    print(color + " is a primary color")
else:
    print(color + " is Not a primary color")