a=input().split()
b=input().split()
c=set(a+b)
d=0
for i in c:
    if i in a and i in b:
        d=d+1
print(d)
        
