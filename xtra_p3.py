"""
Modify this docstring.

Jim Crivello
1/30/23
Domain=Puzzles


Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest
import statistics


# read from second file and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace
  
# read from second file and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Done with files - let the files close and the work begin

# Remove duplicates by creating two sorted sets
# hint: use sorted() to sort the list
# hint: use set() to remove duplicates
# name them wordset1 and wordset2
# wordset1 = set()  # TODO fix this line
# wordset2 = set()  # TODO fix this line

wordlist1.sort()
wordlist2.sort()

wordset1 = set(wordlist1) 
wordset2 = set(wordlist2) 

# initialize a variable maxlen = 10
# maxlen = 1  # TODO fix this line
maxlen = 10 

# use a list comprension to get a list of words longer than 10
# for word in wordset1
# That is:
# in a list (e.g. square brackets)
# say "[Give me word (for each word in wordset1)
#      if len(word) is greater than maxlen]"
# then convert the list to a set to we can take the intersection
# hint: use set()
# name them longwordset1 and longwordset2

tempset1 = set()
for word in wordset1:
    if len(word) > maxlen:
        tempset1.add(word)

tempset2 = set()
for word in wordset2:
    if len(word) > maxlen:
        tempset2.add(word)

# Longwordset1 = set(wordset1)  # TODO: fix this line
# longwordset2 = set(wordset2)  # TODO: fix this line
longwordset1 = set(tempset1)
longwordset2 = set(tempset2)

# find the intersection of the two sets
# that is, the words in both longwordset1 1 & longwordset2
# name this variable longwords
longwords = longwordset1 & longwordset2

# print the length of the sets and the list
print(len(longwordset1))
print(len(longwordset2))
print(len(longwords))
print()
print(f"{sorted(longwords) = }")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")


"""
TESTING DONE
PS C:\Users\JMC\Documents\datafun-03-datatypes> & C:/Users/JMC/AppData/Local/Programs/Python/Python311/python.exe c:/Users/JMC/Documents/datafun-03-datatypes/xtra_p3.py
415
197
13

sorted(longwords) = ['conference.', 'conscience;', 'consequence;', 'constantly.', 'corruption,', 'countenance', 'countenance,', 'enterprise,', 'honourable.', 'immediately.', 'replication', 'themselves,', 'threatening']

TESTING...if nothing prints before the testing is done, you passed!
TESTING DONE
PS C:\Users\JMC\Documents\datafun-03-datatypes> 


"""