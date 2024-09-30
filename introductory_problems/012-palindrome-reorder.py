s=input()
h={}
for c in s:
    h[c]=h.get(c,0)+1
k=0
for c,f in h.items():
    k += f%2
if k>1: print("NO SOLUTION")
else:
    s,m,e = "", "", ""
    for c,f in h.items():
        if f%2==0: 
            s = s + c*(f//2)
            e = c*(f//2) + e
        else: 
            m = c*f
    print(s+m+e)