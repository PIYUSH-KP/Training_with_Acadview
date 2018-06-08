age1 = int(input("Enter age of person1: "))
age2 = int(input("Enter age of person2: "))
age3 = int(input("Enter age of person3: "))

age_list = [age1, age2, age3]

print("the oldest among these is person ",(age_list.index(max(age_list)) + 1), " with age ", max(age_list))

print("the youngest among these is person ",(age_list.index(min(age_list)) + 1), " with age ", min(age_list))



#method 2
if (age1 > age2) and (age1 > age3):
    oldest = age1
elif (age2 > age1) and (age2 > age3):
    oldest = age2
else:
    oldest = age3
print("\n\nIF_ELSE METHOD")
print("\nThe oldest among 3 is person with age ", oldest)


if (age1 < age2) and (age1 < age3):
    youngest = age1
elif (age2 < age1) and (age2 < age3):
    youngest = age2
else:
    youngest = age3

print("The youngest among 3 is person with age ", youngest)
