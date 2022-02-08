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
from zmq import EMTHREAD

nt.download([
    "names",
    "stopwords",
    "vader_lexicon",
    "shakespeare",
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
emotions = pd.read_csv("D:\Cours\Cours_M2\Projet\\emotions.csv")

# Clean data
data = data[(data.Lyrics != "NAN")]
data["Lyrics"].astype(str)
data = data.dropna(how='any', axis=0)

# Slice the data for dev purposes
data=data[:100]

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

emotion_words = dict()
emotion_words["joy"] = ["excited", "delighted", "blissful"]
emotion_words["anger"] = ["furious", "annoyed", "disgusted"]
emotion_words["sadness"] = ["dispointed", "depressed", "bored"]
emotion_words["pleasure"] = ["content", "serene", "relaxed"]

def determine_tag_by_vad(valence, arousal):
    valence = float(valence)
    arousal = float(arousal)
    if valence > 0:
        if arousal > 0:
            if arousal <= 0.25:
                return ["blissful","joy"]
            if 0.25 < arousal <= 0.75:
                return ["delighted","joy"]
            if arousal > 0.75:
                return ["excited","joy"]
        else:
            if arousal >= -0.25:
                return ["content","pleasure"]
            if  -0.25 > arousal >= -0.75:
                return ["serene","pleasure"]
            if arousal < -0.75:
                return ["relaxed","pleasure"]
    else:
        if arousal > 0:
            if arousal <= 0.25:
                return ["disgusted","anger"]
            if  0.25 < arousal <= 0.75:
                return ["annoyed","anger"]
            if arousal > 0.75:
                return ["furious","anger"]
        else:
            if arousal >= -0.25:
                return ["disapointed","sadness"]
            if -0.25 > arousal >= -0.75:
                return ["depressed","sadness"]
            if arousal < -0.75:
                return ["bored","sadness"]

# Add tag and main_tag which represent emotion of songs base on V/A values
tags = list()
main_tag = list()
for y in range(len(data)):
    tags.append(determine_tag_by_vad(data.iloc[y]["valence_tags"], data.iloc[y]["arousal_tags"])[0])
    main_tag.append(determine_tag_by_vad(data.iloc[y]["valence_tags"], data.iloc[y]["arousal_tags"])[1])
data.insert(len(data.columns), 'tag', tags)
data.insert(len(data.columns), 'main_tag', main_tag)

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

# Determine compound of lyrics
# firts we split the lyrics in 4 parts then we check the coumpound value for each part 
# then we mean all compound values to determine the overall coumpound af the lyrics
def determine_lyrics_compound(lyrics):
    size_of_parts = math.ceil(len(lyrics) / 4)
    split_parts = list()
    split_parts.append(lyrics[:size_of_parts])
    split_parts.append(lyrics[size_of_parts:size_of_parts*2])
    split_parts.append(lyrics[:size_of_parts*2:size_of_parts*3])
    split_parts.append(lyrics[size_of_parts*3:])

    scores = list()
    for values in split_parts:
        scores.append(sia.polarity_scores(values)["compound"])
    return scores

compound = list()
for x in range(len(data)):
    compound.append(mean(determine_lyrics_compound(data.iloc[x]["Lyrics"])))
data.insert(len(data.columns), 'mean_compound', compound)

valence = list()
for a in range(len(data)):
    if data.iloc[a]["mean_compound"] > 0.05:
        valence.append("positive")
    elif data.iloc[a]["mean_compound"] < -0.05:
        valence.append("negative")
    elif - 0.05 < data.iloc[a]["mean_compound"] < 0.05:
        valence.append("neutral")
    else:
        valence.append("nan")
data["valence"] = valence
data.head()

# # Determine bags of positive/negative words base on valence of data
# def create_set_of_words_by_frequency(values, list):
#     fd = nt.FreqDist(values)
#     for value in fd.most_common():
#         if value[0].lower() not in stopwords and value[1] > 12:
#             list.append(value[0].lower())

# positive_words = list()
# negative_words = list()
# for i in range(0, len(stemed_data)):
#     if is_negative(detokenized_data[i]):
#         create_set_of_words_by_frequency(stemed_data[i], negative_words)

#     if is_positive(detokenized_data[i]):
#         create_set_of_words_by_frequency(stemed_data[i], positive_words)

# positive_fd = nt.FreqDist(positive_words)
# negative_fd = nt.FreqDist(negative_words)
# intersection = set(positive_fd).intersection(negative_fd)

# for value in intersection:
#     if value in (positive_words and negative_words):
#         positive_words.remove(value)
#     if value in negative_words:
#         negative_words.remove(value)

# top_100_positive = {word for word, count in positive_fd.most_common(100)}
# top_100_negative = {word for word, count in negative_fd.most_common(100)}

# def number_of_word_in(values: list, list_to_check_in):
#     cpt=0
#     for i in values:
#         if i in list_to_check_in:
#             cpt+=1
#     return cpt

# positive_word_count = list()
# negative_word_count = list()
# for val in stemed_data:
#     positive_word_count.append(number_of_word_in(val, top_100_positive))
#     negative_word_count.append(number_of_word_in(val, top_100_negative))
# data.insert(len(data.columns), 'nb_positive', positive_word_count)
# data.insert(len(data.columns), 'nb_negative', negative_word_count)


# data[]



















# def extract_words_by_emotion(emotion):
#     return emotions[emotions.tag == emotion]

# def number_of_words_by_word_list(lyrics, word_list):
#     cpt = 0
#     for i in lyrics:
#         if i in word_list:
#             cpt+=1
#     return cpt

# emotions_dict = dict()    
# for i in tokenized_data:
#         nb_list = list()
#         nb_list.append(number_of_words_by_word_list(i,extract_words_by_emotion("val")))

# # ----------------------------------------------------------------------------------
# # Removing not pertinent data
# data = data.drop(columns=['number_of_emotion_tags','artist','track','seeds',"Lyrics"])

# # Encoding data
# encoder = LabelEncoder()
# data["genre"] = encoder.fit_transform(data["genre"])
# data["tag"] = encoder.fit_transform(data["tag"])
# data["main_tag"] = encoder.fit_transform(data["main_tag"])


# # Input/Output
# X = data.loc[:, data.columns != 'tag']
# Y = data.loc[:, data.columns == 'tag']

# # Train/Test data 
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(X, Y
#                                  , random_state=0
#                                  , train_size=0.7)

# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# print(y_train)
# print(pd.DataFrame(x_test).head())
# exit()
# # FIRST MODEL: LOGISTIC REGRESSION
# from sklearn.linear_model import LogisticRegression

# # Train and predict
# lr_model = LogisticRegression()
# lr_model.fit(x_train,y_train)
# y_predLR=lr_model.predict(x_test)

# # Metrics
# from sklearn import metrics
# lr_model_score=metrics.accuracy_score(y_test, y_predLR)

# # Confusion matrix
# import seaborn as sns
# from sklearn.metrics import confusion_matrix 
# conf = confusion_matrix(y_predLR, y_test) 
# print(conf)
# sns.heatmap(conf, square=True, annot=True, cbar=False
#             , xticklabels=list()
#             , yticklabels=list())
# plt.xlabel('valeurs prédites')
# plt.ylabel('valeurs réelles')