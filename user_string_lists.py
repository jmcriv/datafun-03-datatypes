"""
Modify this docstring.

Jim Crivello
1/30/23
Domain=Puzzles

"""

# ==================================================================
# TASK 3       Introductory Screen Prints & Background Information
# ==================================================================

if __name__ == "__main__":
    print()
    print()
    print("Good morning! My name is Jim, and this program will focus on games I have played and string functions.")
    print("I have developed 5 lists with names of games - all grouped by their first letter - A, B, C, D, and M.")
    print()
    print()

# ==================================================================
# TASK 4       String Lists (Setup Lists & Imports)
# ==================================================================

import statistics
import math
import random

listA = ["ABC", "Acrofit", "Acrostic", "Addoku", "Alphacipher", "Anagrams", "Anagrid", "Anakross"]
print("Here is LIST A")
print("----------------------------------------")
print(listA)
print()

listB = ["Backtrack", "Backwards", "Batoru", "Boggle", "Boxwise", "Bracer"]
print("Here is LIST B")
print("----------------------------------------")
print(listB)
print()

listC = ["Calcudoku", "Campixu", "Campsite", "CanCan", "Chopsticks"]
print("Here is LIST C")
print("----------------------------------------")
print(listC)
print()

listD = ["Dampfross", "Dateline", "Diagramless", "DigitALL", "Dilemma", "Dingbats", "Dominoes"]
print("Here is LIST D")
print("----------------------------------------")
print(listD)
print()

listE = ["Magipic", "Majipiku", "Masyu", "MinuPlu"]
print("Here is LIST E")
print("----------------------------------------")
print(listE)
print()
print()


# ==================================================================
# TASK 4       String Lists 1. Using Python Built-in Functions
# ==================================================================

if __name__ == "__main__":
    print("TASK 4 SECTION - String Lists 1. Using Python Built-in Functions:")
    print("=================================================================")
    print("We will be using the Len, Set, and Zip functions:")
    print()
    print("LIST A PROCESSING")
    print("-----------------")
    number = len(listA)
    print(f"LEN A = NUMBER OF ITEMS IN LIST A = {number}")
    setlistA = set(listA)
    print(f"SET A = {setlistA}")
    print()
    print("LIST B PROCESSING")
    print("-----------------")
    number = len(listB)
    print(f"LEN B = NUMBER OF ITEMS IN LIST B = {number}")
    setlistB = set(listB)
    print(f"SET B = {setlistB}")
    print()
    print("LIST C PROCESSING")
    print("-----------------")
    number = len(listC)
    print(f"LEN C = NUMBER OF ITEMS IN LIST C = {number}")
    setlistC = set(listC)
    print(f"SET C = {setlistC}")
    print()
    print("LIST D PROCESSING")
    print("-----------------")
    number = len(listD)
    print(f"LEN D = NUMBER OF ITEMS IN LIST D = {number}")
    setlistD = set(listD)
    print(f"SET D = {setlistD}")
    print()
    print("LIST E PROCESSING")
    print("-----------------")
    number = len(listE)
    print(f"LEN E = NUMBER OF ITEMS IN LIST E = {number}")
    setlistE = set(listE)
    print(f"SET E = {setlistE}")
    print()
    print("ZIP = TUPLE of LIST A & LISTB")
    print("-----------------------------")
    for LA, LB in zip(listA,listB):        
        print(f'LA={listA}; LB={listB}')
    print()
    print("ZIP = TUPLE of LIST C & LIST D & LIST E")
    print("---------------------------------------")
    for LC, LE, LF in zip(listC,listD,listE):      
        print(f'LC={listC}; LD={listD}; LE={listE}')
    print()
    print()


# ==================================================================
# TASK 4       String Lists 2. Random Choice
# ==================================================================

if __name__ == "__main__":
    print("TASK 4 SECTION - String Lists 2. Random Lists:")
    print("==============================================")
    print("We will be using the Random Choice function to pick one random game from each list.")
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
        f"Five random games I like to play are {random.choice(listA)}, {random.choice(listB)}, "
        f"{random.choice(listC)}, {random.choice(listD)}, and {random.choice(listE)}."
    )
    print()
    print(sentence)
    print()
    print()
    
# ==================================================================
# TASK 4       String Lists 3. Get Unique Words
# ==================================================================

