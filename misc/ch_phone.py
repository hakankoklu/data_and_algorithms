def format_number(number):
    num_str = str(number)
    if len(num_str) <= 3:
        return num_str
    new_str_list = list(num_str)
    new_str_list.reverse()
    new_list = []
    for ind, let in enumerate(new_str_list):
        if ind % 3 == 0 and ind != 0:
            new_list.append(',')
        new_list.append(let)
    new_list.reverse()
    final_str = ''.join(new_list)
    return final_str

print format_number(100000)
