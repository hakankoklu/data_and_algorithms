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
            print i,k,vol
            max_volume = max(vol, max_volume)
    return max_volume

print most_water_container([1,2,4,3])
