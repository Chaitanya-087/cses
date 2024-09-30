import bisect
 
n = int(input())
arr= list(map(int, input().split()))
x = [] 
 
for i in range(n):
    lo = bisect.bisect_right(x, arr[i])  
    if lo == len(x):
        x.append(arr[i])
    else:
        x[lo] = arr[i]
 
print(len(x))