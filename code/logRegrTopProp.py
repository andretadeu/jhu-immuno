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

resp_cols=['Pos7_Prop368',	'Pos7_Prop099',	'Pos3_Prop090',	'Pos1_Prop190',	'Pos6_Prop461',	'Pos3_Prop233',	'Pos6_Prop231',	'Pos6_Prop495',	'Pos5_Prop097',	'Pos8_Prop245',	'Pos3_Prop456',	'Pos3_Prop087',	'Pos3_Prop335',	'Pos6_Prop317',	'Pos1_Prop070',	'Pos4_Prop451',	'Pos3_Prop450',	'Pos1_Prop351',	'Pos8_Prop098',	'Pos8_Prop144',	'Pos2_Prop422',	'Pos7_Prop126',	'Pos5_Prop307',	'Pos4_Prop018',	'Pos1_Prop257',	'Pos8_Prop403',	'Pos5_Prop016',	'Pos6_Prop273',	'Pos9_Prop432',	'Pos3_Prop191',	'Pos6_Prop173',	'Pos4_Prop520',	'Pos3_Prop144',	'Pos5_Prop336',	'Pos1_Prop447',	'Pos4_Prop164',	'Pos7_Prop315',	'Pos8_Prop254',	'Pos6_Prop445',	'Pos9_Prop376',	'Pos3_Prop094',	'Pos3_Prop328',	'Pos3_Prop438',	'Pos7_Prop296',	'Pos1_Prop315',	'Pos7_Prop192',	'Pos2_Prop111',	'Pos7_Prop234',	'Pos8_Prop250',	'Pos5_Prop472',	'Pos5_Prop288',	'Pos8_Prop513',	'Pos5_Prop361',	'Pos2_Prop183',	'Pos5_Prop102',	'Pos3_Prop389',	'Pos5_Prop055',	'Pos5_Prop384',	'Pos1_Prop377',	'Pos4_Prop192',	'Pos5_Prop065',	'Pos7_Prop148',	'Pos6_Prop158',	'Pos7_Prop067',	'Pos8_Prop465',	'Pos3_Prop207',	'Pos7_Prop401',	'Pos6_Prop450',	'Pos5_Prop286',	'Pos5_Prop535',	'Pos1_Prop050',	'Pos4_Prop289',	'Pos3_Prop164',	'Pos4_Prop507',	'Pos7_Prop057',	'Pos2_Prop070',	'Pos5_Prop242',	'Pos1_Prop471',	'Pos1_Prop543',	'Pos1_Prop492',	'Pos1_Prop001',	'Pos1_Prop005',	'Pos1_Prop007',	'Pos1_Prop029',	'Pos1_Prop032',	'Pos1_Prop035',	'Pos1_Prop041',	'Pos1_Prop054',	'Pos1_Prop060',	'Pos1_Prop073',	'Pos1_Prop082',	'Pos1_Prop087']


X = train[resp_cols]
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
# 0.684810126582

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







