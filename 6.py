def solve_riddle(riddle, word_length, start_letter, reverse=False):
    f_ind_start = riddle.find(start_letter)
    print(f_ind_start)
    f_ind_end = f_ind_start + word_length
    print(f_ind_end)
    if (f_ind_start == -1):
        return ""
    else:
        if reverse:
            result = riddle[f_ind_start-word_length:f_ind_start:-1]
        else:
            result = riddle[f_ind_start:f_ind_end]
    return result

print (solve_riddle('mi1powperet', 3, 'r', True))