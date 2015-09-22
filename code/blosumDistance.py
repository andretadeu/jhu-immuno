# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:15:36 2015
Blosum62
@author: brian
"""

from Bio.SubsMat import MatrixInfo

def score_match(pair, matrix):
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def score_pairwise(seq1, seq2, matrix, gap_s, gap_e):
    score = 0
    gap = False
    for i in range(len(seq1)):
        pair = (seq1[i], seq2[i])
        if not gap:
            if '-' in pair:
                gap = True
                score += gap_s
            else:
                score += score_match(pair, matrix)
        else:
            if '-' not in pair:
                gap = False
                score += score_match(pair, matrix)
            else:
                score += gap_e
    return score
    
seq1 = 'AAFDRKSDAK'
seq2 = 'YYYAGSSRL-'
    

seq1 = 'PAVKDLGAEG-ASDKGT--SHVVY----------TI-QLASTFE'
seq2 = 'PAVEDLGATG-ANDKGT--LYNIYARNTEGHPRSTV-QLGSTFE'

blosum = MatrixInfo.blosum62

score_pairwise(seq1, seq2, blosum, 1, 1)