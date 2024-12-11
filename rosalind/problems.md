# ROSALIND Bioinformatics problem sets #
## DNA: Counting DNA Nucleotides
*01_Counting_DNA_Nucleotides/01_Countding_DNA_Nucleotides.py*  

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt, return four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC  
Sample Output: 20 12 17 21



## RNA: Transcribing DNA to RNA (dna_string: str) -> str
*02_Transcribing_DNA_to_RNA/transcribe.py*  

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed 
RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt, return: The transcribed RNA string of t.

Sample Dataset: GATGGAACTTGACTACGTAAATT  
Sample Output: GAUGGAACUUGACUACGUAAAUU


## REVC: Complementing a strand of dna(dna_strand: str) -> str
*shorts.py*  
Dataset: datasets/rosalind_revc.txt  
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string s c formed by reversing the symbols of s, then taking the complement of each symbol 
(e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp, return The reverse complement sc of s.

Sample Dataset: AAAACCCGGT  
Sample Output: ACCGGGTTTT


## PROT: Translating RNA into Protein (rna_string: str) -> str
*shorts.py*  
Dataset: datasets/rosalind_prot.txt  
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). 
Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp), return: The protein string encoded by s.

Sample Dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA  
Sample Output: MAMAPRTEINSTRING


## FIB: Rabbits and recurrence relations (setting: str) -> int
*shorts.py*  

A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn
represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n
-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5 ,return the total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
  
Sample Dataset: 5 3  
Sample Output: 19

Tests:
5 1 - 5
5 3 - 19
29 2 - 1850229480761
29 5 - 108412748857

## GC: Computing GC Content (fasta_input: str) -> tuple
*shorts.py*  

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each), return the ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset:  
> \>Rosalind_6404  
> CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG  
> \>Rosalind_5959  
> CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC  
> \>Rosalind_0808  
> CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT  

Sample Output:  
Rosalind_0808  
60.919540


## HAMM: Counting Point Mutations (raw_input: str) -> int
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp), return the Hamming distance dH(s,t).

Sample Dataset:  
GAGCCTACTAACGGGAT  
CATCGTAATGACGGCCT  

Sample Output:  
7

## SUBS: Find a Motif in DNA (dna_string: str, substring: str) -> str
*shorts.py*  
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s.
The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5,6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s  

Given: Two DNA strings s and t (each of length at most 1 kbp).  
Return: All locations of t as a substring of s.  

Sample Dataset  
GATATATGCATATACTT  
ATAT  

Sample Output  
2 4 10  
*(1-indexed!)*