s=input("enter string:")
s=s.split(' ')
print(s)
print("even length words:")
for i in s:
    if(len(i)%2==0):
        print(i)

#O/P:
#enter string:rbnb cdj college shrirampur
#['rbnb','cdj', 'college', 'shrirampur']
#even length words:
#rbnb
#college
