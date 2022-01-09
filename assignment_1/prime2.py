a=0
n=int(input('enter the no:'))
for i in range(2,n):
    if(n%i==0):
        a=1
        break
if(a==0):
    print('num is prime')
else:
    print('num is prime')

#O/P:
#enter the no:13
#num is prime


