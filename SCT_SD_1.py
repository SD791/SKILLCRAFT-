import tkinter as tk
from tkinter import messagebox


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
     return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
     return (kelvin - 273.15) * 9/5 + 32


def convert_temperature():
    try:
        value = float(entry_value.get())
        from_scale = combo_from.get()
        to_scale = combo_to.get()

        

        if from_scale == to_scale:
            result = value
        elif from_scale == "Celsius" and to_scale == "Fahrenheit":
            result = celsius_to_fahrenheit(value)
        elif from_scale == "Celsius" and to_scale == "Kelvin":
            result = celsius_to_kelvin(value)

        elif from_scale == "Fahrenheit" and to_scale == "Celsius":
            result = fahrenheit_to_celsius(value)
        elif from_scale == "Fahrenheit" and to_scale == "Kelvin":
            result = fahrenheit_to_kelvin(value)
        elif from_scale == "Kelvin" and to_scale == "Celsius":
            result = kelvin_to_celsius(value)
        elif from_scale == "Kelvin" and to_scale == "Fahrenheit":
            result = kelvin_to_fahrenheit(value)

        label_result.config(text=f"Result: {result:.2f} {to_scale}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical value.")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x300")
root.configure(bg='powder blue')

label_input = tk.Label(root, text="Enter Temperature:",fg="black", bg="white")
label_input.grid(row=0, column=0, padx=10, pady=10)


entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10,)


label_from = tk.Label(root, text="From Scale:",fg="black", bg="white")
label_from.grid(row=1, column=0, padx=10, pady=10)


combo_from = tk.StringVar(root)
combo_from.set("Celsius")  
dropdown_from = tk.OptionMenu(root, combo_from, "Celsius", "Fahrenheit", "Kelvin")
dropdown_from.grid(row=1, column=1, padx=10, pady=10)
dropdown_from.config(bg="white")

label_to = tk.Label(root, text="To Scale:",fg="black", bg="white")
label_to.grid(row=2, column=0, padx=10, pady=10)


combo_to = tk.StringVar(root)
combo_to.set("Fahrenheit")
dropdown_to = tk.OptionMenu(root, combo_to, "Celsius", "Fahrenheit", "Kelvin")
dropdown_to.grid(row=2, column=1, padx=10, pady=10,)
dropdown_to.config(bg="white")


button_convert = tk.Button(root, text="Convert",fg="black", bg="white", command=convert_temperature)
button_convert.grid(row=3, column=0, columnspan=2, pady=30)


label_result = tk.Label(root, text="Result: ",fg="black", bg="white")
label_result.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
