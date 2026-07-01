class InvalidAgeError(Exception):
    "custom exception for invalid age values."
    pass


def registar_user(age):
    if age < 0:
        raise InvalidAgeError("invalid age: age cannot be less than 0.")
    elif age > 120:
        raise InvalidAgeError("invalid age: age cannot be greater than 120.")
    return "user registerd successfully."

try:
     print(registar_user(25))
     print(registar_user(5))
except InvalidAgeError as e:
    print(e)

try:
    print(registar_user(150))
except InvalidAgeError as e:
    print(e)