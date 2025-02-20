import tkinter as tk

def on_click(value):
    current_text = entry_var.get()

    if value == "=":
        try:
            result = eval(current_text, {"__builtins__": None}, operations)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + str(value))


def gui_calculator():
    global entry_var  
    root = tk.Tk()
    root.title("Calculator")

    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("7", "8", "9", "/"), ("4", "5", "6", "*"),
        ("1", "2", "3", "-"), ("C", "0", "=", "+"),
        ("%", "//", "**", "")
    ]

    for r, row in enumerate(buttons):
        for c, char in enumerate(row):
            btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda v=char: on_click(v))
            btn.grid(row=r+1, column=c)

    root.mainloop()

