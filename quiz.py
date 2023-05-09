import sys
from questions import QUESTIONS
from string import ascii_lowercase
import random  
import time   

def run_quiz(player_name):
    num_correct = 0
    score = 0
    high_score = 0

    #Wrote leaderboard.txt to create file when first high score is recorded on player first walkthrough of game. Appends the leaderboard list (high score)
    #Open leaderboard.txt file. If it doesnt exist, create it

    with open('leaderboard.txt', 'a+') as f:
        f.seek(0)
        #Read the file and store each line as an element in the list
        leaderboard = f.readlines()
        #Strip any whitespace from each line
        leaderboard = [line.strip() for line in leaderboard]
        #Split each line by comma to seperate score and name
        leaderboard = [line.split(',') for line in leaderboard]
        #Convert each score to an interger and create a list of tuples with score and name
        leaderboard = [(int(score), name) for score, name in leaderboard]
        #Sort the list of tuples by score in descending order
        leaderboard.sort(reverse=True)
        #Only keep the top 10 scores
        leaderboard = leaderboard[:10]
    #Shuffle the questions and select first 7
    random_questions = random.sample(list(QUESTIONS.items()), 7)
    #Loop through each question and its alternatives
    for num, (question, alternatives) in enumerate(random_questions, start = 1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        #Shuffle the alternatives and label the with letters
        random_alternatives = random.sample(alternatives, len(alternatives))
        labeled_alternatives = dict(zip(ascii_lowercase, random_alternatives))
        #Print each alternative with its letter label
        for label, alternative in labeled_alternatives.items():
                print(f"  {label}) {alternative}")

        #Prompt user to select an answer and check if it is correct plus timer function
        start_time = time.time()
        answer_label = input("\nChoice? ")
        elapsed_time = time.time() - start_time
        time_left = 13 - elapsed_time
        if time_left < 0:
             time_left = 0
        score_per_second = 695 // 6
        score += max(0, int((time_left // 2) * -score_per_second))
        if answer_label.strip() == "" or time_left == 0:
             print(f"You ran out of time!!! The answer is {correct_answer!r}.")
             
        elif labeled_alternatives.get(answer_label) == correct_answer:
            num_correct += 1
            score += max(0, int(time_left * score_per_second))
            print(" That is Correct! ")
            if score > high_score:
                high_score = score
        else:
            print(f"Incorrect! The answer is {correct_answer!r}.")
        #Prompt the user to press enter to continue
        input("\nPress enter to continue to the next question...")
            


    #If the players score is higher than any score on the leaderboard, add it to leaderboard
    if not leaderboard or (score, player_name) > leaderboard[-1]:
         with open('leaderboard.txt', 'w') as f:
              leaderboard.append((score, player_name))
              leaderboard.sort(reverse=True)
              leaderboard = leaderboard[:10]
              leaderboard = [f"{score},{name}" for score, name in leaderboard]
              f.write('\n'.join(leaderboard))
         if score > high_score:
              high_score = score
              print("Wow! You got a high score!! Congratulations!!!")

    #Print the player's results and asks if they want to play again
    print(f"\nYou got {num_correct} correct out of {num} questions")
    print(f"Your score is {score}")
    print(f"High score is {high_score}")

    return True if input("Do you want to play again? (y/n) ").lower() == 'y' else False
   

    #Open leaderboard.txt and read its contents
def view_leaderboard():
     with open('leaderboard.txt', 'r') as f:
          leaderboard = f.readlines()
          #Strip any whitespace from each line
          leaderboard = [line.strip().split(',') for line in leaderboard]
          #Convert each score to an interger and create a list of tuples with score and name  
          leaderboard = [(int(score), name) for score, name in leaderboard]
          #Sort the list of tuples by score in descending order
          leaderboard.sort(reverse=True)
          #Print each score and name in the leaderboard with its rank  
          for rank, (score, name) in enumerate(leaderboard, start=1):  
               print(f"{rank}, {name}: {score}")
 