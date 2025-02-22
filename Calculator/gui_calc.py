import tkinter as tk

def on_click(value):
    """Handles button clicks."""
    current_text = entry_var.get()

    if value == "=":
        try:
            # Use eval safely, allowing only math operations
            result = eval(current_text, {"__builtins__": None}, {})
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")

    elif value == ".":
        # Prevent multiple decimals in a single number
        if current_text and current_text[-1].isdigit():
            last_number = current_text.split()[-1]
            if "." not in last_number:
                entry_var.set(current_text + ".")
        elif not current_text:
            entry_var.set("0.")  # Allow starting with "."
        
    else:
        entry_var.set(current_text + str(value))


def restart_calculator():
    entry_var.set("")  # Clear the display


def gui_calculator():
    global entry_var  
    root = tk.Tk()
    root.title("Calculator")

    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("ON", "C", "←", "/"),  
        ("7", "8", "9", "*"),  
        ("4", "5", "6", "-"),  
        ("1", "2", "3", "+"),  
        ("0", ".", "//", "=")  # Added "." button next to "0"
    ]

    for r, row in enumerate(buttons):
        for c, char in enumerate(row):
            if char == "ON":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=restart_calculator, bg="green", fg="white")
            elif char == "C":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda v=char: on_click(v), bg="red", fg="white")
            elif char == "←":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda: entry_var.set(entry_var.get()[:-1]), bg="orange", fg="black")
            else:
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda v=char: on_click(v))

            btn.grid(row=r+1, column=c)

    root.mainloop()

