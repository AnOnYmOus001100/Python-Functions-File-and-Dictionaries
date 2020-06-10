'''
Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''

three = []

with open('school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)
