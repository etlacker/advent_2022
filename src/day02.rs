pub fn part_one(input: &str) -> Option<i32> {
    let plays = input
        .split("\n");
    let mut score: i32 = 0;
    for play in plays {
        let elf: i32 = play.as_bytes()[0] as i32 - 65;
        let me: i32 = play.as_bytes()[2] as i32 - 88;
        if elf == me {
            score += 3;
        } else if (me + 2) % 3 == elf {
            // I beat elf
            score += 6;
        } // else elf beats me, no points awarded
        score += me + 1;
        println!("{}: {} - {} --> score: {}", play, elf, me, score);
    }
    return Some(score);
}