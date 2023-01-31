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
    print("Good morning! My name is Jim, and I am going through my Grandpa's attic.")
    print("Grandpa enjoyed doing jigsaw puzzles. He was great at putting pieces back in the boxes.")
    print("His storage shelf with the puzzles fell over, and Grandpa put the pieces back into the boxes.")
    print("Unfortunately, when putting them back, he guessed at colors as to which pieces went where.")
    print("He was close, but now the totals for box piece count and box lid count don't match.")
    print("Please help us to review the data, so we can put the pieces where they go and solve this, excuse the pun, puzzle.")
    print()
    print("We had some students help us count the pieces in each of the 29 boxes as an extra credit assignment.")
    print("The totals for this 29 box count are in LIST 1. There were 22,300 total pieces.")
    print("The 29 boxes should have a total of 22,300 pieces according to the box lid sum, so no pieces are missing - just some missplaced.")
    print()
    print("The totals of what should be in each box are in lid_count_list.")
    print("Each line in LIST 1(actual box_count_list) corresponds to the same line in lid_count_list.")
    print("LIST X = Times, in hours, it took each of the 10 students to complete the extra credit work.")
    print("LIST Y = Number of pieces each of the 10 students counted.")
    print()

# ==================================================================
# TASK 3      Numeric Lists (Setup Lists & Imports)
# ==================================================================

import statistics
import math

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

print("Here is LIST 1 - Total pieces by box.")
print(list1)
print()

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

print("Here is LIST X - Total hours spent by 10 students.")
print(listx)
print()

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

print("Here is LIST Y - Total pieces counted by the 10 students.")
print(listy)
print()


# ==================================================================
# TASK 3      Lists 1. List Statistics
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 1: LIST STATISTICS")
    print("=======================================")
    print("We will be calculating the mean, median, mode, standard deviation, and variance for each list.")
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
    print()

# ==================================================================
# TASK 3      Lists 2. Correlation and Prediction
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 2: CORRELATION & PREDICTION")
    print("================================================")
    print("We will be calculating the Slope and Intercept of LIST X & LIST Y.")
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
    print("========================================================")
    print("We will be calculating Min, Max, Len, Sum, Average, Set, and Sorted functions.")
    print()
    print("LIST 1 FUNCTIONS")
    print("----------------")
    minimum = min(list1)
    print(f"MINIMUM = {minimum}")
    maximum = max(list1)
    print(f"MAXIMUM = {maximum}")
    number = len(list1)
    print(f"NUMBER OF ITEMS IN LIST = {number}")
    sumlist1 = sum(list1)
    print(f"SUM = {sumlist1}")
    average = round(sumlist1 / number,2)
    print(f"AVERAGE = {average}")
    setlist1 = set(list1)
    print(f"SET = {setlist1}")
    print(f"SORTED LIST 1 - SEQUENTIAL")
    list1.sort()
    # sorted(list1)
    print(list1)    
    print(f"SORTED LIST 1 - REVERSE")
    list1.sort(reverse=True)
    # sorted(list1,reverse=True)
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
    print(f"SORTED LIST X - SEQUENTIAL")
    # listx.sort()
    sorted(listx)
    print(listx)
    print(f"SORTED LIST X - REVERSE")
    listx.sort(reverse=True)
    # sorted(listx,reverse=True)
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
    print("SORTED LIST Y - SEQUENTIAL")
     # listy.sort()
    sorted(listy)
    print(listy)
    print("SORTED LIST Y - REVERSE")
    listy.sort(reverse=True)
    # sorted(listy,reverse=True)
    print(listy)
    print()
    print()

# ==================================================================
# TASK 3      Lists 4. List Methods
# ==================================================================

if __name__ == "__main__":
    print("TASK 3 SECTION LISTS 4 : LIST METHODS")
    print("=====================================")
    print("We will be exploring list methods Append, Extend, Insert, Remove, Count, Sort, Copy, and Pop.")
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
    print(f"LST appended with the number 8 = {lst}")
    
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

    #Set values
    i = 8
    newvalue = 9

    lst.insert(i,newvalue)
    print(f"LST with number 9 inserted at position 8 = {lst}")

    lst.remove(5)
    print(f"LST remove number 5 = {lst}")
  
    lst_count = lst.count(2)
    print(f"LST Count of number 2 occurences = {lst_count}")

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
    print()
    print()


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
    print("We will be exploring COMPREHENSION with LST5.")
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
    
