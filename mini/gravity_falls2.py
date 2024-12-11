ALFABET = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
TEGN = [*''',.;:`´'`"-! ''']

def caesar(rot=13, *, tekst:str) -> set:
    solution = ''
    for symbol in tekst.upper():
        try:
            if symbol not in TEGN:
                solution += ALFABET[(ALFABET.index(symbol)+rot) % 26]
            else:
                raise IndexError  # Det er dette den gjør uansett..
        except ValueError:
            solution += symbol  # if exception, just add it anyway
        except IndexError:
            solution += symbol

    return solution

def atbash(*, tekst: str) -> str:
    solution = ''
    for symbol in tekst.upper():
        try:
            solution += ALFABET[::-1][ALFABET.index(symbol)]
        except ValueError:
            solution += symbol
    
    return solution

def a1z26(tekst: str) -> str:
    solution, sentence = '', []

    list_of_words = tekst.split(' ')

    for word in list_of_words:
        sentence.append(word.split('-'))

    for word in sentence:
        for letter in word:
            try:
                solution += ALFABET[(int(letter)-1)]
            except ValueError:
                solution += letter
            except IndexError:
                solution += letter
        solution += ' '

    return solution



print(
#atbash(tekst='''kfiv vmvitb mlg hprm zmw ylmv irhrmt orpv gsv hsvkziw glmv''')
    atbash(tekst=
            a1z26(tekst='''18-3-10 23-10-20''')
            )
)
print(
    caesar(tekst='''IXQ DQG''', rot=23)
)