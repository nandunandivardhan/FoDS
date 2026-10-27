
import pandas as pd
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Question 8 Dataset",
    filetypes=[("CSV files", "*.csv")]
)

root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    data["Month_sales"] = pd.to_datetime(
        data["Month_sales"],
        format="mixed",
        errors="coerce"
    )

    data["Quantity_Sold"] = pd.to_numeric(
        data["Quantity_Sold"], errors="coerce"
    )

    data = data.dropna(
        subset=["Month_sales", "Quantity_Sold", "Product_ID"]
    )

    latest_month = data["Month_sales"].max()

    monthly_data = data[
        (data["Month_sales"].dt.year == latest_month.year) &
        (data["Month_sales"].dt.month == latest_month.month)
    ]


    top_products = (
        monthly_data.groupby(
            ["Product_ID", "Product_Name"]
        )["Quantity_Sold"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("Month analyzed:", latest_month.strftime("%B %Y"))
    print("\nTop 5 Products Sold:")
    print(top_products.to_string())

else:
    print("No dataset selected.")
