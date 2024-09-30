n=int(input())
s=n*(n+1) // 2
if s & 1: print("NO")
else:
    print("YES")
    t = s // 2
    l = [0]*n
    for i in range(n,0,-1):
        if t == 0: break
        if t - i < 0: continue
        t -= i
        l[i-1] = 1
    print(l.count(1))
    for i in range(n):
        if l[i]:
            print(i+1,end=" ")
    print()
    print(l.count(0))
    for i in range(n):
        if not l[i]:
            print(i+1,end=" ")