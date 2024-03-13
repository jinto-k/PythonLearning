"""
Adding to learn exceptions
"""
try:
    age = int(input("Enter age: "))
    income = 2000
    risk = income / age
    print(risk)

except ValueError:
    print("invalid value ")

except ZeroDivisionError:
    print("age can't be zero")
