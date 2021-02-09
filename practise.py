s=input()
w=s.split()
cnt=0
for i in range(0,len(w)-1):
    for j in range(i+1,len(w)):
        if w[i]==w[j]:
            cnt=cnt+1
print(cnt)
            
            
               
