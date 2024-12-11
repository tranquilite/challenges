"""Denne modulen er *ikke* ment å kjøre som del av noe annet. Den er bare
en samlingsfil av forskjellige oppgaver fra ROSALIND, hvor hver oppgave
er implementert som en enkelt funksjon.
Det er *ingen* sammenhengende konvensjon i grensesnitt, og bare problemene
er dokumentert i problems.md"""
import utility as ut


def REVC_complementing_a_strand_of_dna(dna_strand: str) -> str:
    reverse_strand = dna_strand[::-1]
    complement_strand = ''

    for nucleotide in reverse_strand:
        # This is so baaaad
        if nucleotide in {'A', 'T'}:
            complement_strand += ({'A', 'T'} - {nucleotide}).pop()
        elif nucleotide in {'C', 'G'}:
            complement_strand += ({'C', 'G'} - {nucleotide}).pop()

    return complement_strand


def PROT_translating_rna_into_protein(rna_string: str) -> str:
    protein_sequence = ''
    protein_map = ut.rna_codon_map_conversion()
    try:
        if len(rna_string) % 3 != 0:
            raise ValueError('String length should be multiple of three')

        counter = 0
        while counter < len(rna_string):
            protein_sequence += \
                protein_map[rna_string[counter:counter+3]]
            counter += 3

    except ValueError:
        return []

    # Juster for at rna_codon_map_conversion gir * for non-coding rna
    return protein_sequence.replace('*', '')


def FIB_rabbits_and_recurrence_relations(setting: str) -> int:
    months, kanin_faktor = [int(_) for _ in setting.split()]
    cache = {}

    def fib(month: int, kanin_faktor: int) -> int:
        # Håndter utgangspunktene
        if month in cache:
            return cache[month]
        if month == 1:
            return 1
        if month == 2:  # ..er ikke dette feil?
            return kanin_faktor
        if month in (3, 4):  # nope. Tenk etter
            return fib(month-1, kanin_faktor) + fib(month-2, kanin_faktor)

        kaniner = fib(month-1, kanin_faktor) \
            + kanin_faktor * fib(month-2, kanin_faktor)

        if month not in cache:
            cache[month] = kaniner

        return kaniner

    populasjon = fib(months, kanin_faktor)

    return populasjon


def GC_computing_gc_content(fasta_input: str) -> tuple:
    dna_strings = ut.parse_fasta_str(fasta_input)
    gc_content = {}

    for dna_string in dna_strings:
        gc_string = dna_strings[dna_string].replace('A', '').replace('T', '')
        gc_content[dna_string] = \
            len(gc_string) / len(dna_strings[dna_string]) * 100

    highscore = ('', 0)
    for dna_string in gc_content:
        if gc_content[dna_string] > highscore[1]:
            highscore = (dna_string, gc_content[dna_string])

    return highscore


def HAMM_Counting_point_mutations(raw_input: str) -> int:
    origin, comparison = [e for e in raw_input.split()]
    hamming_distance = 0

    # Følgende oneliner er visstnok også en løsning..
    # return sum(a != b for a, b in zip(origin, comparison))

    if len(origin) != len(comparison):
        return 0

    for idx in range(len(origin)):
        if origin[idx] != comparison[idx]:
            hamming_distance += 1

    return hamming_distance


def SUBS_Finding_a_motif_in_dna(dna_string: str, substring: str) -> str:
    STRLEN = len(substring)
    indices = ''

    for idx in range(len(dna_string)):
        if dna_string[idx:idx+STRLEN] == substring:
            indices += f' {idx+1}'

    return indices


def CONS_overlap_graphs(fasta_input: str) -> str:
    return NotImplementedError


if __name__ == '__main__':
    pass
