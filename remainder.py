a = 10
b = 3

#division returns the number

#Remainder operator returns the remaining value after division


#division = int(a/b)
remainder = a%b

print('%g goes into %g, %g times with remainder of %g',(b,a,remainder))

#if we want to print even numbers(divisible by two) we expect zero remainder
nums = range(-5,6)

for i in nums:
    if i%2 == 0:
        print('%g is an even number' %i)
    else:
        print('%g is and odd number' %i)