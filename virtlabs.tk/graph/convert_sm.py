#!ussr/bin/python3

import sys

length = int(sys.argv[1])
if (len(sys.argv) >= 3):
    string = sys.argv[2]
else:
    print('<3')

arr = []

for i in range(length):
    arr.append([])
    for j in range(length):
        arr[i].append(0)

for i in range(0, len(string), 3):
    arr[i+1][i+2] = 1
    arr[i+2][i+1] = 1

for i in range(length):
    for j in range(length):
        print(arr[i][j], end=' ')
    print('<br>')
