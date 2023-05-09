
import sys
from questions import QUESTIONS
from string import ascii_lowercase
 

from quiz import run_quiz, view_leaderboard

def main_menu():
    while True:
        print("Welcome to Kapuut! The Kahoot karbon kopy multiple choice quiz game made in Python!!!")
        print("Please choose from one of the following options:")
        print("1) Start the Game")
        print("2) View Leaderboard")
        print("3) Exit the Game")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            name = input("Enter your name: ")
            print("Welcome to Kapuut Quiz Game!")
            print("you will be asked 7 multiple choice questions.")
            print("Each question has a time limit of 13 seconds. You will not be able to see it. Exciting, right!!")
            print("You will earn points for each correct answer.")
            print ("The faster you answer, the more points you earn!!!")
            print("Good luck ALL!!!\n")

            play_again = run_quiz(name)
            if not play_again:
                print("Thank you for playing Kapuut! Hope to see you back here real soon!!!")
            break
        elif choice == "2":
            view_leaderboard()
            
        elif choice == "3":
            print("Thank you for playing hope to see you soon!!!")
            break
        else:
            print("invalid choice, please only enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()

