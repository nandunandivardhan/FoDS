
import pandas as pd
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Question 14 Dataset",
    filetypes=[("CSV files", "*.csv")]
)
root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    # Convert dates and ages
    data["Purchase_Date"] = pd.to_datetime(
        data["Purchase_Date"], errors="coerce"
    )
    data["Age"] = pd.to_numeric(
        data["Age"], errors="coerce"
    )

    # Find the latest purchase date
    latest_date = data["Purchase_Date"].max()

    if pd.isna(latest_date):
        print("No valid purchase dates found.")
    else:
        # Select purchases in the 30 days ending on latest_date
        start_date = latest_date - pd.Timedelta(days=29)

        recent = data[
            (data["Purchase_Date"] >= start_date) &
            (data["Purchase_Date"] <= latest_date)
        ].dropna(subset=["Age"])

        # Calculate age frequency
        age_frequency = (
            recent["Age"].astype(int)
            .value_counts()
            .sort_index()
        )

        print("Purchase period:", start_date.date(),
              "to", latest_date.date())
        print("Customers with valid ages:", len(recent))
        print("\nFrequency Distribution of Customer Ages")
        print("----------------------------------------")
        print(age_frequency.to_string())

        print("\nResult: Customer age frequency calculated successfully.")
else:
    print("No file selected.")
