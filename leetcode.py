# top k frequent elements
from collections import Counter

def topk_frequent(numbers, k):
    c = Counter(numbers)
    return [k for k,l in c.most_common(k)]

def most_water_container(lines):
    max_volume = 0
    for i, j in enumerate(lines):
        for k in range(i+1, len(lines)):
            vol = min(j,lines[k]) * (k-i)
            max_volume = max(vol, max_volume)
    return max_volume

def split_sentence(sentence):
    word = []
    words = []
    for i, j in enumerate(sentence):
        if j == ' ' and len(word) > 0:
            words.append(''.join(word))
            word = []
        elif j != ' ':
            word.append(j)
    if len(word) > 0:
        words.append(''.join(word))
    return words

# print split_sentence('dgdsfg   dsfg sdfg   dsfgdfs  dfsg dsf')

def first_missing_number(num_list):
    last_num = num_list[0]
    for i in num_list:
        if i == last_num:
            continue
        elif i == last_num + 1:
            last_num = last_num + 1
            continue
        else:
            return last_num + 1
    return 'none missing'

#print first_missing_number([0,0,0,1,1,2,3,4,4,5,6,7,7,8,9,9,10,10,12,12,13,14])

def look_and_say(text):
    current_num = text[0]
    current_count = 1
    result = ''
    for let in text[1:]:
        if let != current_num:
            result += str(current_count)
            result += current_num
            current_num = let
            current_count = 1
        else:
            current_count += 1
    result += str(current_count)
    result += current_num
    return result

#print look_and_say('11122234455551')

def zigzag_conversion(text, rows):
    line_keys = range(rows)
    lines2 = range(rows-2,0,-1)
    line_keys.extend(lines2)
    count = 0
    lines = {}
    for i in line_keys:
        lines[i] = []
    for i,j in enumerate(text):
        row_no = i % len(line_keys)
        lines[line_keys[row_no]].append(j)
    letters = []
    for i in range(rows):
        for l in lines[i]:
            letters.append(l)
    result = ''.join(letters)
    return result

# print zigzag_conversion('PAYPALISHIRING', 3)

def diagonal_print(word_list):
    for ind, let in enumerate(word_list[0]):
        word_to_print = ''
        for row, word in enumerate(word_list):
            if row + ind < len(word):
                word_to_print += word[row + ind]
        print word_to_print
    for row, word in enumerate(word_list[1:]):
        word_to_print = ''
        for ind, let in enumerate(word_list[-1][:-1]):
            if row + ind < len(word):
                word_to_print += word[row + ind]
        print word_to_print

words = ['abcde', 'fgh', 'ijk']
diagonal_print(words)
