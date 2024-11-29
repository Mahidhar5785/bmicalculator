import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get weight and height from entries
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Validate inputs
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        # Update the labels with the results
        bmi_label.config(text=f"Your BMI: {bmi}")
        category_label.config(text=get_bmi_category(bmi))
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def get_bmi_category(bmi):
    """Determine the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Category: Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Category: Normal weight"
    elif 25 <= bmi < 29.9:
        return "Category: Overweight"
    else:
        return "Category: Obesity"

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Instructions
instructions_label = tk.Label(root, text="Enter your weight and height:")
instructions_label.pack(pady=10)

# Create and place the widgets
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.pack(pady=5)

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=20)

bmi_label = tk.Label(root, text="Your BMI: ")
bmi_label.pack(pady=10)

category_label = tk.Label(root, text="Category: ")
category_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()