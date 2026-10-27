
import pandas as pd
from tkinter import Tk, filedialog
from collections import Counter
import re

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Question 13 Dataset",
    filetypes=[("CSV files", "*.csv")]
)
root.destroy()

if file_path:
    data = pd.read_csv(file_path)

    # Combine text from all rows
    all_text = " ".join(data["text"].dropna().astype(str))

    # Convert to lowercase and extract words
    words = re.findall(r"\b[a-zA-Z]+\b", all_text.lower())

    # Calculate word frequencies
    frequency = Counter(words)

    print("Total words:", len(words))
    print("Unique words:", len(frequency))
    print("\nWord Frequency Distribution")
    print("---------------------------")

    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")

    print("\nResult: Word frequency distribution calculated successfully.")
else:
    print("No file selected.")
