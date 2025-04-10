# Ainsley Pyle
def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    new_string=''
    if len(s) > 2:
        new_string=s[:2]*3
    else:
        new_string=s*3
    return new_string
    
    


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The first element should become the last.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    new_list=[]
    for i in range(1,len(lst)):
        new_list.append(lst[i])
    new_list.append(lst[0])
    return new_list

    #More efficient way to do it would be using the delete or remove function, but have not learned that in class. 
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    count=[character for character in s if character.isdigit()==True]
    return len(count)
    

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    first_element=lst[0]
    min_element=min(lst)
    min_element_index=lst.index(min_element)
    lst[0]=min_element
    lst[min_element_index]=first_element
    return lst
      

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    grades_dict={}
    with open("grades.txt") as file:
        for line in file:
            info=line.strip().split() #Split gets it out of the string.
            grades_dict[info[0]+" " + info[1]]=int(info[2])
    return grades_dict

    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))
print('repeat_start("a") expected: aaa')
print('repeat_start("a") actual:', repeat_start("a"))
print('repeat_start("wow") expected: wowowo')
print('repeat_start("wow") actual:', repeat_start("wow"))
print('repeat_start("b") expected: bbb')
print('repeat_start("b") actual:', repeat_start("b"))


print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))
print('shift_left([5]) expected: [5]')
print('shift_left([5]) actual:', shift_left([5]))
print('shift_left([1, 2, 3, 4, 5, 6, 7]) expected: [2, 3, 4, 5, 6, 7, 1]')
print('shift_left([1, 2, 3, 4, 5, 6, 7]) actual:', shift_left([1, 2, 3, 4, 5, 6, 7]))


print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))
print('count_digits("I was born on 12/18/2002!") expected: 8')
print('count_digits("I was born on 12/18/2002!") actual:', count_digits("I was born on 12/18/2002!"))
print('count_digits("I like dogs!") expected: 0')
print('count_digits("I like dogs!") actual:', count_digits("I like dogs!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))
print('swap([2, 1, 3]) expected: [1, 2, 3]')
print('swap([2, 1, 3]) actual:',swap([2, 1, 3]))
print('swap([9, 4, 5, 6, 7, 1, 2, 3]) expected: [1, 4, 5, 6, 7, 9, 2, 3]')
print('swap([9, 4, 5, 6, 7, 1, 2, 3]) actual:',swap([9, 4, 5, 6, 7, 1, 2, 3]))
print('swap([5,4,3,2,1,1]) expected: [1, 4, 3, 2, 5, 1]')
print('swap([5,4,3,2,1, 1]) actual:',swap([5,4,3,2,1,1]))


print(build_grades_dict())
