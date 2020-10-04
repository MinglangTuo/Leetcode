class idea1():

    def compareLists(self,list1,list2):
        #add all the same elements in new list
        list3 = []
        for i in list1:
            for j in list2:
                if i == j:
                    list3.append(i)
        print(list3)
        return list3

    def removeDuplication(self,list1):
        #remove the duplicated element
        list1 = list(set(list1))
        print(list1)
        return list1

    def plus1(self,list1,list2,list3):
        #输出数组中出现元素最小值
        duplication_number_1 = 0
        duplication_number_2 = 0

        for index in range(len(list3)):
            for list1_element in list1:
                if list3[index] == list1_element:
                    duplication_number_1 = duplication_number_1+1
            for list2_element in list2:
                if list3[index] == list2_element:
                    duplication_number_2 = duplication_number_2+1

            if duplication_number_1>=duplication_number_2 and duplication_number_1 != 1:
                for i in range(duplication_number_2-1):
                    list3.append(list3[index])
            elif duplication_number_1<duplication_number_2 and duplication_number_1 != 1:
                for i in range(duplication_number_1-1):
                    list3.append(list3[index])

            duplication_number_1 = 0
            duplication_number_2 = 0
        print(list3)
