'''
Author: Harry
Licenced to: ABC Company 
************Thanks for reading**********
'''
import os #importing the os module
print("Hello world")


'''
This problem is a solution of
problem 1 of CodeWithHarry Practice set!
'''
# This is also a comment just like the above line 

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
like a diamond in the sky.''')

#Author: Harry
#Location: Mars 
#Date: 23/09/2022

import os 
print(os.listdir())

a_122 = '''harry'''
# a = 'harry'
# a = 'harry'
b = 345
c = 45.32
d = True
# d = None 

# Printing the variables 
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# printing the type of variable 
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = 3
b = 4

# Arithmetic Operators
print("the value of 3+4 is ", 3+4)
print("The value of 3/4 is ", 3/4)
print("The value of 3*4 is ", 3*4)
print("The value of 3-4 is ", 3-4)

#Assignment Operators 
a = 34
a -= 12 
a *= 12
a /= 12
print(a)

# Comparison Operators 
# b = (14<=7)
# b = (14>=7)
# b = (14<7)
# b = (14>7)
# b = (14==7)
b = (14!=7)
print(b)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is ",(bool1 or bool2))
print("The value of not bool2 is ",(not bool2))


a = "35fg4f55"
a = int(a)
print(type(a))
print(a+5)


a = input("Enter a number: ")
a = int(a) #Convert a to an an Integer(If possible)
print(type(a))

a = 30 
b = 15
print("The sum of a and b is ", a+b)

a = 458 
b = 15 

print("The remainder when a is divided by b is",a%b)


a = input ("Enter first number: ")
b = input ("Enter second number: ")
a = int(a)
b = int(b)
avg = (a + b)/2
print("The average of a and b is ", avg)

# b = "Harry's # --> Use this if you have single quotes in your strings
# b = 'Harry"s' 
b = '''Harry's and 
Harry's'''
print(b)
#print(type(b))

# greeting = "Good Morning, "
# name = "Harry"
# print(type(name))

# Concatenating two strings 
# c = greeting + name
# print(c)
name = "Harry"
# print(name[4])
# name[3] = "d" --> Does not work

# print(name[1:4]) 
# print(name[:4]) # is  same as name[0:4]
# print(name[1:]) # is same as name [1:5]
# c = name[-4:-1]) # is same is name [1:5]
# print(c)

name = "HarryIsGood"
# d = name [ 0::3]
d = name[:0:-1]
print(d)

story = "once upon a time there was a youtuber named Harry who uploaded python course with notes"

# String Functions
# print(len(story))
# print(story.count("c"))
# print(story.capitalize())
# print(story.find("upon"))
print(story.replace("Harry", "CodeWithHarry"))

story = "Harry is good. \nHe\tis ve\\ry good"
print(story)

name = input("Enter Your Name\n")
print("Good Afternoon," + name)

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection 
You are selected! 
Have a great day ahead ! 
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter your name \n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)


st = "This is a string with double spaces ok"

st = st.replace("  "," ")
print(st)

letter = "Dear Harry, This Python course is nice! Thanks!"
print(letter)

formatted_letter = "Dear Harry, \n\t This is python course is nice!\n Thanks!"
print(formatted_letter)


# Creat a list using []
a = [1, 2, 3,4,56, 6]

# print the list unsing() function
print(a)

# Acces using index using a[0], a[1], a[2]
print(a[2])

#change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
print(c)

# List slicing
friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:4])
print(friends[-4:])

l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# l1.sort()
# l1.reverse()
# l1.append(45)
# l1.insert(2, 544)
# l1.pop(2)
l1.remove(21)
print(l1)

# Creating a tuple using ()
t = (1, 2, 4, 5)
 
# t1 = ()
# t1 = (1)
t1 = (1,)
print(t1)

# Printing the elements of a tuple 
# print(t[0])

# Cannot update the values of a tuple 
# t[0] = 34 

# Creating a tuple using ()
t = (1, 2, 4, 5, 1, 2, 6)

print(t.count(1))
print(t.count(5))

f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5 ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")
f8 = input("Enter Fruit Number 8: ")

myFruitlist = [f1, f2, f3, f4, f5, f6, f7, f8]
print(myFruitlist)

m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

a = (2, 3,5,6)
a[0] = 45

a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))































