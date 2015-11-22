# -*- coding: utf-8 -*-

import imp
import pandas as pd

booleanMat = imp.load_source(
            'booleanMat',
            'generate_boolean_matrix.py')

data = pd.read_excel('../input/journal.pcbi.1003266.s001-2.XLS')
peptides = list(data['Peptide'])

import csv
for i in range(8,11):
    matrix = booleanMat.generateBooleanMatrix(peptides, i)
    with open('../data/peptide_matrix_' + str(i) + '-mer.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)