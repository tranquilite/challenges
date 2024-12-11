d_ones = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
d_teens = {11:7, 12:6, 13:8, 14:8, 15:7, 16:7, 17:8, 18:8, 19:8}
d_n_ies = {0:0, 1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}


def unity(n):
    l_sum = 0
    n = str(n)
    if len(n) == 1:
        l_sum += d_ones[int(n)]

    cond20 = len(n) == 2
    cond10 = int(n) >= 11 and int(n) <= 19

    if cond20 and cond10:
        l_sum += d_teens[int(n)]
    if cond20 and not cond10:
        l_sum += d_n_ies[int(n[0])]
        l_sum += unity(n[1])
    if len(n) == 3:
        l_sum += d_ones[int(n[0])]
        if not int(n[0]) > 9:
            l_sum += 7
        if not int(n[-2:]) == 0:
            l_sum += 3
        l_sum += unity(n[1:])
    if len(n) == 4:
        l_sum += d_ones[int(n[0])]
        l_sum += 8 #thousand
        if int(n[1:]) != 0:
            l_sum += 3
            l_sum += unity(n[1:])
    return l_sum


def summer(rekke):
    l_sum = 0
    for n in rekke:
        l_sum += unity(n)
    return l_sum
    
rad = range(1,1001)
print(summer(rad))
