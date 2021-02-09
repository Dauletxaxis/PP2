a=input()
b=input()
if b in a:
    print(a+b)
    quit()
for i in range(0,len(b)):
    if b in a+b[len(b)-1-i:len(b)]:
        print(a+b[len(b)-1-i:len(b)])
        quit()
    
