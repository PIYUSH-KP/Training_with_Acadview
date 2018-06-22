print("__"*50)
print("solution 1")
print("__"*50)
# Q.1- Write a Python program to read last n lines of a file

num_lines = sum(1 for line in open('ques1.txt'))
print("Total no. of lines in filr = ",num_lines)

with open("ques1.txt") as f:
    data = f.readlines()


lastline = data[-1]
try:
    n = int(input("Enter the no. of lines to read from end: "))
    if(n>num_lines):
        raise ValueError
except ValueError:
    print("Enetr no. of lines less thsn or equal to total no. of lines in file ie ",num_lines)
    n = int(input("Enter the no. of lines to read from end: "))

last = data[-n:]
print(str(last))



print("__"*50)
print("solution 2")
print("__"*50)
#Q.2- Write a Python program to count the frequency of words in a file.
from collections import Counter
def word_count(name):
        with open(name) as f1:
                return Counter(f1.read().split())

print("Each word with it's frequencey in file: \n",word_count("file1.txt"))


print("__"*50)
print("solution 3")
print("__"*50)
# Q.3- Write a Python program to copy the contents of a file to another file

with open('file1.txt') as f1, open('file2.txt','w') as f2:
    for line in f1:
        f2.write(line)


#file1.txt contains The Zen of python
#file2 is empty

# file1 content will be copied to file2





print("__"*50)
print("solution 4")
print("__"*50)
# Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('father.txt') as f1, open('mother.txt') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1,line2)







print("__" * 50)
print("solution 5")
print("__"*50)
# Q.5- Write a Python program to write 10 random numbers into a file.
# Read the file and then sort the numbers and then store it to another file.
import random

with open('Random.txt', 'w') as f1:
    for x in range(10):
        f1.write(str(random.randint(100, 200)) + " ")

with open('Random.txt') as f1, open('SortedRandom.txt', 'w') as f2:
    for line in f1:
        nos = line.split()
        l = []
        for no in nos:
            l.append(int(no))
        l.sort()

    f2.write(str(l))
