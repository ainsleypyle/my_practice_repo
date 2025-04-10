# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:57:50 2025


@author: ainsl
"""

#To write a comment you use a POUND SIGN
#Block comment is '''
'''This is also a comment'''


#Variables. Do not have to declare data type
x=100
x="hello"
x=[1,2,3]
#Determines data type at run time
print(x)

#Mathematical operators
x=100
y=10
result=x+y
result=x/y #Creates a float
print(int(result)) #This makes it an int
result=x//y #This also makes an int

#Math functions
min_value=min(1,2,3)
print(min_value)
#Variables have underscore all lowercase
#Functions are no underscores with uppercases
raised=pow(2,3)
print(raised)
raised=2**3

#If statements
x=-1
y=0
if x < 0:
    print('x is negative')
    y+=1
elif x > 0:
    print("X is positive")
else: 
    print("x is zero")


#Compound conditional statements
start=10
end=100
if x > start and x < end:
    print("x is within range")
if x < start or x > end:
    print("X is not in range")
    
#Loops
count=0
while count < 5:
    print(count)
    count +=1
    
for i in range(5):
    print(i, end=" ")
print()

for i in range(1,15,2):
    print(i, end=' ') #Space at the end instead of new line
    

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i, lst[i])

for val in lst:
    print(val, end=" ")

for i, val in enumerate(lst): #Index and the value
    print(i,val)
    
    
#In Class Exercise
#1
for i in range(1,20):
     if i % 3 ==0:
         print(i)

#2
count=0
sum=0
while count <= 50:
    if count % 2==0:
        sum+=count
    count+=1
print(sum)

#3
numbers=[5,8,2,15,10,3,7]
for num in numbers:
    if num > 5:
        print(num, end=" ")
   
#Challenge
lst1=[1,2,3,4,5]
lst2=[]
sum=0
for element in lst1:
    sum+=element
    lst2.append(sum)
print(lst2)


#Functions
def hello_world():
    print("Hello World")
#Call
hello_world()

def hello(name):
    print("Hello "+name)
hello("Bob")

def hello2(name="Bob"): #Default value
    print("Hello "+name)
hello2()
hello2("Jane")
    
def swap_function(lst):
    first_elem=lst[0]
    last_elem=lst[len(lst)-1]
    lst[len(lst)-1]=first_elem
    lst[0]=last_elem
    # can also be done like this
    # lst[0]=lst[-1]
    # lst[-1]=tmp
    
lst=[0,3,8,4,5]
swap_function(lst)
print(lst)   

#Strings
hello="hello"
for c in hello:
    print(c)
    
#String slicing. Substring within a string
course="Platform Computing"
plat=course[:8]
computing=course[9:]
#Use find if dont know the end


         