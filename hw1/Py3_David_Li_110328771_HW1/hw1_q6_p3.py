import copy


def interLeave(list1, list2):
    interleave([], list1, list2)

def interleave(list0, list1, list2):
    # base cases
    if len(list1) == 0 and len(list2) == 0:
        print(list0)

    # recursive calls - use backtracking to finish the problem
    if len(list1) > 0:
        list0.append(list1.pop(0))
        interleave(list0, list1, list2)
        list1.insert(0, list0.pop())

    if len(list2) > 0:
        list0.append(list2.pop(0))
        interleave(list0, list1, list2)
        list2.insert(0, list0.pop())

interLeave([1, 2], [3, 4])
