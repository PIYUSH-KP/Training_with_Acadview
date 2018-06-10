# 1.create list
a = []
for i in range(0,5):    # for adding 5 elements
        x = input()
        a.append(x)

# 2.add into list

a = a + ['google','apple','microsoft','tesla']
print(a)
a = a + ['amazon','oracle','apple','apple','apple','apple','google','amazon','microsoft','microsoft']
print(a)
a.append('tesla')
print(a)


for element in a:
	print(element + " occurs " + str(a.count(element)) + " times ")
