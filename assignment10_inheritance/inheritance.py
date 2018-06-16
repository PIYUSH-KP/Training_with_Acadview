#  Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class animal:
    """
    A class which contains properties of animals

    attributes:
    legs : int
    ears : int
    cat_family: bool
    age : int
    """
    def animal_attribute(self,legs,ears,cat_family,age):
        self.legs = legs
        self.ears = ears
        self.cat_family = cat_family
        self.age = age
        print("legs: ",legs)
        print("ears: ", ears, "\nFrom cat_family: ",cat_family,"\nage: ",age)

class tiger(animal):
    def __init__(self):
        print("A tiger is born")

new_tiger = tiger()
new_tiger.animal_attribute(4,2,True,1)

print('__'*40)

# Q.2- What will be the output of following code.

print("Output:")
print("A B\nA B")

print('__'*40)

# Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop():
    def add(self):
        self.name = input(("enter name:"))
        self.age = int(input("enter the age:"))
        self.work_expr = int(input("enter the work experience in years:"))
        self.designation = input("enter the designation:")

    def display(self):
        print("name of this cop: %s\nage of this cop: %d\nwork_experience: %d\ndesignation: %s" % (self.name, self.age, self.work_expr, self.designation))

    def update(self):
        self.name = input(("enter new name:"))
        self.age = int(input("enter the new age:"))
        self.work_expr = int(input("enter the new work experience in years:"))
        self.designation = input("enter the new designation:")


class Mission(Cop):
    mission_name = ''
    mission_duration = ''
    mission_place = ''

    def add_mission_details(self):
        mission_name = input("Enter the mission name:")
        mission_duration = int(input("Enter mission duration in months: "))
        mission_place = input("Enter country for mission: ")


m = Mission()
print("Add data")
m.add()
print("\nshowing added data......")
m.display()
print("\ntime to update data.....")
m.update()
print("\nupdated data below")
m.display()


# Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
print('__'*40)
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)


class rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class square(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


r = rectangle(2, 3)
print("area of rectangle:", r.area())

s = square(5, 5)
print("area of square:", s.area())
