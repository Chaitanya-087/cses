def precomputeLpsArr(pattern):
    N = len(pattern)
    lps = [0] * N
    
    # previous longest prefix suffix length
    length = 0
    i = 1
    
    while i < N:
        if pattern[length] == pattern[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

word=input()
pattern=input()
ans = 0
lps = precomputeLpsArr(pattern)
i,j = 0,0
N,M = len(word),len(pattern)

while (N-i) >= (M-j):
    if pattern[j] == word[i]:
        i+=1
        j+=1
    if j == M:
        ans += 1
        j = lps[j-1]
    elif i < N and pattern[j] != word[i]:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1

print(ans)