if __name__ == "__main__":
    print("TASK 4 SECTION - String Lists 3. Get Unique Words:")
    print("==================================================")
    print("We will be using the Open, Read, Split, and Set functions.")
    print()

    print("OPEN TEXT FILE (text_names_in) AND PRINT CONTENTS")
    print("-------------------------------------------------")
    names = open('text_names_in.txt')
    namescontents = names.read()
    print(namescontents)
    print()
    print()
    
    print("OPEN TEXT FILE (text_names_in), READ CONTENTS, AND PRINT CONTENTS")
    print("-----------------------------------------------------------------")
    with open('text_names_in.txt') as namesread:
        readcontents = namesread.read()
        print(readcontents)
        print()
        print()

    print("USE SET, OPEN TEXT FILE (text_names_in), READ UNIQUE CONTENTS, OUTPUT UNIQUE TO NEW FILE, AND PRINT NEW FILE CONTENTS")
    print("       (FYI - Added duplicate items to end of INPUT file since there were no duplicates in the file.)")
    print("----------------------------------------------------------------------------------------------------------------------")
    print()
    foundset = set()
    with open('text_names_in.txt') as inputfile:
        with open('text_names_out.txt','w') as outputfile:
            for line in inputfile:
                if line not in foundset:
                    outputfile.write(line)
                    foundset.add(line)
        with open('text_names_out.txt') as outputfile:
            readcontents = outputfile.read()
            print(readcontents)
            print()

    
    print("USE SET, OPEN, READ, and SPLIT functions to pull a text file's data starting with letter P. Using file text_names_in.")
    print("       (FYI - Added duplicate items to end of INPUT file since there were no duplicates in the file.)")
    print("---------------------------------------------------------------------------------------------------------------------")
    print()
    foundset = set()
    with open('text_names_in.txt') as inputfile:
        with open('text_names_out2.txt','w') as outputfile:
            for line in inputfile:
                if line.startswith('P'):
                    text = str(line.split(', ',2))
                    outputfile.write(text)
                    foundset.add(line)
        with open('text_names_out2.txt') as outputfile:
            readcontents1 = outputfile.read()
            print("OUTPUT FILE CONTENT")
            print(readcontents1)
            print()
            readcontents2 = foundset
            print("SET CONTENT")
            print(readcontents2)
            print()

    print("USE SPLIT functions to pull a text file's data and separate with commas.")
    print("------------------------------------------------------------------------")
    print()

    # def split(word):
    #     return list(word)
    # word = "BINGO"
    # print(split(word))

    
    with open('text_simple_in.txt') as inputfile2:
        readcontentsX = inputfile2.read()
        print("TEXT SIMPLE IN FILE BEFORE SPLIT")
        print(readcontentsX)
        print()
          
    foundset = set()
    with open('text_simple_in.txt') as inputfile2:
        with open('text_simple_out.txt','w') as outputfile2:
            print("TEXT SIMPLE IN FILE AFTER SPLIT")
            for line in inputfile2:
                text1=line
                def split(text1):
                    return list(text1)
                # text1=line 
                print(split(text1)) 
                text2 = str(split(text1))           
                outputfile2.write(text2)
                foundset.add(line)

    print()
    print()
    print("USE SORT and LEN")
    print("----------------")
    print()
    
    
    foundset = set()
    with open('text_names_in2.txt') as inputfile:
        with open('text_names_out3.txt','w') as outputfile:
            contentsinput1 = inputfile.readlines()
            print("SORTED NAMES FROM TEXT FILE- SEQUENTIAL")
            contentsinput1.sort()
            print(contentsinput1)
            outputfile.write(str(contentsinput1))
            print("COUNT OF NAMES IN TEXT_NAMES_3 (NORMAL SORT)")
            leninput1 = len(contentsinput1)
            print(leninput1)
            print()
    with open('text_names_in2.txt') as inputfile:
        with open('text_names_out4.txt','w') as outputfile:
            contentsinput2 = inputfile.readlines()
            print("SORTED NAMES - REVERSE")
            contentsinput2.sort(reverse=True)
            print(contentsinput2)
            outputfile.write(str(contentsinput2))
            print("COUNT OF NAMES IN TEXT_NAMES_4 (REVERSE SORT)")
            leninput2 = len(contentsinput2)
            print(leninput2)
            print()
        
