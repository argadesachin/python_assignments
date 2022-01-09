p=int(input('starting no:'))
q=int(input('ending no:'))
for n in range(p,q):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
            break
    if(f==0):
        print(n)

#O/P:
#starting no:10
#ending no:25
#11
#13
#17
#19
#23
