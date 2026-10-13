
import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

# Select the dataset
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Fuel Efficiency Dataset",
    filetypes=[("CSV files", "*.csv")]
)

root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    efficiency = data[
        "highway_mpg(Fuel Efficiency)"
    ].to_numpy(dtype=float)

    average = np.mean(efficiency)

    print("Average Fuel Efficiency:",
          round(average, 2), "MPG")

    model_avg = data.groupby(
        ["make", "model"]
    )["highway_mpg(Fuel Efficiency)"].mean()

    print("\nAvailable car models (first 10):")
    for make, model in model_avg.index[:10]:
        print(make, model)

    make1 = input("\nEnter first car make: ").strip().lower()
    model1 = input("Enter first car model: ").strip().lower()

    make2 = input("Enter second car make: ").strip().lower()
    model2 = input("Enter second car model: ").strip().lower()

    model_avg.index = pd.MultiIndex.from_tuples(
        [(str(a).lower(), str(b).lower())
         for a, b in model_avg.index],
        names=["make", "model"]
    )

    car1 = (make1, model1)
    car2 = (make2, model2)

    if car1 in model_avg.index and car2 in model_avg.index:
        mpg1 = model_avg.loc[car1]
        mpg2 = model_avg.loc[car2]

        print("\nFirst car average:", round(mpg1, 2), "MPG")
        print("Second car average:", round(mpg2, 2), "MPG")

        if mpg1 != 0:
            improvement = ((mpg2 - mpg1) / mpg1) * 100
            print("Percentage change:",
                  round(improvement, 2), "%")
        else:
            print("Cannot calculate percentage change.")
    else:
        print("Car model not found. Check the make and model names.")

else:
    print("No dataset selected.")
