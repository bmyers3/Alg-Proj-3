Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> x = 0
>>> y = 0
>>> a = random.uniform(0, 1)
>>> b = random.uniform(0, 1)
>>> c = random.uniform(0, 1)
>>> for i in range(10000):
	if(a + (b+c) == (a + b) + c):
		x = x + 1
	else:
		y = y + 1
	a = random.uniform(0, 1)
	b = random.uniform(0, 1)
	c = random.uniform(0, 1)

	
>>> print(x, ", ", y)
8237 ,  1763
>>> 