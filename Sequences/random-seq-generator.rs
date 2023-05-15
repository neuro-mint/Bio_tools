#![allow(non_snake_case)]
use std::io;
use rand::Rng;

fn main() {
    const DNA_NUCLEOTIDES: &[u8] = b"ATGC";
    const RNA_NUCLEOTIDES: &[u8] = b"AUGC";
    let mut rng = rand::thread_rng();

    let mut nuc_type:String = String::new();
    println!("DNA or RNA");
    io::stdin()
        .read_line(&mut nuc_type)
        .expect("Failed to read line");

    let mut len:String  = String::new();
    println!("Enter length of DNA sequence");
    io::stdin() 
        .read_line(&mut len)
        .expect("Failed to readd line");    
    let len: u32 = len.trim().parse().expect("Please enter a whole number");

    let n: &str = nuc_type.trim();
    match n {
        "DNA" => {
            let random_DNA_seq: String = (0..len)
            .map(|_| {
                let idx = rng.gen_range(0..DNA_NUCLEOTIDES.len());
                DNA_NUCLEOTIDES[idx] as char
            }).collect();
            println!("{:?}", random_DNA_seq);
        },

        "RNA" => {
            let random_RNA_seq: String = (0..len)
            .map(|_| {
                let idx = rng.gen_range(0..RNA_NUCLEOTIDES.len());
                RNA_NUCLEOTIDES[idx] as char
            }).collect();
        println!("{:?}", random_RNA_seq);
        },

        _ => println!("Please enter a valid nucleic acid")
    }
}
