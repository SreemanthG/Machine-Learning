# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:42:28 2020

@author: Admin
"""

a=input("Enter a number: ")
b=a*10
print(a,b)

fopen = open('test.txt', 'r')
for line in fopen:
    print(line)


fopen = open('test.txt', 'r')
lines = []
for line in fopen:
    lines.append(line)
print(lines)


for line in fopen:
    print(line, end=':')


###

fopen = open('test.txt', 'r')
highest_score = 0
for line in fopen:
    line_float = float(line)
    
    if(line_float > highest_score):
        highest_score = line_float

fopen.close()
print("The Highest Score is", highest_score)


###

fopen = open('test.txt', 'r')
linesContent = fopen.readlines()
fopen.close()

# Inserting a line at third position
linesContent.insert(2 , "This line was inserted via Python code!\n")

# opening file in write mode
fopen = open("test.txt" , "w")

#writing new lines content
fopen.writelines(linesContent)
fopen.close()

####

f = open('myfile.txt' , 'w')
f.write("Python is object oriented programming language")
f.close()

# open file in read mode
f = open('myfile.txt' , 'r')

# getting file content
content = f.read()
f.close()

# converting content to a list
L = content.split()

# removing the 3rd element
L.pop(2)

# opening file in write mode by overwriting the existing content
f = open('myfile.txt' , 'w')

#building file content
for word in L:
    f.write(word + " ")

f.close()
