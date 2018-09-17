def read_program():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines

def remove_code(lines):
    in_multiline = False
    result = []
    for line in lines:
        # end of multiline
        if '*/' in line:
            result.append(line)
            in_multiline = False
        # start of multiline
        elif '/*' in line:
            result.append(line)
            in_multiline = True
        # during multiline
        elif in_multiline:
            result.append(line)
        # single line
        elif '//' in line:
            start = line.find('//')
            result.append(line[start:])
    return result
res = remove_code(read_program())
print('\n'.join(res))