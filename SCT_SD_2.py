import tkinter as tk
from tkinter import messagebox
import random


def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Guess", "Please enter a number between 1 and 100.")
            return
        if guess == random_number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            new_game()
        elif guess < random_number:
            result_label.config(text="Too low! Try again.")
        else:
            result_label.config(text="Too high! Try again.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer.")


def new_game():
    global random_number
    random_number = random.randint(1, 100) 
    result_label.config(text="Enter your guess:")
    guess_entry.delete(0, tk.END)  


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")
root.configure(bg='powder blue')

instructions_label = tk.Label(root, text="Guess the number between 1 and 100!",bg="white",fg="black")
instructions_label.grid(row=0, column=0, columnspan=2, pady=10)


guess_label = tk.Label(root, text="Enter your guess:",bg="white",fg="black")
guess_label.grid(row=1, column=0)

guess_entry = tk.Entry(root)
guess_entry.grid(row=1, column=1)


check_button = tk.Button(root, text="Check Guess", command=check_guess,bg="white",fg="black")
check_button.grid(row=2, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Enter your guess:",bg="white",fg="black")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

new_game()


root.mainloop()
