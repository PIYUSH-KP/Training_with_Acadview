#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return (math.pi * self.radius**2)

    def getCircumference(self):
        return (2 * math.pi * self.radius)


r = float(input("Enter radius of circle: "))
c1 = Circle(r)
ar = c1.getArea()
print("Area of circle is: ", ar)
per = c1.getCircumference()
print("Perimeter of circle is: ", per)




# Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.
print('__'*40)
class Student():
    name = ''
    roll = 0
    def __init__(self):
        name = input("Enter name of student: ")
        self.name = name
        roll = int(input("Enter roll number of student:"))
        self.roll= roll
    def display(self):
        print("name of student is: ",self.name)
        print("Roll no. of student is: ",self.roll)
        

s1 = Student()
s1.display()





# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
print('__'*40)
class Temprature():
  def  convertFahrenhiet(self,celsius):
      return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
      return (farenhiet-32)*(5/9)


t1 = Temprature()
celsius = float((input("Enter temperature in celcius: ")))
f = t1.convertFahrenhiet(celsius)
print("The temperature in farenhiet is: ",f, " degree farenhiet")


farenhiet = float((input("Enter temperature in farenhiet: ")))
c = t1.convertCelsius(farenhiet)
print("The temperature in celsius is: ",c, " degree celsius")





#Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.

print('__'*40)
class MovieDetails():
    def __init__(self,movie_name,artist_name,release_year,ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.release_year = release_year
        self.ratings = ratings

    def display(self):
        print("Name of movie: ",self.movie_name)
        print("Name of artist of movie: ",self.artist_name)
        print("Name of movie: ",self.release_year)
        print("Name of movie: ",self.ratings)

    def update_details(self):
        self.movie_name = input("Enter new movie name: ")
        self. artist_name = input("Enter new artist's name: ")
        self.release_year = int(input("Enter release year: "))
        self.ratings = int(input("Enter ratings out of 10: "))


m_name = input("Enter movie name: ")
a_name = input("Enter artist's name: ")
r_year = int(input("Enter release year: "))
rate = int(input("Enter ratings out of 10: "))

md1 = MovieDetails(m_name,a_name,r_year,rate)
md1.display()
print("-"*20)
md1.update_details()
print('-'*20)
md1.display()









# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
# 1. Display expenditure and savings
# 2. Calculate total salary
# 3. Display salary


print('__'*40)
class Expenditure():
    def __init__(self,expenditure,savings):
        self.expenditure = expenditure
        self.savings = savings

    def disp(self):
        print("Expenditure = ", self.expenditure)
        print("Savings = ",self.savings)

    def total_sal(self):
        return (self.expenditure + self.savings)

    def disp_sal(self):
        self.tot_salary = self.total_sal()
        print("Total salary : ", self.tot_salary)

ex = int(input("enter total expenditure: "))
sav = int(input("Enter total savings: "))

e1 = Expenditure(ex,sav)
e1.disp()
e1.disp_sal()


