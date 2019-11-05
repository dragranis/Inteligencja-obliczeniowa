import pandas as pd
import numpy as np
import math as math
from sklearn import tree
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


data_file = pd.read_csv('iris.csv')

def check_flower(flower):
    sl = flower.sepallength;
    sw = flower.sepalwidth;
    pl = flower.petallength;
    pw = flower.petalwidth;

    if pw<1: return 'Iris-setosa';
    elif pl<=4.8: return 'Iris-versicolor';
    else: return 'Iris-virginica';

correct = 0;


for i in range(len(data_file)):
    variety = check_flower(data_file.iloc[i]);
    if variety == data_file.iloc[i].variety:
        correct+=1;


print("Poprawnych odgadnięć: ",correct);
print("Dokładność: ",(correct/len(data_file))*100 )


print("Działanie bibloteki sklearn")

training_set = []
testing_set = []


all_inputs = data_file[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].values
all_classes = data_file['variety'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)


decision_tree = tree.DecisionTreeClassifier()
decision_tree.fit(train_inputs,train_classes)
print(decision_tree.score(test_inputs,test_classes))

tree.plot_tree(decision_tree.fit(train_inputs, train_classes))