hrs =float(input('Enter your Work Hours:'))
rate=float(input('Enter your pay rate per hour:'))


def computepay(hrs,rate):
 if hrs>40.0:
     pay=1.5*(hrs-40.0)*rate
     py=(40*rate)+pay
     return py
 else:
     py=hrs*rate
     return py
p = computepay(hrs,rate)
print('Pay',p)
