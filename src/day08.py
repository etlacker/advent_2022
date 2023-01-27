from pprint import pprint


def calc_count(trees):
    count = 0
    for index in range(0, len(trees)):
        count += 1  # first tree is always visible
        visible = trees[index][0] # may not account for last pos.
        # print('v', visible)
        for twodex in range(1, len(trees[0])):
            # print(f't: {trees[index][twodex]} > {visible} ?')
            if int(trees[index][twodex]) > int(visible):
                count += 1
                visible = trees[index][twodex]
        # print(count, ''.join(trees[index]))
    return count

def main():
    with open('inputs/08.txt', 'r') as forrest:
        trees = forrest.readlines()
        trees = [t.strip() for t in trees]
    
    count = 0
    count += calc_count(trees)

    print('\n\n')

    tree2 = list(zip(*trees[::-1]))
    print(trees == tree2)
    # [print(t) for t in trees]
    count += calc_count(trees)

    print('\n\n')

    trees = list(zip(*trees[::-1]))
    count += calc_count(trees)

    print('\n\n')    

    trees = list(zip(*trees[::-1]))
    count += calc_count(trees)

    print(f'Part One: Final count is {count}')
    # 2234 too high
    # 2227 too high

    # Need to keep track of trees that have already been seen: 
    # dict with tuple of position and record of state? BSA?

    #test = 42

if __name__ == "__main__":
    main()
