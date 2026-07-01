mode="global mode"

def outer_function():
    mode="outer mode"

    def inner_function():
         mode="inner mode"

    print("local scope(inner function):",mode)
    inner_function()
    print("enclosing scope(outer function):",mode)
outer_function()    
print("global scope:",mode)