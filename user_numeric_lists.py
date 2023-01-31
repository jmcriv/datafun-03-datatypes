"""
Modify this docstring.

Jim Crivello
1/30/23
Domain=Puzzles

"""

import statistics
import math

# ==================================================================
# INTRODUCTORY SCREEN PRINTS - BACKGROUND INFORMATION
# ==================================================================

if __name__ == "__main__":
    print()
    print()
    print("Good morning! My name is Jim, and I am going through my Grandpa's attic.")
    print("Grandpa enjoyed doing jigsaw puzzles. He was great at putting pieces back in the boxes.")
    print("His shelf with the puzzles fell over, and Grandpa put the pieces back into the boxes.")
    print("Unfortunately, when putting them back, he guessed at colors as to which pieces went where.")
    print("He was close, but now the totals for piece count and box count don't match.")
    print("Please help us to review the data, so we can put the pieces where they go and solve this, excuse the pun, puzzle.")
    print("We had some students help us count the pieces in each of the 29 boxes as an extra credit assignment.")
    print("The totals for this box count are in LIST 1. There were 22,300 total pieces.")
    print("The 29 boxes should have a total of 22,300 pieces, so no pieces are missing - just some missplaced.")
    print("The totals of what should be in each box are in lid_count_list.")
    print("Each line in LIST 1(actual box_count_list) corresponds to the same line in lid_count_list.")
    print("LIST X = Times, in hours, it took each of the 10 students to complete the extra credit work.")
    print("LIST Y = Number of pieces each of the 10 students counted.")
    print()


# ==================================================================
# SETUP LISTS      (Task 3. Numeric Lists)
# ==================================================================

list1= [
    1254,
    634,
    795,
    466,
    1059,
    306,
    849,
    763,
    196,
    846,
    1197,
    979,
    1312,
    670,
    777,
    1204,
    157,
    164,
    809,
    609,
    788,
    487,
    1462,
    958,
    961,
    1032,
    403,
    909,
    254,
]

lid_count_list = [
    1250,
    650,
    800,
    450,
    1050,
    300,
    850,
    750,
    200,
    850,
    1200,
    1000,
    1300,
    650,
    800,
    1200,
    150,
    150,
    850,
    600,
    800,
    500,
    1450,
    950,
    950,
    1050,
    400,
    900,
    250,
]

print("LIST 1")
print(list1)

listx = [
    1,
    2,
    4,
    5,
    6,
    7,
    8,
    10,
    12,
    13,
]

print("LIST X")
print(listx)

listy = [
    423,
    912,
    1212,
    1466,
    1748,
    1871,
    2078,
    3158,
    4520,
    4912,
]

print("LIST Y")
print(listy)
print()


# ==================================================================
# TASK 3      Lists 1. List Statistics
# ==================================================================


if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 1: LIST STATISTICS")
    print("=======================================")
    print("We will be calculating the mean, median, and mode.")
    print("We will also be calculating the standard deviation and variance.")
    print()
    print("LIST 1 STATISTICS")
    print("-----------------")
    mean = round(statistics.mean(list1),2)
    print(f"LIST 1 Mean = {mean}")  
    median = statistics.median(list1)
    print(f"LIST 1 Median = {median}") 
    mode = statistics.mode(list1)
    print(f"LIST 1 Mode = {mode}") 
    stdev = round(statistics.stdev(list1),2)
    print(f"LIST 1 STDEV = {stdev}")
    variance = round(statistics.variance(list1),2)
    print(f"LIST 1 Variance = {variance}") 
    print()
    print("LIST X STATISTICS")
    print("-----------------")
    mean = round(statistics.mean(listx),2)
    print(f"LIST X Mean = {mean}")  
    median = statistics.median(listx)
    print(f"LIST X Median = {median}") 
    mode = statistics.mode(listx)
    print(f"LIST X Mode = {mode}") 
    stdev = round(statistics.stdev(listx),2)
    print(f"LIST X STDEV = {stdev}")
    variance = round(statistics.variance(listx),2)
    print(f"LIST X Variance = {variance}") 
    print()
    print("LIST Y STATISTICS")
    print("-----------------")
    mean = round(statistics.mean(listy),2)
    print(f"LIST Y Mean = {mean}")  
    median = statistics.median(listy)
    print(f"LIST Y Median = {median}") 
    mode = statistics.mode(listy)
    print(f"LIST Y Mode = {mode}") 
    stdev = round(statistics.stdev(listy),2)
    print(f"LIST Y STDEV = {stdev}")
    variance = round(statistics.variance(listy),2)
    print(f"LIST Y Variance = {variance}") 
    print()

