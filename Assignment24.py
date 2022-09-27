
# 1. Write a python program to create a user class with 3 properties : name, age, email.
class User:
    def __init__(self):
        self.name = "Mohanish"
        self.age = 28
        self.email = "mohanish.devrukhkar@gmail.com"

    def Greetings(self):
        print("Hello {}, Have A good day!!!".format(self.name))

    def condition(self,obj):
        return obj.ram



u = User()
print(u.name)
print(u.age)
print(u.email)


# 2. Write a python program to create a user class with a method to greet the user.
u.Greetings()

# 3. Write a python program to create 2 objects of the user class and assign different values.

u1 = User()
u2 = User()
u1.name = "Rhuta"
u1.age = 29
u1.email = "pooja.patil369@gmail.com"

u2.name= "Om"
u2.age = 16
u2.email = "omekbote@gmail.com"

u1.Greetings()
u2.Greetings()

# 5. Write a python program to delete the age property of the user.
#del u1.age
#print(u1.age)

# 6. Write a python program to create 3 user objects and find the youngest of all.
print(min(u.age, u1.age, u2.age))


# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class Laptop:
    def __init__(self):
        self.brand = "Lenovo"
        self.ram = 16
        self.cpu = "i7 10 gen"
        self.hdd = "1 Tb"

    def showConfig(self):
        print("Brand of laptop is {}, it have {} gb of Ram, with {} CPU and {} of hdd.".format(self.brand,self.ram,self.cpu,self.hdd))


l = Laptop()
l.showConfig()


# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.
l2 = Laptop()
l2.ram = 8

l3 = Laptop()
l3.ram=32

lis = [{"Brand":l.brand,"Ram":l.ram,"cpu": l.cpu,"Hdd": l.hdd}, {"Brand" : l2.brand, "Ram": l2.ram, "cpu": l2.cpu, "Hdd": l2.hdd}, {"Brand": l3.brand, "Ram": l3.ram, "cpu": l3.cpu, "Hdd": l3.hdd}]

def condition(obj):
    return obj["Ram"]


lap_list = [l, l2, l3]
lis.sort(key=condition)
print(lis)

#9. Write a python program to create a School class and 3 instance variables and 1 class variable.

class School:
    school_name = "Python"

    def __init__(self):
        self.student_name = "Mohanish"
        self.student_age = 27
        self.student_marks = 98


# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. Also define instance methods to input fields and display field values

class Employee:

    def __init__(self):
        self._name = "Mohanish"
        self._empid = 101
        self._salary = 300000

    def setName(self,name):
        self._name = name

    def setEmployee_id(self,empid):
        self._empid = empid

    def setSalaray(self,salary):
        self._salary = salary

    def getName(self):
        return self._name

    def getEmployeeId(self):
        return self._empid

    def getSalary(self):
        return self._salary

    def EmployeeInformation(self):
        print("Name: {} \nEmployeeId = {} \nSalary ={} \n".format(self.getName(),self.getEmployeeId(),self.getSalary()))


emp = Employee()
emp.EmployeeInformation()

emp2 = Employee()
emp2.setName("Rhuta")
emp2.setEmployee_id(102)
emp2.setSalaray(2002035)

emp2.EmployeeInformation()







