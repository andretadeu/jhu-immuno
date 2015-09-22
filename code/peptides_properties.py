

import sys

peps = {}
letmap = {
'ALA': 'A',
'ARG': 'R',
'ASN': 'N',
'ASP': 'D',
'CYS': 'C',
'GLN': 'Q',
'GLU': 'E',
'GLY': 'G',
'HIS': 'H',
'ILE': 'I',
'LEU': 'L',
'LYS': 'K',
'MET': 'M',
'PHE': 'F',
'PRO': 'P',
'SER': 'S',
'THR': 'T',
'TRP': 'W',
'TYR': 'Y',
'VAL': 'V'
}

props = {
'X': [0.0] * 544
}

with open('../input/journal.pcbi.1003266.csv') as fjour:
    for i, l in enumerate(fjour.readlines()):
        if i == 0:
            continue
        ls = l.split(';')
        if len(ls[0]) != 9:
            continue
        peps[ls[0]] = ls[len(ls)-2]

print len(peps)


def fil(x):
    if x == 'NA':
        return 0.0
    else:
        return float(x)

        
with open('../data/aaProp20x544.csv') as fprop:
    for i, l in enumerate(fprop.readlines()):
        if i == 0:
            continue
        ls = l.split(',')
        key = ls[0].upper().replace('"','')
        # print letmap[key]
        vals = map(fil, ls[1:])
        # print vals
        props[letmap[key]] =  vals

# print props.keys()

# for l in props.keys():
#     print l, len(props[l])
# sys.exit(0)


def colname(i,j):
    return "Pos%d_Prop%03d," % (i, j)

with open('../data/peptide_9_props.csv', 'w') as fmat:
    fmat.write('PEPTIDE,')
    for i in range(9):
        for j in range(544):
            fmat.write(colname(i+1,j+1))
    fmat.write('\n')    
    for pep in peps:
        fmat.write(pep)
        fmat.write(',')
        for ami in pep:
            for val in props[ami]:
                fmat.write(str(val))
                fmat.write(',')
        fmat.write('\n')
        #break


