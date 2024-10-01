s = input()
n = len(s)
i, j = 0, n - 1
base = 31
mod = 10**9 + 7
powers = [1] * n

for k in range(1, n):
    powers[k] = (powers[k - 1] * base) % mod

prefix, suffix = 0, 0
while i < n - 1:
    prefix = (prefix * base + ord(s[i])) % mod
    suffix = (suffix + powers[i] * ord(s[j])) % mod
    if prefix == suffix:
        print(i + 1)
    i += 1
    j -= 1