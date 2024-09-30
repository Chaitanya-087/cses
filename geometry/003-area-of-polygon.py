n=int(input())
points = []
for _ in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

def det(a,b):
    return a[0]*b[1] - a[1]*b[0]

def area(p):
    return (sum(det(p[i],p[i+1]) for i in range(n-1)) + det(p[-1],p[0]))

print(abs(area(points)))



