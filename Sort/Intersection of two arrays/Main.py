from Idea1 import idea1

class main():
    #initalize
    new_idea1 = idea1()
    list1 = [1,2,2,1,3]
    list2 = [2,2,1,2,1,1]

    #Operations
    list3 = new_idea1.compareLists(list1,list2)
    list3 = new_idea1.removeDuplication(list3)
    list3 = new_idea1.plus1(list1,list2,list3)