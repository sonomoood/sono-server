FROM mongo:latest

COPY music.json .

CMD mongoimport -d sonomood -c musics --uri=mongodb://mongodb:27017  --drop --jsonArray music.json
