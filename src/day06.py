import sys


def part_one():
    with open('input/06.txt', 'r') as stream:
        signal = stream.readlines()

    print('Part1: ')


def part_two():
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
