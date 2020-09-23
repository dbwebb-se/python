"""
Implementation of bubblesort
"""
l = [2,5,1,0,3]
print(l)
n = len(l)
for j in range(n-1):
    for i in range(n-1):
        if l[i] > l[i+1]:
            tmp = l[i]
            l[i] = l[i+1]
            l[i+1] = tmp
print(l)
