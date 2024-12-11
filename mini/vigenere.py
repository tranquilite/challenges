import itertools

alfabet = [*'''ABCDEFGHIJKLMNOPQRSTUVWXYZ''']
glyph = [*'''-' ,.''']


def cipher(klartekst, nokkel):
    glyphs = []
    for e in ciphertekst:
        if e in alfabet:
            glyphs.append(-1)
        else:
            glyphs.append(glyph.index(e))
    glyphs = []

    kol, rad = populer(klartekst, nokkel)
    cipherkode = [(kol+rad) for kol, rad \
                  in zip(kol, rad)]

    return expy(cipherkode, glyphs)


def decipher(ciphertekst, nokkel):
    glyphs = []
    for e in ciphertekst:
        if e in alfabet:
            glyphs.append(-1)
        else:
            glyphs.append(glyph.index(e))

    kol, rad = populer(ciphertekst, nokkel)
    cipherkode = [(kol-rad) for kol, rad \
                  in zip(kol, rad)]

    return expy(cipherkode, glyphs)


def populer(tekst, nokkel):
    while len(nokkel) < len(tekst):
        nokkel += nokkel
    _tekst = [e for e in tekst.upper() if e in alfabet]
    _nokkel = [e for e in nokkel.upper() if e in alfabet]
    kolonne = [(alfabet.index(tegn)) for tegn in _tekst]
    rad = [(alfabet.index(tegn)) for tegn in _nokkel]

    return kolonne, rad


def expy(string, filter_array):
    toPrint = ''
    i = 0
    print(len(string), len(filter_array))
    for e in filter_array:
        print(e)
        i += 1
        if e == -1:
            toPrint += alfabet[string[e] % len(alfabet)]
        else:
            toPrint += (glyph[e])
        
    print(''.join([alfabet[(e % len(alfabet))] for e in string]))
    return toPrint


if __name__ == '__main__':
    # print(cipher('attackatdawn', 'lemon'), decipher('lxfopvefrnhr', 'lemon'))
    print(decipher('''FOC'T FW MVV VIBE EZBAV KF NOW KTB'K FO IHG BBAV VIBE.''', 'CAPACITOR'))
    # print(decipher('''YM’KL ECN PPK WFOM UBR KQVXNLK, DCI SIK’U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH" HVV: TMEASZFA LOS YCDT PRWKTIYEKGL DBV XQDTYRDGVI''', 'cipher'))

    # print('''don't do the time crime if you can't do the time time'''.upper())
    # print(decipher('''VIBE EZBAV''', '''CAPACITOR'''))
    # print(decipher('''VIBE ''', '''CAPACITOR'''))
