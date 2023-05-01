import tkinter as tk
import tkinter.messagebox as messagebox

class EncryptDecryptApp:
    def __init__(self, master):
        self.master = master
        master.title("Encrypt/Decrypt App")

        #INPUT/OUTPUT
        self.input_label = tk.Label(master, text="Input Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_entry = tk.Text(master, width=30, height=5)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.output_label = tk.Label(master, text="Output Text:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5)
        self.output_entry = tk.Text(master, width=30, height=5)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)

        #Buttons
        self.encrypt_button = tk.Button(master, text="Encrypt", width=10, command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=0, padx=5, pady=5)

        self.decrypt_button = tk.Button(master, text="Decrypt", width=10, command=self.decrypt_text)
        self.decrypt_button.grid(row=2, column=1, padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Clear", width=10, command=self.clear_fields)
        self.clear_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        #CIPHER
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.key = "qwertyuiopasdfghjklzxcvbnm"

    def encrypt_text(self):
        input_text = self.input_entry.get("1.0", tk.END).lower()
        output_text = ""
        for char in input_text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                output_text += self.key[char_index]
            else:
                output_text += char
        self.output_entry.delete("1.0", tk.END)
        self.output_entry.insert("1.0", output_text)

    def decrypt_text(self):
        input_text = self.input_entry.get("1.0", tk.END).lower()
        output_text = ""
        for char in input_text:
            if char in self.key:
                char_index = self.key.index(char)
                output_text += self.alphabet[char_index]
            else:
                output_text += char
        self.output_entry.delete("1.0", tk.END)
        self.output_entry.insert("1.0", output_text)

    def clear_fields(self):
        self.input_entry.delete("1.0", tk.END)
        self.output_entry.delete("1.0", tk.END)
root = tk.Tk()
app = EncryptDecryptApp(root)
root.mainloop()
