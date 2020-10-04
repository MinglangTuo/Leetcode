from Idea1 import idea1

class main():

    #Initialize
    string1 = "raat"
    string2 = "car"
    hashmap1 = {}
    hashmap2 = {}
    new_idea1 = idea1()


    #Text Analyze
    new_idea1.analyzeText(hashmap1,string1)
    new_idea1.analyzeText(hashmap2,string2)
    new_idea1.printHashMap(hashmap1)
    new_idea1.printHashMap(hashmap2)

    #compare HashMaps
    new_idea1.compareHashMaps(hashmap1,hashmap2)