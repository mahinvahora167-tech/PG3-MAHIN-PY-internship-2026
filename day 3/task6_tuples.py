admin={"add","edit","delete","view"}
editor={"add","edit"}

required="add"

if required in editor:
    print("editor can perform action")
else:
    print("editor cannot perform action")