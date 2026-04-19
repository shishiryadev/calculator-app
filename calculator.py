import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Basic Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)
        
        # Variable to store the expression
        self.expression = ""
        
        # Create the display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.window, bg="black")
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Entry widget for display
        self.display = tk.Entry(
            display_frame, 
            font=("Arial", 18), 
            justify="right",
            state="readonly",
            readonlybackground="white"
        )
        self.display.pack(fill=tk.BOTH, ipady=10)
    
    def create_buttons(self):
        # Button frame
        button_frame = tk.Frame(self.window)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        # Button layout
        buttons = [
            ['C', '⌫', '√', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '=']
        ]

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '=':
                    if j == 2:
                        continue
                    btn = tk.Button(
                        button_frame,
                        text=text,
                        font=("Arial", 14),
                        command=lambda: self.calculate(),
                        bg="#ff9500",
                        fg="white",
                        activebackground="#ffad33"
                    )
                    btn.grid(row=i, column=j-1, columnspan=2, sticky="nsew", padx=2, pady=2)
                else:
                    # Determine button color
                    if text in ['C', '⌫', '√']:
                        bg_color = "#a6a6a6"
                        fg_color = "black"
                    elif text in ['+', '-', '*', '/']:
                        bg_color = "#ff9500"
                        fg_color = "white"
                    else:
                        bg_color = "#333333"
                        fg_color = "white"

                    btn = tk.Button(
                        button_frame,
                        text=text,
                        font=("Arial", 14),
                        command=lambda t=text: self.button_click(t),
                        bg=bg_color,
                        fg=fg_color,
                        activebackground="#555555"
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        # Configure grid weights for responsive design
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, value):
        if value == 'C':
            self.clear()
        elif value == '⌫':
            self.backspace()
        elif value == '√':
            self.square_root()
        else:
            self.add_to_expression(value)
    
    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_display()
    
    def clear(self):
        self.expression = ""
        self.update_display()
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()
    
    def square_root(self):
        try:
            if self.expression:
                result = math.sqrt(float(self.expression))
                self.expression = str(result)
                self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")
            self.clear()
    
    def calculate(self):
        try:
            if self.expression:
                # Replace display symbols with Python operators
                expression = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.expression = str(result)
                self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            self.clear()
    
    def update_display(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
        self.display.config(state="readonly")
    
    def run(self):
        self.window.mainloop()

# Create and run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()