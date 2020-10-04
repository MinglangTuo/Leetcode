
class idea1():

    def sortArray(self,list):
        new_list = []
        index1 = 0
        index2 = 1

        for i in list:
            new_list.append(i)

        for i in list:
            if (i % 2 == 0):
                new_list[index1] = i
                index1 = index1+2
            else:
                new_list[index2] = i
                index2 = index2+2
        print(new_list)


