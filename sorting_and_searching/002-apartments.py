n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
s=list(map(int,input().split()))
s.sort()
a.sort()
ans,i,j = 0,0,0
while i < n and j < m:
    if abs(a[i] - s[j]) <= k:
        ans += 1
        i += 1
        j += 1
    elif a[i] < s[j]:
        i += 1
    else:
        j += 1
print(ans)