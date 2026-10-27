
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Sales Dataset",
    filetypes=[("CSV files", "*.csv")]
)

root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    data["order_date"] = pd.to_datetime(
        data["order_date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    data["sales"] = pd.to_numeric(
        data["sales"].astype(str).str.replace(",", ""),
        errors="coerce"
    )

    data = data.dropna(subset=["order_date", "sales"])

    data["Month"] = data["order_date"].dt.to_period("M")
    monthly_sales = data.groupby("Month")["sales"].sum()

    print("Monthly Sales:")
    print(monthly_sales)

    plt.figure(figsize=(12, 5))
    plt.plot(
        monthly_sales.index.astype(str),
        monthly_sales.values,
        marker="o"
    )
    plt.title("Monthly Sales - Line Plot")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(
        monthly_sales.index.astype(str),
        monthly_sales.values
    )
    plt.title("Monthly Sales - Bar Plot")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

else:
    print("No dataset selected.")
