weight = int(input("Enter weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == "l":
    new_weight = weight * 0.453592
    print(f"you are {new_weight} kilo")
elif unit.lower() == "k":
    new_weight = weight * 2.20462
    print(f"you are {new_weight} pounds")
else:
    print("what dude?")