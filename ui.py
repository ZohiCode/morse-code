# ui.py
import tkinter as tk
from tkinter import messagebox
from morse import text_to_morse


def convert_to_morse(entry_text, result_label):
    input_text = entry_text.get()
    if input_text:
        morse_code = text_to_morse(input_text)
        result_label.config(text=morse_code)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir kelime veya cümle girin!")


def create_ui():
    window = tk.Tk()
    window.title("Morse Kodu Çevirici")
    window.geometry("400x300")
    window.configure(bg="#2C3E50")

    label_title = tk.Label(window, text="Morse Kodu Çevirici", font=("Helvetica", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
    label_title.pack(pady=20)

    label_text = tk.Label(window, text="Metni girin:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
    label_text.pack(pady=5)

    entry_text = tk.Entry(window, width=30, font=("Helvetica", 12), bd=2, relief="flat", bg="#ECF0F1", fg="#2C3E50")
    entry_text.pack(pady=10)

    result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1", wraplength=350)
    button_convert = tk.Button(window, text="Morse Koduna Çevir", command=lambda: convert_to_morse(entry_text, result_label), font=("Helvetica", 12, "bold"), bg="#3498DB", fg="black", relief="flat")
    button_convert.pack(pady=10)

    result_label.pack(pady=10)

    window.mainloop()
