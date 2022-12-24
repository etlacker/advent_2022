use std::{env, fs};
use std::time::Instant;

// mod day01;
// mod day02;
mod day03;

fn main() {
    println!("-- Running Problem --");
    let input = read_file("inputs", 03);

    let start_time = Instant::now();
    // println!("Day 1 Part 1: Highest: {:?}", day01::part_one(&input).unwrap());
    // println!("Day 1 Part 2: Sum of Highest 3: {:?}", day01::part_two(&input).unwrap());
    println!("Day 3 Part 1: Score: {:?}", day03::part_two(&input).unwrap());
    println!("Total time: {:?}", Instant::now() - start_time);

}

fn read_file(folder: &str, day: u8) -> String {
    let cwd = env::current_dir().unwrap();
    let filepath = cwd.join("src").join(folder).join(format!("{:02}.txt", day));
    let f = fs::read_to_string(filepath);
    f.expect("could not open input file")
}
