#1. Write a python script to create a Profile class with 3 attributes (name, email, age).
class Profile:
    name = ""
    __email = ''
    __age = 0

    platform = "Python"

# 2. Write a python script to update the above Profile class with encapsulation.

    def setName(self, name):
        self.name = name

    def setEmail(self,email):
        self.__email = email

    def seAge(self,age):
        self.__age = age

    def getName(self):
        return self.name

    def getEmail(self):
        return self.__email

    def getAge(self):
        return self.__age

#4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

    @classmethod
    def accessingPlatform(cls):
        return cls.platform


#5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
#6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.

class Calculator2:
    @staticmethod
    def multiplication(number,number2):
        return number*number2

    @staticmethod
    def division(number,number2):
        if number == 0 or number2 == 0:
            return "Can not Divide by 0"
        else:
            return number//number2


class Calculator(Calculator2):
    @staticmethod
    def Addition(number,number2):
        return number+number2

    @staticmethod
    def Subtraction(number,number2):
        return number-number2


# 7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).
class Phone:
    @staticmethod
    def calling():
        print("Calling...")

    @staticmethod
    def Sms():
        print("Messaging...")


# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
class SmartPhone(Calculator2, Phone):
    def dataFetch(self,obj):
        obj.fetch()


#9. Write a python script to create an application like Truecaller where names and numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of anumber and 2nd to add a new entry).
class TrueCaller:
    number_data = {}
    @classmethod
    def newData(cls,number,name):
        cls.number_data[number]=name
    @classmethod
    def fetch(cls, number):
        print(cls.number_data[number])


    @classmethod
    def fetchAllData(cls):
        for k, v in cls.number_data.items():
            print("Number: {}, Name: {} ".format(k,v))


sp = SmartPhone()
tc = TrueCaller()

sp.dataFetch(tc)





