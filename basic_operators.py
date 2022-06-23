from IPython.display import display,Math
################# Using if statements #################

if 4+2 == 6:
    print('true')

#example 2:

    x1 =5
    x2 =4

if x1>x2:
    print('%g is greater than %g',(x1,x2))
elif x1<x2:
    print('%g is greater than %g'%(x2,x1))
else:
    print('%g is equal to %g' %(x1,x2))

####Given variables i,j print i**-j where i>0,j>0###

for i in range(0,4):
    for j in range(0,5):
        if i>0 and j>0:
            display(Math('%g^{-%g} = %g' %(i,j,i** -j)))
