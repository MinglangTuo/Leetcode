class arraySort():
    def __init__(self,list1,list2):
        self.new_list = []
        self.list1 = list1
        self.list2 = list2
        self.index = 0


    def handleArray1(self,length):
        '''创建指针，读取list2的内容'''
        for i in range(length):
            self.handleArray2()
            #print(self.list1)
        self.list1.sort()
        #print(self.list1)
        self.new_list.extend(self.list1)
        print(self.new_list)

    def handleArray2(self):
        '''移除list1里面的元素'''
        element = self.list2[self.index]


        while element in self.list1:
            self.list1.remove(element)
            self.new_list.append(element)

        self.index = self.index + 1


