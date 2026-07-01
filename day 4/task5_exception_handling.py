class InvalidRangError(Exception):

    pass


while True:
    try:
        number = int(input("enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise InvalidRangError("number must be between 1 and 10.")
        
        print(f"valid input: {number}")
        break
    
    except ValueError:
        print("Ereoe: please enter a valid numeric value.")
    except InvalidRangError as e:
        print(f"Error: {e}")