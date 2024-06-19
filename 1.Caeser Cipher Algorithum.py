import tkinter as tk
from tkinter import messagebox
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")

        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        # Text to Encrypt/Decrypt
        tk.Label(self.root, text="Text:").grid(row=0, column=0, padx=10, pady=10)
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        # Shift Value
        tk.Label(self.root, text="Shift:").grid(row=1, column=0, padx=10, pady=10)
        self.shift_entry = tk.Entry(self.root, width=5)
        self.shift_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Encrypt Button
        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        # Decrypt Button
        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(row=2, column=1, padx=10, pady=10)

        # Result
        tk.Label(self.root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
        self.result_label = tk.Label(self.root, text="", width=50)
        self.result_label.grid(row=3, column=1, padx=10, pady=10)

    def encrypt_text(self):
        try:
            text = self.text_entry.get()
            shift = int(self.shift_entry.get())
            encrypted_text = encrypt(text, shift)
            self.result_label.config(text=encrypted_text)
        except ValueError:
            messagebox.showerror("Input Error", "Shift value must be an integer.")

    def decrypt_text(self):
        try:
            text = self.text_entry.get()
            shift = int(self.shift_entry.get())
            decrypted_text = decrypt(text, shift)
            self.result_label.config(text=decrypted_text)
        except ValueError:
            messagebox.showerror("Input Error", "Shift value must be an integer.")
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
