'''
# Function of the code
This code is meant to show how to manipulate multiple Duty Cycles of a PWM using a for loop, however, the for loop can not be used as it is.

In this code, dc2 has been initialized with the value 4. In a up and down fade, the value 4 can be going up or down, depending on the sign of the increment.
Within the for loop, no increment can be asigned, unless it is known in what direction the fade is going.

# Visual explenation:

         /\        
        /  \     +a
 -a    /    \    /
   \  4      4  /
    \/        \/


# Possible solutions:
- always go up when starting the code (a = +1)
- have a starting delay, esssentialy creating a phase shift in fades

'''


dc1 = -2
dc2 = 4
dc3 = 10
a1 = 0
a2 = 0
a3 = 0



dcList = [dc1, dc2, dc3]
aList = [a1, a2, a3]

for i in range(len(dcList)):    # "range(len(<list>))" creates index numbers for a list, allowing element modification.
                                # len(<list>) gives the total number of items (n) and range(n) generates numbers from 0 to n-1, essentially creating the index for <list>.
                                # Example: [0, 1, 2, 3, 4, 5] if n == 6.
    if dcList[i] <= 0:              
        aList[i] = 1
    if dcList[i] == 10:
        aList[i] = -1
    dcList[i] = dcList[i] + aList[i]

print(dcList) # Expected output: [-1, 5, 9] -> Output: [-1, 4, 9] -> dc2 stays unchanged!
print(aList) # Expected output: [1, 1, -1] -> Output: [1, 0, -1] -> a2 stays unchanged!