#Chargement de la base
import pandas as pd
trainingData = pd.read_csv("classified_dataset.csv", sep=';')

print ("-> Liste des colonnes et leurs types :","\n", trainingData.dtypes)
print ("-> 10 premières lignes :","\n", trainingData[:5])
print ("-> 5 premièrs titres :","\n", trainingData.Title[:5])

tags = trainingData.Tag
all_tags = list(set(tags))
print("-> Nos labels de classification :","\n", all_tags)

#-----------------------------------
from sklearn import preprocessing
Encoder1 =preprocessing.LabelEncoder()
trainingData["Tag"]=Encoder1.fit_transform(trainingData[ "Tag" ])
#-----------------------------------
#transformer d'abord data en numpy avec la méthode to_numpy
dataNp=trainingData.to_numpy()
#séparation des données explicatives X et de la cible Y avec le slicing
X = dataNp[:, :14]
#y vecteur de la var. à prédire
Y = dataNp[:, 14:]
#-----------------------------------
from sklearn.ensemble import RandomForestClassifier
#création d'une instance de la classe
clf_RF= RandomForestClassifier()
#Subdivision des données en données train et test avec la fonction train_test_split du module model_selection de pandas
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
clf_RF.fit(x_train,y_train.ravel())
y_pred_RF=clf_RF.predict(x_test)
#Calculer les scores pour Random Forest
TPR_RF = metrics.recall_score(y_true=y_test, y_pred=y_pred_RF, average=None)
FPR_RF = metrics.precision_score(y_true=y_test, y_pred=y_pred_RF, average=None)
F1_RF = metrics.f1_score(y_true=y_test, y_pred=y_pred_RF, average=None)

print("-> Calcul des scores :","\n", TPR_RF,"\n", FPR_RF ,"\n",F1_RF)
