
    #Providing multiple choices for answers. Updated Questions and answers - 
    #Changed QUESTIONS to a dictionary where the keys are the questions and the values are the list of answer alternatives.

    #Family Guy Quiz Questions and Multiple choice answers

QUESTIONS = {
    "When the family became the Super Griffins, what was Chris's superpower?": [
        "He can start fires with his mind",
        "Super Speed",
        "He can turn invisible",
        "He can control lemmings by whistling",
        

    ],
    "Who provides the voice of Peter Griffin?": [
        "Seth MacFarlane",
        "Brian Peter Green",
        "Seth Rogan",
        "Bill Burr",
        

    ],
    "How old is Brian the dog in dog years?": [
        "Seven","One", "Nine", "Five",

    ],
    "Fill in the blank on this letter written by Peter; Dear_____, enclosed is a rubber band, a paper clip and a drinking straw. Please save my dog.": [
        "MacGyver","Magnum P.I.", "Die Hard", "Harry Potter", 

    ],
    "Peter begins exploiting Lois's fighting ability after she learns what fictional martial art?": [
        "Tae-Jitsu", "Tae-Bo", "Fight Club", "Tang-soo-do",

    ],
    "Who provides the voice of Meg Griffin?": [
        "Mila Kunis","Meg Ryan", "Jodie Foster", "Nancy Cartwright", 

    ],
    "Peter's great great uncle Agnus Griffin invented what sport?": [
        "Golf","Badmington", "Frisbee Golf", "Synchronised Swimming",

    ],
    "What did Peter and Lois's pet rock do the first day they took it home?": [
        "It peed on the carpet",
        "It ran into oncoming traffic",
        "It attacked the mailman",
        "It ate all the food that was on the table for dinner",

    ],
    "What did Peter want to name Meg when she was born?": [
        "Twiki",
        "Princess Fairybottom",
        "Heavenly Hiraani Tiger Lily Hutchence Geldof-Griffin",
        "Dianne Simmons Griffin",

    ],
    "When Peter turns the house into a puppet, what does it say?": [
        "Bring me a toolshed, for I am hungry",
        "Bring me Kevin Bacon nomnomnom",
        "Hey you! What you lookin at!",
        "Hey Lois! Look at me!",
    #General knowledge quiz questions and multiple choice answers
    ],
    "What is age is the longest recorded age that an elephant has ever lived?": [
        "86 years","17 years", "49 years", "142 years",

    ],
    "What is a Tarsier?": [
        "A primate","A bird", "A marsupial", "A lizard", 

    ],
    "In darts, what's the most points you can score with a single throw?": [
       "60 points", "20 points", "50 points", "100 points",

    ],
    "Which of these animals does NOT appear in the Chinese zodiac?": [
        "Bear", "Dog", "Dragon", "Rabbit",

    ],
    "What is a Pomelo?": [
        "The largest citrus fruit",
        "A breed of dog", 
        "An old fashioned punching bag", 
        "A type of hat", 
        

    ],
    "Who killed Greedo?": [
        "Han Solo", "Hannibal Lecter", "Harry Potter", "Hercules",

    ],
    "How many points is the letter X worth in Scrabble?": [
        "Eight", "Zero", "Eleven", "Four", 

    ],
    "Who are known as Brahmins?": [
        "Members of India's highest caste",
        "Surfers in California",  
        "It's a totally made up word", 
        "Hill people from the Appalachian Mountains",

    ],
    "How many holes are on a standard bowling ball?": [
        "Three", "Two", "Five", "Seven",

    ],
    "How did Spider-man get his powers?": [
        "Bitten by a radioactive spider",
        "He was born with them",
        "Military experiment gone horribly wrong",
        "Woke up with them after a strange dream",

    #Capital Cities of the World questions and Multiple choice answers
    ],
    "What is the capital of Spain?": [
        "Madrid", "Salvador", "Gqeberha", "Belmopan", 

    ],
    "What is the capital of Italy?": [
        "Rome", "Ankara", "Gyros", "Reggiano",

    ],
    "What is the capital of Germany?": [
       "Berlin", "Bruge", "Bandung", "Brassels",

    ],
    "What is the capital of Canada?": [
        "Ottawa", "Toronto", "Winnipeg", "Montreal",

    ],
    "What is the capital of Lebanon?": [
        "Beirut", "Durban", "Gaborone", "Lagos",

    ],
    "What is the capital of Argentina?": [
        "Buenos Aires", "Nelson", "Brasilia", "Dodoma",

    ],
    "What is the capital of Brazil?": [
        "Brasilia", "Dodoma", "Mombasa", "Doha",

    ],
    "What is the capital of Colombia?": [
        "Bogota", "Mandalay", "Bern", "Edirne",

    ],
    "What is the capital of North Korea?": [
        "Pyongyang", "Bloemfontein", "Port Harcourt", "Gyeongbokgung",

    ],
    "What is the capital of Kenya?": [
        "Nairobi", "Kisumu", "Namibia", "Georgetown",

    ],


#Updated code from main.py to loop over the new dictionary. 
# For each question, you print the list of answers and then try to pick out the correct answer.
#Then I worked out how to use the sort() function to change the order of the answer alternatives.
#Added a label to each alternative and ask user to enter the label.


#Updated the code to use the enumerate() function to print the index of each answer alternative.


}

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

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start = 1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label) 
    if answer == correct_answer:
        print("* Correct! *")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")