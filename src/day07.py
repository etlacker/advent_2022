
# a dict of {'name': [children, size]}

class directory_node:

    def __init__(self, name, prev, root):
        self.name = name
        self.files = []
        self.dirs = []
        self.size = 0
        self.prev = prev
        self.root = root

    def pretty_print(self):
        if self.dirs != []:
            for dir in self.dirs:
                dir.pretty_print()
        print(self.name, self.files)


def consume(node, stack):
    command = stack[0].strip()
    print('--> start\tcommand: ', command, '\tcurrent dir: ', node.name)
    if command == 'end':
        return node.root
    if command[0] == '$':
        if command[2:4] == 'cd':
            if command[5] == '/':
                consume(node.root, stack[1:])
            elif command[5] == '.':
                consume(node.prev, stack[1:])
            else:
                for dir in node.dirs:
                    print(f'\tcmd[5:] -> [{command[5:].strip()}], dir.name -> [{dir.name}]')
                    if dir.name == command[5:].strip():
                        consume(dir, stack[1:])
                print(f'\t\tNo Match for {command[5:]} in ', node.dirs)
        elif command[2:4] == 'ls':
            index = 1
            while True:
                if stack[index][0] != '$':
                    if stack[index][0].isnumeric():
                        print(f'\tAdding File: {stack[index].split()[1].strip()}')
                        node.files.append(i.strip() for i in stack[index].split())
                        index += 1
                    elif stack[index].strip() != 'end':
                        print(f'\tAdding Dir: {stack[index].split()[1].strip()}')
                        node.dirs.append(directory_node(stack[index].split()[1].strip(), node, node.root))
                        index += 1
                else:
                    if stack[index] == 'end end':
                        break
                    consume(node, stack[index:])


def part_one():

    directory = directory_node('/', None, None)
    directory.root = directory

    with open('inputs/07.txt', 'r') as input:
        commands = input.readlines()

    consume(directory, commands)

    directory.pretty_print()


def main():
    print("Part 1: ", part_one())


if __name__ == "__main__":
    main()
