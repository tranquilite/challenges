from sys import argv

alfabet = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
tegn = [*''',.;:`´'`"-!''']


def rot(tekst='', rot=13) -> str:
    '''
    Implementerer enkel ROT-n-kryptering.
    '''

    #print('ROT'+str(rot)+':', end='\t')

    solution = ''
    print(tekst)
    for e in tekst.upper():
        try:
            solution += alfabet[(alfabet.index(e)+(rot)) % 26]

        except ValueError:
            solution += e

    return solution


def atbash(tekst=''):
    '''
    Atbash er en simpel substitusjonscipher som reverserer
    alfabetet, slik at
    A = Z, B = Y, ... Z = A
    '''
    solution = ''

    for e in tekst.upper():
        try:
            solution += alfabet[alfabet[-1::-1].index(e)]
        except ValueError:
            solution += e
    return solution


'''def A1Z26(tekst=''):
    
    Implementerer A1Z26, et substitusjonscipher som erstatter
    alfabetisk med numerisk representasjon.
    A = 1, B = 2, ... Z = 26
   

    print('A1Z26:', end='')

    for e in tegn:
        tekst = tekst.replace(e, ' ')
    tekst, klartekst = tekst.split(), ''
    norsk_alfabet = alfabet+['æ', 'ø', 'å']
    for e in tekst:
        try:
            for i in enumerate(norsk_alfabet, start=1):
                if i[0] == int(e):
                    klartekst += i[1] + ' '

        except ValueError:
            print('', end='')
        except TypeError:
            print('', end='')

    if len(klartekst) is not 0:
        print('\t'+klartekst)
    else:
        print('\tIngen løsning')'''


def vigenere(tekst, nokkel):
    '''
    Eh.. Helvete heller.
    '''

    kolonne, rad, cipherkode = [], [], []
    ciphertekst = ''
    indices = alfabet+tegn
    print(indices)

    for symbol in tekst.upper():
        print(tekst, symbol)
        kolonne.append(indices.index(symbol))

    for symbol in nokkel.upper():
        rad.append(indices.index(symbol))

    cipherkode = [(kolonne+rad) for kolonne, rad in zip(kolonne, rad)]

    print(cipherkode)

    for e in cipherkode:
        ciphertekst += indices[(e % len(indices))]

    print(tekst)
    print(ciphertekst)


if __name__ == '__main__':
    #cipher = '''14-5-24-20 21-16: "6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5'19 7-18-5-22-5-14-7-5."'''
    #cipher = 'kfiv vmvitb mlg hprm zmw ylmv irhrmt orpvgsv hsvkziw glmv zkdwhyv ehdur'.upper()
    # cipher = '''16-23-2-15-10-17'''
    # cipher = '''P W B O J Q'''
    # cipher = '''WY WURSHV ZLOO UXLQ BRXU OLIH'''
    # cipher = '''QHAW ZHHN:  UHWXUQ WR EXWW LVODQG'''
    # cipher = '''SMERHOL ||| OMHADAWN ||| GORBASH'''
    #  cipher = '''VXFQLKB-AYRTHHEJ!'''
    # cipher = '''18-3-10 23-10-20 17-23-11-19-5 23-6-19 17-6-19-23-4 20-15-5-4-6-23-21-4-15-9-10-5
    #        22-3-4 5-11-23-12-12 4-16-23-15-10 6-19-23-21-4-15-9-10-5'''
    # cipher = '''IFMMP KFSFNZ T EPOOS S KBTPO C TBSDE CSDOEPQ CST GPSFWFS!'''
    # cipher = '''Xpcveaoqfoxso'''
    # cipher = '''R C J W J T Q W K S E W F S Q F S W D T O E D F W U D O I J E V C D E K W L L D P W O J F S W U D O I J E '''
    # next needs vigniere, key='cipher'
    cipher = '''YM'KL ECN PPK WFOM UBR KQVXLNK, DCI SIK'U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH " HVV: TMEASZFA LOS YDCT PRWKTIYEKGL DBV XQDTYRDQVI'''
    #cipher='''4-8-15-16-23-42'''

    #rot(tekst=cipher, rot=13)
    #rot(tekst=cipher, rot=23)
    #atbash(tekst=cipher)
    #A1Z26(tekst=cipher)
    #rot(tekst='I LOVE YOU', rot=13)
    vigenere(tekst=cipher, nokkel='CIPHER')
