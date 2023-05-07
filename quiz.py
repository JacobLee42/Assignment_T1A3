import sys
from questions import QUESTIONS
from string import ascii_lowercase
import random
    #Providing multiple choices for answers. Updated Questions and answers - 
    #Changed QUESTIONS to a dictionary where the keys are the questions and the values are the list of answer alternatives.

    #Family Guy Quiz Questions and Multiple choice answers




#Updated code from main.py to loop over the new dictionary. 
# For each question, you print the list of answers and then try to pick out the correct answer.
#Then I worked out how to use the sort() function to change the order of the answer alternatives.
#Added a label to each alternative and ask user to enter the label.


#Updated the code to use the enumerate() function to print the index of each answer alternative.




#for question, alternatives in QUESTIONS.items():
#    correct_answer = alternatives[0]
#    sorted_alternatives = sorted(alternatives)
#    for label, alternative in enumerate(sorted_alternatives): 
 #       print(f" {label}) {alternative}")

 #   answer_label = int(input(f"{question}? "))
 #   answer = sorted_alternatives[answer_label]
 #   if answer == correct_answer:
 #      print("Correct!")
 #   else:
 #      print(f"The answer is {correct_answer!r}, not {answer!r}")


 #Organised the jumbled alternative answers as sorted_alternatives. 
 # Input always returns a string so remebered to convert to an interger before using it the function.
#added num_correct function to keep track of user correct guesses. Worked out how to add score and high score tallies to function.
def run_quiz(player_name):
    num_correct = 0
    score = 0
    high_score = 0

#Wrote leaderboard.txt to create file when first high score is recorded on player first walkthrough of game. Appends the leaderboard list (high score)
    with open('leaderboard.txt', 'a+') as f:
        f.seek(0)
        leaderboard = f.readlines()
        leaderboard = [line.strip() for line in leaderboard]
        leaderboard = [line.split(',') for line in leaderboard]
        leaderboard = [(int(score), name) for score, name in leaderboard]
        leaderboard.sort(reverse=True)
        leaderboard = leaderboard[:10]
#Shuffle the questions and select first 7
    random_questions = random.sample(list(QUESTIONS.items()), 7)

    for num, (question, alternatives) in enumerate(QUESTIONS.items(), start = 1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        #Shuffle the alternatives
        random_alternatives = random.sample(alternatives, len(alternatives))
        labeled_alternatives = dict(zip(ascii_lowercase, random_alternatives))

        for label, alternative in labeled_alternatives.items():
                print(f"  {label}) {alternative}")

        answer_label = input("\nChoice? ")
        answer = labeled_alternatives.get(answer_label) 
        if answer == correct_answer:
            num_correct += 1
            score += 695
            print(" That is Correct! ")
            if score > high_score:
                high_score = score
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
            score += 0

    if (score, player_name) > leaderboard[-1]:
         with open('leaderboard.txt', 'w') as f:
              leaderboard.append((score, player_name))
              leaderboard.sort(reverse=True)
              leaderboard = leaderboard[:10]
              leaderboard = [f"{score},{name}" for score, name in leaderboard]
              f.write('\n'.join(leaderboard))
         


    print(f"\nYou got {num_correct} correct out of {num} questions")
    print(f"Your score is {score}")
    print(f"High score is {high_score}")

    return True if input("Do you want to play again? (y/n) ").lower() == 'y' else False

def view_leaderboard():
     with open('leaderboard.txt', 'r') as f:
          leaderboard = f.readlines()
          leaderboard = [line.strip().split(',') for line in leaderboard]
          leaderboard = [(int(score), name) for score, name in leaderboard]
          leaderboard.sort(reverse=True)
          for rank, (score, name) in enumerate(leaderboard, start=1):
               print(f"{rank}, {name}: {score}")
