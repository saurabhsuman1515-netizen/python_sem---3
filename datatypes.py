a = 10
print(a)
print(type(a))

b = 10.00
print(b)
print(type(b))

c = 10/3
print(c)
print(type(c))

d = "saurabh"
print(d)
print(type(d))

e = 'a'
print(e)
print(type(e))

import math
math.pi
print(math.pi)

import random
random.random()
print(random.random()) #parenthese is use because random is a function

random.choice([1,2,3,4,5])
print(random.choice)
print(random.choice)
print(random.choice)
print(random.choice)
# error
import random

print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))

username = "saurabhsuman"
print(len(username))
print(username[0])
print(username[3])
print(username[-1])#indexing start from end
# username[0]='a'   [#Giving type error cause of string is immutable]
print(username[1:3]) #slicing
 
n = [1,2,3]
m = n
print (m)
print (n)
print(m==n) # same values
print (m is n) #checking refrence value

a = [2,3,4]
b = [2,3,4]
print(a is b)

print(repr('saurabh'))
print(str('saurabh'))
print('chai')