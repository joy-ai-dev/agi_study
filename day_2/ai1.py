from sklearn import tree

# Example data: [height, weight], 0=short, 1=tall
X = [[150, 50], [160, 55], [170, 60], [180, 70]]
y = [0, 0, 1, 1]  # labels

clf = tree.DecisionTreeClassifier()
clf.fit(X, y)  # train
print(clf.predict([[175, 65]]))  # predict
