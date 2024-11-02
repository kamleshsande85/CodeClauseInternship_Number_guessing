import tkinter as tk
import random
from tkinter import messagebox

# Function to guess the number


def Guess_number():
    try:
        # Get the user's guess from the entry
        user_guess = int(entry.get())
        if user_guess < 1 or user_guess > 100:
            messagebox.showwarning(
                title="Warning", text="Please enter a number between 1 and 100.")
            return

        if user_guess == rndom_number:
            messagebox.showinfo("Correct", "Correct number ")
            root.quit()  # Close the application
        elif user_guess > rndom_number:
            messagebox.showinfo("high", "Too high ")
        else:
            messagebox.showinfo("Low", "Too low ")

    except ValueError:
        messagebox.showerror(
            title="Error", text="Please enter a valid integer.")


# Initialize the main window
root = tk.Tk()
root.geometry("500x200")
# root.maxsize(200, 200)
# root.minsize(200, 200)
root.title("Number Guessing")
root.config(bg="#33DEED")

# Generate a random number once at the start
rndom_number = random.randint(1, 100)

# Create the main frame and widgets
frame1 = tk.Frame(root, bg="#032124")
frame1.pack()

label = tk.Label(frame1, text="Enter number (1 to 100):",
                 bg="#032124", fg="white")
label.grid(row=0, column=0, pady=1)

entry = tk.Entry(frame1)
entry.grid(row=0, column=1, padx=10, pady=10)

submitBtn = tk.Button(frame1, text="Submit",
                      command=Guess_number, bg="#032124", fg="white")
submitBtn.grid(row=1, columnspan=2)

# Start the main loop
root.mainloop()
