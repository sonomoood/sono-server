#Chargement de la base
import pandas as pd
trainingData = pd.read_csv("classified_dataset.csv", sep=';')

print ("-> Liste des colonnes et leurs types :","\n", trainingData.dtypes)
print ("-> 10 premières lignes :","\n", trainingData[:5])
print ("-> 5 premièrs titres :","\n", trainingData.Title[:5])

#-----------------------------------
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics
import numpy as np

Encoder1 =preprocessing.LabelEncoder()
trainingData["Tag"]=Encoder1.fit_transform(trainingData[ "Tag" ])
tags = Encoder1.classes_
print("-> Nos labels de classification :","\n", tags)

trainingData["Title"]=Encoder1.fit_transform(trainingData[ "Title" ])


#-----------------------------------
#transformer d'abord data en numpy avec la méthode to_numpy
dataNp=trainingData.to_numpy()
#séparation des données explicatives X et de la cible Y avec le slicing
X = dataNp[:, 1:13]
print(" -> size(X)=", X.shape,"\n", "X=", X)
#y vecteur de la var. à prédire
Y = dataNp[:, 13:]
print(" -> size(Y)=", Y.shape,"\n", "Y=", Y)
#-----------------------------------
from sklearn.ensemble import RandomForestClassifier
#création d'une instance de la classe
clf_RF= RandomForestClassifier()
#Subdivision des données en données train et test avec la fonction train_test_split du module model_selection de pandas
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
clf_RF.fit(x_train,y_train.ravel())
# y_pred_RF=clf_RF.predict(x_test)
print("For songs : Dreadlock Holiday , Angels")
input=[[12,1,0,17,0,2,10,6,11,0,12,5], [2,8,0,20,2,5,12,8,1,0,3,2]]
print("DATA: ", input)
y_pred_RF=clf_RF.predict(input)
print("LABEL: ", tags[y_pred_RF])

#test
#Pain(1) Confidence(2) Fear(3)	Serenity(4)	Madness(5)	Passion(6)	Love(7) Confusion(8) Hope(9) Anger(10) Happiness(11) Sadness(12)
input_non_classified=[[0,5,0,17,0,40,50,6,10,0,30,0]]
print("DATA: ", input_non_classified)
y_pred_RF2=clf_RF.predict(input_non_classified)
print("LABEL: ", tags[y_pred_RF2])
