class idea1():

    def __init__(self):
        self.hashmap = {}


    def Reorder(self,list1,list2):
        string = ""
        index = 0
        for i in list1:
            self.hashmap[i] = list2[index]
            index = index + 1

        tuple = sorted(self.hashmap.items())

        for i in tuple:
            string = string + i[1]

        print(string)

