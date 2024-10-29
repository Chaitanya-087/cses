q=int(input())
for _ in range(q):
    k=int(input())
    k-=1
    n=1
    while k>9*n*pow(10,n-1):
        k-=9*n*pow(10,n-1)
        n+=1
    num=pow(10,n-1)+k//n
    print(str(num)[k%n])