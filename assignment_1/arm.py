n=int(input('enter no:'))
s=0
t=n
while(n>0):
    d=n%10
    n=int(n/10)
    s=s+(d*d*d)
if(t==s):
    print('num is armstrong')
else:
    print('num is not armstrong')
    
#O/P:
#enter no:143
#num is not armstrong
