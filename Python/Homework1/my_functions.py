#Ainsley Pyle

def list_sum(input_list):
    """
    This function takes a list as an input and returns 
    the sum of all of the numbers in the list.
    """
    sum=0
    for i in input_list:
        sum += i
    return "The sum is " + str(sum) 

def triangle_area(base,height):
    """
    This function takes in the base and height ints and 
    returns the area of a triangle with those values.""" 
    area= 1/2 * base * height
    return "The area is " + str(area)




#Test Data
print(list_sum([1,2,3,4,5,6,7,8,9,10]))
print(list_sum([2,2,2]))
print(list_sum([10,10,10,10,10]))

print(triangle_area(2,2))
print(triangle_area(10,5))
print(triangle_area(1,1))

