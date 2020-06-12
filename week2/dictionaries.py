#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")


# In[ ]:


#We can accumulate counts for more than one character as we traverse the text. Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")


# In[ ]:


'''
OK, but you can see this is going to get tedious if we try to accumulate counts for all the letters. We will have to initialize a lot of accumulators, and there will be a very long if..elif..elif statement. Using a dictionary, we can do a lot better.

One dictionary can hold all of the accumulator variables. Each key in the dictionary will be one letter, and the corresponding value will be the count so far of how many times that letter has occurred.
'''
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
x['t'] = 0  # initialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x['t'] = x['t'] + 1  # increment the t counter
    elif c == 's':
        x['s'] = x['s'] + 1  # increment the s counter

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


# In[ ]:


'''
This hasn’t really improved things yet, but look closely at lines 8-11 in the code above. Whichever character we’re seeing, t or s, we’re incrementing the counter for that character. So lines 9 and 11 could really be the same.
'''
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
x['t'] = 0  # intiialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x[c] = x[c] + 1   # increment the t counter
    elif c == 's':
        x[c] = x[c] + 1   # increment the s counter

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


# In[ ]:


'''
 Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary and add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.
'''
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


# In[ ]:


'''
Note that the print statements at the end pick out the specific keys ‘t’ and ‘s’. We can generalize that, too, to print out the occurrence counts for all of the characters, using a for loop to iterate through the keys in x.
'''
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")


# In[ ]:


'''
Note that only those letters that actually occur in the text are shown. Some punctuation marks that are possible in English, but were never used in the text, are omitted completely. The blank line partway through the output may surprise you. That’s actually saying that the newline character, \\n, appears 5155 times in the text. In other words, there are 5155 lines of text in the file. Let’s test that hypothesis.
'''
f = open('scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))
print(txt_lines[70:85])


# In[ ]:


'''
2. Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.

'''
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()

word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    
    word_counts[word] += 1
 
print (word_counts)


# In[ ]:


'''
3. Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
'''
stri = "what can I do"

char_d = {}
for word in stri:
    for char in word:
        if char not in char_d:
            char_d[char] = 0
        char_d[char] += 1
print (char_d)


# In[ ]:


'''

'''

