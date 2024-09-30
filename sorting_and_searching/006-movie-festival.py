n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x: x[1])
 
time=0
cnt=0
for a,l in arr:
    if a >= time:
        cnt+=1
        time=l
print(cnt)