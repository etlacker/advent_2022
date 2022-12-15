use std::{env, fs};
use std::time::Instant;

mod day01;

fn main() {
    println!("-- Running Problem --");
    let input = read_file("inputs", 01);

    let start_time = Instant::now();
    day01::part_one(&input);
    println!("Total time: {:?}", Instant::now() - start_time);

}

fn read_file(folder: &str, day: u8) -> String {
    let cwd = env::current_dir().unwrap();

    let filepath = cwd.join("src").join(folder).join(format!("{:02}.txt", day));

    let f = fs::read_to_string(filepath);
    f.expect("could not open input file")
}
