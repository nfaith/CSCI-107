# -----------------------------------------+
# Faith Nelson                             |
# CSCI 107, Assignment 7                   |
# Last Updated: November 2, 2018           |
# -----------------------------------------|
# This program mimics the game             |
# Manufactoria.                            |
# -----------------------------------------+


# -----------------------------------------------------------+
# test: Determine whether a given function accepts a string. |
# -----------------------------------------------------------|
# fn: The function to use, e.g. four_or_more_reds          |
# string: The string to test, e.g. "rrrbbb"                  |
# -----------------------------------------------------------+
    
def test(fn, string):

    if fn(string):
        result = "accepted"
    else:
        result = "not accepted"

    print('The string "' + string + '" is ' + result)

# -----------------------------------------------------------+
# four_or_more_reds: Counts the number of r's in a string.   |   
# -----------------------------------------------------------|
# string: The string to test, e.g. "rrrbbb"                  |
# -----------------------------------------------------------+
def four_or_more_reds(string):
    num = string.count('r')
    if num >=4:
        return True
    else:
        return False

# -----------------------------------------------------------+
# alternating_colors: Searches for alternating patterns by   |
# looking for repeating letters.                             |   
# -----------------------------------------------------------|
# string: The string to test, e.g. "rrrbbb"                  |
# -----------------------------------------------------------+
def alternating_colors(string):
    x = "rr"
    y = "bb"
    if x in string or y in string:
        return False
    else:
        return True
    

    
# --------------------------------------------------+
# manufactoria: The main function for Assignment 7. |
# --------------------------------------------------+

def manufactoria():

    # test strings to see if they contain four or more reds
    
    print("Testing four or more reds")
    print("---------------------------")
    test(four_or_more_reds, "")
    test(four_or_more_reds, "r")
    test(four_or_more_reds, "b")
    test(four_or_more_reds, "rbbbbbrbbbbbrbbbb")
    test(four_or_more_reds, "bbbbrbbbb")
    test(four_or_more_reds, "rbbrbbrr")  
    test(four_or_more_reds, "rrrrr")
    test(four_or_more_reds, "brrbrr")

    # test to see if strings contain alternating numbers of 
    # the same symbol that are odd numbers that increase by 2.

    print()
    print("Testing alternating colors")
    print("--------------------------")

    # these tests should accept
    test(alternating_colors, "")
    test(alternating_colors, "r")
    test(alternating_colors, "rb")
    test(alternating_colors, "rbrbrbr")
    test(alternating_colors, "b")
    test(alternating_colors, "brbr")
    test(alternating_colors, "brbrbrbr")

    # these tests should not accept
    test(alternating_colors, "rr")
    test(alternating_colors, "bb")
    test(alternating_colors, "rbrbrrbr")
    test(alternating_colors, "brbbbr")


# -----------------------------------------------------------+

manufactoria()       # run the simulation 
