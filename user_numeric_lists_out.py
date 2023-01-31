"""

PS C:\Users\JMC\Documents\datafun-03-datatypes> & C:/Users/JMC/AppData/Local/Programs/Python/Python311/python.exe c:/Users/JMC/Documents/datafun-03-datatypes/user_numeric_lists.py




Good morning! My name is Jim, and I am going through my Grandpa's attic.
Grandpa enjoyed doing jigsaw puzzles. He was great at putting pieces back in the boxes.
His storage shelf with the puzzles fell over, and Grandpa put the pieces back into the boxes.
Unfortunately, when putting them back, he guessed at colors as to which pieces went where.
He was close, but now the totals for box piece count and box lid count don't match.
Please help us to review the data, so we can put the pieces where they go and solve this, excuse the pun, puzzle.

We had some students help us count the pieces in each of the 29 boxes as an extra credit assignment.
The totals for this 29 box count are in LIST 1. There were 22,300 total pieces.
The 29 boxes should have a total of 22,300 pieces according to the box lid sum, so no pieces are missing - just some missplaced.

The totals of what should be in each box are in lid_count_list.
Each line in LIST 1(actual box_count_list) corresponds to the same line in lid_count_list.
LIST X = Times, in hours, it took each of the 10 students to complete the extra credit work.
LIST Y = Number of pieces each of the 10 students counted.

Here is LIST 1 - Total pieces by box.
[1254, 634, 795, 466, 1059, 306, 849, 763, 196, 846, 1197, 979, 1312, 670, 777, 1204, 157, 164, 809, 609, 788, 487, 1462, 958, 961, 1032, 403, 909, 254]

Here is LIST X - Total hours spent by 10 students.
[1, 2, 4, 5, 6, 7, 8, 10, 12, 13]

Here is LIST Y - Total pieces counted by the 10 students.
[423, 912, 1212, 1466, 1748, 1871, 2078, 3158, 4520, 4912]

TASK 3 SECTION LISTS 1: LIST STATISTICS
=======================================
We will be calculating the mean, median, mode, standard deviation, and variance for each list.

LIST 1 STATISTICS
-----------------
LIST 1 Mean = 768.97
LIST 1 Median = 795
LIST 1 Mode = 1254
LIST 1 STDEV = 358.31
LIST 1 Variance = 128384.25

LIST X STATISTICS
-----------------
LIST X Mean = 6.8
LIST X Median = 6.5
LIST X Mode = 1
LIST X STDEV = 4.02
LIST X Variance = 16.18

LIST Y STATISTICS
-----------------
LIST Y Mean = 2230
LIST Y Median = 1809.5
LIST Y Mode = 423
LIST Y STDEV = 1502.04
LIST Y Variance = 2256123.33


TASK 3 SECTION LISTS 2: CORRELATION & PREDICTION
================================================
We will be calculating the Slope and Intercept of LIST X & LIST Y.
We will be calculating the future value of LIST Y based on next LIST X value=15.

SLOPE = 361.7445054945055
INTERCEPT = -229.86263736263754
FUTURE X = 15
FUTURE Y = 5196


TASK 3 SECTION LISTS 3: USING PYTHION BUILT-IN FUNCTIONS
========================================================
We will be calculating Min, Max, Len, Sum, Average, Set, and Sorted functions.

LIST 1 FUNCTIONS
----------------
MINIMUM = 157
MAXIMUM = 1462
NUMBER OF ITEMS IN LIST = 29
SUM = 22300
AVERAGE = 768.97
SET = {1032, 777, 909, 403, 788, 795, 157, 670, 1312, 1059, 164, 809, 1197, 306, 1204, 1462, 958, 961, 196, 846, 849, 466, 979, 609, 1254, 487, 634, 763, 254}
SORTED LIST 1 - SEQUENTIAL
[157, 164, 196, 254, 306, 403, 466, 487, 609, 634, 670, 763, 777, 788, 795, 809, 846, 849, 909, 958, 961, 979, 1032, 1059, 1197, 1204, 1254, 1312, 1462]
SORTED LIST 1 - REVERSE
[1462, 1312, 1254, 1204, 1197, 1059, 1032, 979, 961, 958, 909, 849, 846, 809, 795, 788, 777, 763, 670, 634, 609, 487, 466, 403, 306, 254, 196, 164, 157]

LIST X FUNCTIONS
----------------
MINIMUM = 1
MAXIMUM = 13
NUMBER = 10
SUM = 68
AVERAGE = 6.8
SET = {1, 2, 4, 5, 6, 7, 8, 10, 12, 13}
SORTED LIST X - SEQUENTIAL
[1, 2, 4, 5, 6, 7, 8, 10, 12, 13]
SORTED LIST X - REVERSE
[13, 12, 10, 8, 7, 6, 5, 4, 2, 1]

LIST Y FUNCTIONS
----------------
MINIMUM = 423
MAXIMUM = 4912
NUMBER = 10
SUM = 22300
AVERAGE = 2230.0
SET = {423, 4520, 1871, 912, 4912, 1748, 3158, 1466, 1212, 2078}
SORTED LIST Y - SEQUENTIAL
[423, 912, 1212, 1466, 1748, 1871, 2078, 3158, 4520, 4912]
SORTED LIST Y - REVERSE
[4912, 4520, 3158, 2078, 1871, 1748, 1466, 1212, 912, 423]


TASK 3 SECTION LISTS 4 : LIST METHODS
=====================================
We will be exploring list methods Append, Extend, Insert, Remove, Count, Sort, Copy, and Pop.

LST appended with the number 8 = [1, 2, 2, 3, 4, 5, 7, 8]
LST extended with LST2= [1, 2, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15]
LST with number 9 inserted at position 8 = [1, 2, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LST remove number 5 = [1, 2, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LST Count of number 2 occurences = 2
SORTED LST - SEQUENTIAL
[1, 2, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15]
SORTED LST - REVERSE
[15, 14, 13, 12, 11, 10, 9, 8, 7, 4, 3, 2, 2, 1]
SORTED LST - SEQUENTIAL PRIOR TO POPS
[1, 2, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LST Pop item at top of list = [2, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LST Pop item at end of list = [2, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14]


TASK 3 SECTION LISTS 5 : TRANSFORMATIONS - FILTERING & MAPPING
==============================================================
We will be exploring FILTER and MAP with LST3.

LST3 - PRIOR TO FILTERING TO KEEP X < 4
[1, 2, 2, 3, 4, 5, 7, 8, 12, 27]
LST3 AFTER RUNNING LAMBDA FILTERING: [1, 2, 2, 3]

LST3 - RESET TO ORIGINAL LST3 LIST
[1, 2, 2, 3, 4, 5, 7, 8, 12, 27]

LST3 - PRIOR TO MAPPING X to CUBEROOT of X (ROUNDED TO TENTHS)
[1, 2, 2, 3, 4, 5, 7, 8, 12, 27]
LST3 AFTER RUNNING MAPPING FOR CUBEROOT: [1.0, 1.3, 1.3, 1.4, 1.6, 1.7, 1.9, 2.0, 2.3, 3.0]

LST3 - RESET TO ORIGINAL LST3 LIST
[1, 2, 2, 3, 4, 5, 7, 8, 12, 27]

LST3 - PRIOR TO MAPPING FOR VOLUME OF CUBE SIDES
[1, 2, 2, 3, 4, 5, 7, 8, 12, 27]
LST3 AFTER RUNNING MAPPING FOR VOLUME OF SIDES: [1, 8, 8, 27, 64, 125, 343, 512, 1728, 19683]

TASK 3 SECTION LISTS 6 : TRANSFORMATIONS USING LIST COMPREHENSION
=================================================================
We will be exploring COMPREHENSION with LST5.

LST5 - PRIOR TO LIST COMPREHENSIONS
[1, 5, 11, 20, 22, 25, 40, 68, 75, 90]
LST5 AFTER FINDING VALUES < 38: [True, True, True, True, True, True, False, False, False, False]
LST5 AFTER TRIPLING VALUES: [3, 15, 33, 60, 66, 75, 120, 204, 225, 270]
LST5 VALUES & NUMBER OF TIMES DIVISIBLE BY 5: [1, 0, 1, 0, 2, 0, 0, 3, 0, 0]

PS C:\Users\JMC\Documents\datafun-03-datatypes> 






"""