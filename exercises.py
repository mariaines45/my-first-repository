#Create a function that returns a list of numbers from 0 to 500

def list_numbers():
    list = []
    n = 0

    while n < 501:
        list.append(n)
        n = n + 1
    
    return(list)

list = list_numbers()

print(list)

#Create a function that takes a list of numbers (you can use the one you created in the previous exercise) and returns the sum of all of them

def sum_numbers(list):
    sum = 0

    for i in list:
        sum = sum + i
    print (sum)

sum_numbers(list)

#Investigate the range() function. After you’ve used it, create a function that receives a number as parameter and prints all numbers from it to zero (using a for loop).

def sum_to_zero(n):
    all = range(n,-1,-1)

    for i in all:
        print(i)

sum_to_zero(6) 

#Create a function that takes a list of numbers and returns the maximum value among them

def maximum(numbers):
    return max(numbers)

print(maximum([1,2,3]))

#Create a function that takes a list of numbers and returns the minimum value among them

def minimum(numbers):
    return min(numbers)

print(minimum([1,2,3]))

#Create a function that prints the numbers 1 to 50 (using iteration)

numbers = range(0,51)

def print_numbers(numbers):
    for number in numbers: 
        print(number)

print_numbers(list_numbers)

#Create a program that prints multiplication tables from 1 to 10

def multiplication_tables(number):

    multiply = range(0,11)

    for i in multiply:
        print(number,"*",i,"=",number * i)

multiplication_tables(6)

#Create a function inverted_piramid that writes the pyramid of stars in an inverted fashion.

def inverted_pyramid():
    stars = range(5,-1,-1)

    for i in stars:
        print("*" * i)

inverted_pyramid()

#Create a function multiplicate that takes two integers (a and b, for example) and returns a times b. Do not use the * operator.

def multiplicate(a,b):
    multiplicate  = range(0,a)
    result = 0

    for i in multiplicate:
        result = result + b
    return result

print(multiplicate(2,4))

#Create a function exponentiate that takes two arguments base and exponent and raises base to the exponent power. Do not use the ** operator.

def exponentiate(c,d):
    exponent = range(1,d)
    result = c

    for i in exponent:
        result = result * c
    return result

print(exponentiate(2,3))

