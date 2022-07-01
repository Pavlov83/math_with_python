#!/usr/bin/env python
# coding: utf-8

# In[13]:


from numpy import random

def guessNum():
    
    num = random.randint(1,100)
    
    guess = int(input('Please guess num 1 - 100:  '))
    
    while guess != num:
        if guess < num :
            print('Too low')
        elif guess > num :
            print('Too high')
        guess=(int(input('Guess again')))
    print("That is the num!")
    print(num)

