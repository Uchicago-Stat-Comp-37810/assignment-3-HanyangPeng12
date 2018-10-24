# Name: Hanyang Peng
# hw3.py

##### Template for Homework 3, exercises 1 -  ######

import math
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

def is_divisible(m,n):
	if(n==0):
		return False
	if(m%n==0):
		return True
	else:
		return False

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # What should this return?  False
#0 can't be divisor
print(is_divisible(42,-6))  # This should return True


# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(m,n):
	if(m==n):
		return False
	else:
		return True

#Also we can define like this:
def not_equal2(m,n):
	if(m>n):
		return True
	elif(m<n):
		return True
	else:
		return False

# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(1.1,2.1)) # This should return True
print(not_equal(1.101,-1.101)) # This should return True
print(not_equal(4.5,4.5)) # This should return False

print(not_equal2(1.1,2.1)) # This should return True
print(not_equal2(1.101,-1.101)) # This should return True
print(not_equal2(4.5,4.5)) # This should return False

# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
	return a*b+c

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test = multadd(0.5,math.cos(math.pi/4),math.sin(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(2,math.log(12,7),math.ceil(276.0/19.0))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
	n=random.randint(0,100)
	print("We generate a random integer, which is", n)
	if(n%3==0):
		return True
	else:
		return False

# Test Cases
##### YOUR CODE HERE #####
print(rand_divis_3())
