import gravity_falls2 as gf


rot_tests = {
    '''V YBIR LBH''':'''I LOVE YOU''',
    '''zkdwhyv ehdur''':'''WHATEVS BEARO'''
 
}

clusterfuck = {
    #'''WY WURSHV ZLOO UXLQ BRXU OLIH''':''' ''',
    #'''QHAW ZHHN:  UHWXUQ WR EXWW LVODQG''':''' ''',
    '''YM'KL ECN PPK WFOM UBR KQVXLNK, DCI SIK'U VDA JFTOTA AYQ BWL VVCT "EBTGGB BHWKGZH " HVV: TMEASZFA LOS YDCT PRWKTIYEKGL DBV XQDTYRDQVI''':''' ''',
    '''SMERHOL ||| OMHADAWN ||| GORBASH''':''' ''',
    '''VXFQLKB-AYRTHHEJ!''':''' ''',
    '''IFMMP KFSFNZ T EPOOS S KBTPO C TBSDE CSDOEPQ CST GPSFWFS!''':''' ''',
    '''Xpcveaoqfoxso''':''' ''',
    '''R C J W J T Q W K S E W F S Q F S W D T O E D F W U D O I J E V C D E K W L L D P W O J F S W U D O I J E ''':''' ''',
    '''zkd whyv ehdur''':''' '''
}

A1Z26_tests = {
    '''16-23-2-15-10-17''':''' ''',
    '''18-3-10 23-10-20 17-23-11-19-5 23-6-19 17-6-19-23-4 20-15-5-4-6-23-21-4-15-9-10-5
       22-3-4 5-11-23-12-12 4-16-23-15-10 6-19-23-21-4-15-9-10-5''':''' ''',
    '''4-8-15-16-23-42''':''' ''',
    '''6-12-1-7''':''' '''
}

atbash_tests = {
    '''kfiv vmvitb mlg hprm zmw ylmv irhrmt orpv gsv hsvkziw glmv''':'''PURE ENERGY NOT SKIN AND BONE RISING LIKE THE SHEPARD TONE'''
}

for test in clusterfuck:
    print( gf.rot(tekst=test, rot=23) )
