import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import string

def analyze_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text to analyze.")
        return

    cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()

    char_with_spaces = len(text)
    char_without_spaces = len(text.replace(" ", ""))
    word_count = len(words)
    word_freq = Counter(words)

    most_common = word_freq.most_common(1)[0] if word_freq else ("None", 0)

    result = (
        f"Total Words: {word_count}\n"
        f"Characters (with spaces): {char_with_spaces}\n"
        f"Characters (without spaces): {char_without_spaces}\n"
        f"Most Repeated Word: '{most_common[0]}' ({most_common[1]} times)\n\n"
        f"Word Frequencies:\n"
    )

    for word, count in word_freq.items():
        result += f"{word}: {count}\n"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                input_text.delete("1.0", tk.END)
                input_text.insert(tk.END, data)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def save_report():
    report = output_text.get("1.0", tk.END).strip()
    if not report:
        messagebox.showwarning("Nothing to Save", "Please analyze some text first.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(report)
            messagebox.showinfo("Saved", "Analysis report saved successfully.")
        except:
            messagebox.showerror("Error", "Failed to save the file.")


window = tk.Tk()
window.title("Text Analyzer")
window.geometry("700x700")


tk.Label(window, text="Enter or Load your text:").pack()
input_text = tk.Text(window, height=10)
input_text.pack(pady=5)


button_frame = tk.Frame(window)
button_frame.pack()

tk.Button(button_frame, text="Analyze Text", command=analyze_text).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Load from File", command=load_file).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear", command=clear_text).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Save Report", command=save_report).grid(row=0, column=3, padx=5)


tk.Label(window, text="Analysis Result:").pack()
output_text = tk.Text(window, height=20)
output_text.pack(pady=5)


window.mainloop()
