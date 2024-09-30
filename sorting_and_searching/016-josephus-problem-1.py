from collections import deque
n=int(input())
q=deque(range(1, n+1))
f=True
while q:
    e=q.popleft()
    if f:
        q.append(e)
    else:
        print(e, end=' ')
    f=not f