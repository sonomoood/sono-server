##  What is Sonomood?
<p>
Sonomood is a web app for digital music streaming.  

Based on user preferences, this application detects the user's mood and suggests songs according to his mood.
</p>

## How to start with Sonomood?
To launch the backend (Dev Mode)
```bash
docker-compose up --build --force-recreate
```

### Run tests
To run tests type
```bash
yarn test
```
### Dataset provenance
[https://www.kaggle.com](https://www.kaggle.com/neisse/scrapped-lyrics-from-6-genres?select=lyrics-data.csv)

### Test UI
[http://localhost:3000/healthcheck](http://localhost:3000/healthcheck)
[http://localhost:3000/getSongsByMood](http://localhost:3000/healthcheck)
[http://localhost:3000/classifyNewSong](http://localhost:3000/healthcheck)

### API docs
[http://localhost:3000/api-docs/#/](http://localhost:3000/api-docs/#/)


### Test dico (for developers)
To install ts-node (see : dataset/help.txt)
```bash
ts-node create-dico.ts > out.txt
``` 

