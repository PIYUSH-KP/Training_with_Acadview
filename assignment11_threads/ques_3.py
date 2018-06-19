import threading as th
import time


# Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec


def delay_print():
    arr = [1, 2, 3, 4, 5]
    delay = 2
    for i in arr:
        print(th.currentThread().getName(), i)
        time.sleep(delay)
        delay += 2

d = th.Thread(name="Elements of arr: ", target=delay_print)
d.start()