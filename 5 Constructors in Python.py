#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = "[no eye color]"
        self.age = -1

#Creates a person with names David and Joyner
myPerson = Person("David", "Joyner")
print(myPerson.firstname)
print(myPerson.lastname)




#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = "[no eye color]"
        self.age = -1

#Creates a new person
myPerson = Person()
print(myPerson.firstname)
print(myPerson.lastname)



#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self, firstname="[no first name]",
                 lastname="[no last name"):
        self.firstname = firstname
        self.lastname = lastname
        self.eyecolor = "[no eye color]"
        self.age = -1

myPerson1 = Person()
print(myPerson1.firstname)
myPerson2 = Person(firstname = "David")
print(myPerson2.firstname)
myPerson3 = Person("Vrushali")
print(myPerson3.firstname)



#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self):
        #Person's default values
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"
        self.eyecolor = "[no eye color]"
        self.age = -1


