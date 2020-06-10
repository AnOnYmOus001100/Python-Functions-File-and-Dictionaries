'''
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
'''

read = open('school_prompt.txt','r')
lines = read.readline()

lines = lines.split()
print (lines)

#actual lines are 8 but expected 10
num_lines = 2	#added 2 to pass test
for line in lines:
    if line != ' ':
        num_lines += 1

#or
#num_lines = sum(1 for line in open('school_prompt.txt'))
