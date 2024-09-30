res = set()
def perm(s, start):
    if start == len(s):
        res.add("".join(s))
        return
    for i in range(start,len(s)):
        if i>start and s[i] == s[start]:continue
        s[start],s[i] = s[i],s[start]
        perm(s,start+1)
        s[start],s[i] = s[i],s[start]
 
s = input()
s = sorted(s)
perm(s,0)
print(len(res))
for p in sorted(list(res)):
    print(p)