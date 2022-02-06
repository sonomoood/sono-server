
### Dataset provenance
[https://www.kaggle.com](https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres?select=lyrics-data.csv)

A) To run ML Python service:
----------------------------

Use the specific docker compose file using this command
```bash
$ docker-compose -f docker-compose-ML.yml up --build --force-recreate -d
```

B) To list running Docker images use:
-------------------------------------
```bash
$ docker ps
```

C) Test the service:
--------------------
Just give a text to the end point to get label.
```bash
$ echo $(curl http://localhost:4000 -d 'I am so happy to be home tonight' --silent)
# >> happy
```

D) Words recognition:
---------------------
Current ML implementation is based upon word recognition to tag text.
If no word is recognize within the text, so the engine returns an error message.
```bash
For example:
$ echo $(curl http://localhost:4000 -d 'some unrecognizable text' --silent)
# >> Unrecognized text content. Plase provide some known words.
```

E) Tag lyrics:
--------------
If we wanted to tag a big text content using curl command, we would use a file containing that text.
```bash
For example send the file test_song1.txt
$ echo $(curl http://localhost:4000 -d '@test_song1.txt' --silent)
# >> happy
```
