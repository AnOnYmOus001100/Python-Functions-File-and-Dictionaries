#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
1. Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
'''
def sublist(lst):
    sublist = []
    count = 0
    while count < len(lst):
        if lst[count] != 5:
            sublist.append(lst[count])
        else:
            return sublist
        count += 1
        
    return sublist

list1 = [12,44,21,5,6,76,5]
list2 = [2,43,56,12,4,33]
print (sublist(list1))
print (sublist(list2))


# In[2]:


'''
2. Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
'''
def check_nums(lst):
    ele = 0
    sublist = []
    
    while ele < len(lst):
        if lst[ele] != 7:
            sublist.append(lst[ele])
        else:
            return sublist
        ele += 1
    return sublist

list1 = [12,434,11,45,7,44,32]
list2 = [22,34,113,0,3]

print (check_nums(list1))
print (check_nums(list2))


# In[3]:


'''
3. Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
'''
def sublist(lst):
    sub = []
    counter = 0
    
    while counter < len(lst):
        if lst[counter] != "STOP":
            sub.append(lst[counter])
        else:
            return sub
        counter += 1
    return sub

list1 = ["ANY","START","NOT","STOP","BACK"]
list2 = ["HERE","HOP","HI","BANG"]

print (sublist(list1))
print (sublist(list2))


# In[4]:


# 4. Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

def stop_at_z(lst):
    counter = 0
    sublist = []
    
    while counter < len(lst):
        if lst[counter] != "z":
            sublist.append(lst[counter])
        else:
            return sublist
        counter += 1
    return sublist

list1 = ["a","any","can","z","c","none"]
list2 = ["not","here","d","nine"]
print (stop_at_z(list1))
print (stop_at_z(list2))


# In[6]:


'''
5. Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
'''
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
print (sum1)
    
sum2 = 0
x = 0

while x < len(lst):
    sum2 += lst[x]
    x += 1
print (sum2)

def sum_check():
    if sum1 == sum2:
        return True
    else:
        return False

print ("Is sum1 and sum2 equal ",sum_check())


# In[7]:


#6. Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(lst):
    counter = 0
    sub10 = []
    
    while counter < len(lst):
        if lst[counter] != 'bye' and counter < 10:
            sub10.append(lst[counter])
        else:
            return sub10
        counter += 1
    return sub10

list1 = ['any','bot','hope','bye','hack']
list2 = ['by','faith','none','hi','crack','let']
list3 = ['by','faith','none','hi','crack','let','any','bot','hope','no','bye','hack']

print (beginning(list1))
print (beginning(list2))
print (beginning(list3))


# In[ ]:




