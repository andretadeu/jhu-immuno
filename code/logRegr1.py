# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:16:08 2015
get dat and put it in pandas data set
@author: brian
"""

import pandas as pd


train = pd.read_excel('../input/journal.pcbi.1003266.s001-2.XLS')


resp_cols  = ['MHC']

pd.crosstab(train['MHC'],train['Immunogenicity'])

from sklearn import preprocessing
lb = preprocessing.LabelBinarizer(neg_label='non-immunogenic',pos_label='immunogenic' )

train['y']=train.Immunogenicity.map({'non-immunogenic':0, 'immunogenic':1})

dum2=pd.get_dummies(train.MHC)

X = dum2
y = train.y



# TASK 3: split the data into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# TASK 4: fit a logistic regression model and examine the coefficients
from sklearn.linear_model import LogisticRegression



logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)
zip(dum2.columns, logreg.coef_[0])




