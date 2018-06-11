# Q.1- Take 10 integers from user and print it on screen

for i in range(10):
    x = int(input("Enter a number: "))
    print(x)



# Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while(True):
    print(x)



# Q.3- Create a list of integer elements by user input.
# Make a new list which will store square of elements of previous list.

l = []
squares = []
n = int(input("Enter the no. of elements in list: "))
for j in range(n):
    k = int(input("Enter the elements of list: "))
    l.append(k)
for m in l:
    squares.append(m*m)

print("original list: ",l)
print("square list: ",squares)




#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

a = ['Piyush', 9.5, 10, 'Acadview', 5, 6, 'LPU', 16, 8.58, 'Python', 'Code', 35, 8.44]
int_list = []
float_list = []
string_list = []
for b in a:
    if (type(b) == int):
        int_list.append(b)
    elif (type(b) == float):
        float_list.append(b)
    else:
        string_list.append(b)

print("List of Integer: ", int_list)
print("List of Floats: ", float_list)
print("List of Strings: ", string_list)




# Q.5- Using range(1,101), make a list containing even and odd numbers.

even = []
odd = []

for c in range(1,101):
    if c%2 == 0:
        even.append(c)
    else:
        odd.append(c)

print('Even List ',even , '\n' , 'Odd List ', odd)





# Q.6- Print the following patterns:
#   *
#   **
#   ***
#   ****

for d in range(1,5):
    print(d*'*')




# Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

dic = {}
e = int(input('Enter the no. of items in dictionary: '))
for f in range(e):
    name = input('Enter Name: ')
    age = int(input('Enter age: '))
    dic[name] = age
print(dic)

print("VALUES --> kEYS")
for g in dic:
    print(dic[g],' --> ',g)





# Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.


li = []
for ji in range(10):
    ki = int(input("Enter the elements of list: "))
    li.append(ki)
print('Old list: ',li)
mi = int(input("Enter the element to be removed: "))

li = [a for a in li if a != mi]

print("Removed " , mi , ' : ', li)
