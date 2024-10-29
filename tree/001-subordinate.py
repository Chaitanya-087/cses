import sys
sys.setrecursionlimit(10**6)
n=int(input())
arr = list(map(int,input().split()))
adj = [[] for _ in range(200005)]
subordinate = [0] * 200005
def dfs(n):
    for child in adj[n]:
        subordinate[n] += dfs(child)
    return subordinate[n] + 1
for i in range(n-1):
    adj[arr[i]].append(i+2)
dfs(1)
print(*subordinate[1:n+1])