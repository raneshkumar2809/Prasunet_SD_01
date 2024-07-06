import tkinter as tk
from tkinter import messagebox
from convert_temp_to import celsius_to_kelvin, celsius_to_fahrenheit, kelvin_to_celsius, kelvin_to_fahrenheit, fahrenheit_to_celsius, fahrenheit_to_kelvin

# Temperature convertion function
def convert_temperature():
    try:
        value = float(entry.get()) # getting value of temperature
        unit = unit_var.get() # getting selected units of temperature
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric temperature.")
        return

    if unit == "Select":
        messagebox.showerror("Input Error", "Please select a temperature unit.")
        return
    elif unit == "Celsius":
        temp_k = celsius_to_kelvin(value)
        temp_f = celsius_to_fahrenheit(value)
        result.set(f"{value}°C = {temp_f:.2f}°F = {temp_k:.2f}K")
    elif unit == "Kelvin":
        temp_c = kelvin_to_celsius(value)
        temp_f = kelvin_to_fahrenheit(value)
        result.set(f"{value}K = {temp_c:.2f}°C = {temp_f:.2f}°F")
    elif unit == "Fahrenheit":
        temp_c = fahrenheit_to_celsius(value)
        temp_k = fahrenheit_to_kelvin(value)
        result.set(f"{value}°F = {temp_c:.2f}°C = {temp_k:.2f}K")
    else:
        messagebox.showerror("Input Error", "Invalid unit. Please select 'Celsius', 'Kelvin', or 'Fahrenheit'.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

window.configure(bg="#f2f2f2")
window.geometry("500x300")

header = tk.Label(window, text="Temperature Converter", bg="#4a90e2", fg="white", font=("Helvetica", 16, "bold"))
header.pack(fill="x", pady=10)

frame = tk.Frame(window, bg="#f2f2f2")
frame.pack(pady=20)

entry_label = tk.Label(frame, text="Enter temperature:", bg="#f2f2f2", font=("Helvetica", 12))
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

unit_var = tk.StringVar(value="Select")
unit_menu = tk.OptionMenu(frame, unit_var, "Celsius", "Kelvin", "Fahrenheit")
unit_menu.grid(row=0, column=2, padx=10, pady=10)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature, bg="#4a90e2", fg="white", font=("Helvetica", 12))
convert_button.grid(row=1, column=0, columnspan=3, pady=10)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, bg="#f2f2f2", font=("Helvetica", 12, "bold"))
result_label.pack(pady=20)

# Run the application
window.mainloop()