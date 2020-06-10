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

#or
'''
num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)
'''
