pub fn part_one(input: &str) -> Option<i32> {
    let partner_assignments = input.split("\n");
    let mut count = 0;
    for assignment in partner_assignments {
        println!("assignments: {:?}", assignment);

        let mut splitter = assignment.split(",");
        let mut sections: Vec<(u32, u32)> = Vec::new();

        splitter
            .next()
            .unwrap()
            .split("-")
            .for_each(|x| { sections.push((x.parse::<u32>().unwrap(), 1 as u32)); });
        splitter
            .next()
            .unwrap()
            .split("-")
            .for_each(|x| { sections.push((x.parse::<u32>().unwrap(), 2 as u32)); });

        sections.sort_by(|(a,_), (b,_)| a.cmp(&b));
        
        print!("\tsections: {:?}", sections);
        
        // Check if one assignment covers the other
        if sections[0].1 == sections[3].1 { count += 1; }
        if sections[0].0 == sections[1].0 {
            // if they are the same (one section assign.)
            // if they are different
        }
        // Check if the two ranges begin on the same number and 
        else if sections[0].0 == sections[1].0 &&
                (sections[0].1 == sections[3].1 ||
                sections[1].1 == sections[3].1) {
        }
        // Then, check if an elf has only one assigned section that is 
        // equal to the last of the previous assignment or the first of the next assignment.
        else if sections[1].0 == sections[2].0 {
            if sections[0].0 == sections[1].0 || sections[2].0 == sections[3].0 { count += 1; }
        } 
        // Then check same assignments
        else if sections[0].0 == sections[1].0 && sections[2].0 == sections[3].0 { count += 1; }

        println!("\t\tscore: {}", count);
    }
    return Some(count);
}