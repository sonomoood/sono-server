### Dataset provenance
[https://www.kaggle.com](https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres?select=lyrics-data.csv)

A) To list running docker images use:
-------------------------------------
```bash
$ docker ps
```

B) Test the service:
--------------------
Just give a text to the end point to get label. 
```bash
$ echo $(curl http://localhost:4000 -d 'I am so happy to be home tonight' --silent)
# >> happy
```

C) Tag lyrics:
--------------
If we wanted to tag a big text content using curl command, we would use a file containing that text.
```bash
For example send the file test_song1.txt
$ echo $(curl http://localhost:4000 -d '@test_song1.txt' --silent)
# >> happy
```
