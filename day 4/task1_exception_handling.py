def safe_division(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "error: division by zero is not allowed."
    except TypeError:
        return "error: please enter numberic values only."
    
print(safe_division(20,2))
print(safe_division(20,0))
print(safe_division(20,"5"))