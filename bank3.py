import pandas as pd

data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Ravi", "Suresh", "Mahesh", "Priya", "Anil", "Kiran"],
    "Balance": [250000, 500000, 750000, 300000, 900000, 450000],
    "Loan": [200000, 600000, 400000, 700000, 300000, 550000],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Mumbai", "Chennai", "Hyderabad"]
}

df = pd.DataFrame(data)

print("Customers with Loans > ₹5 Lakh:")
print(df[df["Loan"] > 500000])