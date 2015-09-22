# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:53:12 2015

@author: brian
"""

import pandas as pd
import numpy as np

###############################################################################
# import some data to play with

# The iris dataset
X    = pd.read_csv('../data/aaProp20x544.csv', na_values = 'NA')

from sklearn.decomposition import PCA
pca = PCA(n_components=100)

len(X)
len(list(X.columns.values))

X['YANJ020101']

#X['CEDJ970101']

#means = X.mean()

#len(means)

#means
#X

X_1 = X.drop(X.columns[[0]], axis = 1)

X_no_nas = X_1.fillna(means)
X_norm = (X_no_nas - X_no_nas.mean()) / (X_no_nas.max() - X_no_nas.min())
# X_norm = X_no_nas / X_no_nas.mean()
#for col in range(len(list(X.columns.values))):
    #col_avg = sum(X[col]) / len(X[col])
    #print col_avg
#    for row in range(len(X)):
        

#y   = train.Hazard   

pca.fit(X_norm)

print(pca.explained_variance_ratio_)

X_norm.insert(0, '', X.icol(0))

X_norm.to_csv('../data/aaProp20x544-norm.csv')

X_new = pca.transform(X) 
v0 = pca.transform(pca.components_[0])
v0 /= v0[-1]

def test():
    L = [4, 'NA', 5]
    df = pd.Series(L)
    if (pd.isnull(df[1])):
        print "Found null"
    if (np.isnan(df[1])):
        print "Found NaN"