def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"error: missing required key: {e}")
    else:
        print("order details:")
        print(f"item: {item}")
        print(f"price:${price}")
    finally:
        print("processing complete")

process_order({"item": "laptop", "price": 999.99})

print()

process_order({"item": "mouse"})