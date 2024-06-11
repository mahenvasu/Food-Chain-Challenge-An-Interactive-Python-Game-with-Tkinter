import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Choices for the game
choices = ['Lion', 'Fox', 'Rabbit', 'Grass']

# Variables to track game statistics
attempts = 0
wins = 0
losses = 0
tie = 0

# Function to handle the game logic
def play_game(player_choice):
    global attempts, wins, losses, tie
    
    computer_choice = random.choice(choices)
    result = ""
    
    if player_choice == computer_choice:
        result = "It's a tie!"
        tie += 1
    elif  (player_choice == 'Lion' and computer_choice == 'Fox') or \
          (player_choice == 'Lion' and computer_choice == 'Rabbit')or \
          (player_choice == 'Lion' and computer_choice == 'Grass')or \
          (player_choice == 'Fox' and computer_choice == 'Rabbit') or \
          (player_choice == 'Fox' and computer_choice == 'Grass') or \
          (player_choice == 'Rabbit' and computer_choice == 'Grass'):
        result = "You win!"
        wins += 1
    else:
        result = "Computer wins!"
        losses += 1

    attempts += 1
    result_message = f"Computer chose: {computer_choice}\n{result}\n\nAttempts: {attempts}\nWins: {wins}\nLosses: {losses}\nTies: {tie}"
    result_label.config(text=result_message)
    update_history(player_choice, computer_choice, result)

# Function to update game history
def update_history(player_choice, computer_choice, result):
    if len(history_list) >= 5:
        history_list.pop(0)
    history_list.append(f"Player: {player_choice}, Computer: {computer_choice}, Result: {result}")
    history_text = "\n".join(history_list)
    history_label.config(text=history_text)

# Function to reset the game statistics
def reset_game():
    global attempts, wins, losses, tie
    attempts = 0
    wins = 0
    losses = 0
    tie = 0 
    result_label.config(text="")
    history_list.clear()
    history_label.config(text="")
    messagebox.showinfo("Reset", "Game statistics have been reset!")

# Setting up the main application window
root = tk.Tk()
root.title("Food Chain Challenge: Lion vs Fox vs Rabbit vs Grass")
root.geometry("800x700")
root.config(bg="lightblue")

# Welcome message
welcome_label = tk.Label(root, text="Welcome to Food Chain Challenge!\nChoose your move to start playing.", font=("Helvetica", 16), bg="lightblue")
welcome_label.pack(pady=20)

# Adding a label for the game title
title_label = tk.Label(root, text="Food Chain Challenge\n Lion vs Fox vs Rabbit vs Grass", font=("Helvetica", 24, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Frame to hold the buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

# Load images for buttons
lion_img = ImageTk.PhotoImage(Image.open("lion.jpg").resize((100, 100)))
fox_img = ImageTk.PhotoImage(Image.open("fox.jpg").resize((100, 100)))
rabbit_img = ImageTk.PhotoImage(Image.open("rabbit.jpg").resize((100, 100)))
grass_img = ImageTk.PhotoImage(Image.open("grass.jpg").resize((100, 100)))

# Adding buttons for player choices with images
lion_button = tk.Button(button_frame, image=lion_img, command=lambda: play_game('Lion'))
lion_button.grid(row=0, column=0, padx=20)

fox_button = tk.Button(button_frame, image=fox_img, command=lambda: play_game('Fox'))
fox_button.grid(row=0, column=1, padx=20)

rabbit_button = tk.Button(button_frame, image=rabbit_img, command=lambda: play_game('Rabbit'))
rabbit_button.grid(row=0, column=2, padx=20)

grass_button = tk.Button(button_frame, image=grass_img, command=lambda: play_game('Grass'))
grass_button.grid(row=0, column=3, padx=20)

# Result label to display game results and stats
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightblue")
result_label.pack(pady=20)

# History label to display the history of the last few games
history_list = []
history_label = tk.Label(root, text="", font=("Helvetica", 14), bg="lightblue", justify=tk.LEFT)
history_label.pack(pady=20)

# Adding a reset button
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), width=10, command=reset_game)
reset_button.pack(pady=10)

# Adding an exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14), width=10, command=root.quit)
exit_button.pack(pady=10)

# Running the main event loop
root.mainloop()
