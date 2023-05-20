#!/usr/bin/env python3

depth = int(input('Input depth of Pascal triangle: '))
# calculate triangle itself
source_tr = [[1]]
for i in range (1, depth):
    source_tr.append([])
    source_tr[i].append(1)
    for j in range(1, i):
        source_tr[i].append(source_tr[i - 1][j - 1] + source_tr[i - 1][j])
    source_tr[i].append(1)

# calculate length of each 'brick' of triangle
num_str_len_needed = len(str(max(source_tr[-1]))) + 1
# make it even number
if num_str_len_needed % 2 != 0:
    num_str_len_needed += 1

# calculate length of longest line and center of triangle
longest_str = ''
for i, n in enumerate(source_tr[-1]):
    longest_str += str(source_tr[-1][i]).ljust(num_str_len_needed, ' ')
tr_center = int(round(len(longest_str) / 2, 0))

# define var for formatted triangle
triangle = []
# for every line in triangle
for n, line in enumerate(source_tr):
    line_str = ''
    max_num_in_line = max(line)

    # form line 
    for i in line:
        line_str += str(i).ljust(num_str_len_needed, ' ')

    # calculate position of current line relative to center of triangle
    max_num_pos = line_str.find(str(max_num_in_line)) if n % 2 != 0 else line_str.find(str(max_num_in_line)) - int(num_str_len_needed / 2)
    # if max num is not in center of triangle - add offset (1/2 of brick length)
    while max_num_pos < tr_center - int(num_str_len_needed / 2):
        line_str = ' ' * int(num_str_len_needed / 2) + line_str
        max_num_pos = line_str.find(str(max_num_in_line)) if n % 2 != 0 else line_str.find(str(max_num_in_line)) - int(num_str_len_needed / 2)

    # add line to result triangle
    triangle.append(line_str)

# print triangle
for l in triangle:
    print(l)
