import pandas as pd

data = {
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor", "Mouse"],
    "Price": [55000, 25000, 3000, 2000, 15000, 800],
    "Category": ["Electronics", "Electronics", "Audio", "Accessories", "Electronics", "Accessories"],
    "Quantity": [10, 20, 50, 30, 15, 100],
    "Rating": [4.5, 4.3, 4.1, 4.0, 4.6, 3.9]
}

df = pd.DataFrame(data)

print("Cheapest Product:")
print(df.loc[df["Price"].idxmin()])