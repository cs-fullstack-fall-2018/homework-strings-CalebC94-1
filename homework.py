# Exercises Homework Problem 1: Naughty Strings
#
# What is the error message returned when you improperly use quotes inside of strings?
# Provide an example and explain the error message.
input("that is not right)
#                      ^
# SyntaxError: EOL while scanning string literal
# EOL, meaning End Of Line, occurred because a quotation mark was missing
#
# Homework Problem 2: Fruits and Vegetables
#
# x = ["apple", "banana", "carrot"]
#
# Write one line of code that when executed returns "apples bananas and carrots".

x =["apple", "banana", "carrot"]
print(x[0] +'s', x[1] +'s and', x[2] +'s')