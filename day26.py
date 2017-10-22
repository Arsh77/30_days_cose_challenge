d1,m1,y1 = list(map(int, input().strip().split()))
d,m,y = list(map(int, input().strip().split()))
f=0
if y1>y:
    f=10000
elif y1==y:
    if m1>m:
        f = 500*(m1-m)
    elif m1==m and d1>d:
        f=15*(d1-d)
print(f)        
        