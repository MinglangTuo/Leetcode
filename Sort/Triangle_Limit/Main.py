from Idea1 import idea1

class main():
    list = [1,6,2,3]
    new_idea1 = idea1(list)
    trangle = new_idea1.ChosenTrangle()
    #print(trangle)
    if len(trangle) == 3:
        length = trangle[0]+trangle[1]+trangle[2]
        print(length)
    else:
        print(0)