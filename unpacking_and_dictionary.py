example = (1, 2, 3, 4)
x, y, z, a = example  # unpacking


customer ={
    "name": "john smith",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Levi"  # to change a value (don't mind the warning above)
customer["pet"] = "dog"
print(customer["pet"])
print(customer.get("age"))

# the major difference between these two ways of getting a value from a dictionary
# using key is that, the first one will give an error when the key is invalid.
# the second one returns None

print(customer.get("birthdate", "Jan 1 1990"))  # A default value can be given for an invalid key

# following is an example with dictionaries
user_num = input("phone: ")

output = ""
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

for num in user_num:
    output += numbers.get(num, "!") + " "

print(output)

# following is an emoji converter using dictionaries

message = input("> ")
words = message.split(" ")
output_emoji = ""
emojis = {
    ":)": "😀",
    ":(": "🥲"
}

for word in words:
    output_emoji += emojis.get(word,word) + " "

print(output_emoji)

