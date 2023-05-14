from colorama import Fore, Style
from colored import fg, bg, attr
from rich.console import Console
import emoji

#
console = Console()

# Try to import the run_quiz and view_leaderboard functions from the quiz module
try:
    from quiz import run_quiz, view_leaderboard
# If the quiz module cannot be imported, print error message
except ImportError:
    print("Error: Could not import quiz module.") 
# Define a function called print_menu that prints the game menu. Use Colorama package for color. Rich package for emojis.
def print_menu():
    print(Fore.BLUE + "Welcome to Kapuut! 🎉 The Kahoot karbon kopy multiple choice quiz game made in Python!!!" + Style.RESET_ALL)
    print("Please choose from one of the following options:👇")
    print(Fore.YELLOW + "1)" + Fore.YELLOW + "Start the Game🎮")
    print(Fore.GREEN + "2)" + Fore.GREEN +  "View Leaderboard🏆")
    print(Fore.RED + "3)" + Fore.RED +  "Exit the Game❌" + Style.RESET_ALL)
# Define a function called start_game. Use colored package.
def start_game():
    print(f"{fg('blue')}Welcome to Kapuut Quiz Game! {attr('reset')}")
    print(f"{fg('yellow')}You will be asked 7 multiple choice questions. {attr('reset')}")            
    print(f"{fg('green')}You will earn points for each correct answer. {attr('reset')}")               
    print(f"{fg('red')}Good luck ALL!!!\n {attr('reset')}")
    run_quiz()
    return input(f"{fg('blue')}Do you want to play again? (y/n) {attr('reset')}").lower() != 'y'
# Define a function called main_menu that displays the main menu and handles user input
def main_menu():
    # Loop indefinately
    while True: 
        # Call the print_menu function to display menu
        print_menu()   
        # Get user choice  
        choice = input("Enter your choice (1-3): ")
        try:
            # If user chose option 1, start the game
            if choice == "1":   
               # Call the start_game function and store its return value in play_again            
               play_again = start_game()
               # If play_again False, thank user and break loop
               if not play_again:
                    print(Fore.GREEN + "Thank you for playing Kapuut! Hope to see you back here real soon" + Style.RESET_ALL)
                    print(emoji.emojize(":grinning_face_with_big_eyes:"))
                    break
               # If user chose option 2, view leaderboard
            elif choice == "2":
                view_leaderboard()  
                # If user chose option 3, thank them and break out of loop          
            elif choice == "3":
                print(Fore.YELLOW + "Thank you for playing hope to see you soon!!!" + Style.RESET_ALL)
                print(emoji.emojize(":grinning_face_with_big_eyes:"))
                break
            else:
                raise ValueError(Fore.RED + "invalid choice, please only enter 1, 2 or 3." + Style.RESET_ALL)
        except ValueError as e:
            print(f"error: {e}")
        except Exception as e:
            print(f"Error: {e}")            
        exit() 

    # If this script is being run directly and not imported as a module, call the main_menu function to start game        

if __name__ == "__main__":    
    main_menu()
