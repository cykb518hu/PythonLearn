class Employee:

    empCount=0
    __privateCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
        Employee.__privateCount+=1
    
    def displayCount(self):
         print ("Total Employee:", Employee.empCount)

    def displayEmployee(self):
        print ("name:",self.name,  ",Salary ",self.salary)


    

    
