def get_element(my_list,index):
    try:
        return my_list[index]
    
    except IndexError:
        return None
    
number=[21,49,28,67,90]

print("output 1:",get_element(number,2))
print("output 2:",get_element(number,10))
    
