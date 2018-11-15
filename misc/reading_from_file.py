"""python3 reading_from_file.py < sample_file > sample_response
will read sample_file line by line and write the std out into sample response
"""


if __name__ == '__main__':
    count = 0
    while True:
        try:
            line = input()
            if 'a' in line:
                print(line)
                count += 1
        except EOFError:
            break
    print(count)
