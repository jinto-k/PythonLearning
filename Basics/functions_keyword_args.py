def greet_user(first_name, last_name):
    print(f"{first_name} {last_name}")


greet_user("John", "smith")  # positional argument
greet_user(last_name="ackerman", first_name="levi")  # keyword arguments
greet_user("John", last_name="cena")  # keyword args should always be after positional args


def square(number):
    return number * number


result = square(3)
print(result)
