""" Author: Hayden Yeoman Date written: 5/11/23 Assignment: Final Project
 Short Desc:  gui tkinter rock paper scissors game human vs computer"""

"""tkinter module used for creating the graphical user interface """
import tkinter as tk
"""used to randomly select the computer's choice in the game."""
import random

# Define the main window
root = tk.Tk() #root represents main window
root.title("Rock Paper Scissors") 

# Define the second window
result_window = tk.Toplevel() #result_window Represents the second window which is used for displaying results
result_window.title("Result")

# Define how to track  the score and total games played
player_score = 0 #player_score keeps track of the player(users) score
computer_score = 0 # computer_score keeps track of the computers score
total_games = 0 #total_games keeps track of the total games played

# Define the function for the game
def play(player_choice):
    global player_score, computer_score, total_games
    total_games += 1
    computer_choice = random.choice(['rock', 'paper', 'scissors'])#giving options to computer_choice

    #defining tie
    if player_choice == computer_choice: 
        result = "Tie!"
    #defining how the player wins
    elif player_choice == 'rock' and computer_choice == 'scissors' or \
         player_choice == 'paper' and computer_choice == 'rock' or \
         player_choice == 'scissors' and computer_choice == 'paper':
        result = "You win!"
        player_score += 1

    #defining how the computer wins
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update the result window
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
    games_played_label.config(text=f"Total games played: {total_games}")

# Create the PhotoImage Objects
try:
    button_size = 30 #specifies the size of the buttons
    rock_image = tk.PhotoImage(file="rock.png") # PhotoImage object for the rock
    paper_image = tk.PhotoImage(file="paper.png") #PhotoImage object for the paper
    scissors_image = tk.PhotoImage(file="scissors.png") #PhotoImage objects for the scissors
#when ran with correct images alt text does not appear tho shows it did it in the debugger in vs

# scales the size of an images to fit a specified display height and width
    def scale_image(image, display_height, display_width):
        h,w = image.height(), image.width()
    # h 900
    # w 700
        x = h / display_height
        y = w / display_width
        return image.subsample(int(x), int(y))

    rock_image = scale_image(rock_image, 30, 30)
    paper_image = scale_image(paper_image, 30, 30)
    scissors_image = scale_image(scissors_image, 30, 30)

    #does the above unless the variables = none 
except:
    rock_image = None
    paper_image = None
    scissors_image = None   
    button_size = 2

# Create the buttons the main window
rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'), image=rock_image, height=button_size, width=button_size) #Button for selecting the rock option in the main window.
rock_button.pack(side=tk.LEFT, padx=10, pady=10)
paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'), image=paper_image, height=button_size, width=button_size) #Button for selecting the paper option in the main window.
paper_button.pack(side=tk.LEFT, padx=10, pady=10) 
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('scissors'),image=scissors_image, height=button_size, width=button_size) #Button for selecting the scissors option in the main window.
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

#declares what happens when hover_over event is activated
def hover_over(event):
    button = event.widget
    button.config(bg = "green"  )
    button.borderwidth = 3

#declares what happens when mouse_over event is activated
def mouse_off(event):
    button = event.widget
    button.config(bg = "teal"  )
    button.borderwidth = 3

#binds events to rock_button
rock_button.bind('<Enter>', hover_over)
rock_button.bind('<Leave>', mouse_off)

#binds events to paper_button
paper_button.bind('<Enter>', hover_over)
paper_button.bind('<Leave>', mouse_off)

#binds events to scissors_button
scissors_button.bind('<Enter>', hover_over)
scissors_button.bind('<Leave>', mouse_off)

# Define the function to exit the GUI
def exit_game():
    root.quit()

# Create the exit button
exit_button = tk.Button(root, text="Exit", command=exit_game)# Button for exiting the game.
exit_button.pack(side=tk.LEFT, padx=10, pady=10)

#binds events to exit_button
exit_button.bind('<Enter>', hover_over)
exit_button.bind('<Leave>', mouse_off)

# Create the labels for the result window
result_label = tk.Label(result_window, font=('Helvetica', 24)) #Label widget for displaying the game result in the result window.
result_label.pack(padx=50, pady=20)
score_label = tk.Label(result_window, font=('Helvetica', 18)) #Label widget for displaying the scores in the result window.
score_label.pack(padx=50, pady=10)
games_played_label = tk.Label(root, text="Total games played: 0") # Label widget for displaying the total number of games played in the main window.
games_played_label.pack(side=tk.BOTTOM, padx=10, pady=10)
#  start over
root.mainloop()