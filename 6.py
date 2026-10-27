
import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Grocery Purchase Dataset",
    filetypes=[("CSV files", "*.csv")]
)

root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    prices = data["Item_Price"].to_numpy(dtype=float)
    quantities = data["Quantity"].to_numpy(dtype=float)
    discounts = data["Discount_Rate_Percent"].to_numpy(dtype=float)
    taxes = data["Tax_Rate_Percent"].to_numpy(dtype=float)

    subtotal = prices * quantities

    discount_amount = subtotal * discounts / 100

    discounted_amount = subtotal - discount_amount


    tax_amount = discounted_amount * taxes / 100

    final_amount = discounted_amount + tax_amount

    print("Number of items:", len(data))
    print("Subtotal:", round(np.sum(subtotal), 2))
    print("Total discount:", round(np.sum(discount_amount), 2))
    print("Total tax:", round(np.sum(tax_amount), 2))
    print("Final grocery purchase cost:",
          round(np.sum(final_amount), 2))

else:
    print("No dataset selected.")
