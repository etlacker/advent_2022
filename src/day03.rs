use std::{collections::{HashSet}};

pub fn part_one(input: &str) -> Option<i32> {
    let ruksacks = input.split('\n');
    let mut score = 0;
    for sack in ruksacks {
        let (s1, s2) = sack.split_at(sack.len()/2);
        let first_cmp_val: HashSet<i32> = s1.chars().map(|x| x.to_string().as_bytes()[0] as i32 ).collect();
        let second_cmp_val: HashSet<i32> = s2.chars().map(|x| x.to_string().as_bytes()[0] as i32 ).collect();
        let common_val: Vec<&i32> = first_cmp_val.intersection(&second_cmp_val).collect();
        // let first_cmp: HashSet<String> = s1.chars().map(|x| x.to_string() ).collect();
        // let second_cmp: HashSet<String> = s2.chars().map(|x| x.to_string() ).collect();
        // let common: Vec<&String> = first_cmp.intersection(&second_cmp).collect();
        let numerical = common_val.get(0).unwrap() as &&i32;
        if **numerical - 96 > 0 { score += **numerical - 96;}
        else { score += **numerical - 38; }
        // println!("s: {}, \ns1: {:?}, s2: {:?}, common: {:?}, score: {}", sack, first_cmp, second_cmp, common, score);
    }
    return Some(score);
}

pub fn part_two(input: &str) -> Option<i32> {
    let mut rucksacks = input.split("\n").peekable();
    let mut score: i32 = 0;
    while rucksacks.peek() != None {
        let b1: HashSet<char> = rucksacks.next().unwrap().chars().collect();
        let b2: HashSet<char> = rucksacks.next().unwrap().chars().collect();
        let b3: HashSet<char> = rucksacks.next().unwrap().chars().collect();
        // println!("b1: {:?}\nb2: {:?}\nb3: {:?}", b1, b2, b3);

        let common_vals: HashSet<_> = b1.intersection(&b2).cloned().collect();
        // println!("common_vals: {:?}", common_vals);
        let common_val: Vec<&char> = b3.intersection(&common_vals).collect();
        // println!("common_val: {:?}", common_val);

        let numerical = **common_val.get(0).unwrap() as i32;
        // println!("{}", numerical);
        if numerical - 96 > 0 { score += numerical - 96;}
        else { score += numerical - 38; }
    }
    return Some(score);
}