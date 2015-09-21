import pandas as pd
from sklearn import tree

# X = [[0, 1], [1, 1]]
# Y = [0, 1]
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X, Y)

data = pd.read_excel('/home/andre/sandbox/jhu-immuno/journal.pcbi.1003266.s001-2.XLS')

resp_cols = [ 'MHC' ]

data['y'] = data.Immunogenicity.map({'non-immunogenic': 0, 'immunogenic': 1 })

X = data[resp_cols]
Y = data.y
clf = tree.DecisionTreeClassifier()

dummy = pd.get_dummies(data.MHC)

clf.fit(dummy, Y)

from sklearn.externals.six import StringIO
f = tree.export_graphviz(clf, out_file = 'decision_tree')