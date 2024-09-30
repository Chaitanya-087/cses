import math
n=int(input())
x,y=[],[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

area = 0 

for i in range(n):
    area += x[i] * y[i + 1]
    area -= x[i + 1] * y[i]
area = abs(area)

boundary = 0
for i in range(n):
    if x[i] == x[i+1]:
        boundary += abs(y[i] - y[i+1])
    elif y[i] == y[i+1]:
        boundary += abs(x[i] - x[i+1])
    else:
        boundary += math.gcd(abs(x[i] - x[i+1]), abs(y[i] - y[i+1])) 
        
print((area + 2 - boundary) // 2, boundary)   
