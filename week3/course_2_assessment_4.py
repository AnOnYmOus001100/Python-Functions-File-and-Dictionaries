#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(num):
    return num
print (int_return(5))


# In[2]:


#Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(num):
    return num+2
print (add(5))


# In[3]:


#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(string):
    return string+"Nice to meet you!"
print(change("helo"))


# In[4]:


#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
print(accum([3,4,1,0]))


# In[5]:


#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(lst):
    count_length = 0
    for num in lst:
        count_length += 1
    if count_length >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"
print(length([2,4,5,5,6,7]))
print (length([1]))


# In[6]:


'''
You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
'''
def divide(num):
    return num/2

def sum(num):
    return divide(num) + 6

print(divide(5))
print(sum(4))


# In[ ]:




