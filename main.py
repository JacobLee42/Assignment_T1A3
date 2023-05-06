
    #Using lists and tuples to avoid repeating code
  #Family Guy Quiz Questions and Answer key
QUESTIONS = [
    ("When the family became the Super Griffins, what was Chris's superpower?", "He can start fires with his mind"),
    ("Who provides the voice of Peter Griffin?", "Seth MacFarlane"),
    ("How old is Brian the dog in dog years?", "Seven"),
    ("Fill in the blank on this letter written by Peter; Dear_____, enclosed is a rubber band, a paper clip and a drinking straw. Please save my dog.", "MacGyver"),
    ("Peter begins exploiting Lois's fighting ability after she learns what fictional martial art?", "Tae-Jitsu"),
    ("Who provides the voice of Meg Griffin?", "Mila Kunis"),
    ("Peter's great great uncle Agnus Griffin invented what sport?", "Golf"),
    ("What did Peter and Lois's pet rock do the first day they took it home?", "It peed on the carpet"),
    ("What did Peter want to name Meg when she was born?", "Twiki"),
    ("When Peter turns the house into a puppet, what does it say?", "Bring me a toolshed, for I am hungry"),
    #General Knowledge Quiz Questions and Answer key
    ("What age is the recorded longest age that an elephant has ever lived?", "86 years"),
    ("what is a Tarsier?", "A Primate"),
    ("In darts, what is the most points you can score with a single throw?", "60 points"),
    ("Which of these animals does NOT appear in the Chinese Zodiac?", "Bear"),
    ("What is a Pomelo?", "The largest citrus fruit"),
    ("Who killed Greedo?", "Han Solo"),
    ("How many points is the letter X worth in Scrabble?", "Eight"),
    ("Who are known as Brahmins?", "Members of India's highest caste"),
    ("How many holes are on a standard bowling ball?", "Three"),
    ("How did Spider-man get his powers?", "Bitten by a radioactive spider"),
    #Capital Cities Of The World Questions and Answer key
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

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}?")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")


