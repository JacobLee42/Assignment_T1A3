# T1A3
## Plan and Implement a Terminal Application 
### Kapuut (Kahoot karbon kopy)

## Link to Github source repository: https://github.com/JacobLee42/Assignment_T1A3/tree/main
## Link to youtube slide presentation: https://youtu.be/nmaFtCD_B9s
## Identify any code style guide or styling conventions that the application will adhere to. Reference the style guide appropriately.

Welcome to my Terminal Application project! I decided to design a multiple choice quiz game based on our favourite classroom learning game - Kahoot! The game has features similar to the Kahoot game we all love (except for the timer/sliding point scale - but that's a whole other story).

So this project is essentially making sure that we understand how to write terminal applications and utilise and understand the python programming language.

In class I believe that we use PEP 8 as our styling guide and it is the official style guide for python code. PEP 8 was written by the creator of python, Guido van Rossum, and it provides guidelines for writing readable and consistant code. PEP stands for Python Enhancement Proposal and it covers topics such as naming conventions, indentation and code layout. Some of the key guidelines in PEP include:

    - Use 4 spaces per indentation level.
    - Use blank lines to seperate functions and classes, and larger blocks of code inside functions.
    - When possible, put comments on a line of their own.
    Use spaces around operators and after commas, but not directly inside bracketing constructs.
    - Name variables and functions using lowercase with words seperated by underscore (e.g. view_leaderboard)
    - Name classes using CamelCase (e.g. MyClass)

Since this is the only styling I know (for now) as it was taught in class, I will be adhering to this style and hopefully my code should adhere to those key guidelines listed above.

https://peps.python.org/pep-0008/

https://dev.to/codacy/3-popular-python-style-guides-that-will-help-your-team-write-better-code-1h0m

## Develop a list of features that will be included in the application. It must include:
    - at least THREE features
    - describe each feature

Main Page: The main.py page contains several functions that help implement our awesome muliple choice quiz game. The print_menu function displays the game menu to the user. The start_game function starts the game by calling the run_quiz function and then asks the user if they want to play again. The main_menu function displays the main menu and handles user input using a while loop.

The while loop in the main_menu function runs indefinately until the user chooses to exit the game. Inside the loop, the print_menu function is called to display the menu and the user's choice is obtained using the input function. The user's choice is stored in a variable called choice.

Conditional control structures are used to determine what action to take based on the user's choice. The main page has some features built in also, such as start game, view leaderboard and exit game. If the user chose option 1, the start_game function is called its return value is stored as a variable called play_again. If play_again is False, a message is printed thanking the user for playing and then the loop is exited using the break statement.

If the user chose option 2, the view_leaderboard function is called. If the user chose option 3, a message is printed thanking them for playing and then the loop will exit using the break statement.

If the user enters an invalid choice, a ValueError is raised with an error message. The exception is then caught in an except block and the error message is printed.

There are some instances of variable scope within the main.py code. Variables defined inside a function, such as choice and play_again are local to that function and cannot be accessed outside of it. Variables defined outside of any function, such as those imported from the quiz.py module at the top of the code script, have global scope and can be accessed from any function in the code.

Update Leaderboard: Wouldn't be much of a fun game without being able to beat a high score! And Kapuut is no differrent in that regard. The update_leaderboard function takes several arguments; score, player_name, high_score, leaderboard.

The function uses conditional control structures to check if the leaderboard is empty of if the current score is greater than the last score on leaderboard. If either condition is true, the function opens a file called leaderboard.txt (file handling) in write mode and appends a tuple containing the current score and player name to the leaderboard list.

The leaderboard list is then sorted in descending order and sliced to include only the top 10 scores. A new list of formatted strings is created for each element in the leaderboard list and then written to the file.

If the current score is greater than the high score, the high score is updated and a message is printed congratulating the player. The function then returns the updated high score.

The function overall shows the use of conditional control structures to check conditions and take different actions based on those conditions. The code shows the use of variables and variable scope by way of the arguments passed to the function are local to that function and cannot be outside of it. The high_score variable is updated inside the function and the updated value is returned by the function.

Play Question: It would certainly be a dull game without questions to ask! And what's a multiple choice quiz game without choices in answers! 

The play_question function takes three arguments; num, question and data. The function uses data passed in the data argument to extract the labeled alternatives, correct answer and answer label for the current question being displayed on screen. The ask_question function is called with these values as arguments to ask the user the current question and get their answer.

The print_question_result function is then called to print the result of the current question. The function returns a tuple containing the score for the current question, the user's answer label (a, b, c, d) the correct answer and the labeled alternatives.

https://www.geeksforgeeks.org/python-scope-of-variables/

https://www.w3schools.com/PYTHON/python_scope.asp

https://pythonbasics.org/scope/

Coder academy recorded class session T1W7 Tuesday: Loops, Functions


## Link to my Trello project management plan: 
https://trello.com/b/63HOEnUC/jacob-quiz-checklist

### Link to how to use Trello:
https://www.youtube.com/watch?v=6drUzoeHZkg 


## Design help documentation which includes a set of instructions which accurately describe how to use and install the app.

# Kapuut Help Documentation
## Installation
1. Open a terminal (I use wsl(Unbutu)) and navigate to the directory you want to use.
2. In the terminal type ./run.sh and the game should load automatically once the packages are installed. Easy Peasy!
    If it doesn't work...

1. Make sure you have python 3 installed on your system. In the command prompt and enter the following:
    python3 --version
    this will show current version of python installed on your computer. I have wsl as stated before so to install python 3 you enter:
    sudo apt-get install python3
2. Then run these commands to create a virtual environment before we install the requirements:
    python 3 -m venv kapuut-venv
    source kapuut-venv/bin/activate
3. Install the dependencies required by the app to run by enetring:
    pip3 install -r requirements.txt


## System Requirements
 Python 3
 A terminal or command prompt

 ## Usage
 Make sure you are in the Kapuut-venv directory. You will see this in your terminal. Run the game by entering this:
 python3 main.py

 THATS IT!!!


 
 # RESOURCES

 ### These are what I used to help me create the terminal application:

  https://www.youtube.com/watch?v=QPp09g8Rspg

  https://www.makeuseof.com/python-make-interactive-quiz-game/

  https://brockbyrdd.medium.com/creating-a-multiple-choice-quiz-in-python-terminal-1c46123b86d5

  https://pythonprogramming.altervista.org/how-to-generate-multiple-choice-questions-with-python/

  https://stackoverflow.com/questions/60576809/how-do-i-implement-a-timer-on-each-question-asked-in-a-quiz

  https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/

  https://discuss.python.org/t/implementing-a-countdown-in-a-quiz-game-that-resets-upon-answer-and-starts-over-from-scratch-on-new-question-given/20738

  https://pypi.org/

  https://blog.inedo.com/python/modularization-and-packages/

  https://www.youtube.com/watch?v=PBUtAdR1n6g

  https://towardsdatascience.com/cleaning-refactoring-and-modular-the-must-foundations-to-improve-your-python-code-and-carrer-65ef71cdb264

  https://www.youtube.com/watch?v=StQO2oaOMw4

  All videos of classes from week 7 and week 8 about anything python, including Simons mock app we did on Sat week 8 was very helpful.

