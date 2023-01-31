"""


PS C:\Users\JMC\Documents\datafun-03-datatypes> & C:/Users/JMC/AppData/Local/Programs/Python/Python311/python.exe c:/Users/JMC/Documents/datafun-03-datatypes/user_tuples_etc.py 

Good morning! My name is Jim, and this program will focus on people I play games with and Tuple functions.


My Tuesday group has five people. Here are the ages of the game players.
(26, 35, 49, 54, 58)
My Friday group has six people. Here are the ages of the game players.
(34, 35, 49, 54, 58, 62)

tupleA = (26, 35, 49, 54, 58)
tupleB = (34, 35, 49, 54, 58, 62)
tupleCat = (26, 35, 49, 54, 58, 34, 35, 49, 54, 58, 62)
tupleAThrice = (26, 35, 49, 54, 58, 26, 35, 49, 54, 58, 26, 35, 49, 54, 58)
tupleD = (1, 2, 3)


Let's divide 45 by 4 to see the quotient and remainder.
Quotient: 11, Remainder: 1



Let's work with Sets and use the numbers from our game group Tuples.
SET A=TUPLE A   SET B=TUPLE B


SET A: {(26, 35, 49, 54, 58)}
SET B: {(34, 35, 49, 54, 58, 62)}


Let's make a Union of setA and setB.
setC = setA | setB
SET C: {(26, 35, 49, 54, 58), (34, 35, 49, 54, 58, 62)}


Let's make an Intersection of setA and setB by adjusting the groups to five people each.
setD = setA & setB
SET D: {35}


Let's find the Difference of setA and setB (items in setA, but not in setB).
setE = setA - setB
SET E: {48, 24, 58, 54}



Let's remove duplicates from a list. We will conver the list to a Set, and then back to a List to remove duplicates.
--------------------------------------------------------------------------------------------------------------------
List of Words with duplicates: ['crosswords', 'jumbles', 'logic', 'suduko', 'jumbles', 'logic', 'wordle']
Conversion to Set: {'crosswords', 'jumbles', 'suduko', 'logic', 'wordle'}
List of Words with duplicates removed: [{'crosswords', 'jumbles', 'suduko', 'logic', 'wordle'}]


List of Dictionaries
---------------------
Player A Dictionary: {'name': 'Jim', 'age': 54, 'numwins': 19}

Player B Dictionary: {'name': 'Bob', 'age': 62, 'numwins': 22}

Skills Dictionary: {'low': 0, 'medium': 1, 'high': 2}

Remaining Players Dictionary: {'name': ['Dave', 'Sue', 'Debbie', 'Wendy'], 'age': [36, 48, 28, 36], 'numwins': [25, 13, 20, 31]}



Dictionary of Statistical and Aggregate Data
---------------------------------------------
{'One': 1, 'fish': 3, 'two': 1, 'red': 1, 'blue': 1, 'fish.': 1}


PS C:\Users\JMC\Documents\datafun-03-datatypes> 

"""