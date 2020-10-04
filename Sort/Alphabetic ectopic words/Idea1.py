class idea1():

    def analyzeText(self,hashMap,string):
        #transfer the string to HashMap
        length = len(string)
        for i in range(length):
            if string[i] not in hashMap:
                hashMap[string[i]] = 1
            else:
                hashMap[string[i]] = hashMap[string[i]]+1

    def printHashMap(self,hashMap):
        #print the HashMap
        print(hashMap)


    def compareHashMaps(self,hashmap1,hashmap2):
        #compare different hashmaps

        # compare the length of digits
        length1 = len(hashmap1)
        length2 = len(hashmap2)
        length = 0
        if length1!=length2:
            print("Cannot be the Alphabetic ectopic words!")
        # compare the value of the digits (condition1)
        else:
            for key1 in hashmap1:
                for key2 in hashmap2:
                    if key1 == key2:
                        if hashmap1[key1]==hashmap2[key2]:
                            print(key1+"="+key2+"\n")
                            length = length+1
                        else:
                            #(condition2)
                            print("Cannot be the Alphabetic ectopic words!")
                    else:
                        pass

        if length != length1:
            #(condition3)
            print("Cannot be the Alphabetic ectopic words!")





