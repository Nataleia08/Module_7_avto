def flatten(data):
    s = []
    if len(data) == 0:
        return []
    elif type(data[0]) == list:
        s.extend(flatten(data[0]))
        if len(data) == 1:
            return s
        else: 
            if len(data) == 1:
                return s
            elif len(data) == 2:
                if type(data[1]) == list:
                    s.extend(flatten(data[1]))
                    return s
                else:
                    s.append(data[1])
            else:
                if type(data[1:]) == list:
                    s.extend(flatten(data[1:]))
                else:
                    s.append(data[1:])
    elif type(data[0]) != list:
        s.append(data[0])
        if len(data) == 1:
            return s
        elif len(data) == 2:
            if type(data[1]) == list:
                s.extend(flatten(data[1]))
                return s
            else:
                s.append(data[1])
        else:
            if type(data[1:]) == list:
                s.extend(flatten(data[1:]))
            else:
                s.append(data[1:])
    return s

print(flatten([1, 2, [3, 4, [5, 6]], 7]))