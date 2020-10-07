class idea1():
    def __init__(self,list):
        list.sort()
        self.list = list
        self.flag = True

    def JudgeArithmetic(self):
        index = 0
        value = self.list[1]-self.list[0]
        length = len(self.list) - 1


        for i in range(length):
            if self.list[index+1] - self.list[index] != value:
                self.flag = False
            index = index + 1

