import time
def time_it(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("time taken:",round(end-start,5),"seconds")
    return wrapper
@time_it
def calculate_sum():
    total=0
    for i in range(1,1000001):
        total+=i
    print("sum:",total)
calculate_sum()