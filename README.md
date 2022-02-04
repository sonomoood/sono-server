##  What is Sonomood?
<p>
Sonomood is a web app for digital music streaming.  

Based on user tweets, this application detects the user's mood and suggests songs according to his mood.
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

### Test UI (Endpoints)
[http://localhost:3000/FeedSongMood](http://localhost:3000/healthcheck)  

[http://localhost:3000/GetMoodFromTweets](http://localhost:3000/healthcheck)  



### API docs
[http://localhost:3000/api-docs/#/](http://localhost:3000/api-docs/#/)


