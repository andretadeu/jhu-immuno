# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:49:37 2015

@author: brian
"""

import pandas as pd

props = pd.read_csv('../data/peptide_9_props.csv')



immun = pd.read_excel('../input/journal.pcbi.1003266.s001-2.XLS')
# understanding the apply method
immun['length'] = immun.Peptide.apply(len)

immun = immun[immun.length ==9]


both =  pd.merge(props, immun, left_on='PEPTIDE', right_on='Peptide')

train = both

train['y']=train.Immunogenicity.map({'non-immunogenic':0, 'immunogenic':1})

# dum2=pd.get_dummies(train.MHC)

# pd.concat(dum2,train)

train = train.drop(['Immunogenicity','PEPTIDE','Peptide','Species','MHC','Unnamed: 4897'],axis=1)


X = train.drop(['y'],axis=1)
y = train.y




# TASK 3: split the data into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# TASK 4: fit a logistic regression model and examine the coefficients
from sklearn.linear_model import LogisticRegression



logreg = LogisticRegression(C=1e1,penalty='l1')
logreg.fit(X_train, y_train)
propImp =zip(X.columns, logreg.coef_[0])
pd.DataFrame(propImp).to_clipboard()


from sklearn import metrics 
# predict and calculate AUC 
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

y_pred_class = logreg.predict(X_test) 

print metrics.roc_auc_score(y_test, y_pred_prob)
# 0.858192133098 with Tdf vectorizer and stop_words='english',ngram_range=(1, 2), max_features=1000
# 0.846367492831 adding 'OL_GENERAL','INSITE_PAGE','BROWSER_OS','BROWSER2'
# 0.846423953016 ngram_range=(1,3)
# 0.810 max_feature 100
# 0.8399 rang=(1,4) max features 2000
print metrics.accuracy_score(y_test, y_pred_class)
# 74.7% with CountVectorizer() 
# 65%
# 76% with TfidfVectorizer(stop_words='english',ngram_range=(1, 2), max_features=1000) 
confusion = metrics.confusion_matrix(y_test, y_pred_class)
print  confusion
sensitivity =float(confusion[1,1])/(confusion[1,0] + confusion[1,1])
print 'sensitivity is %f' % sensitivity
# sensitivity is 50, 56% with CountVectorizer() 

#Q why is sensitivity .09 with tdf if
specificity =float(confusion[0,0])/(confusion[0,0] + confusion[0,1])
print 'specificity is %f' % specificity


import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.plot(fpr, tpr)







