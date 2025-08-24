a=input("String")
c=0
w=1
for i in a:
    if i!='':
        c+=1
    else:
        w+=1
    x=a.count('\n')+1
print(c-x+1) 
print(w+x-1)
print(x)