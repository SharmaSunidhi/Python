def positive(list):
    new_list=[]
    for num in list:
        if(num>0):
            new_list.append(num)
    return new_list

list=[12,-7,5,64,-14]
print(positive(list))
