
    #Family Guy Quiz
QUESTIONS = [
    ("When the family became the Super Griffins, what was Chris's superpower?", "He can start fires with his mind"),
    ("Who provides the voice of Peter Griffin?", "Seth Macfarlane"),
    ("How old is Brian the dog in dog years?", "Seven"),
    ("Fill in the blank on this letter written by Peter; Dear_____, enclosed is a rubber band, a paper clip and a drinking straw. Please save my dog.", "MacGyver"),
    ("Peter begins exploiting Lois's fighting ability after she learns what fictional martial art?", "Tae-Jitsu"),
    ("Who provides the voice of Meg Griffin?", "Mila Kunis"),
    ("Peter's great great uncle Agnus Griffin invented what sport?", "Golf"),
    ("What did Peter and Lois's pet rock do the first day they took it home?", "It peed on the carpet"),
    ("What did Peter want to name Meg when she was born?", "Twiki"),
    ("When Peter turns the house into a puppet, what does it say?", "Bring me a toolshed, for I am hungry"),
    #General Knowledge Quiz
    ("What age is the recorded longest age that an elephant has ever lived?", "86 years"),
    ("what is a Tarsier?", "A Primate"),
    ("In darts, what is the most points you can score with a single throw?", "60"),
    ("Which of these animals does NOT APPEAR in the Chinese Zodiac?", "Bear"),
    ("What is a Pomelo?", "The largest citrus fruit"),
    ("Who killed Greedo?", "Han Solo"),
    ("How many points is the letter X worth in Scrabble?", "8"),
    ("Who are known as Brahmins?", "Members of India's highest castle"),
    ("How many holes are on a standard bowling ball?", "3"),
    ("How did Spider-man get his powers?", "Bitten by a radioactive spider"),
    #Capital Cities Of The World
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the Capital of Canada?", "Ottawa"),
    ("What is the capital of Lebanon?", "Beirut"),
    ("What is the capital of Argentina?", "Buenos Aires"),
    ("What is the capital of Brazil?", "Brasilia"),
    ("What is the capital of Colombia?", "Bogota"),
    ("What is the capital of North Korea?", "Pyongyang"),
    ("What is the capital of Kenya?", "Nairobi"),

]














QUESTIONS = {
    "When the family became The Super Griffins, what was Chris's superpower?": [
        "Super Speed",
        "He can turn invisible",
        "He can control lemmings by whistling",
        "He can start fires with his mind",

    ],
    "Who provides the voice of Peter Griffin?": [
        "Brian Peter Green",
        "Seth Rogan",
        "Bill Burr",
        "Seth MacFarlane",

    ],
    "How old is Brian the dog in dog years?": [
        "One", "Nine", "Seven", "Five",

    ],
    "Fill in the blank on this letter written by Peter; Dear_____, enclosed is a rubber band, a paper clip and a drinking straw. Please save my dog.": [
        "Magnum P.I.", "Die Hard", "Harry Potter", "MacGyver",

    ],
    "Peter begins exploiting Lois's fighting ability after she learns what fictional martial art?": [
        "Tae-Jitsu", "Tae-Bo", "Fight Club", "Tang-soo-do",

    ],
    "Who provides the voice of Meg Griffin?": [
        "Meg Ryan", "Jodie Foster", "Nancy Cartwright", "Mila Kunis",

    ],
    "Peter's great great uncle Agnus Griffin invented what sport?": [
        "Badmington", "Golf", "Frisbee Golf", "Synchronised Swimming",

    ],
    "What did Peter and Lois's pet rock do the first day they took it home?": [
        "It ran into oncoming traffic",
        "It attacked the mailman",
        "It peed on the carpet",
        "It ate all the food that was on the table for dinner",

    ],
    "What did Peter want to name Meg when she was born?": [
         "Princess Fairybottom", "Heavenly Hiraani Tiger Lily Hutchence Geldof-Griffin", "Twiki", "Dianne Simmons Griffin",

    ],
    "When Peter turns the house into a puppet, what does it say?": [
        "Bring me a toolshed, for I am hungry",
        "Bring me Kevin Bacon nomnomnom",
        "Hey you! What you lookin at!",
        "Hey Lois! Look at me!",
    ],


}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives): 
        print(f" {label}) {alternative}")

        answer_label = int(input(f" {question}? "))
        answer = sorted_alternatives[answer_label]
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")

