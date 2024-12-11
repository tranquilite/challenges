"""Verktøy-fil for ROSALIND-problemer. I essens bare en samling som
gjør småoppgaver som ble gjentatt og gjentatt ("kodededuplisering")"""
import time


def rna_codon_map_conversion() -> dict:
    '''Konverterer Kodon-kartet fra Rosalind til dict'''
    raw_rna_codon_map = '''
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G'''.split()

    rna_codon_map = {}
    counter = 0

    while (counter < len(raw_rna_codon_map)):
        rna_codon_map[raw_rna_codon_map[counter]] = \
            raw_rna_codon_map[counter+1]
        counter += 2

    # HOTFIX - Non-coding codons
    for codon in ['UAA', 'UAG', 'UGA']:
        rna_codon_map[codon] = '*'

    return rna_codon_map


def protein_rna_map() -> dict:
    '''Flipp rna_codon_map '''
    rna_map = rna_codon_map_conversion()
    amino_acid_map = {}

    for codon in rna_map:
        seq = rna_map[codon]
        if seq in amino_acid_map:
            amino_acid_map[seq].append(codon)
        else:
            amino_acid_map[seq] = [codon]

    return amino_acid_map


def parse_fasta_str(raw_fasta: str) -> dict:
    """ Tra en streng med \n-newlines og gir tilbake en dict av formen
    'Rosalind_01': 'CACTG'.
    Hvis strengen ikke er gyldig fasta-format, vil et tomt {} produseres."""
    string_name, string_dict = '', {}
    try:
        for line in raw_fasta.split():
            if line[0] == '>':  # en ny strengsekvens
                string_name = line[1:]  # dropp > og erklær ny string_name
                string_dict[string_name] = ''  # wakey wakey dicty
            else:
                string_dict[string_name] += line
    except KeyError:
        """Hvis det ikke er funnet en linje som begynner med >,
        så er dette ikke en rosalind fasta-streng, og string_dict får ikke
        minst én nøkkel og gir en KeyError"""
        return {}
    else:
        return string_dict


def timer(func):
    ''' Decorator for å rast sjekke hastigheten på funksjoner'''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper


def fprint(func):
    ''' Ble lat - decorator for å printe returnverdi'''
    def wrapper(*args, **kwargs):
        fnc_call = func(*args, **kwargs)
        print(f'>>{fnc_call}')
        return fnc_call
    return wrapper


if __name__ == '__main__':
    pass  # Test space
