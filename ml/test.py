#Chargement de la base
from sklearn import datasets
iris = datasets.load_iris()


print(type(iris)) # Ce n'est pas un DataFrame, mais une sorte de dictionnaire
print(dir(iris)) #les compostantes de la base
print(iris.feature_names) # Les noms des paramètres de nos donénes/enregistrements
print(iris.data[:5]) # aperçu des 5 premiers enregistrements
print(iris.target_names)# nos labels de classification
