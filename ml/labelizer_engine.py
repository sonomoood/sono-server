#Chargement de la base
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
import numpy as np 


def ff(row):
    return row / sum(row)

def get_label(trainingData, data):

    #initialisation du générateur
    np.random.seed(10)

    #print("-> TrainingData input :","\n", trainingData)
    
    # Encode tags:
    #Encoder1 =preprocessing.LabelEncoder()
    #trainingData["Tag"]=Encoder1.fit_transform(trainingData[ :-1 ])
    #tags = Encoder1.classes_
    #print("-> Nos labels de classification :","\n", tags)

    # remove titles:
    dataNp=np.array(trainingData)
    X = dataNp[: ,:-1].astype(np.float)
    Y = dataNp[: ,-1]

    print ("X:", '\n', X, '\n', 'Y:', '\n', Y)
    

    #XX = np.apply_along_axis(sorted, 1, np.array([[8,1,7], [4,3,9], [5,2,6]]))
    normalizedX = np.apply_along_axis(lambda row: 100 * row / sum(row), 1, X)
    Encoder1 =preprocessing.LabelEncoder()
    normalizedY=Encoder1.fit_transform(Y)
    tags = Encoder1.classes_

    data = np.array(data)
    normalizedData = 100 * data / sum(data)

    #print ("-> Liste des colonnes et leurs types :","\n", trainingData.dtypes)
    #print ("-> X :", X)
    #print ("-> Y :", Y)
    #print ("-> data :", data)
    #print (" ==> normalizedX:", normalizedX)
    #print (' ==> normalizedY:', normalizedY)
    #print (" ==> normalizedData:", normalizedData)
    #print (" ==> Nos labels de classification :","\n", tags)

    #print ("-> 5 premièrs titres :","\n", trainingData.Title[:5])


    #-----------------------------------
#    dataNp=trainingData.to_numpy()
    #séparation des données explicatives X et de la cible Y avec le slicing
 #   X = dataNp[:, 1:13]
    #y vecteur de la var. à prédire
 #   Y = dataNp[:, 13:]
    #-----------------------------------
    #création d'une instance de la classe
    clf_RF= RandomForestClassifier()
    #Subdivision des données en données train et test avec la fonction train_test_split du module model_selection de pandas
    x_train, x_test, y_train, y_test = train_test_split(normalizedX, normalizedY, test_size=0.2, random_state=0)
    clf_RF.fit(x_train,y_train.ravel())

 #   print ([data])

    y_pred_RF=tags[clf_RF.predict([normalizedData])][0]
    return y_pred_RF

 #   return tags[y_pred_RF][0]

    
    
