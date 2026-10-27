
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Sales Excel Dataset",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

root.destroy()

if file_path:
    data = pd.read_excel(file_path, sheet_name="Sales")

    data["Month_sales"] = pd.to_datetime(
        data["Month_sales"], errors="coerce"
    )
    data["Total"] = pd.to_numeric(
        data["Total"], errors="coerce"
    )

    data = data.dropna(subset=["Month_sales", "Total"])

    monthly_sales = data.groupby(
        data["Month_sales"].dt.to_period("M")
    )["Total"].sum()

    print("\nMonthly Sales:")
    print(monthly_sales.to_string())

    plt.figure(figsize=(10, 5))
    plt.plot(
        monthly_sales.index.astype(str),
        monthly_sales.values,
        marker="o"
    )
    plt.title("Monthly Sales - Line Plot")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(
        monthly_sales.index.astype(str),
        monthly_sales.values
    )
    plt.title("Monthly Sales - Scatter Plot")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(
        monthly_sales.index.astype(str),
        monthly_sales.values
    )
    plt.title("Monthly Sales - Bar Plot")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("No file selected.")
