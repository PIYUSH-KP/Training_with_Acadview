import threading as th
import time

# Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.
def ques_2():
    for i in range(1, 11):
        print(th.currentThread().getName(), i)
        time.sleep(1)


b = th.Thread(name="\nPrinting 1 to 10:", target=ques_2)
b.start()
