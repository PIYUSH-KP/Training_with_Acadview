import threading as th
import time


# Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
def ques_1():
    print(th.currentThread().getName(), 'BORN')
    time.sleep(5)
    print('After 5 seconds....\n I AM BACK')


a = th.Thread(name="5 seconds of sleep", target=ques_1)
a.start()
