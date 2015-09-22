# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:53:12 2015

@author: brian
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


###############################################################################
# import some data to play with

# The iris dataset
train    = pd.read_csv('../data/train.csv')

labelCats = ['T1_V11','T1_V12','T1_V15','T1_V16','T1_V17','T1_V4','T1_V5','T1_V6','T1_V7','T1_V8','T1_V9','T2_V11','T2_V12','T2_V13','T2_V3','T2_V5']
trainLabel = train[labelCats].copy()
for label in labelCats:  
    lbl = LabelEncoder()
    trainLabel[label] = lbl.fit_transform(trainLabel[label])
    
train = pd.get_dummies(train)

trainAll = pd.concat([train,trainLabel],axis=1)

from sklearn.decomposition import PCA
pca = PCA(n_components=100)

y   = train.Hazard   

X = trainAll.drop('Hazard',axis=1)
pca.fit(X)

print(pca.explained_variance_ratio_)

X_new = pca.transform(X) 
v0 = pca.transform(pca.components_[0])
v0 /= v0[-1]