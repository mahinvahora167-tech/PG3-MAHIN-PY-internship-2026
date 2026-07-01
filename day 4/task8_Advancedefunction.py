def require_positive(func):
    def wrapper(a,b):
        if a>0 and b>0:
             return func(a,b)
        else:
            print("error:both numbers must be positive")
        return wrapper
    
@require_positive
def divide(a,b):
    print("division result=",a/b)

divide(21,5)
divide(-2,5)
