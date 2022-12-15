pub fn part_one(input: &str) -> Option<u32> {
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
    println!("highest: {}", sums[0]);
    return Some(sums[0]);
}
