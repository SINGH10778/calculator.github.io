import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current text
    entry.insert(tk.END, current + value)

# Function to clear the input field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equals():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Show result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression and result
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout and functionality
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_clear).grid(row=row, column=col)
    elif text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=button_equals).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda value=text: button_click(value)).grid(row=row, column=col)

# Start the GUI loop
root.mainloop()
