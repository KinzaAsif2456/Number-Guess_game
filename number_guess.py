
import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 50:
            feedback_label.config(text="Enter a number between 1 and 50", fg="orange")
        elif guess < target_number:
            feedback_label.config(text="Too low!", fg="#3498db")  # Light blue
            root.config(bg="#eaf2f8")  # Light background for low guess
        elif guess > target_number:
            feedback_label.config(text="Too high!", fg="#e74c3c")  # Light red
            root.config(bg="#fdebd0")  # Light background for high guess
        else:
            feedback_label.config(text="Correct!", fg="#2ecc71")  # Light green
            root.config(bg="#d4efdf")  # Light background for correct guess
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            reset_game()
    except ValueError:
        feedback_label.config(text="Enter a valid number", fg="orange")

def reset_game():
    global target_number
    target_number = random.randint(1, 50)
    entry.delete(0, tk.END)
    feedback_label.config(text="")
    root.config(bg="#ffffff")  # Reset background color to white

# Setup the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

target_number = random.randint(1, 50)

# Add widgets
label = tk.Label(root, text="Guess a number between 1 and 50")
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Guess", command=check_guess)
button.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Helvetica", 14))
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
