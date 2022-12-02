def token_parser(s):
    if len(s) == 0:
        return []
    s_list = s.split(" ")
    oper_list = ["*", "+", "-", "/", ")", "("]
    for opr in oper_list:
        for i in s_list:
            if (i.find(opr)!= -1) and (len(i) >= 2):
                i_new = i.split(opr)
                k = s_list.index(i)
                s_list.remove(i)
                n = 0
                for k_i in i_new:
                    if k_i != "":
                        s_list.insert(k + n, k_i)
                        if i_new[-1] != k_i:
                            s_list.insert(k+1, opr)
                            n = n + 2
                    else:
                        if i_new[-1] != k_i:
                            s_list.insert(k, opr)
                        n = n + 1
    return s_list

print(token_parser('(2+ 3) *4 - 5 * 3'))