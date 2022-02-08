from types import NoneType
import lyricsgenius as lg
import pandas as pd
import urllib3, socket
from urllib3.connection import HTTPConnection
from requests.exceptions import Timeout

HTTPConnection.default_socket_options = ( 
    HTTPConnection.default_socket_options + [
    (socket.SOL_SOCKET, socket.SO_SNDBUF, 100000000),
    (socket.SOL_SOCKET, socket.SO_RCVBUF, 100000000)])

pd.set_option('display.max_colwidth', None)
data = pd.read_csv("muse_v3.csv")
data = data.drop(columns=['lastfm_url', 'spotify_id','mbid'])
data = data[0:5000]

genius = lg.Genius('1b7jhgZeKGwiDL3cYx9UN8dIwjTrniZwYZby7FXH_JcXAUUnunzHS3j07K5J3Iet', remove_section_headers=True, skip_non_songs=True)
genius.timeout = 15
lyrics = list()
for i in range(0,len(data)):
    retries = 0
    while retries < 3:
        try:
           song = genius.search_song(data.iloc[i]['track'],data.iloc[i]['artist'])
        except Timeout as e:
            retries += 1
            continue
        if song is not None:
            song.lyrics = ' '.join(song.lyrics.splitlines()).replace(',', ' ')
            lyrics.append(song.lyrics)
        else:
            lyrics.append('NAN')
        break

data.insert(len(data.columns), 'Lyrics', lyrics)

# #export to csv
data.to_csv("lyrics.csv", index=False, encoding='utf-8-sig')
