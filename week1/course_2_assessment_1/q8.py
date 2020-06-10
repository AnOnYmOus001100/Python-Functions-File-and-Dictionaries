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
'''
fileref = open('school_prompt.txt', 'r')
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]
'''
