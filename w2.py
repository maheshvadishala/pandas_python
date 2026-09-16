import pandas as pd

data = {
    "City": ["Rajahmundry", "Hyderabad", "Chennai", "Delhi", "Mumbai", "Bangalore"],
    "Temperature": [36, 39, 37, 34, 32, 28],
    "Humidity": [75, 60, 70, 45, 80, 65],
    "Rainfall": [120, 80, 150, 40, 200, 100]
}

df = pd.DataFrame(data)

print("Hottest City:")
print(df.loc[df["Temperature"].idxmax()])