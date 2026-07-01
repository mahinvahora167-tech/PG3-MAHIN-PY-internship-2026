inventory={"pen":110,"notebook":50}

if"notebook" in inventory:
    inventory["notebook"]-= 1
    print("notebook sold")
else:
    print("notebook not found")

if"Bag" in inventory:
         inventory["bag"] -= 1
         print("bag sold")
else:
        print("bag not found")

print("updated inventory:")
print(inventory)