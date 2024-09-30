s=input()
m=1
cnt=1
for i in range(1,len(s)):
    if s[i]==s[i-1]: cnt+=1
    else: cnt=1
    m=max(m,cnt)
print(m)