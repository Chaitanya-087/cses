n=int(input())
arr=list(map(int, input().split()))
arr.sort()
x=arr[n//2]
print(sum(abs(num-x) for num in arr))