# ==================================================================
# TASK 3      Lists 2. Correlation and Prediction
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 2: CORRELATION & PREDICTION")
    print("================================================")
    print("We will be calculating the Slope and Variance of LIST X & LIST Y.")
    print("We will be calculating the future value of LIST Y based on next LIST X value=15.")
    print()
    slope, intercept = statistics.linear_regression(listx,listy)
    print(f"SLOPE = {slope}")
    print(f"INTERCEPT = {intercept}")
    future_x = 15
    future_y = round(slope * future_x + intercept)
    print(f"FUTURE X = {future_x}")
    print(f"FUTURE Y = {future_y}")
    print()
    print()

# ==================================================================
# TASK 3      Lists 3. Using Python Built-In Functions
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 3: USING PYTHION BUILT-IN FUNCTIONS")
    print("=================================================")
    print("We will be calculating assorted built-in functions including:")
    print("Min, Max, Len, Sum, Average, Set, Sorted.")
    print()
    print("LIST 1 FUNCTIONS")
    print("----------------")
    minimum = min(list1)
    print(f"MINIMUM = {minimum}")
    maximum = max(list1)
    print(f"MAXIMUM = {maximum}")
    number = len(list1)
    print(f"NUMBER = {number}")
    sumlist1 = sum(list1)
    print(f"SUM = {sumlist1}")
    average = round(sumlist1 / number,2)
    print(f"AVERAGE = {average}")
    setlist1 = set(list1)
    print(f"SET = {setlist1}")
    list1.sort()
    print(f"SORTED LIST 1 - SEQUENTIAL")
    print(list1)
    list1.sort(reverse=True)
    print(f"SORTED LIST 1 - REVERSE")
    print(list1)
    print()
    print("LIST X FUNCTIONS")
    print("----------------")
    minimum = min(listx)
    print(f"MINIMUM = {minimum}")
    maximum = max(listx)
    print(f"MAXIMUM = {maximum}")
    number = len(listx)
    print(f"NUMBER = {number}")
    sumlistx = sum(listx)
    print(f"SUM = {sumlistx}")
    average = round(sumlistx / number,2)
    print(f"AVERAGE = {average}")
    setlistx = set(listx)
    print(f"SET = {setlistx}")
    listx.sort()
    print(f"SORTED LIST X - SEQUENTIAL")
    print(listx)
    listx.sort(reverse=True)
    print(f"SORTED LIST X - REVERSE")
    print(listx)
    print()
    print("LIST Y FUNCTIONS")
    print("----------------")
    minimum = min(listy)
    print(f"MINIMUM = {minimum}")
    maximum = max(listy)
    print(f"MAXIMUM = {maximum}")
    number = len(listy)
    print(f"NUMBER = {number}")
    sumlisty = sum(listy)
    print(f"SUM = {sumlisty}")
    average = round(sumlisty / number,2)
    print(f"AVERAGE = {average}")
    setlisty = set(listy)
    print(f"SET = {setlisty}")
    listy.sort()
    print(f"SORTED LIST Y - SEQUENTIAL")
    print(listy)
    listy.sort(reverse=True)
    print(f"SORTED LIST Y - REVERSE")
    print(listy)
    print()

# ==================================================================
# TASK 3      Lists 4. List Methods
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 4 : LIST METHODS")
    print("=====================================")
    print("We will be exploring list methods including:")
    print("Append, Extend, Insert, Remove, Count, Sort, Copy, Pop.")
    print()
    
    lst = [
        1,
        2,
        2,
        3,
        4,
        5,
        7,
        ]

    lst.append(8)
    print(f"LST appended with #8 = {lst}")
    
    lst2 = [
        10,
        11,
        12,
        13,
        14,
        15,
        ]

    lst.extend(lst2)
    print(f"LST extended with LST2= {lst}")

    i = 8
    newvalue = 9
    lst.insert(i,newvalue)
    print(f"LST with #9 inserted at position 8 = {lst}")

    lst.remove(5)
    print(f"LST remove #5 = {lst}")
  
    lst_count = lst.count(2)
    print(f"LST Count of #2 occurences = {lst_count}")

    lst.sort()
    print(f"SORTED LST - SEQUENTIAL")
    print(lst)
    lst.sort(reverse=True)
    print(f"SORTED LST - REVERSE")
    print(lst)

    lst.sort()
    print(f"SORTED LST - SEQUENTIAL PRIOR TO POPS")
    print(lst)
    lst.pop(0)
    print(f"LST Pop item at top of list = {lst}")
    lst.pop()
    print(f"LST Pop item at end of list = {lst}")

