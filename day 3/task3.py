

unique_order=[]

for n1 in n:
        if n1 not in unique_order:
            unique_order.append(n1)
print("original values:",n)
print("after removing duplicate values list:",unique_order)