import copy

def interleave(list1, list2):
    for i in range(0, len(list1)):
        slice1 = list1[:i]
        slice2 = list1[i:]
        for j in range(0, len(list2)):
            slice3 = list2[:j]
            slice4 = list2[j:]
            #print(slice1)
            #print(slice2)
            #print(slice3)
            #print(slice4)

            # slice 1, 3, 4, 2

            newList1 = list(copy.deepcopy(slice1))
            newList2 = list(copy.deepcopy(slice2))
            newList3 = list(copy.deepcopy(slice3))
            newList4 = list(copy.deepcopy(slice4))
            newList1.extend(newList3)
            newList1.extend(newList4)
            newList1.extend(newList2)
            print(newList1)

            newList1 = list(copy.deepcopy(slice1))
            newList2 = list(copy.deepcopy(slice2))
            newList3 = list(copy.deepcopy(slice3))
            newList4 = list(copy.deepcopy(slice4))
            newList1.extend(newList2)
            newList1.extend(newList3)
            newList1.extend(newList4)
            print(newList1)

            newList1 = list(copy.deepcopy(slice1))
            newList2 = list(copy.deepcopy(slice3))
            newList3 = list(copy.deepcopy(slice2))
            newList4 = list(copy.deepcopy(slice4))
            newList1.extend(newList2)
            newList1.extend(newList3)
            newList1.extend(newList4)
            print(newList1)


#def insertList(list1, list2, index):
    #for i in range(0, len(list2)):
        #print("List2: ", list2)
        #list1.insert(list2[i], index)
        #index += 1
        #print("List1: ", list1)
        #return list1

print(interleave([1, 2], [3, 4]))