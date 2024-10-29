def count_strings(n,s):
    """Count the number of strings of length n that contain s as a substring."""
    mod = 10**9 + 7
    m=len(s)
    if m > n:
        return 0
    possible = n - m + 1
    return possible * pow(26, n - m, mod) % mod

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(count_strings(n,s))
    