import math
from re import A
import nltk as nt
from numpy import mean
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import pycountry as pyc
from nltk.stem import PorterStemmer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

nt.download([
    "stopwords",
    "crubadan"
])

# Import english stopwords
stopwords = nt.corpus.stopwords.words("english")

# Object to detect languages of lyrics
tc = nt.classify.textcat.TextCat()

# Stemmer of words
ps = PorterStemmer()

# Object to token lyrics
tokenizer = nt.RegexpTokenizer(r"\w+")

# Retrieve datas
data = pd.read_csv("D:\Cours\Cours_M2\Projet\\10001-12000.csv")

# Clean data
data = data[(data.Lyrics != "NAN")]
data["Lyrics"].astype(str)
data = data.dropna(how='any', axis=0)

# Slice the data for dev purposes
data=data[:10]

# Keep only english songs
for i,_ in enumerate(data):
    val = pyc.languages.get(alpha_3=data.iloc[i]["Lyrics"])
    if val != None and val.name != "English":
        data.drop(i)

# Tokenize the lyrics
def tokenize_lyrics_from_list(lyrics):
    new_data = list()
    for words in lyrics:
        new_data.append(tokenizer.tokenize(words))
    return new_data

# Filter the lyrics on tokenized lyrics
def remove_number_and_stopwords(lyrics):
    for words in lyrics:
        for word in words:
            if not(word.isalpha()) or word.lower() in stopwords:
                words.remove(word)

#Stem words of lyrics on tokenized lyrics
def stem_words(lyrics):
    new_data = list()
    for words in lyrics:
        lyrics_words = list()
        for word in words:
            lyrics_words.append(ps.stem(word))
        new_data.append(lyrics_words)
    return new_data

tokenized_data = tokenize_lyrics_from_list(data["Lyrics"])
remove_number_and_stopwords(tokenized_data)
stemed_data = stem_words(tokenized_data)

tokenized_filtered_stemed_data= list()
for a in tokenized_data:
    tokenized_filtered_stemed_data.append(stem_words(a))

# Normalize data
data[["arousal_tags","valence_tags"]] = StandardScaler().fit_transform(data[["arousal_tags","valence_tags"]])

# To be able to analyze sentiment we need to detokenize data
detokenized_data = list()
for lyrics in stemed_data:
    detokenized_data.append(TreebankWordDetokenizer().detokenize(lyrics))


# Create a sentiment analyzer object and detect the valence of lyrics
sia = SentimentIntensityAnalyzer()
def is_positive(lyrics: str) -> bool:
    return sia.polarity_scores(lyrics)["compound"] >= 0.05

def is_negative(lyrics: str) -> bool:
    return sia.polarity_scores(lyrics)["compound"] <= -0.05

def is_neutral(lyrics: str) -> bool:
    return sia.polarity_scores(lyrics)["compound"] > -0.05 and sia.polarity_scores(lyrics)["compound"] < 0.05

# ---------------------------------------------------------------------------------
def get_value(lyrics):
    return [is_positive(lyrics), is_negative(lyrics), is_neutral(lyrics)]

print("Track: {}, Positive: {}, Negative: {}, Neutral: {}".format(data.iloc[1]["track"],
get_value(is_positive(data.iloc[1]["Lyrics"])),
get_value(is_negative(data.iloc[1]["Lyrics"])),
get_value(is_neutral(data.iloc[1]["Lyrics"]))))