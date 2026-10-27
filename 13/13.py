
import re
from collections import Counter
from tkinter import Tk, filedialog

# Select a text file
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Text File",
    filetypes=[("Text files", "*.txt")]
)

root.destroy()

if file_path:
    # Read the text file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Convert to lowercase and extract words
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    # Calculate word frequency
    word_frequency = Counter(words)

    print("\nTotal words:", len(words))
    print("\nWord Frequency Distribution:")
    print("-" * 35)

    for word, count in sorted(word_frequency.items()):
        print(f"{word}: {count}")

    print("\nResult: Word frequency distribution calculated successfully.")

else:
    print("No file selected.")
