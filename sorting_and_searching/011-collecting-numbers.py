n=int(input())
arr=list(map(int,input().split()))
ans = 1
indices = [0] * (n+1)
for i in range(n):
    indices[arr[i]] = i
 
for i in range(1,n):
    if indices[i+1] < indices[i]:
        ans+=1
print(ans)