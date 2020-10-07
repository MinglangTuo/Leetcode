class gotSalary():
    def __init__(self,list):
        list.sort()
        self.list = list
        self.salary = 0

    def getAverageSalary(self):
        length = len(self.list)
        self.list = self.list[1:length-1]
        for i in self.list:
            self.salary = self.salary + i
        self.salary = self.salary/(length-2)
        return self.salary