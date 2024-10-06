list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = [0,2,4,6,8,10,12,14,16,18,20]
list3 = list1 + list2
list4 = []
for i in range(0, len(list3) + 1):
    if list4 == 0:
        list4.append(list3[0])
    elif list3[i] <= list3[len(list3)-1]:
        list4.append(list3[i])
print(list4)