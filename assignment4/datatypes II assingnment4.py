# Q1. count length of tuple

a = (1,'piyush',3.5,[4,5,6],True,'acadview')
print("Length of tuple is: ",len(a))


# Q2. find maximum and minimum in tuple
tuple2 = (9,76,34,56,12,1,45)
print("maximum element in tuple is : ",max(tuple2))
print("minimum element in tuple is : ",min(tuple2))

tuple3 = ('piyush', 'ayush', 'new' , 'buck' , 'zebra')
print("maximum element in tuple is : ",max(tuple3))
print("minimum element in tuple is : ",min(tuple3))


# Q3. product of all elements in tuple

tuple4 = (1,2,3,4,5,6)
product = 1
for x in tuple4:
    product *= x
print("Product of all elements in tuple is: ",product)


# Q4. SETS

#create 2 sets

set1 = set()
set2 = set()
for i in range(5):
    x = input('Enter elements for set 1: ')
    set1.add(x)

for j in range(7):
    x = input('\nEnter elements for set 2: ')
    set2.add(x)

print('Set1: ',set1)
print('Set2: ',set2)

#difference between two sets

diff = set2 - set1   #method1
print(diff)

print(set2.difference(set1)) #method2

#compare sets
a = set({0,1,2,3})
b = set({0,1,2,3})
print(a ^ b)    # gives empty set means a and b are same
print(a == b)   # gives True means sets are same

c = set({3,4,5,6,7,})
print(a == c)      #gives false i.e stes are not same
print(a ^ c)       #gives {0,1,2,4,5,6,7}

#intersection of two sets
intersec = set1 & set2
print(intersec)

print(set1.intersection(set2))


# Q5. dictionary
dict1 = {}
for i in range(10):
    Name = input("Enter the student name :")
    Marks = int(input("Enter the marks:"))
    dict1[Name] = Marks
    

print(dict1)

#Q6. sort according to marks
#method 1
for key, value in sorted(dict1.items(), key=lambda item: (item[1], item[0])):
    print ("%s: %d" % (key, value))

#method 2
new_tup = tuple([(v,k) for k,v in dict1.items()])
#print("dictionary sorted according to marks",sorted(new_tup))
p = sorted(new_tup)
q = dict(p)
print("dictionary sorted according to marks..")
print(q)

# Q7. MISSISSIPPI
dict2 = {}
for i in 'MISSISSIPPI':
    key = dict2.keys()
    if i in key:
        dict2[i] += 1
    else:
        dict2[i] = 1
print("\n\nCount of each letter in MISSISSIPPI  ",dict2)





