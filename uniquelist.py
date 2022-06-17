list1 = [1,2,3,4,5,6,78,9,9,2,3,]
list2=[]
def unique(list1):
    for i in list1:
        if i not in list2:


            list2.append(i)
    return list2


unique(list1)
print(unique(list1))
