
from curses.ascii import NUL
import imp
import re
import dico as dico_api
import labelizer_engine

if __name__ == '__main__':
    dico = dico_api.loadDico()
    trainingDataSet = dico_api.generateTrainSet(dico)

    text1="I am so happy to be home tonight"
    tag1=labelizer_engine.get_label(trainingDataSet, dico_api.computeThemeOccurences(text1, dico))

    text2="My pain is so deep"
    tag2=labelizer_engine.get_label(trainingDataSet, dico_api.computeThemeOccurences(text2, dico))

    text3="I want to see you soon"
    tag3=labelizer_engine.get_label(trainingDataSet, dico_api.computeThemeOccurences(text3, dico))

    text4="one, more.... day in heaven toto"
    tag4=labelizer_engine.get_label(trainingDataSet, dico_api.computeThemeOccurences(text3, dico))



    print (f"Tag for '{text1}' ===> '{tag1}'")
    print (f"Tag for '{text2}' ===> '{tag2}'")
    print (f"Tag for '{text3}' ===> '{tag3}'")
    print (f"Tag for '{text4}' ===> '{tag4}'")

    
