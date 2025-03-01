#Function of the code: define xyz, convert xyz into new abc, print and print a random number

import random                       #imports module "random"

x = 1                               #type asignment
y = 2.8
z = 1j

a = float(x)                        #type conversion
b = int(y)
c = complex(x)

print(a)                            #prints
print(b)
print(c)

print(type(a))                      #prints the type
print(type(b))
print(type(c))

print(random.randrange(1,10))       #prints a random int int between 1-10