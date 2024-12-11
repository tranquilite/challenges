def rot_n(cipher=''):
    alfabet = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    for rot in range(0,27):
        staged = ''

        for letter in cipher:
            try:
                staged += alfabet[(alfabet.index(letter)+rot) % 26]
            except ValueError:
                staged += letter


        print(rot,':', staged)

if __name__ == '__main__':
    rot_n('P ZQAE TQR')
    # rot_n('WY WURSHV ZLOO UXLQ BRXU OLIH')


# 1: I LOVE YOU -> [8] [11, 14, 21, 4] [24, 14, 20]
# 2: P ZQAE TQR -> [15] [15, 16, 0, 4] [19, 16, 17]
# 3: I SJTX MJK -> [8] [18, 9, 19, 23] [12, 9, 10]
# 2-1           =  [7]   [4, 2, 21, 0] [-5, 2, -3]
# 3-2           =  [-7] [3, -7, 0, 19] [-7, -7, -7]
# 2, 3, 5, 7, 11, 19



def isPrime(n):
    #meep morp. Dumb helper.
    primeness = True
    for j in range(2, n):
        if n%j == 0:
            primeness = False
            break
    return primeness
