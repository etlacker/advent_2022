#     [C]             [L]         [T]
#     [V] [R] [M]     [T]         [B]
#     [F] [G] [H] [Q] [Q]         [H]
#     [W] [L] [P] [V] [M] [V]     [F]
#     [P] [C] [W] [S] [Z] [B] [S] [P]
# [G] [R] [M] [B] [F] [J] [S] [Z] [D]
# [J] [L] [P] [F] [C] [H] [F] [J] [C]
# [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
#  1   2   3   4   5   6   7   8   9
import sys


def part_one():
    stacks = [[],
              ['Z', 'J', 'G'],
              ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
              ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
              ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
              ['G', 'C', 'F', 'S', 'V', 'Q'],
              ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
              ['H', 'F', 'S', 'B', 'V'],
              ['F', 'J', 'Z', 'S'],
              ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
              ]

    with open('inputs/05.txt', "r") as moves:
        for line in moves.readlines():
            [_, ammount, _, stack_a, _, stack_b] = line.split(' ')
            for i in range(0, int(ammount)):
                stacks[int(stack_b)].append(stacks[int(stack_a)].pop())

    print('Part1: ')
    print(stacks)


def part_two():
    stacks = [[],
              ['Z', 'J', 'G'],
              ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
              ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
              ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
              ['G', 'C', 'F', 'S', 'V', 'Q'],
              ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
              ['H', 'F', 'S', 'B', 'V'],
              ['F', 'J', 'Z', 'S'],
              ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
              ]

    with open('inputs/05.txt', "r") as moves:
        for line in moves.readlines():
            [_, ammount, _, stack_a, _, stack_b] = line.split(' ')
            temp = []
            for i in range(0, int(ammount)):
                temp.append(stacks[int(stack_a)].pop())
            while temp:
                stacks[int(stack_b)].append(temp.pop())

    print('Part2: ')
    print(stacks)


def main():
    for arg in sys.argv[1:]:
        if arg == 'p1':
            part_one()
        elif arg == 'p2':
            part_two()
        else:
            print('bruh.')


if __name__ == "__main__":
    main()
