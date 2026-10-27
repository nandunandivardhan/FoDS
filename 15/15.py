
import pandas as pd
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Question 15 Dataset",
    filetypes=[("CSV files", "*.csv")]
)
root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    # Convert likes to numeric values
    data["Likes"] = pd.to_numeric(
        data["Likes"], errors="coerce"
    )

    likes = data["Likes"].dropna().astype(int)

    # Calculate frequency distribution
    frequency = likes.value_counts().sort_index()

    print("Total posts with valid likes:", len(likes))
    print("Unique like counts:", len(frequency))

    print("\nFrequency Distribution of Likes")
    print("--------------------------------")
    print(frequency.to_string())

    print("\nResult: Likes frequency distribution calculated successfully.")
else:
    print("No file selected.")
