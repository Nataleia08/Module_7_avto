def encode(data):
    res_list = []
    if type(data) == str:
        data_list = list(data)
    else:
        data_list = data
    if len(data_list) == 0:
        return []
    elif len(data_list) == 1:
        res_list.append(data_list[0])
        res_list.append(1)
        return res_list
    else:
        k = 0
        while k < (len(data_list)-1):
            if data_list[k] != data_list[k+1]:
                res_list.append(data_list[0])
                res_list.append(k+1)
                res_list.extend(encode(data_list[k+1:]))
                return res_list
            k = k + 1
        res_list.append(data_list[0])
        res_list.append(len(data_list))
        return res_list

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))