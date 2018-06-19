# Q4. Call factorial function using thread.
import threading as th
def fact(n):
    a = 1
    for i in range(n, 0, -1):
        a *= i
    print(th.currentThread().getName(), a)


n = int(input("Enter number to calculate factorial of "))
t = th.Thread(name="factorial is: ", target=fact, args=(n,))
t.start()