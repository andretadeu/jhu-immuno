# -*- coding: utf-8 -*-

# title + citation + 20 + blank == 23

d = {}

currname = ""
with open("../input/amino_acid_prop_cleaned.txt") as fi:
    for i, x in enumerate(fi.readlines()):
        if i % 23 == 0:
            currname = '_' + x.replace('\n','').replace(' ','_').replace('(','').replace(')','').replace('.','')
            d[currname] = []
        if i % 23 == 1:
            continue
        if i % 23 == 22:
            continue
        else:
            pass
            d[currname].append(float(x.split()[0]) )

#print d.keys()
#print len(d)

letters=[ 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V' ]

lkeys = list(d.keys())
lkeys.sort()

with open('../input/amino_acid_prop_cleaned.csv', 'w') as fo:
    fo.write('letter,');
    for k in lkeys:
        fo.write(k)
        fo.write(',')
    fo.write('\n')
    for i in range(20):
        fo.write(letters[i])
        fo.write(',')
        for k in lkeys:
            fo.write(str(d[k][i]))
            fo.write(',')
        fo.write('\n')





