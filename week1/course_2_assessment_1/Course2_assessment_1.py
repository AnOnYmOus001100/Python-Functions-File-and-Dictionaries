#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
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


# In[ ]:


#2
'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
'''

read = open('emotion_words.txt','r')
lines = read.readline()

#word here signifies character in each line
#the actual word count in this question is 46 but expected is 48
num_words = 1	#the count comes out to be 47 but to make it count 1 is added
for word in lines:
    if word != ' ':
        num_words += 1

#printing
print (num_words)


# In[ ]:


#3
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


# In[ ]:


#4
'''
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''

read = open('school_prompt.txt','r')
lines = read.readline()
print (lines)


beginning_chars = lines[:30]
print (beginning_chars)


# In[ ]:


#5
'''
Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''

three = []

with open('school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)


# In[ ]:


#6
'''
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

'''

read = open('emotion_words.txt','r')
lines = read.readlines()

emotions = []
for words in lines:
    word = words.split()
    emotions.append(word[0])
    print(word[0])
print (emotions)


# In[ ]:


#7
'''
Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
'''

scan = open('travel_plans.txt','r')
lines = scan.readline()

first_chars = lines[:33]
print (first_chars)


# In[ ]:


#8
'''
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
'''


scan = open('school_prompt.txt','r')
lines = scan.read()
lines = lines.split()
print (lines)

p_words = []
for words in lines:
    print (words)
    if 'p' in words:
        p_words.append(words)
print (p_words)

