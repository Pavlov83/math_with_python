#By given input x,y press 1 to compute x to the power of y and x divided by y

print('Please enter first input number')
x = int(input())

print('Please enter second input number')
y = int(input())

print('Please enter 1 for power x,y or 2 for divide x/y')
func = int(input())

def powers(x,y):
    print('%g^(%g) = %g' %(x,y,x**y))

def division(x,y):
    print('%g/%g = %g'%(x,y,x/y))

if(func == 1):
    powers(x,y)
elif(func == 2):
    division(x,y)
else:
    print(
        'Invalid selection'
    )


