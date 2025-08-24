#Tuple
#program-1
a=int(input("Enter a number"))
b=int(input("Enter a number"))
(a,b)=(b,a)
print(a)
print(b)
#program-2
pi=3.14
def circle(r):
    return(2*pi*r)
radius=float(input("Enter a number"))
(circum)=circle(radius)
print(circum)
#program-3
numbers=(-3,4,2,-45,933)
positive=()
for i in numbers:
    if i>0:
        positive+=(i,)
print(positive)