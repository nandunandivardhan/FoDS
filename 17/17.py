
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re
from collections import Counter
import matplotlib.pyplot as plt

stop_words = {
    "the", "and", "is", "a", "an", "in", "on", "at",
    "to", "of", "for", "with", "was", "were", "are",
    "am", "be", "been", "being", "it", "this", "that",
    "i", "we", "you", "he", "she", "they", "my", "our",
    "your", "but", "or", "as", "from", "by", "not",
    "very", "too", "have", "has", "had", "do", "does",
    "did", "would", "could", "should", "will", "can"
}

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Customer Feedback CSV",
    filetypes=[("CSV Files", "*.csv")]
)

if file_path:
    data = pd.read_csv(file_path)

    if "feedback" not in data.columns:
        print("Error: feedback column not found!")
    else:
        text = " ".join(
            data["feedback"].dropna().astype(str)
        ).lower()

    
        text = re.sub(r"[^a-z\s]", " ", text)

        words = text.split()

        clean_words = [
            word for word in words
            if word not in stop_words
        ]

        word_frequency = Counter(clean_words)

        n = int(input("Enter the value of N: "))

        if n <= 0:
            print("Enter a positive number.")
        else:
            top_words = word_frequency.most_common(n)

            print("\nTOP", n, "MOST FREQUENT WORDS")
            print("--------------------------------")

            for word, count in top_words:
                print(word, ":", count)

            print("\nTotal words after preprocessing:",
                  len(clean_words))

            if top_words:
                words_list = [item[0] for item in top_words]
                counts = [item[1] for item in top_words]

                plt.figure(figsize=(10, 5))
                plt.bar(words_list, counts)

                plt.xlabel("Words")
                plt.ylabel("Frequency")
                plt.title("Top N Frequent Words in Customer Feedback")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

else:
    print("No file selected.")
