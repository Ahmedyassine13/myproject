def subtask7_3(n):
    x=0
    while(x*x<n):
        x=x+1
    return (x-1)*(x-1)

a=int(input("enter a number:"))
y=subtask7_3(a)
print("this is thr number:"+str(y))

