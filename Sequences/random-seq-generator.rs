#![allow(non_snake_case)]
use std::io;
use rand::Rng;    

fn main() {
    let mut nuc_type:String = String::new();
    println!("DNA or RNA");
    io::stdin()
        .read_line(&mut nuc_type)
        .expect("Failed to read line");
    let n: &str = nuc_type.trim();
    match n {
        "DNA" => DNA_genseq(),
        "RNA" => RNA_genseq(),
        _ => println!("Please enter a valid nucleic acid")
    }
}

fn DNA_genseq() {
    const NUCLEOTIDES: &[u8] = b"ATGC";
    let mut rng = rand::thread_rng();

    let mut len:String  = String::new();
    println!("Enter length of DNA sequence");
    io::stdin() 
        .read_line(&mut len)
        .expect("Failed to readd line");    
    let len: u32 = len.trim().parse().expect("Please enter a whole number");
   
    let random_DNA_seq: String = (0..len)
        .map(|_| {
            let idx = rng.gen_range(0..NUCLEOTIDES.len());
            NUCLEOTIDES[idx] as char
        }).collect();
    println!("{:?}", random_DNA_seq);
}

fn RNA_genseq() {
    const NUCLEOTIDES: &[u8] = b"AUGC";
    let mut rng = rand::thread_rng();

    let mut len:String  = String::new();
    println!("Enter length of RNA sequence");
    io::stdin() 
        .read_line(&mut len)
        .expect("Failed to readd line");    
    let len: u32 = len.trim().parse().expect("Please enter a whole number");
   
    let random_RNA_seq: String = (0..len)
        .map(|_| {
            let idx = rng.gen_range(0..NUCLEOTIDES.len());
            NUCLEOTIDES[idx] as char
        }).collect();
    println!("{:?}", random_RNA_seq);
}
