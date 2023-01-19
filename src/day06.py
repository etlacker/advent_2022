import sys


def is_unique(lst):
    while len(lst) > 1:
        check = lst[0]
        lst.remove(lst[0])
        if check in lst:
            return False

    return True


def part_one():
    with open('inputs/06.txt', 'r') as stream:
        signal = stream.readline()

    lst = [c for c in signal[:3]]

    for index in range(3, len(signal)):
        char = signal[index]
        print(lst, char)
        if char not in lst and is_unique(lst[:]):
            print(index + 1)
            return
        else:
            lst.remove(lst[0])
            lst.append(char)

    print('Part1: ')


def part_two():
    with open('inputs/06.txt', 'r') as stream:
        signal = stream.readline()

    lst = [c for c in signal[:13]]

    for index in range(14, len(signal)):
        char = signal[index]
        # print(lst, char)
        if char not in lst and is_unique(lst[:]):
            print(index + 1)
            return
        else:
            lst.remove(lst[0])
            lst.append(char)

    print('Part2: ')


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
