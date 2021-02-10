a=input().split()
b=input().split()
c=set(a+b)
for i in c:
    if i in a and i in b:
        print(i,end=' ')
    
