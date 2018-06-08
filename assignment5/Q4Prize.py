
prize = ['No Prize', 'Wooden Dog', 'Book', 'Chocolates']
points = int(input("Enetr points: "))
if(points>=1 and points<=200):
    if( points in range(1,51)):
        print("Congratulations! You have won a %s !" %(prize[0]))
    elif(points in range(51,151)):
        print("Congratulations! You have won a %s !" %(prize[1]))
    elif(points  in range(151,181)):
        print("Congratulations! You have won a %s !" %(prize[2]))
    elif (points in range(181,201)):
        print("Congratulations! You have won a %s !" %(prize[3]))
    else:
          print("Sorry! No prize this time")
else:
         print("Wrong Input")
