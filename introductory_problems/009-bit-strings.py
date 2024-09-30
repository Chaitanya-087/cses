n=int(input())
MOD=10**9+7
res = 1
b = 2
while n:
    if n & 1:
        res = (res * b) % MOD
 
    b = (b * b) % MOD
    n >>= 1
print(res)