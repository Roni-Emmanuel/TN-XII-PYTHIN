x=int(input("Enter any number"))
y=int(input("Enter any number"))
if x>y:
    min=x
else:
    min=y
while(1):
    if(min%x==0) and (min%y==0):
        print("LCM IS",min)
        break
    min=min+1