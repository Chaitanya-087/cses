n=int(input())
arr=list(map(int,input().split()))
s=set()
ans=0
l=0
for a in arr:
    while a in s:
        s.remove(arr[l])
        l+=1
    s.add(a)
    ans=max(ans,len(s))
print(ans)