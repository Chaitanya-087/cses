n=int(input())
arr=list(map(int, input().split()))
def solve(i, sum1, sum2):
    if i == n:
        return abs(sum1-sum2)
    return min(solve(i+1,sum1+arr[i],sum2), solve(i+1,sum1,sum2+arr[i]))
print(solve(0,0,0))