print(1+True)
# here True treated as 1. 
# False treated as 0.
print(int(2.23))
print(float(39))

# decimal
print(0.1+0.1+0.1)
print(0.1+0.1+0.1-0.3)  #unexpected output
#use method 
from decimal  import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))
# same for fraction
from fractions import Fraction

import math
print(math.floor(3.5)) #always gives lower values
print(math.trunc(2.8)) #always goes towards zero.

# binary,hexal,octal representation
print(oct(64))
print(hex(64))
print(bin(3))
print(int('0o100',8))
print(int('040',6))
print(int('1001',2))

# random libraray
import random
print(random.random())  #gives random value between 0 t0 1
print(random.randint(1,4))  #gives random digit betwwen 1 to 4
l = ['saurabh','vedant','aditya','jay']
print(random.choice(l))
random.shuffle(l)
print(l)

# sets
set1 = {1,2,3,4}
print(set1 & {1,4}) # inter section of sets
print(set1 | {6,7,8}) #union of sets
# same operation act as diffrence(-),supersets,subsets, etc

# empty set is described as 
print(type(set()))
# it act as dictonary
print(type({}))