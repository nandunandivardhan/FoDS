
import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select House Dataset",
    filetypes=[("CSV files", "*.csv")]
)

if file_path:
    data = pd.read_csv(file_path)

    house_data = data[["bedrooms", "price"]].to_numpy(
        dtype=float
    )

    selected_houses = house_data[
        house_data[:, 0] > 4
    ]

    if len(selected_houses) > 0:
        average_price = np.mean(selected_houses[:, 1])

        print("Number of houses with more than 4 bedrooms:",
              len(selected_houses))
        print("Average sale price:",
              round(average_price, 2))
    else:
        print("No houses with more than 4 bedrooms.")

else:
    print("No dataset selected.")

root.destroy()

