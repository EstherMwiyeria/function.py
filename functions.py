def hello (name):
    print(f"Hello {name}")

def welcome(student,school):
    print(f"Welcome to {school},{student}")

def year_Of_Birth(name,age):
    year = 2023-age
    print(f"{name} was born in {year}")

# write a function that accepts any number of arguments
def hello(*names):
    for name in names:
        print(f"Hello {name}")

# Given two lists, write a function to find the common elements between them and return them in a new list.

list1 = ["apples","bananas","mangoes","avocados","grapes","oranges"]
list2 = ["pineapples","grapes","pawpaws","melons","mangoes"]

def fruit_List():
    print(set(list1).intersection(list2))


#Write a function to create and print a list  where the values are the squares pf numbers
#  between 1 and 30(both included)
def squareroot():
    v =list()
    for n in range(1,30):
        v.append(n**2)
        return v
print(squareroot())   

#1.Write a Python function to find the maximum of three numbers

def maximum(a,b,c):
    if a >=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c
print(maximum(2,8,9))


#Write a python function to sum all the numbers in a list
#Sample List: (8,2,3,0,7)
def sum(numbers):
    answer = 0
    for z in numbers:
        answer +=z
    return answer
print(sum((8,2,3,0,7)))

#write a python function to multiply all the numbers in a list .

def multiply(numbers):
    answer =1
    for b in numbers:
        answer*= b
    return answer

print(multiply((8,2,3,-1,7)))  

#write a function that print even numbers from a given list

def evens(even):
    numbers = []
    for x in even:
        if x %2 == 0:
            numbers.append(x)
    return numbers
print(evens([1,2,3,4,5,6,7,8,9]))

#write a python function that checks whether a past string is a palindrome or not
def palindrome(string):
    if string == string[::-1]:
        return(True)
    else:
        return(False)
print(palindrome("noon"))