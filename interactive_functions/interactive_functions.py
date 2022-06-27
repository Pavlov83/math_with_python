
def my_function():
    print('my_function works')

#function parameters
def print_name(name):
    print("My name is %s," %name)
print_name('Paul')

##compute remainder

def compute_remainder(x,y):
    div = int(x/y)
    remain = x%y
    print('%g goes into %g,%g times.The remainder  is %g.'%(x,y,div,remain))

def division_with_input():
    print('Please enter x')
    x = int(input())
    print('Please enter y')
    y = int(input())
    div = int(x/y)
    remain = x%y
    print('%g goes into %g,%g times.The remainder is %g.' %(x,y,div,remain))


division_with_input()