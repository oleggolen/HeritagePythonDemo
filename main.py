class Employee:
    __employeeType = 'Employee'

    def __init__(self, firstname, familyname, middleinitial, hirigdate, department):
        self.__firstname = firstname
        self.__familyname = familyname
        self.__middleinitial = middleinitial
        self.__hiringdate = hirigdate
        self.__department = department

    def __str__(self):
        return 'Firstname: ' + self.__firstname + '\nLastname:' + self.__familyname + "\nMiddlename:" + self.__middleinitial + '\nHiring date:' + self.__hiringdate + '\nDepartment:' + self.__department

    def getfirstname(self):
        return self.__firstname

    def getlsatname(self):
        return self.__familyname

    def getmiddleinitial(self):
        return self.__middleinitial

    def gethiringdate(self):
        return self.__hiringdate

    def getdepartment(self):
        return self.__department

    def getemployeetype(self):
        return self.__employeeType


class Manager:
    __team = []
    __employeeType = "Manager"

    def __init__(self, firstname, familyname, middleinitial, hirigdate, department, level):
        self.__firstname = firstname
        self.__familyname = familyname
        self.__middleinitial = middleinitial
        self.__hiringdate = hirigdate
        self.__department = department
        self.__level = level

    def __str__(self):
        return 'Firstname: ' + self.__firstname + '\nLastname:' + self.__familyname + "\nMiddlename:" + self.__middleinitial + '\nHiring date:' + self.__hiringdate + '\nDepartment:' + self.__department + "\nLevel: " + str(self.__level)

    def getfirstname(self):
        return self.__firstname

    def getlsatname(self):
        return self.__familyname

    def getmiddleinitial(self):
        return self.__middleinitial

    def gethiringdate(self):
        return self.__hiringdate

    def getdepartment(self):
        return self.__department

    def getlevel(self):
        return self.__level

    def getteam(self):
        return self.__team

    def getemployeetype(self):
        return self.__employeeType


def printemployee(employe):
    print('Firstname', employe.getfirstname())
    print('Lastname:', employe.getlsatname())
    print('Middlename', employe.getmiddleinitial())
    print('Hiring date', employe.gethiringdate())
    print('Department:', employe.getdepartment())
    if employe.getemployeetype() == 'Manager':
        print('Level', employe.getlevel())
        for member in employe.getteam():
            printemployee(member)
            print()


employee = Employee('Oleg', 'Golenischev', 'K', '19.08.1994', 'Teachers')
print(employee)
print()
manager = Manager('Ivan', 'Netreba', 'I', '20.12.20', 'Managers', 3)
print(manager)
print()
printemployee(employee)
print()
printemployee(manager)
