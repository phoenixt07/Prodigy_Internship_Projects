import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps

class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        
        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()
        
        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack()
        
        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()
        
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()
        
        self.image = None
        self.encrypted_image = None
    
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)
    
    def display_image(self, img):
        img = ImageOps.contain(img, (500, 500))  # Resize image to fit in the display area
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk
    
    def encrypt_image(self):
        if self.image:
            self.encrypted_image = self.image.copy()
            self._process_image(self.encrypted_image, encrypt=True)
            self.display_image(self.encrypted_image)
        else:
            messagebox.showerror("Error", "No image loaded")
    
    def decrypt_image(self):
        if self.encrypted_image:
            decrypted_image = self.encrypted_image.copy()
            self._process_image(decrypted_image, encrypt=False)
            self.display_image(decrypted_image)
        else:
            messagebox.showerror("Error", "No encrypted image found")
    
    def save_image(self):
        if self.encrypted_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("All files", "*.*")])
            if file_path:
                self.encrypted_image.save(file_path)
        else:
            messagebox.showerror("Error", "No encrypted image to save")
    
    def _process_image(self, img, encrypt=True):
        pixels = img.load()
        key = 123  # Simple encryption key for XOR operation
        
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j][:3]  # Ensure we only get RGB values
                if encrypt:
                    pixels[i, j] = (r ^ key, g ^ key, b ^ key)
                else:
                    pixels[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR with the same key to decrypt

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
