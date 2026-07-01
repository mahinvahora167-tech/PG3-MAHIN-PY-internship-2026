def bulid_invoice(customer_name,*args,**kwargs):
    total=sum(args)

    print("Customer Name:",customer_name)
    print("Total Price:",total)
    print("Extra details:")
    for key,value in kwargs.items():
        print(key,":",value)

bulid_invoice("Shana",150,245,300,discount=50, tax=18)
