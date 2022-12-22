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
    }
    return Some(score);
}

pub fn part_two(input: &str) -> Option<i32> {
    let plays = input
        .split("\n");
    let mut score: i32 = 0;
    for play in plays {
        let elf: i32 = play.as_bytes()[0] as i32 - 65;
        let outcome: i32 = play.as_bytes()[2] as i32 - 88;
        if outcome == 0 { // Outcome = X = 0 = LOSE
            score += ((elf + 2) % 3) + 1;
        }
        else if outcome == 2 { // Outcome = Z = 2 = WIN
            score += ((elf + 1) % 3) + 1;
        } else { // Outcome = Y = 1 = TIE
            score += elf + 1;
        }
        score += outcome * 3; // account for lose (0), tie (3), win (6)
    }
    return Some(score);
}