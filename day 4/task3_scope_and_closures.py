def create_counter():
    count=0

    def counter():
        nonlocal count
        count+=1
        return counter
    return counter
counter1=create_counter()
counter2=create_counter()

print("counter 1 calls:")
print("first call=",counter1())
print("second call=",counter1())
print("third call=", counter1())
print("four call=",counter1())
print("fifth call=",counter1())

print("\ncounter 2 calls:")
print("firdt call=",counter2())
print("second call=",counter2())
print("third call=",counter2())