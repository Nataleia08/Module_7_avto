def data_preparation(list_data):
    new_list = list_data.copy()
    for i in new_list:
        if type(i) == list:
            if len(i) > 3: 
                new_i = i.copy()
                new_i.sort(reverse=True)
                new_i.pop(0)
                new_i.pop(-1)
                list_data.extend(new_i)
                list_data.remove(i)
            else: 
                list_data.extend(i)
                list_data.remove(i)
    list_data.sort(reverse=True)
    return list_data

data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])