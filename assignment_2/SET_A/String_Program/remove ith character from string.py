s=input("Enter String:")
print("original string=",s)
newstr=" "
pos=int(input("enter the position to remove character:"))
for i in range(len(s)):
    if(i!=pos):
        newstr=newstr+s[i]
print("after removal character string=",newstr)


#O/P:
#Enter String:rbnb college spur
#original string= rbnb colleges
#enter the position to remove character:9
#after removal character string=  rbnb collge spur
