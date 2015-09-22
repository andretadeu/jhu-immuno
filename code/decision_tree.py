import pandas as pd
from sklearn import tree

# X = [[0, 1], [1, 1]]
# Y = [0, 1]
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X, Y)

data = pd.read_excel('/home/andre/sandbox/jhu-immuno/input/journal.pcbi.1003266.s001-2.XLS')

resp_cols = [ 'MHC' ]

data['y'] = data.Immunogenicity.map({'non-immunogenic': 0, 'immunogenic': 1 })

X = data[resp_cols]
Y = data.y

dummy = pd.get_dummies(data.MHC)

# from sklearn.externals.six import StringIO
# f = tree.export_graphviz(clf, out_file = 'decision_tree')

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dummy, Y, random_state=1)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

pred_y = clf.predict(X_test)

from sklearn.externals.six import StringIO
with open('decision_tree.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file = 'decision_tree')

import os
os.unlink('decision_tree.dot')

dict = {}
for el in pred_y:
    if el in dict:
        dict[el] += 1
    else:
        dict[el] = 1
