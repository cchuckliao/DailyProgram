#  有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os


def all_program(file):
    lst = []
    files = os.listdir(file)
    for program in files:
        if program.endswith('py'):
            lst.append(os.path.join(file, program))
    print(lst)
    statistic = [0, 0, 0]
    for program in lst:
        lst_b = statistic_program(program)
        lst_c = list(zip(statistic, lst_b))
        statistic = [x + y for x, y in lst_c]
    return statistic


def statistic_program(program):
    statistic = [0, 0, 0]
    with open(program, encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                statistic[2] += 1
            elif line == '\n':
                statistic[1] += 1
            else:
                statistic[0] += 1
    return statistic


if __name__ == '__main__':
    file = r'C:\Users\dell\PycharmProjects\daily program'
    program_list = all_program(file)
    print(
        f'there are {program_list[0]} lines of code, {program_list[1]} blank lines and {program_list[2]} '
        f'lines of annotation')
