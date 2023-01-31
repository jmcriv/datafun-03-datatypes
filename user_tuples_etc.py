"""
Modify this docstring.

Jim Crivello
1/30/23
Domain=Puzzles

"""

# ==================================================================
# TASK 5       Introductory Screen Prints & Background Information
# ==================================================================

if __name__ == "__main__":
    print()
    print()
    print("Good morning! My name is Jim, and this program will focus on people I play games with and Tuple functions.")
    print()
    print()

# ==================================================================
# TASK 5       Tuple and More (Setup Tuples & Imports)
# ==================================================================

import statistics
import math
import random

# import any modules first

# Create some tuples
# tupleA = (1, 2, 3, 4, 5)
# tupleB = (4, 5, 6, 7, 8)

if __name__ == "__main__":
    print()
    print("My Tuesday group has five people. Here are the ages of the game players.")
    tupleA = (26, 35, 49, 54, 58)
    print(tupleA)
    print("My Friday group has six people. Here are the ages of the game players.")
    tupleB = (34, 35, 49, 54, 58, 62)
    print(tupleB)
    print()
    
    # tuple concatenation
    tupleCat = tupleA + tupleB

    # tuple repetition
    tupleAThrice = tupleA * 3

    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    print(f"{tupleA = }")
    print(f"{tupleB = }")
    print(f"{tupleCat = }")
    print(f"{tupleAThrice = }")

    tupleD = (1, 2, 3)
    hasOne = 1 in tupleD  # True
    hasFour = 4 in tupleD  # False
    print(f"{tupleD = }")

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (1, 2, 3)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    # Use tuples to return multiple values from a function

    print()
    print()
    print("Let's divide 45 by 4 to see the quotient and remainder.")
    x=45
    y=4
    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    q, r = divide_and_remainder(x, y)
    print(f"Quotient: {q}, Remainder: {r}")
    print()
    print()

    print()
    print("Let's work with Sets and use the numbers from our game group Tuples.")
    print("SET A=TUPLE A   SET B=TUPLE B")
    print()
    print()

    #setA = {1, 2, 3, 4, 5}
    #setB = {4, 5, 6, 7, 8}
    setA = ({tupleA})
    setB = ({tupleB})
    print(f"SET A: {setA}")
    print(f"SET B: {setB}")
    print()
    print()
    
    print("Let's make a Union of setA and setB.")
    print("setC = setA | setB")
    # set union
    setC = setA | setB
    print(f"SET C: {setC}")
    print()
    print()

    print("Let's make an Intersection of setA and setB by adjusting the groups to five people each.")
    setA = {24, 35, 48, 54, 58}
    setB = {34, 35, 49, 56, 62}
    print("setD = setA & setB")
    # set intersection
    setD = setA & setB
    print(f"SET D: {setD}")
    print()
    print()

    print("Let's find the Difference of setA and setB (items in setA, but not in setB).")
    print("setE = setA - setB")
    # set difference
    setE = setA - setB
    print(f"SET E: {setE}")
    print()
    print()
    print()

    # sets are often used to remove duplicates from a list
    # after gettin the set, convert it back to a list with list() or []
    print("Let's remove duplicates from a list. We will conver the list to a Set, and then back to a List to remove duplicates.")
    print("--------------------------------------------------------------------------------------------------------------------")
    listWords = ["crosswords", "jumbles", "logic", "suduko", "jumbles", "logic", "wordle"]
    print(f"List of Words with duplicates: {listWords}")
    setWords = set(listWords)
    print(f"Conversion to Set: {setWords}")
    listWordsNoDuplicates = list(setWords)
    listWordsNoDuplicates = [setWords]  # same as above
    print(f"List of Words with duplicates removed: {listWordsNoDuplicates}")
    print()
    print()

    playerA_dict = {"name": "Jim", "age": 54, "numwins": 19}
    playerB_dict = {"name": "Bob", "age": 62, "numwins": 22}
    skills_dict = {"low": 0, "medium": 1, "high": 2}
    players_dict = {
        "name": ["Dave", "Sue", "Debbie", "Wendy"],
        "age": [36, 48, 28, 36],
        "numwins": [25, 13, 20, 31],
    }

    print(f"List of Dictionaries")
    print("---------------------")
    print(f"Player A Dictionary: {playerA_dict}")
    print()
    print(f"Player B Dictionary: {playerB_dict}")
    print()
    print(f"Skills Dictionary: {skills_dict}")
    print()
    print(f"Remaining Players Dictionary: {players_dict}")
    print()
    print()
    print()

    # Define your PyBuddies in a dictionary
    # With few chnages, you could read in many PyBuddies from a JSON file.


    # In data anlytics, dictionaries are used to store and manipulate
    # tabular data, e.g. from database records or Excel rows.


    # Dictionaries can be used to store and aggregate statistical data,
    # such as counts or sums. For example, a dictionary of word-count pairs.

    print(f"Dictionary of Statistical and Aggregate Data")
    print("---------------------------------------------")

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    print(word_counts_dict)

    print()
    print()

