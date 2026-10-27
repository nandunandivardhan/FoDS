
import pandas as pd
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

    data["quantity"] = pd.to_numeric(
        data["quantity"], errors="coerce"
    )


    data = data.dropna(
        subset=["order_date", "quantity", "product_name"]
    )


    latest_date = data["order_date"].max()
    start_date = latest_date.to_period("M").start_time


    monthly_data = data[
        (data["order_date"] >= start_date) &
        (data["order_date"] <= latest_date)
    ]


    top_5 = (
        monthly_data.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("Month analyzed:", start_date.strftime("%B %Y"))
    print("\nTop 5 Products Sold:")
    print(top_5.to_string())

else:
    print("No dataset selected.")
