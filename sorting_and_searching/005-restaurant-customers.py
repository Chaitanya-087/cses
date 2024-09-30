n=int(input())
a=[]
l=[]
for _ in range(n):
    t,k=map(int,input().split())
    a.append(t)
    l.append(k)
 
a.sort()
l.sort()
 
cnt = 0
maxi = 0
i,j=0,0
while i<n and j<n:
    if a[i]<=l[j]:
        cnt+=1
        i+=1
    else:
        cnt-=1
        j+=1
    maxi=max(maxi,cnt)
print(maxi)