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
