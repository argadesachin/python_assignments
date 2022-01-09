def max(a,b,c):
    if(a>b and a>c):
        print(f"{a} is max")
    elif(b>a and b>c):
        print(f"{b} is max")
    else:
        print(f"{c} is max")

a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
max(a,b,c)

#output:
#enter value of a:17
#enter value of b:9
#enter value of c:27
#27 is max
