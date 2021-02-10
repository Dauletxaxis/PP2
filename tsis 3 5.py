a=input().split()
d=a+a
b=int(input())
c=b%len(a)
if c>=0:
    print(d[len(a)-c:len(a)-1-c+len(a)+1])
