def _encircular(command_str):
    gcount = command_str.count('G')
    rcount = command_str.count('R')
    lcount = command_str.count('L')
    if gcount == 0:
        return 'Yes'
    rl_diff = abs(rcount - lcount)
    if rl_diff % 4 == 0:
        return 'No'
    return 'Yes'