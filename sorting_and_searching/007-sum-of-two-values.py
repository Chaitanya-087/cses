n,x=map(int,input().split())
a=list(map(int,input().split()))
if min(a) > x:
    print("IMPOSSIBLE")
    exit()
a=[[num,i+1] for i,num in enumerate(a)]
a.sort()
def twoSum(arr,k):
    l,r=0,len(arr)-1
    while l < r:
        _sum = arr[l][0] + arr[r][0]
        if _sum == k:
            return [arr[l][1],arr[r][1]]
        elif _sum < k:
            l += 1
        else:
            r -= 1
    return []
res=twoSum(a,x)
if res:
    print(*sorted(res))
else:
    print("IMPOSSIBLE")