largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num=='done':
        break
    try:
        n=float(num)
        if largest==None:
            largest=n
        elif n>largest:
            largest=n

        if smallest==None:
            smallest=n
        elif n<smallest:
            smallest=n
    except:
        print('Invalid input')
        continue

print("Maximum is",int(largest))
print("Minimum is",int(smallest))
