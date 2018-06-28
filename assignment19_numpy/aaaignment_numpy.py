# Question 1

import numpy as np
a = np.random.rand(10,1)
print(a)
print("Mean of elements in array: ",np.mean(a))


# Question 2

b = np.random.rand(20,1)
print(b)
#standard deviation
print("standard deviation of elemrnts in array: ",np.std(b))
#variance
print("variance of elemrnts in array: ",np.var(b))



# Question 3

c = np.random.rand(10,20)
print(c)
d = np.random.rand(20,25)
print(d)

m = np.dot(c,d)
print("Matrix Multiplication of c and d: \n",m)

print("\n sum of elememts in multiplication array is: ", np.sum(m))



# Question 4

A = np.arange(1,11).reshape(10,1)
def fun(x):
    return 1 / (1 + np.exp(-x))

fun = np.vectorize(fun)

new_array = fun(A) 
print("after applyin function to A: \n",new_array)
