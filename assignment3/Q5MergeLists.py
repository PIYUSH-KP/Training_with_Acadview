a = [5,7,9,11,13,15,19,21] #string 1 sorted in ascending order
b = [1,2,4,6,8,10,14,18,20] #string 2 sorted in ascending order
c = a + b
print("List after merging a and b : " +str(c))
c.sort()   # sort merged list
print("Sorted list after merging a and b : " + str(c))
