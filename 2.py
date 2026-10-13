import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Product Dataset",
    filetypes=[("CSV files", "*.csv")]
)

if file_path:
    data = pd.read_csv(file_path)

    prices = data["Price"].to_numpy(dtype=float)
    average_price = np.mean(prices)

    print("Number of product records:", len(prices))
    print("Average product price:", round(average_price, 2))
else:
    print("No dataset selected.")

root.destroy()
