n=int(input())
if n==3 or n==2: print('NO SOLUTION')
else:
    for i in range(1,n+1):
        if i & 1 == 0: print(i, end=' ')
    for i in range(1,n+1):
        if i & 1: print(i, end=' ')