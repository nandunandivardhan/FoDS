import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Sales Dataset",
    filetypes=[("CSV files", "*.csv")]
)

if file_path:
    data = pd.read_csv(file_path)

    data["Month_sales"] = pd.to_datetime(
        data["Month_sales"], format="%B %Y"
    )

    monthly_sales = data.groupby("Month_sales")["Total"].sum()
    monthly_sales = monthly_sales.sort_index()

    quarterly_sales = monthly_sales.groupby(
        monthly_sales.index.quarter
    ).sum()

    sales_data = np.array([
        quarterly_sales.get(q, 0) for q in range(1, 5)
    ])

    print("Quarter 1 sales:", round(sales_data[0], 2))
    print("Quarter 2 sales:", round(sales_data[1], 2))
    print("Quarter 3 sales:", round(sales_data[2], 2))
    print("Quarter 4 sales:", round(sales_data[3], 2))
    print("Total yearly sales:", round(np.sum(sales_data), 2))

    if sales_data[0] != 0:
        percentage = (
            (sales_data[3] - sales_data[0])
            / sales_data[0]
        ) * 100

        print("Percentage change from Q1 to Q4:",
              round(percentage, 2), "%")
    else:
        print("Cannot calculate percentage change because Q1 sales are zero.")

else:
    print("No dataset selected.")

root.destroy()
