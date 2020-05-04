"""
Given a string consisting of words separated by spaces. Determine how many
words it has. To solve the problem, use the method count.

"""

import copy
my_string = input("Enter your text here:") 

#print(my_string.count(" ") + 1)

space = "space"
count = 0
for i in my_string:
    if i == " " and space == " ": 
        continue
    elif i == " ": 
        count += 1
        space = copy.copy(i)
        continue
    else:
        space = copy.copy(i)
        continue

print(f"Your text is: {my_string} \nIt has {count + 1} words") 



