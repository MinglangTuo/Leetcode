class idea1():

    def __init__(self,list):
        self.flag = False
        self.new_list = []
        self.list = list

    def ChosenTrangle(self):
        '''选择最长的三条边'''
        self.list.sort(reverse = True)

        try:
            self.new_list.append(self.list[0])
            self.new_list.append(self.list[1])
            self.new_list.append(self.list[2])
            self.WhetherTrangle(self.new_list)
        except IndexError:

            #print("zero!")
            self.flag = True




        if self.flag == False:
            self.list.pop(0)
            self.new_list.clear()
            self.ChosenTrangle()

        return self.new_list

    def WhetherTrangle(self,list):
        '''判断是否为三角形'''
        edge1 = list[0]
        edge2 = list[1]
        edge3 = list[2]

        if(edge1+edge2>edge3 and edge2+edge3>edge1 and edge1+edge3>edge2):
            self.flag = True








