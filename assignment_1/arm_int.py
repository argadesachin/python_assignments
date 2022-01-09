a=int(input('enter the starting:'))
b=int(input('enter the ending:'))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
        n=int(n/10)
        s=s+(d*d*d)
    if(s==i):
        print(i)

#O/P:
#enter the starting:100
#enter the ending:1000
#153
#370
#371
#407
