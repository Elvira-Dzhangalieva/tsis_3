def unique(x):
    list1 = []
    for i in x:
        if i not in list1:
            list1.append(i)
    return list1
    
list = input().split()
print(unique(list))
