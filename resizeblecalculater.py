import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable Calculator")
        self.root.geometry("400x500")  # Initial size
        self.root.resizable(True, True)  # Allow resizing

        # Entry widget for display
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Buttons layout
        self.buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        # Create buttons dynamically
        for r, row in enumerate(self.buttons, 1):
            for c, char in enumerate(row):
                btn = tk.Button(root, text=char, font=("Arial", 20), command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        # Configure row/column weights for responsiveness
        for i in range(5):
            root.rowconfigure(i, weight=1)
            root.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.display.delete(0, tk.END)  # Clear display
        elif char == "=":
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()