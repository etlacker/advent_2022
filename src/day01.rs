pub fn part_one(input: &str) -> Option<u32> {
    let sums = sorter_helper(input);
    return Some(sums[0]);
}

pub fn part_two(input: &str) -> Option<u32> {
    let sums = sorter_helper(input);
    return Some(vec![sums[0], sums[1], sums[2]].iter().sum());
}

fn sorter_helper(input: &str) -> Vec<u32> {
    let mut sums = input
        .split("\n\n")
        .map(|x| {
            x
                .split('\n')
                .map(|y| 
                    y.parse::<u32>().unwrap()
                )
                .sum::<u32>()
        })
        .collect::<Vec<u32>>();
    sums.sort();
    sums.reverse();
    return sums;
}
