# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:12:24 2018

@author: Amit
"""
# =============================================================================
#               1. Importing libraries
# =============================================================================
from tkinter import *
from tkinter import Text
from tkinter import Button
from tkinter import filedialog
import sys
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# =============================================================================
#                       2. creating functions 
# =============================================================================
def show_data():
    #selecting datafile
    name = filedialog.askopenfilename(initialdir = "/", title ="select file")
    print (name)
    txtarea.insert(0.0,name)
    dataset = pandas.read_csv(name)
    
    # showing and describing data
    shape = "\n" + str(dataset.shape)
    txtarea.insert(END,"\nShape of dataset:")
    txtarea.insert(END, shape)
    print(shape)
    headf= "\n" + str(dataset.head(20))
    txtarea.insert(END,"\n\nFirst 20 rows of dataset:")
    txtarea.insert(END, headf)
    print(headf)
    desc = "\n" + str(dataset.describe())
    txtarea.insert(END,"\n\nDescription of dataset:")
    txtarea.insert(END, desc)
    print(desc)
    classgroup = "\n" + str(dataset.groupby("species").size()) +"\n\n"
    print(classgroup)
    txtarea.insert(END,"\n\nGroup by species:")
    txtarea.insert(END,classgroup)
    
    # plotting dataset
    print("\nBox Plot")
    dataset.plot(kind = "box", subplots = False, layout = (3,3))
    plt.show()
    
    print("\nHistogram")
    dataset.hist()
    plt.show()
    
    print("\nScatter Plot")
    scatter_matrix(dataset)
    plt.show()
    
    # dividing dataset into training and validation set
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

    #Set-up the test harness to use 10-fold cross validation.
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    
    # evaluate each model in turn
    results = []
    names = []
    print("\nAccuracy")
    txtarea.insert(END,"Accuracy of models with Training sets and crossvalidation:\n")
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
       # msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        msg = "\n"+"{}:{} {}".format(name, cv_results.mean(),cv_results.std())
        print(msg)
        txtarea.insert(END,msg)
	
    #Select the best model.
    # Compare Algorithms

    #plt.title("Algorithm Comparison")
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results) 
    ax.set_xticklabels(names)
    #plt.xlabel(names)
    plt.show()
    
    # Make predictions on validation dataset

    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    print('for knn');
    txtarea.insert(END,"\n\nFor KNN on validation set: \n\n")
    predictions = knn.predict(X_validation)
    txtarea.insert(END,"Accuracy:")
    acc = str(accuracy_score(Y_validation, predictions)) + "\n"
    txtarea.insert(END,acc )
    txtarea.insert(END,"\n Confusion Matrix: \n")
    conf_mat = str(confusion_matrix(Y_validation, predictions)) + "\n" 
    txtarea.insert(END,conf_mat)
    txtarea.insert(END,"\n Classification Report: \n")
    cls_rpt = str(classification_report(Y_validation, predictions)) +"\n"
    txtarea.insert(END,cls_rpt)
    print(acc)
    print(conf_mat)
    print(cls_rpt)
    
    svm = SVC();
    svm.fit(X_train, Y_train);
    print('for svm');
    txtarea.insert(END,"\nFor SVM on validation set: \n")
    predictions = svm.predict(X_validation)
    txtarea.insert(END,"Accuracy:")
    acc = str(accuracy_score(Y_validation, predictions)) + "\n"
    txtarea.insert(END,acc)
    txtarea.insert(END,"\n Confusion Matrix: \n")
    conf_mat = str(confusion_matrix(Y_validation, predictions)) + "\n"  
    txtarea.insert(END,conf_mat)
    txtarea.insert(END,"\n Classification Report: \n")
    cls_rpt = str(classification_report(Y_validation, predictions)) +"\n"
    txtarea.insert(END,cls_rpt)
    print(acc)
    print(conf_mat)
    print(cls_rpt)
    
# =============================================================================
#                      3. Creating GUI 
# =============================================================================
root = Tk()
root.title("GUI")
root.geometry("820x430")
filebutton = Button(root, text = "select", highlightcolor="blue", command = show_data)
filebutton.grid(row = 0, column = 0, sticky = [W,E])
sbar = Scrollbar(root)
sbar.grid(sticky = E)
txtarea = Text(root, width = 100, bd = 5, wrap = WORD, yscrollcommand = sbar.set)
txtarea.grid(row = 1, column = 0, sticky = W)
sbar.config(command = txtarea.yview)

root.mainloop()
