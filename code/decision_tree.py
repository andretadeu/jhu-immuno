# Disclaimer: you must have Graphviz installed to run this script

import os
import pandas as pd
from sklearn import tree

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

tree_class = tree.DecisionTreeClassifier()
tree_class.fit(X_train, y_train)

with open('decision_tree.dot', 'w') as f:
    f = tree.export_graphviz(tree_class, feature_names=list(X.columns), out_file = f)

os.system('dot -v -Tpdf decision_tree.dot -o ../pics/decision_tree.pdf')
os.unlink('decision_tree.dot')

tree_class2 = tree.DecisionTreeClassifier(max_depth = 5)
tree_class2.fit(X_train, y_train)

with open('decision_tree2.dot', 'w') as f2:
    f = tree.export_graphviz(tree_class2, feature_names=list(X.columns), out_file = f2)

os.system('dot -v -Tpdf decision_tree2.dot -o ../pics/decision_tree2.pdf')
os.unlink('decision_tree2.dot')
