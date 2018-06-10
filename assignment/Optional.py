a = [1,2,3,4,5,6,7,8,9,10,11,13,15,17,18,20,23,34,65,78,97]
even_count = 0
odd_count = 0
for i in a:
    if(i%2==0):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("odd count = " + str(odd_count))
print("even count = " +str(even_count))