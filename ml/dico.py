
from curses.ascii import NUL
import re

words_occurence='words_occurence.csv'
tagged_songs='tagged_songsV2.csv'

def loadDico():
    with open(words_occurence) as file:
        data = {}
        for line in file.read().splitlines()[1:]:
            ll = line.lower().split(';')
            if (len(ll) == 3 and ll[2]): 
                themes = list(dict.fromkeys(ll[2].split()))
                data[ll[0]] = themes # remove dupplication
        return data


def computeThemeOccurences(text, dico=NUL, allThemes=[], foundThemes=set()):
    if dico == NUL: dico = loadDico()

    if len (allThemes) == 0:
        for v in dico.values(): 
            for t in v: 
                if not t in allThemes: allThemes.append(t)
    #print (f"ALL THEMES: {allThemes}")
    themes = {}
    for t in allThemes: themes[t] = 0
    
    words = re.sub(re.compile('\W'), ' ', text).lower().split()

    #print (f'WORDS::: {words}')

    for word in words:
        for theme in dico.get(word) if word in dico else []:
            themes[theme] += 1
            foundThemes.add(theme)

    occurences = []
    for t in allThemes: occurences.append(themes.get(t))
    return occurences


def generateTrainSet(dico):
    allThemes = []


    referencedTheme = set()
    trainingData = []
    with open(tagged_songs) as file:
        for line in file.read().splitlines()[1:]:
            pos = line.rindex(';')
            text = line[0:pos]
            tag = line[pos+1:].lower()

            taggedOccurences = computeThemeOccurences(text, dico, allThemes, referencedTheme)
            taggedOccurences.append(tag)
            trainingData.append(taggedOccurences)
            #print (f"LINE: {text} ====> {tag}")
    
    notTaggedTheme = [t for t in allThemes if t not in referencedTheme]
    if len(notTaggedTheme) != 0:
        raise Exception(f"""
        Some themes of your dictionary are not represented by training data.
        Found not referenced theme :{notTaggedTheme}.
        Please provide samples for them, or supress them from dictionnary.""")

    #print (f"TRAINING DATA:")
    #for r in trainingData: print (r)
    
    return trainingData

if __name__ == '__main__':
    dico = loadDico()
    generateTrainSet(dico)

    message = 'I am home and feel so peace inside.'
    #message = 'Outside into the rain, I remember the past so sadely'
    print (f"Occurences for sample text: '{message}'::: {computeThemeOccurences(message)}")
    
