

hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter rate:"))
if h<=40.0 :
 ans=h*rate
 print(ans)
elif h>40.0 :
 left=h-40
 left = left*rate*1.5
 pay = left+40*rate
 print(pay)
