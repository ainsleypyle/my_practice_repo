# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:37:11 2025

@author: ainsl
"""

# #Reading in input from the command line.
# name=input("Please enter your name ")
# print("Hello, ", name)

# try:
#     num=int(input("Enter a number"))
#     print(num)
#     double=num*2 #thinks it is a string unless type casted
#     print(double)
# except: 
#     print("You didn't enter a number")

with open("movies.txt") as file:
    for line in file:
        line=line.strip()
        print(line)

with open("heights.txt") as file:
    for line in file:
        info=line.strip().split() #Split gets it out of the string.
        info[2]=int(info[2])
        print(info)

filename=input("Enter a filename")
with open(filename) as file:
    line_count=1
    for line in file:
        print(str(line_count) + '.'+ line.strip())
        line_count +=1