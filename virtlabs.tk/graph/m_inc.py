#!ussr/bin/python3

import sys
import math

str = sys.argv[1]
len = int(math.sqrt(len(str)))
len_line = int(str.count('1') / 2)

arr = []

for i in range(len):
    arr.append([])
    for j in range(len_line):
        arr[i].append(0)

k = 0

for i in range(len):
    for j in range(i, len):
        if (str[i * len + j] == '1'):
            arr[i][k] = 1
            arr[j][k] = 1
            k += 1

for i in range(len):
    for j in range(len_line):
        print(arr[i][j], end=' ')
    print('<br>')
