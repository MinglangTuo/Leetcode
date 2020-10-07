class distanceSequenceMatrix():

    def __init__(self):
        self.list = []
        self.distances = []

    def points(self,R,C):
        '''构建出数据结构存储相关的矩阵'''
        for raw in range(R):
            for column in range(C):
                new_list = (raw,column)
                self.list.append(new_list)
        print(self.list)

    def calculateDistance(self,r,c):
        '''计算出到特定点到各点的距离'''

        for point in self.list:
            distance = abs(r-point[0]) + abs(c-point[1])
            print(distance)
            self.distances.append(distance)
        self.distances.sort()

