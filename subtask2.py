list=[]
x=0
n=0
s=0
x=int(input("enter a number: "))
while(x!=-1):
    list.append(x)
    s=s+x
    n=n+1
    x=int(input("enter a number: "))
if n==0:
    s=-1
    a=-1
    m=0
else:
    a=s/n
    m=min(list)

print(f"the sum is {s}, and the mean is {a}, and the minimum is {m}")