# ========================================================================
# TASK 3      Lists 5. List Transformations - Using Filtering and Mapping
# ========================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 5 : TRANSFORMATIONS - FILTERING & MAPPING")
    print("==============================================================")
    print("We will be exploring FILTER and MAP with LST3.")
    print()
    
    lst3 = [
        1,
        2,
        2,
        3,
        4,
        5,
        7,
        8,
        12,
        27,
        ]

    lst4 = lst3

    print(f"LST3 - PRIOR TO FILTERING TO KEEP X < 4")
    print(lst3)
    less_than_4 = list(filter(lambda x: x < 4, lst3))
    print(f"LST3 AFTER RUNNING LAMBDA FILTERING: {less_than_4}")
    print()
    
    lst3 = lst4
    print(f"LST3 - RESET TO ORIGINAL LST3 LIST")
    print(lst3)
    print()

    print(f"LST3 - PRIOR TO MAPPING X to CUBEROOT of X (ROUNDED TO TENTHS)")
    print(lst3)
    cuberootx = list(map(lambda x: x **(1/3),lst3))
    round_to_tenths = [round(num, 1) for num in cuberootx]
    print(f"LST3 AFTER RUNNING MAPPING FOR CUBEROOT: {round_to_tenths}")
    print()

    lst3 = lst4
    print(f"LST3 - RESET TO ORIGINAL LST3 LIST")
    print(lst3)
    print()

    print(f"LST3 - PRIOR TO MAPPING FOR VOLUME OF CUBE SIDES")
    print(lst3)
    lst3_volume = list(map(lambda x: x ** 3,lst3))
    print(f"LST3 AFTER RUNNING MAPPING FOR VOLUME OF SIDES: {lst3_volume}")
    print()

# ======================================================================
# TASK 3      Lists 6. List Transformations - Using List Comprehension
# ======================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 6 : TRANSFORMATIONS USING LIST COMPREHENSION")
    print("=================================================================")
    print("We will be exploring OMPREHENSION with LST3.")
    print()
    
    lst5 = [
        1,
        5,
        11,
        20,
        22,
        25,
        40,
        68,
        75,
        90,
        ]

    lst6 = lst5

    print(f"LST5 - PRIOR TO LIST COMPREHENSIONS")
    print(lst5)
    less_than_38 = [x < 38 for x in lst5]
    print(f"LST5 AFTER FINDING VALUES < 38: {less_than_38}")
    lst5 = lst6
    tripled_scores = [x * 3 for x in lst5]
    print(f"LST5 AFTER TRIPLING VALUES: {tripled_scores}")
    lst5 = lst6
    divisible_by_5 = [x % 5 for x in lst5]
    print(f"LST5 VALUES & NUMBER OF TIMES DIVISIBLE BY 5: {divisible_by_5}")
    print()
    

"""
lst5 = lst6
    print(f"LST5 - RESET TO ORIGINAL LST5 LIST")
    print(lst5)
    print()

# import some modules first - how many can you make use of?

import statistics
import math

# define some functions

if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# define a variable with some univariant data
# (one varabile, many readings)
score_list = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues_list = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# Descriptive: Averages and measures of central tendency
# Use statisttics module to get mean, median, mode
# for a values list

mean = statistics.mean(score_list)
median = statistics.median(score_list)
mode = statistics.mode(score_list)

# Descriptive: Measures of spread
# Get standard deviation and variance for a values list

stdev = statistics.stdev(score_list)
variance = statistics.variance(score_list)

# Descriptive: Measures of correlation
# Use two numerical lists of the same size
# Use statisttics module to get correlation between list1 and list2

correlationxy = statistics.correlation(xtimes_list, yvalues_list)


# Predictive: Machine Learning - Linear Regression
# If the corrlation is close to 1.0, then the data is linearly related
# If so, use statistics module to get linear regression for list1 and list2
# This is a form of supervised machine learning - it uses all known data
# Use the slope and intercept and an unknown (future) x to predict a y value
# Python functions can return multiple values

slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)

# Once we have learned the slope and intercept
# of the best-fit straight line through the data,
# we can use it to make predictions

# Predict the y value for a given x value outside the range of the data

x_max = max(xtimes_list)
newx = x_max * 1.5  # predict for a future x value

# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

newy = slope * newx + intercept


# BUILT-IN FUNCTIONS ......................................
# Many built-in functions work on lists
# try min(), max(), len(), sum(), sorted(), reversed()

# Using the score list provided above, do the following:
# Calcuate the max and min scores
max = max(score_list)
min = min(score_list)

# Calculate the length of the list
len = len(score_list)

# Calculate the sum of the list
sum = sum(score_list)

# Calculate the average of the list
avg = sum / len

# Return a new list soreted in ascending order
asc_scores = sorted(score_list)

# Return a new list soreted in descending order
desc_scores = sorted(score_list, reverse=True)

"""

