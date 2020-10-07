class binaryArraySort():
    def __init__(self):
        self.list = []
        self.new_list = []

    def Transform(self,list):
        '''对数组中的元素进行转换'''
        for i in list:
            BinaryNumber = bin(i)
            #转换为2进制
            self.list.append(BinaryNumber)
        self.list.sort()

        for j in self.list:
            j = int(j,2)
            #转换回来10进制
            self.new_list.append(j)
        print(self.new_list)