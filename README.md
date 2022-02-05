##  What is Sonomood?
<p>
Sonomood is a web app for digital music streaming.  

Based on user's tweets, this service detects the user's mood and suggests songs according to his mood.
</p>

## About Sonomood

### Twitter API
Sonomood uses Twitter API so you need to get your own credential to use Sonomood, go to [Twitter API documention](https://developer.twitter.com/en/docs) for more.

### Yarn
Sonomood uses [yarn](https://classic.yarnpkg.com/en/) as its dependency management tool so you need to install it and then run ```yarn install``` in the root directory of the project.


## How to start with Sonomood?
### Install
First, clone this repository.
```
git clone https://github.com/sonomoood/sono-server.git
```

To launch the backend (Dev Mode)
```bash
docker-compose up --build --force-recreate
```
### Config file
rename ```src/configs/template.json``` to ```development.json``` and update the file with your data.

For the twitter section you must add your own bearer token in order to use the Twitter API.

## ML Python service
[ML Service README](test-ml/README_ML.md)  

[URL in AWS](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-windows.html)

### Run tests
To run tests type
```bash
yarn test
```
### Test UI (Endpoints)
[http://localhost:3000/FeedSongMood](http://localhost:3000/healthcheck)

[http://localhost:3000/GetMoodFromTweets](http://localhost:3000/healthcheck)


### Swagger - Open API
[http://localhost:3000/api-docs](http://localhost:3000/api-docs)
