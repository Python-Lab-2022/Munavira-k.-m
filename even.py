list = [2, 4, 6, 8, 10]
for i in list:
    divid = i %2
    if divid == 0 :
        list.remove(i)
print(list)
