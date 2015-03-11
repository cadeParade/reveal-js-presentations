def merge_sort(lst):
    # here we are breaking everything down into a list of one
    if len(lst) < 2:      #if length of lst is 1, return lst
        return lst
    mid = int(len(lst)/2)     #index at half the list
    lst1 = merge_sort(lst[:mid])      #divide list in half
    lst2 = merge_sort(lst[mid:])      #assign other half

    # here we are comparing the first items of each pair of lists and interleaving a result list
    result_list = []
    while len(lst1) > 0 and len(lst2) > 0:  #if items left in both lists
        #compare first items of each list
        if lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))  #append and rm first item of lst1
        else:
            result_list.append(lst2.pop(0))  #append and rm first item of lst2

    result_list.extend(lst1)
    result_list.extend(lst2)

    return result_list


print merge_sort([54, 2, 3, 9, 23, 8, 0, 4, 6])
