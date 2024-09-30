n,x=list(map(int,input().split()))
p=list(map(int,input().split()))
cnt,_ = 0,p.sort()
l,r=0,n-1
while l <= r:
    t=p[l]+p[r]
    cnt += 1
    if t<=x:
        l += 1
        r -= 1
    else:
        r -= 1
print(cnt)