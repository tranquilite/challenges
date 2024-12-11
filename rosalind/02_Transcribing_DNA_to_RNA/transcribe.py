

def transcribe(dna_string: str) -> str:
    dna_nucleobase = [*'ACGT']
    rna_nucleobase = [*'ACGU']
    rna_string = ''

    for nucleobase in dna_string:
        try:
            rna_string += rna_nucleobase[dna_nucleobase.index(nucleobase)]
        except ValueError:  # nucleobase not in nucleobase preset
            continue

    return rna_string


def transcribe2(dna_string: str) -> str:
    return dna_string.replace('T', 'U')


if __name__ == '__main__':
    sample = 'GATGGAACTTGACTACGTAAATT'
    if transcribe2(sample) == 'GAUGGAACUUGACUACGUAAAUU':
        print('Sample correct')
    else:
        print('Transcription error')

    '''
    dna_fhandle = open('rosalind_rna.txt', 'r')
    rna_fhandle = open('rosalind.output.txt', 'w')

    rna_fhandle.write(transcribe(dna_fhandle.read()))

    rna_fhandle.close()
    dna_fhandle.close()
'''
