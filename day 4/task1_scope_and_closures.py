count=0

def call_counter():
    global count
    count += 1
    print("function called",count,"time(mahin)")
call_counter()
call_counter()
call_counter()
call_counter()
call_counter()

print("\nfinal count=",count)
