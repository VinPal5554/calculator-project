import tkinter as tk

# Define themes
themes = {
    'light': {
        'bg': 'white',        # Background color for light mode
        'fg': 'black',        # Text color for light mode
        'btn_bg': '#f0f0f0',  # Button background color
        'btn_fg': 'black',    # Button text color
        'btn_active': '#e0e0e0', # Button pressed color
    },
    'dark': {
        'bg': '#2e2e2e',      # Background color for dark mode
        'fg': 'white',        # Text color for dark mode
        'btn_bg': '#444',     # Button background color
        'btn_fg': 'white',    # Button text color
        'btn_active': '#666', # Button pressed color
    }
}

# Default theme
current_theme = 'light'

def apply_theme(root, entry, buttons, theme):
    """Applies the selected theme to the GUI."""
    # Apply background and text color to root window
    root.configure(bg=themes[theme]['bg'])
    entry.configure(bg=themes[theme]['bg'], fg=themes[theme]['fg'])

    # Apply button colors
    for btn in buttons:
        btn.configure(
            bg=themes[theme]['btn_bg'],
            fg=themes[theme]['btn_fg'],
            activebackground=themes[theme]['btn_active']
        )


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

def toggle_theme(entry, buttons):
    """Switches between light and dark mode."""
    global current_theme
    current_theme = 'dark' if current_theme == 'light' else 'light'
    apply_theme(root, entry, buttons, current_theme)



def restart_calculator():
    entry_var.set("")  # Clear the display


def gui_calculator():
    global entry_var, root, buttons 
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
        ("0", ".", "//", "="),  
        ("Theme", "", "", "")  
    ]
    
    button_widgets = []  # List to store button widgets for theme updates

   # Create calculator buttons and apply the theme
    for r, row in enumerate(buttons):
        for c, char in enumerate(row):
            if char == "ON":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda: entry_var.set(""), bg="green", fg="white")
            elif char == "C":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda: entry_var.set(""), bg="red", fg="white")
            elif char == "←":
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda: entry_var.set(entry_var.get()[:-1]), bg="orange", fg="black")
            elif char == "Theme":
                # Adjust the size of the "Toggle Theme" button to match other buttons
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda: toggle_theme(entry, button_widgets))
            else:
                btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda v=char: on_click(v))

            btn.grid(row=r+1, column=c)
            button_widgets.append(btn)  # Store button widget for later theming

    # Apply initial theme
    apply_theme(root, entry, button_widgets, current_theme)

    root.mainloop()

