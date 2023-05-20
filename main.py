#!/usr/bin/env python3

from classes import pascal_tr

if __name__ == '__main__':
    depth = int(input('Input depth of Pascal triangle: '))
    tr = pascal_tr(depth)
    tr.print_triangle()
