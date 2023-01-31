"""
Modify this docstring.

Jim Crivello
1/30/23
Domain=Puzzles

"""

import statistics
import math
import random

# ==================================================================
# TASK 4       Introductory Screen Prints & Background Information
# ==================================================================

if __name__ == "__main__":
    print()
    print("====================")
    print("TASK 4 PROGRAM START")
    print("====================")
    print()


# ==================================================================
# TASK 4       String Lists (Setup Lists)
# ==================================================================

listA = ["ABC", "Acrofit", "Acrostic", "Addoku", "Alphacipher", "Anagrams", "Anagrid", "Anakross"]
print("LIST A")
print(listA)
print()

listB = ["Backtrack", "Backwards", "Batoru", "Boggle", "Boxwise", "Bracer"]
print("LIST B")
print(listB)
print()

listC = ["Calcudoku", "Campixu", "Campsite", "CanCan", "Chopsticks"]
print("LIST C")
print(listC)
print()

listD = ["Dampfross", "Dateline", "Diagramless", "DigitALL", "Dilemma", "Dingbats", "Dominoes"]
print("LIST D")
print(listD)
print()

listE = ["Magipic", "Majipiku", "Masyu", "MinuPlu"]
print("LIST E")
print(listE)
print()


# ==================================================================
# TASK 4       String Lists 1. Using Python Built-in Functions
# ==================================================================

if __name__ == "__main__":
    print("TASK 4 SECTION - String Lists 1. Using Python Built-in Functions:")
    print("=================================================================")
    print("We will be calculating assorted built-in functions including:")
    print("Len, Set, and Zip.")
    print()
    print("LIST A PROCESSING")
    print("-----------------")
    number = len(listA)
    print(f"NUMBER OF ITEMS IN LIST A = {number}")
    setlistA = set(listA)
    print(f"SET = {setlistA}")
    print()
    print("LIST B PROCESSING")
    print("-----------------")
    number = len(listB)
    print(f"NUMBER OF ITEMS IN LIST B = {number}")
    setlistB = set(listB)
    print(f"SET = {setlistB}")
    print()
    print("LIST C PROCESSING")
    print("-----------------")
    number = len(listC)
    print(f"NUMBER OF ITEMS IN LIST C = {number}")
    setlistC = set(listC)
    print(f"SET = {setlistC}")
    print()
    print()
    print("LIST D PROCESSING")
    print("-----------------")
    number = len(listD)
    print(f"NUMBER OF ITEMS IN LIST D = {number}")
    setlistD = set(listD)
    print(f"SET = {setlistD}")
    print()
    print("LIST E PROCESSING")
    print("-----------------")
    number = len(listE)
    print(f"NUMBER OF ITEMS IN LIST E = {number}")
    setlistE = set(listE)
    print(f"SET = {setlistE}")
    print()
    print("TUPLE of LIST A & LISTB")
    print("-----------------------")
    for LA, LB in zip(listA,listB):        
        print(f'LA={listA}; LB={listB}')
    print()
    print("TUPLE of LIST C & LIST D & LIST E")
    print("--------------------------------")
    for LC, LE, LF in zip(listC,listD,listE):      
        print(f'LC={listC}; LD={listD}; LE={listE}')
    print()


# ==================================================================
# TASK 4       String Lists 2. Random Choice
# ==================================================================

if __name__ == "__main__":
    print("TASK 4 SECTION - String Lists 2. Random Lists:")
    print("==============================================")
    print("We will be using the Random Choice function")
    print()

    listA = ["ABC", "Acrofit", "Acrostic", "Addoku", "Alphacipher", "Anagrams", "Anagrid", "Anakross"]
    print("LIST A")
    print(listA)
    print()

    listB = ["Backtrack", "Backwards", "Batoru", "Boggle", "Boxwise", "Bracer"]
    print("LIST B")
    print(listB)
    print()

    listC = ["Calcudoku", "Campixu", "Campsite", "CanCan", "Chopsticks"]
    print("LIST C")
    print(listC)
    print()

    listD = ["Dampfross", "Dateline", "Diagramless", "DigitALL", "Dilemma", "Dingbats", "Dominoes"]
    print("LIST D")
    print(listD)
    print()

    listE = ["Magipic", "Majipiku", "Masyu", "MinuPlu"]
    print("LIST E")
    print(listE)
    print()

    sentence = (
        f"The five games I like to play the most are {random.choice(listA)}, {random.choice(listB)}, "
        f"{random.choice(listC)}, {random.choice(listD)}, and {random.choice(listE)}."
    )
    print()
    print(sentence)
    print()
    

    

"""
# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":


Examples of using string lists


import random

# Define a string list
list_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

# Define a list of outcomes
list_outcomes = ["win", "lose", "draw"]

# Define a list of calls
list_calls = ["heads", "tails"]

# Define a list for rock, paper, scissors
list_rps = ["rock", "paper", "scissors"]

# Define a list of colors
list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Define a list of nouns
list_nouns = ["dog", "cat", "mouse", "bird", "fish", "snake"]

# Define a list of verbs
list_verbs = ["runs", "jumps", "swims", "flies", "crawls", "studies"]

# Define a list of adjectives
list_adjectives = ["happy", "sad", "angry", "scared", "confused", "bored"]

# Define a list of adverbs
list_adverbs = ["quickly", "slowly", "happily", "sadly", "angrily", "scaredly"]


# read in woodchuck to get a list of words
with open("text_woodchuck.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates

# Print the count and list of words
word_ct = len(list_words)

# Print the count and list of unique words
unique_word_ct = len(unique_words)


# Create a random sentence
# e.g. "The angry dog runs quickly."
sentence = (
    f"The {random.choice(list_adjectives)} {random.choice(list_nouns)} "
    f"{random.choice(list_verbs)} {random.choice(list_adverbs)}."
)
print()
print(sentence)
print()
print("To see more results, add print statements to the code.")
print("To play a continuous game, modify the code.")
print("Use these examples to learn lists and transformations.")
print("Then apply what you know to your domain.")
print()


# Game bot for rock, paper, scissors ................

# Define a function to get the winner message
# Use keyword arguments to be clear about the order of the arguments
def get_winner_message(userguess, botguess):
    if userguess == botguess:
        return "We tied!"
    elif userguess == "rock":
        if botguess == "paper":
            return "I win!"
        else:
            return "You win!"


ready_for_continous_game = False  # change this when ready

while True:
    if not ready_for_continous_game:
        quit()  # don't get stuck in an infinite loop until ready

    print()
    user_choice = input("Say rock, paper, or scissors or q to quit:")
    if user_choice == "q":
        break  # break out of the loop
    # if still here, the bot makes a choice
    # don't indent unnecessarily
    bot_choice = random.choice(list_rps)
    print(f"You said {user_choice}.")
    print(f"I said {bot_choice}.")
    # When calling a function, the order of arguments matters!
    # We don't want to accidentally provide the guesses in the wrong order
    # So we'll use keyword arguments so the order doesn't matter
    msg1 = get_winner_message(userguess=user_choice, botguess=bot_choice)
    msg2 = get_winner_message(botguess=bot_choice, userguess=user_choice)
    if msg1 == msg2:
        print(msg1)
    print()
    print("This program will run forever unless you type q to quit.")
    print("or use Ctrl-C to stop the program.")
    print()

"""