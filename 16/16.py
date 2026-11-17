
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re
from collections import Counter

# Open file picker
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Customer Reviews Dataset",
    filetypes=[("CSV Files", "*.csv")]
)

if file_path:
    # Read dataset
    data = pd.read_csv(file_path)

    # Check review column
    if "Review" not in data.columns:
        print("Error: Review column not found!")
    else:
        # Combine all customer reviews
        text = " ".join(data["Review"].dropna().astype(str))

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation and numbers
        text = re.sub(r"[^a-z\s]", "", text)

        # Split into words
        words = text.split()

        # Calculate word frequency
        word_frequency = Counter(words)

        # Display results
        print("\nWORD FREQUENCY DISTRIBUTION")
        print("--------------------------------")

        for word, count in word_frequency.most_common():
            print(word, ":", count)

        print("\nTotal words:", len(words))
        print("Unique words:", len(word_frequency))

else:
    print("No file selected.")
