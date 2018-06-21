""""
Q.1- Name and handle the exception occured in the following program:

a=3
 if a<4:
    a=a/(a-3)
     print(a)
"""
print("Name of error:  ZeroDivisionError" )

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)

except ZeroDivisionError:
    print("cannot divide by zero")

finally:
    print("Don't ever try to divide by zero")



print("__"*50)
"""
Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3]
print(l[3])
"""

print("Name of error:  IndexError")

l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("bhai list se bahar jaa rha anddr reh")
finally:
    print("Always cut you dress according to your cloth")


print("__"*50)
"""
Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
"""

print("output in below 2 lines: \nAn exception\nNameError: Hi there")



print("__"*50)



"""Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
"""

print("output in below 2 lines: \n-5.0\na/b result in 0")


print("__"*50)

# Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error


#ValueError
try:
    a = int(input("Enter a digit: "))
except ValueError as VE:
    print("You were supposed to enter nothing but Integer\n",VE)
else:
    print(a)


#IndexError
l = [1,2,3,4,5,6,7]
try:
    print(l[10])
except IndexError as IE:
    print("\n\nAbhi Index Error Hona tha, exception handling kr li\n",IE)
else:
    print(l[10])


try:
    from math import bang_bang
except ImportError as ie:
    print("\nKya import karna chahte ho bhai! bang_bang math me nhi hai\n",ie)
else:
    print("ho gya import")



print("__"*50)

#Q.6- Create a user-defined exception AgeTooSmallError()
# that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18)


class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter age: "))
except ValueError:
    print("enter integer as age and nothin else")
    age = int(input("Enter age: "))

while (age <= 18):
    try:
        if (age < 18):
            raise AgeTooSmallError

    except AgeTooSmallError:
        print("enter age greater than 18")
        age = int(input("Enter age: "))

print("your entered age is: ", age)
