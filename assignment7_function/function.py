# Q.1- Create a function to calculate the area of a circle by taking radius from user.

import math

def ar(r):
    return math.pi * r**2

radius = float(input("Enter radius of circle: "))
area_c = ar(radius)

print("Area of circle is:", area_c)



# Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the
# perfect numbers between 1 and 1000.
# [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.

def perfect(x):
    sum = 0
    for i in range(1, x):
        if (x % i == 0):
            sum = sum + i

    if (x == sum):
        print('perfect')
    else:
        print('nah, not perfect')

a = int(input("Enter the no. to be checked for perfect or not: "))
perfect(a)




# Q.3- Print multiplication table of 12 using recursion.

#table of any no. till multiplictaion upto 10
def table(n,i=1):
    if i>10:
        print("Table till  10 completed")
    else:
        print(n, ' X ' , i ,' = ',  n*i)
        return table(n,i+1)

#Enter 12 for table of 12
n = int(input("Enter the no. to print it's table: "))
table(n)



# Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a: int , b: int)->int:
        if (b == 1):
            return (a)
        if (b != 1):
            return (a * power(a, b - 1))

base = int(input("Enter base: "))
exp = int(input("Enter exponent value: "))
print('Result of ',base,'^',exp ,'is:', power(base, exp))




# Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary

fact = {0:1,1:1}

def factorial(n):
    if n in fact.keys():
        return fact[n]
    else:
        newVal = n*factorial(n-1)
        fact[n] = newVal
        return newVal

p = int(input("Enter the no. to calculate factorial : "))
print(factorial(p))
print(fact)