"""

LIST METHODS ............................................... 

Here are some common methods that operate on an instance of a list.

append(x): Add an item to the end of the list.
extend(iterable): Add all the items from an iterable (such as another list)
     to the end of the list.
insert(i, x): Insert an item at a given position.
remove(x): Remove the first occurrence of an item.
pop([i]): Remove the item at the given position in the list, 
    and return it. If no index is specified, 
    removes and returns the last item in the list.
clear(): Remove all items from the list.
index(x[, start[, end]]): Return the index of the first occurrence of
     an item.
count(x): Return the number of occurrences of an item.
sort(key=None, reverse=False): Sort the items in the list 
     in ascending order.
reverse(): Reverse the order of the items in the list.
copy(): Return a shallow copy of the list.



# append an item to the end of the list
lst = [1, 2, 3]
lst.append(4)

# extend the list with another list
lst.extend([4, 5, 6])

# insert an item at a given position (0 = first item)
i = 0
newvalue = 42
lst.insert(i, newvalue)

# remove an item
item_to_remove = 42
lst.remove(item_to_remove)

# Count how many times 111 appears in the list
ct_of_111 = score_list.count(111)

# Sort the list in ascending order using the sort() method
asc_scores2 = score_list.sort()

# Sort the list in descending order using the sort() method
desc_scores2 = score_list.sort(reverse=True)

# Copy the list to a new list
new_scores = score_list.copy()

# Remove the first item from the new list
# The first item in a list is at index 0
# Think of it as an offset from the beginning of the list
first = new_scores.pop(0)

# Remove the last item from the new list
# The last item in a list is at index -1
last = new_scores.pop(-1)

# Remove the item at index 3 from the new list
fourth = new_scores.pop(3)
print(new_scores)
print(fourth)
print(new_scores)


# TRANFORMATIONS ............................

# FILTER and MAP are critical in big data applications

# Use the built-in function filter() anywhere you need to filter a list
# Filter the new list to only include scores greater than 100
# You could pass in a named function, but honestly this is easier
# Say "keep x such that x > 100 is True" given new_scores
# Cast the result using square brackets to get a list
scores_over_100 = [filter(lambda x: x > 100, new_scores)]

# Use the built-in function map() anywhere you need to transfrom

# Map each element to its square
# Say "map x to x squared" given new_scores
# Cast the result using square brackets to get a list
doubled_scores = [map(lambda x: x * 2, new_scores)]

# Map each element to its square root
# Say "map x to the square root of x" and cast to a list
sqrt_scores = map(lambda x: math.sqrt(x), new_scores)

# Map each element (radius) to its area
radius_list = [1, 2, 3, 4, 5]
# Say "map r to pi r squared" and cast to a list
area_list = [map(lambda r: math.pi * r * r, radius_list)]


# TRANFORMATIONS - Using List Comprehensions
# List comprehensions are a concise way to create lists
# They work like map and filter, but are more concise
# They are the preferred "pythonic" way to do transformations

# With comprehensions, we start with what we WANT
# Filter the new list to only include scores greater than 100
# Say "keep x (for each x in new_scores) IF  x > 100"
scores_over_100 = [x for x in new_scores if x > 100]

# Try again "keep x (for each x in new_scores) IF  x < 42"
scores_under_42 = [x for x in new_scores if x < 42]

# Map each element to its square
# Say "give me x squared (for each x in new_scores)"
doubled_scores = [x * 2 for x in new_scores]

# Map each element to its square root
# Say "give me the square root of x (for each x in new_scores)"
# and cast it to a list using square brackets
sqrt_scores = [math.sqrt(x) for x in new_scores]

# Map each element (radius) to its area
# Say "give me pi r squared (for each r in radius_list)"
# and cast it to a list using square brackets
area_list = [math.pi * r * r for r in radius_list]

# Map each element (radius) to its circumference
# Say "give me 2 pi r (for each r in radius_list)"
# and cast it to a list using square brackets
circumference_list = [2 * math.pi * r for r in radius_list]

# Mastering comprehesions is a key skill for data scientists
numbers = [1, 2, 3, 4]
squares = [x ** 2 for x in numbers]

print()
print("Add print statements to the code to see what happens.")
print("Explore enough to understand.")
print("Then apply what you know to your own domain.")
print()








# -------------------------------------------------------------
# REFERENCE SECTION
# -------------------------------------------------------------

# define more functions here (see instuctions)

# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"

# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.


def get_area_of_lot(length, width):
    
    Return area of a lot given the length and width of the lot.

    Could this fail?

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None

"""