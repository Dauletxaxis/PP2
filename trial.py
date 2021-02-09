a=input()
s=a.split()
w=0
l=[]
for i in s:
    w=w+int(i)
    l.append(w)
print(max(l))
