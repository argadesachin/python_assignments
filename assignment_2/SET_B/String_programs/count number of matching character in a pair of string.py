s1=input("enter string 1:")
s2=input("enter string 2:")
c1=0
for i in range(max(len(s1), len(s2))):
    for j in range(min(len(s1), len(s2))):
        if(s1[i]==s2[j]):
            c1=c1+1
            break
print("no of matching character=",c1)

#O/P:
#enter string 1:sachin
#enter string 2:argade
#no of matching character=1
