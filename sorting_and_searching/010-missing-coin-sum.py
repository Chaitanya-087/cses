n=int(input())
arr=list(map(int,input().split()))
acc=0
for a in sorted(arr):
    if a > acc+1:
        break
    acc+=a
print(acc+1)