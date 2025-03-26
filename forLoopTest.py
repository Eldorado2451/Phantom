
dc1 = -2
dc2 = 4
dc3 = 10
a1 = 0
a2 = 0
a3 = 0



dcList = [dc1, dc2, dc3]
aList = [a1, a2, a3]

for i in range(len(dcList)):
    for j in range(len(aList)):         # FIXME: this does not work as intended! the nested loop is not executed 
        if dcList[i] <= 0:              # well enough. The same index i should be used for both lists.
            aList[j] = 1
        if dcList[i] == 10:
            aList[j] = -1
dcList[i] = dcList[i] + aList[j]

for k in range(len(dcList)):
    print(dcList[k]) # Expected output: -1, 5, 9

print(aList)

