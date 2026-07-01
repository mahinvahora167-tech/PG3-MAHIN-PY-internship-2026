product={
    "pen":20,
    "book":150,
    "bag":1000,
    "bottle":500,
    "pencil":10
}
above_100={product:price for product,price in product.items()if price>100}

print("product priced above 100:")
print(above_100)