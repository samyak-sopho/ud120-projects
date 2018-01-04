#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np
clf = svm.SVC(C=10000.0)

## reducing training set for fast computation
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

# calculating training time
t0 = time()
clf.fit(features_train, labels_train);
print "training time:", round(time()-t0, 3), "s"

# calculating testing time
t0 = time()
pred = clf.predict(features_test);
print "testing time:", round(time()-t0, 3), "s"

ans = 0
for i in range(len(pred)):
	if pred[i] == 1:
		ans += 1

print ans
# finding accuracy
acc = accuracy_score(pred, labels_test);
print acc

n = len(features_test[0,:])
a = np.zeros((3, n))
for i in range(n):
	a[0,i] = features_test[10,i]
for i in range(n):
	a[1,i] = features_test[26,i]
for i in range(n):
	a[2,i] = features_test[50,i]

print clf.predict(a)
#########################################################
