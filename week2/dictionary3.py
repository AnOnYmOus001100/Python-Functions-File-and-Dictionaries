#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
'''
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] += 1
print (d)    
    
keys = list(d.keys())
    
min_value = keys[0]
for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print (min_value)
    


# In[ ]:


'''
5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
'''
product = "iphone and android phones"

lett_d = {}
for letter in product:
    if letter not in lett_d:
        lett_d[letter] = 0
    lett_d[letter] += 1
print (lett_d)

keys = list(lett_d.keys())
max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print (max_value)

