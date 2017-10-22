import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap = 0
a1=0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a1=a[j]
            a[j]=a[j+1]
            a[j+1]=a1
            swap+=1
    if swap==0:
        break
print('Array is sorted in',swap,'swaps.')        
print('First Element:',a[0])
print('Last Element:',a[-1])

  