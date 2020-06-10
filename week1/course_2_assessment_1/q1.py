'''
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
'''

read = open('travel_plans.txt','r')
lines = read.readlines()
num = 0
for line in lines:
    for char in line:
        num += 1
print (num)
read.close()

#or
'''
fileref = open("travel_plans.txt","r")
num = 0
for i in fileref:
    num += len(i)
fileref.close()
'''
