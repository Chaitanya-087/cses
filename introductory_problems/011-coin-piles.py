t=int(input())
for _ in range(t):
    a,b = list(map(int, input().split()))
    if (a+b)%3==0 and max(a,b) <= 2*min(a,b):
        print("YES")
    else:
        print("NO")