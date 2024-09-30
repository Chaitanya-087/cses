n=int(input())
z,r=0,5
while n//r>0:
    z+=n//r
    r*=5
print(z)     