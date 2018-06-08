n =int(input("enter the number of items: "))
cost = n*100
if cost>1000:
    print("Total cost will be:",cost-0.1*cost)
else:
    print("Total cost will be:",cost)
