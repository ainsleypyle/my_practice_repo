# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:35:30 2025

@author: ainsl
"""

cart=["apples", "bananas", "cherries"]


#To add
cart.append("dounuts")
cart.append("eggs")
cart.append("flour")
print(cart)

#To remove cherries
cart.remove("cherries")
print(cart)
#If not in list, you will get an error
if "pineapple" in cart:
    cart.remove("pineapple") #Checking if in the list first
#To remove at an index:
cart.pop(3)
print(cart)
cart.pop() #Removes last element like a stack
print(cart)
#To reverse
cart.reverse()
print(cart)
#To sort alphabetically
cart.sort()

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

#Splicing
fruit_basket=cart[3: ]
print(cart)
print(fruit_basket)

#Empty list
squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

#List comprehension
squares=[i*i for i in range(1,10)]
cart=['apples', 'bananas', 'dounuts', 'bananas', 'grapes', 'oranges']
cart_b=[i for i in cart if i.startswith('b')]

inventory=[0]*len(cart)
print(inventory)
inventory[0]=100

#Sets
number_set=set()
number_set={1,1,2,3,4,0,10,5} #Cant have duplicates
print(number_set) #Does not print duplicates
number_set.add(-10) #Use a set over a list if you care about not allowing duplicates. 

num_lst=[1,1,4,5,5,6,6]
no_dups=set(num_lst)
print(no_dups)
no_dups=list(no_dups) 

#Sorted set. Returns a sorted lst
ns=sorted(number_set)
print(ns)

#Dictionaries
fav_snacks={}
fav_snacks={
    "kathleen": "tortilla chips",
    "maggie":"pretzels",
    "emily":"buffalo chicken dip",
    "ava": "chocolate"
        }
print(fav_snacks)
#Adding another person to dictionary
fav_snacks['wade']='popcorn'
print(fav_snacks)
print("kathleens favorite snack is " + fav_snacks['kathleen']) #To get the value just give the key
#print("kathleens favorite snack is " + fav_snacks['bob']) gives an error because no bob
if 'bob' in fav_snacks:
    print("kathleens favorite snack is " + fav_snacks['bob'])
#Iterating through
for key in fav_snacks:
    print(key+"'s favorite food is " +fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}")

for key,value in fav_snacks.items():
    print(key, value)

keys=fav_snacks.keys()
values=fav_snacks.values()

#Value can be anything. List, string, int, etc
fav_snacks['alice']=['chips','nuts']
print(fav_snacks)
