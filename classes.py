from dataclasses import dataclass

@dataclass
class pascal_tr:
    ''' Class to work with pascal triangles '''
    depth: int                  # depth of triangle
    triangle_raw: list          # 2-dimentional arr
    triangle_printable: list    # 1-dimentional arr with spaces

    def __init__(self, depth):
        self.depth = int(depth)
        self.triangle_raw = self.get_triangle_raw(depth)
        self.triangle_printable = self.get_triangle_printable()

    def get_triangle_raw(self, depth:int):
        ''' Returns 2-dimention arr with Pascal triangle '''
        raw_tr = [[1]]
        for i in range (1, depth):
            raw_tr.append([])
            raw_tr[i].append(1)
            for j in range(1, i):
                raw_tr[i].append(raw_tr[i - 1][j - 1] + raw_tr[i - 1][j])
            raw_tr[i].append(1)
        return raw_tr

    def __get_needed_num_len(self, tr:list):
        ''' Returns length of one 'brick' in Pascal triangle '''
        num_len = len(str(max(tr[-1]))) + 1
        if num_len % 2 != 0:
            num_len += 1
        return num_len

    def __get_triangle_center_pos(self, tr:list):
        ''' Returns center position of triangle '''
        num_str_len_needed = self.__get_needed_num_len(tr)
        longest_str = ''
        for n in tr[-1]:
            longest_str += str(n).ljust(num_str_len_needed, ' ')
        tr_center = int(round(len(longest_str) / 2, 0))
        return tr_center

    def __get_max_num_pos(self, tr:list, line_num:int, line_str:str):
        ''' Returns position of biggest number in line '''
        line = tr[line_num]
        max_num_in_line = max(line)
        num_str_len_needed = self.__get_needed_num_len(tr)
        res = line_str.find(str(max_num_in_line)) if line_num % 2 != 0 else line_str.find(str(max_num_in_line)) - int(num_str_len_needed / 2)
        return res 

    def get_triangle_printable(self):
        ''' Returns printable 1-dimention arr '''
        tr = self.triangle_raw
        res_tr = []
        num_str_len_needed = self.__get_needed_num_len(tr)
        tr_center = self.__get_triangle_center_pos(tr)
        for n, line in enumerate(tr):
            line_str = ''
            for i in line:
                line_str += str(i).ljust(num_str_len_needed, ' ')
            max_num_pos = self.__get_max_num_pos(tr, n, line_str)
            while max_num_pos < tr_center:
                line_str = ' ' * int(num_str_len_needed / 2) + line_str
                max_num_pos = self.__get_max_num_pos(tr, n, line_str)
            res_tr.append(line_str)
        return res_tr

    def print_triangle(self):
        ''' Prints Pascal's triangle in console '''
        for l in self.triangle_printable:
            print(l)
