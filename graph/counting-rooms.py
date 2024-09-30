from collections import deque
n,m=map(int,input().split())
grid=[["#" for _ in range(m)] for _ in range(n)]

for i in range(n):
    grid[i]=list(input())

def isValid(grid,r,c):
    return 0 <= r < n and 0 <= c < m and grid[r][c] == "."

def bfs(r,c):
    q=deque([(r,c)])
    while q:
        x,y=q.popleft()
        for dx,dy in ((0,1),(0,-1),(-1,0),(1,0)):
            if isValid(grid,x+dx,y+dy):
                q.append((x+dx,y+dy))
                grid[x+dx][y+dy]="#"

cnt=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==".":
            bfs(i,j)
            cnt+=1
print(cnt)