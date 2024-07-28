'''
This script is to execute Math operations & string formatting

'''
x = 2
y = 3

print (f"Mutiplication of two numbers: {x*y}")
print (f"Division of two numbers: {(x / y):9.2f}")
print (f"Mod of two numbers: {x%y}")
print ("Mod of two numbers: %s" %(x%y))
print ('Mod of two numbers {}:'.format(x%y))
#num1 = int(input("Enter number1"))
#num2 = int(input("Enter number2"))
#result = num1%num2
print ('Result of decimal precision {:100.2f}'.format(x/y))
print ('Value of x: {0:>8} Value of y : {0:8<}'.format(x,y))