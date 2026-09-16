import pandas as pd

data = {
    "Player": ["Virat", "Rohit", "Dhoni", "Gill", "Rahul", "Surya", "Pant"],
    "Team": ["RCB", "MI", "CSK", "GT", "LSG", "MI", "DC"],
    "Runs": [741, 550, 450, 890, 620, 700, 580],
    "Matches": [15, 14, 16, 15, 14, 15, 14],
    "Average": [53, 42, 38, 59, 48, 50, 44],
    "Strike Rate": [145, 138, 130, 155, 142, 150, 140]
}

df = pd.DataFrame(data)
print("\n4. Highest Strike Rate")
print(df.loc[df["Strike Rate"].idxmax()])