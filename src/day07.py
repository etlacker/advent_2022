
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
    if len(stack) <= 1:
        return node.root
    command = stack[0].strip()
    # print('--> start\tcommand: ', command, '\tcurrent dir: ', node.name)
    if command[0] == '$':
        if command[2:4] == 'cd':
            if command[5] == '/':
                return consume(node.root, stack[1:])
            elif command[5] == '.':
                return consume(node.prev, stack[1:])
            else:
                for dir in node.dirs:
                    # print(
                    #     f'\tcmd[5:] -> [{command[5:].strip()}], dir.name -> [{dir.name}]')
                    if dir.name == command[5:].strip():
                        return consume(dir, stack[1:])
                # print(f'\t\tNo Match for {command[5:]} in ', node.dirs)
        elif command[2:4] == 'ls':
            index = 1
            while True:
                # print('while -> ', stack[index].strip())
                if stack[index][0] != '$':
                    if stack[index][0].isnumeric():
                        file = stack[index].split(' ')
                        node.files.append((file[0].strip(), file[1].strip()))
                        index += 1
                    elif stack[index].strip() != 'end end':
                        dir = stack[index].split(' ')
                        node.dirs.append(directory_node(
                            dir[1].strip(), node, node.root))
                        index += 1
                    else:
                        return
                elif stack[index].strip() == 'end end':
                    return node.root
                else:
                    return consume(node, stack[index:])


def calculate_storage_size(node):
    size = 0
    if node.files != []:
        # print(f'Node: {node.name}\tfiles: {[x for x in node.files]}')
        for file in node.files:
            size += int(file[0])
    if node.dirs != []:
        for dir in node.dirs:
            size += calculate_storage_size(dir)
    node.size = size
    return size


def sum_of_lt_tenk_dirs(node):
    # print(f'Node: {node.name}\tSize: {node.size}')
    branch_size = 0
    if node.dirs != []:
        for dir in node.dirs:
            branch_size += sum_of_lt_tenk_dirs(dir)
        if node.size <= 100000:
            return node.size + branch_size
        else:
            return branch_size
    else:
        if node.size <= 100000:
            return node.size
        else:
            return 0


def find_smallest_needed(node, target_size):
    print(f'Node: {node.name}\t\tSize: {node.size}\t\tDirs: {node.dirs}')
    possible_dirs = []
    if node.dirs != []:
        for dir in node.dirs:
            possible_dirs.extend(find_smallest_needed(dir, target_size))
        if node.size >= target_size:
            return possible_dirs.extend([node.size])
        else:
            return possible_dirs
    else:
        if node.size >= target_size:
            return [node.size]
        else:
            return [0]


def main():

    directory = directory_node('/', None, None)
    directory.root = directory

    with open('inputs/07.txt', 'r') as input:
        commands = input.readlines()

    print('Consuming...')
    consume(directory, commands)
    print('Consumed all commands.')

    print('\nCalculating storage sizes...')
    calculate_storage_size(directory)
    print('Storage size calculated.')

    print('\nFinding directories and summing...')
    print(f'Part One: {sum_of_lt_tenk_dirs(directory)}')

    print('Finding smallest directory above 30000000...')
    possible = find_smallest_needed(directory, 30000000 - (70000000 - directory.size))
    print(type(possible), possible)
    print(f'Should delete dir of size: {possible.sort()[0]}')


if __name__ == "__main__":
    main()
