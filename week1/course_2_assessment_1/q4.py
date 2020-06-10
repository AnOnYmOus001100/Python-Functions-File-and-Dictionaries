'''
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''

read = open('school_prompt.txt','r')
lines = read.readline()
print (lines)


beginning_chars = lines[:30]
print (beginning_chars)

#or
'''
f = open('school_prompt.txt', 'r')
beginning_chars = f.read(30)
print(beginning_chars)
'''
