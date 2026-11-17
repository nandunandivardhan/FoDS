
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from scipy import stats

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Exp18 Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if file_path:

    data = pd.read_csv(file_path)

    print("\n========== DATASET ==========")
    print(data.head(10))

    print("\nTotal number of records:", len(data))

    required_columns = ["Age", "BodyFat"]

    if all(col in data.columns for col in required_columns):


        data["Age"] = pd.to_numeric(
            data["Age"], errors="coerce"
        )

        data["BodyFat"] = pd.to_numeric(
            data["BodyFat"], errors="coerce"
        )

        data = data.dropna(
            subset=["Age", "BodyFat"]
        )

        # Statistical analysis
        print("\n========== STATISTICAL ANALYSIS ==========")

        for column in ["Age", "BodyFat"]:

            print("\nVariable:", column)
            print("--------------------------------")

            print("Mean:",
                  round(data[column].mean(), 2))

            print("Median:",
                  round(data[column].median(), 2))

            print("Standard Deviation:",
                  round(data[column].std(), 2))

        # Boxplots
        plt.figure(figsize=(8, 5))

        data[["Age", "BodyFat"]].boxplot()

        plt.title("Boxplots of Age and Body Fat")
        plt.ylabel("Values")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Scatter plot
        plt.figure(figsize=(8, 5))

        plt.scatter(
            data["Age"],
            data["BodyFat"],
            alpha=0.7
        )

        plt.xlabel("Age")
        plt.ylabel("Body Fat (%)")
        plt.title("Scatter Plot: Age vs Body Fat")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Q-Q plot for Age
        plt.figure(figsize=(7, 5))

        stats.probplot(
            data["Age"],
            dist="norm",
            plot=plt
        )

        plt.title("Q-Q Plot of Age")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Q-Q plot for Body Fat
        plt.figure(figsize=(7, 5))

        stats.probplot(
            data["BodyFat"],
            dist="norm",
            plot=plt
        )

        plt.title("Q-Q Plot of Body Fat")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        print("\nAnalysis completed successfully!")

    else:
        print("Required columns Age and BodyFat not found.")

else:
    print("No file selected.")
