'''
Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
'''

scan = open('travel_plans.txt','r')
lines = scan.readline()

first_chars = lines[:33]
print (first_chars)

#or
'''
f = open('travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)
'''
