

def g(x: str) -> tuple:
    return (x.count('A'), x.count('C'), x.count('G'), x.count('T'))


with open('rosalind_dna2.txt') as kilde:
    sekvens = (kilde.readlines())[0][0:-1]
    print(str(g(sekvens))[1:-1])
