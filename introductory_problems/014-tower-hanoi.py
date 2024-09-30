n=int(input())
def solve(s,h,d,n):
    if n == 1:
        print(f'{s} {d}')
        return
    solve(s,d,h,n-1)
    print(f'{s} {d}')
    solve(h,s,d,n-1)

print(2**n-1)
solve(1,2,3,n)