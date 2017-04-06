#!ussr/bin/python3

import sys
import math

str = sys.argv[1]
len = math.sqrt(len(str))
len_line = str.count('1') / 2

for i in range(len):
    for j in range(len_line):
        arr[i][j] = 0

k = 0;

for i in range(len):
    for j in range(len):
        if (str[i + j + 1] == 1)
            arr[i][k] = 1
            arr[j][i] = 1
            k++

for i in range(len)
    for (j = 0; j < len_line; j++)
        print(arr[i][j], end=' ')
