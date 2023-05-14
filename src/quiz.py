import random  
from string import ascii_lowercase
from questions import questions_dict
from colorama import Fore, Style

# Defines a function called load_leaderboard
def load_leaderboard():
    try:
        with open('leaderboard.txt', 'a+') as f:
            #Strip any whitespace from each line and Split each line by comma to seperate score and name
            leaderboard = [line.strip().split(',') for line in f.readlines()]           
            #Convert each score to an interger and create a list of tuples with score and name
            leaderboard = [(int(score), name) for score, name in leaderboard]
            #Sort the list of tuples by score in descending order
            leaderboard.sort(reverse=True)
            #Only keep the top 10 scores
            leaderboard = leaderboard[:10]
        return leaderboard
    except IOError:
        print("Error: Could not open leaderboard file")

# define a function called print_results
def print_results(num_correct, score, num, high_score):
    # print a formatted string that displays the number of correct answers out of the total number of questions
    print(f"\nYou got {num_correct} correct out of {num} questions")
    # check if score is greater than zero
    if score > 0:
        # if the score is greater than zero, print a formatted string that displays the score as an interger
        print(f"you got {int(score)} points")
    else:
        # if the score is not greater than zero, print string that says that you got zero points
        print("You got 0 points")
        # print a formated string that displays high score
    print(f"high score is {high_score}")

# defines a function called update_leaderboard
def update_leaderboard(score, player_name, high_score, leaderboard, num_correct, num):
        
    # check if the leaderboard is empty or if tuple of (score, player_name) is greater than the last element in leaderboard
    if not leaderboard or score > leaderboard[-1][0]:
        #open a file called leaderboard.txt in write mode
        with open('leaderboard.txt', 'w') as f:
            # append the tuple to the leaderboard list
            leaderboard.append((score, player_name))
            #sort leaderboard list in descending order
            leaderboard.sort(reverse=True)
            # slice leaderboard list to include the top 10 scores or elements only
            leaderboard = leaderboard[:10]
            # create a new list of formatted strings for each element in leaderboard list
            leaderboard = [f"{score},{name}" for score, name in leaderboard]
            # writes the elements of the leaderboard list to the file seperated by newlines and add a newline at the end
            f.write('\n'.join(leaderboard) + '\n')
            
        if score > high_score:
            high_score = score
            print("Wow! You got a high score!! Congratulations!!!")    
    return high_score
    
# defines a function called check_answer which takes 3 args: correct_answer, answer_label and labeled_alternatives. 
def check_answer(correct_answer, answer_label, labeled_alternatives):
    answer_is_correct = correct_answer == labeled_alternatives.get(answer_label)
    return labeled_alternatives.get(answer_label), answer_is_correct


# defines the play_question function. 
def play_question(num, question, data):
    labeled_alternatives = data["alternatives"]
    correct_answer = data["correct_answer"]
    answer_label, labeled_alternatives = ask_question(num, question, labeled_alternatives)
    answer_label = labeled_alternatives.get(answer_label, "")
    # calls the check_answer function with correct_answer, answer_label and labeled_alternatives as arguments
    if check_answer(correct_answer, answer_label, labeled_alternatives):
        
        question_score = calculate_score(answer_label, labeled_alternatives)
    else:
        # if check_answer returns False, set question_score to zero
        question_score = 0
    print_question_result(answer_label, correct_answer, question_score)
    return question_score, answer_label, correct_answer, labeled_alternatives 
         
   # defines the run_quiz function
def run_quiz():    
    try:
        # use input function to prompt the user to enter their name
        name = input("Enter your name: ")
        #set the initial value of high_score to zero
        high_score = 0
        # create an empty list called leaderboard
        leaderboard = []
        # use a while loop to keep running the quiz until the user chooses to stop
        while True:
            score = 0
            num_correct = 0
            # use the random sample function to select 7 random questions from the questions_dict dictionary
            random_questions = random.sample(list(questions_dict.items()), 7)
            # use a for loop to iterate over the enumerated random_questions list starting from index 1
            for num, (question, data) in enumerate(random_questions, start=1):
                question_score, answer_label, correct_answer, labeled_alternatives = play_question(num, question, data)
                score += question_score
                if check_answer(correct_answer, answer_label, labeled_alternatives):
                    num_correct += 1                              
             #   
            high_score = update_leaderboard(score, name, high_score, leaderboard, num_correct, num)
            print_results(num_correct, score, len(random_questions), high_score)
            # 
            if input("Do you want to play again? (y/n) ").lower() != 'y':
                #if their response is not y, break out of the while loop
                break
            # if a ValueError exception is raised during the execution of the try block, print out an error message
    except ValueError as e:
        print(f"Error: {e}")        
    except Exception as e:
        print(f"Error: {e}")
        exit()




def ask_question(num, question, alternatives=None):    
    print(f"\n{Fore.BLUE}Question {num}:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{question}?{Style.RESET_ALL}")
    # Shuffle and label the alternatives
    labeled_alternatives = shuffle_and_label(alternatives) if alternatives else None
    # Print each alternative with its letter label
    for label, alternative in labeled_alternatives.items():
        print(f"  {Fore.GREEN}{label}){Style.RESET_ALL} {Fore.GREEN}{alternative}{Style.RESET_ALL}")
    answer_label = input(f"\n{Fore.RED}\nChoice?{Style.RESET_ALL}")
   
    return answer_label, labeled_alternatives


# defines a function called shuffle_and_label that shuffles the alternative
def shuffle_and_label(alternatives):
    # use random.sample function to randomises the alternative answers, which includes the correct answer
    random_alternatives = random.sample(alternatives, len(alternatives))
    labeled_alternatives = dict(zip(ascii_lowercase, random_alternatives))
    return labeled_alternatives

# defines calculate_score function
def calculate_score(answer_label, labeled_alternatives):  
    #checks value associated with the key answer_label in the labeled_alternatives dictionary to see they are equal  
    if labeled_alternatives.get(answer_label) == labeled_alternatives.get(labeled_alternatives.get("correct")):
        return 695
    else:
        return 0 
    

def print_question_result(answer_label, correct_answer, question_score):
    if answer_label.strip() == "":
        print(f"The answer is {correct_answer!r}.")
    elif answer_label == correct_answer:
        print("Correct!")
        
    else:
        print(f"Incorrect! The answer is {correct_answer!r}.")
        


def view_leaderboard():
    try:
        with open('leaderboard.txt', 'r') as f:
            leaderboard = f.readlines()
            leaderboard = [line.strip().split(',') for line in leaderboard]
            leaderboard = [(int(score), name) for score, name in leaderboard]
            leaderboard.sort(reverse=True)
            for rank, (score, name) in enumerate(leaderboard, start=1):
                print(f"{rank}, {name}: {score}")
    except (FileNotFoundError, IOError):
        print("Error: Could not open leaderboard file.")
    except ValueError:
        print("Error: Could not parse leaderboard data.")
    except Exception as e:
        print(f"Error: {e}")