y=int(input('enter year:'))
if(y%4==0 or y%400==0 and y%100!=0):
    print('year is leap')
else:
    print('year is not leap')

#O/P:
#enter year:2024
#year is leap
