class Employee:

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

    def printMinInfo(self):
        return self.__firstname + ' ' + self.__familyname + ' ' + self.__middleinitial


class Manager(Employee):
    __team = []

    def __init__(self, firstname, familyname, middleinitial, hirigdate, department, level):
        super().__init__(firstname, familyname, middleinitial, hirigdate, department)
        self.__level = level

    def __str__(self):
        return super(Manager, self).__str__()+'\nLevel: ' + str(self.__level)

    def getlevel(self):
        #super(Manager, self).__middleinitial =

        return self.__level

    def getteam(self):
        return self.__team

    def printMinInfo(self):
        return str(self.__level) + ' ' + str(len(self.__team))


def printemployee(employe):
    print(employe)
    print()
    print(employe.printMinInfo())


employee = Employee('Oleg', 'Golenischev', 'K', '19.08.1994', 'Teachers')
print(employee)
print()
manager = Manager('Ivan', 'Netreba', 'I', '20.12.20', 'Managers', 3)
print(manager)
print(manager.getlevel())
print()
printemployee(employee)
print()
printemployee(manager)
print(employee.printMinInfo())
print()
print(manager.printMinInfo())

