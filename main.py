
    
 

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
            play_again = run_quiz(name)
            if not play_again:
                print("Thank you for playing Kapuut! Hope to see you back here real soon!!!")
            continue
        elif choice == "2":
            view_leaderboard()
            continue
        elif choice == "3":
            print("Thank you for playing hope to see you soon!!!")
            break
        else:
            print("invalid choice, please only enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()

