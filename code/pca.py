# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:53:12 2015

@author: brian
"""

import pandas as pd


###############################################################################
# import some data to play with

# The iris dataset
X    = pd.read_csv('../data/train.csv')

from sklearn.decomposition import PCA
pca = PCA(n_components=100)

y   = train.Hazard   

pca.fit(X)

print(pca.explained_variance_ratio_)

X_new = pca.transform(X) 
v0 = pca.transform(pca.components_[0])
v0 /= v0[-1]