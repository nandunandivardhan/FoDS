
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Temperature and Rainfall Dataset",
    filetypes=[("CSV files", "*.csv")]
)

root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    data["Date"] = pd.to_datetime(
        dict(year=data["Year"], month=data["Month"], day=1),
        errors="coerce"
    )

    data = data.dropna(subset=["Date", "tem", "rain"])
    data = data.sort_values("Date")

    print("Total records:", len(data))
    print("\nFirst five records:")
    print(data[["Month", "Year", "tem", "rain"]].head().to_string(index=False))

    plt.figure(figsize=(12, 5))
    plt.plot(data["Date"], data["tem"], marker="o", markersize=2)
    plt.title("Monthly Temperature - Line Plot")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.scatter(data["Date"], data["rain"], s=12)
    plt.title("Monthly Rainfall - Scatter Plot")
    plt.xlabel("Year")
    plt.ylabel("Rainfall")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("\nResult: Temperature line plot and rainfall scatter plot generated.")

else:
    print("No file selected.")
