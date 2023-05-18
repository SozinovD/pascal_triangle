#!/usr/bin/env python3

depth = int(input('Input depth of Pascal triangle: '))
res = [[1]]
for i in range (1, depth):
    res.append([])
    res[i].append(1)
    for j in range(1, i):
        res[i].append(res[i - 1][j - 1] + res[i - 1][j])
    res[i].append(1)

num_str_len_needed = len(str(max(res[-1]))) + 1
longest_str = ''
for i, n in enumerate(res[-1]):
    longest_str += str(res[-1][i]).rjust(num_str_len_needed, ' ')
tr_center = int(round(len(longest_str) / 2, 0)) - num_str_len_needed if num_str_len_needed > 4 else int(round(len(longest_str) / 2, 0))

triangle = []
for n, line in enumerate(res):
    line_str = ''
    max_num_in_line = max(line)

    for i, num in enumerate(line):
        if i == 0:
            line_str += str(num)
            continue
        if len(str(num)) < num_str_len_needed:
            num_str = str(num)
            side = 'l'
            while len(num_str) < num_str_len_needed:
                num_str = ' ' + num_str
        line_str += num_str

    max_num_pos = line_str.find(str(max_num_in_line)) if n % 2 != 0 else line_str.find(str(max_num_in_line)) - int(num_str_len_needed / 2)
    while max_num_pos < tr_center:
        
        line_str = ' ' + line_str
        max_num_pos = line_str.find(str(max_num_in_line)) if n % 2 != 0 else line_str.find(str(max_num_in_line)) - int(num_str_len_needed / 2)

    triangle.append(line_str)

for l in triangle:
    print(l)
