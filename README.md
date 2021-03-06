## About Sonomood
<p>
Sonomood is a web app for digital music streaming.  

Based on user's tweets, this service detects the user's mood and suggests songs according to his mood.
</p>  

### - Twitter API
Sonomood uses Twitter API so you need to get your own credential to use Sonomood, go to [Twitter API documention](https://developer.twitter.com/en/docs) for more.

### - Yarn
Sonomood uses [yarn](https://classic.yarnpkg.com/en/) as its dependency management tool so you need to install it and then run ```yarn install``` in the root directory of the project.


## How to start with Sonomood?
### - Install
First, clone this repository.
```
git clone https://github.com/sonomoood/sono-server.git
```
### Config files
Add the file ```src/configs/local.json``` with a twitter section and your own bearer token in order to use the Twitter API.
```json
//src/configs/local.json
{
    "twitter": {
        "bearerToken": "YOUR BEARER TOKEN HERE"
    }
}
```
More information on configuration files [here.](https://github.com/lorenwest/node-config/wiki/Configuration-Files)

### - To launch the backend (Dev Mode)
```bash
docker-compose up --build --force-recreate
```

## ML Python service
The labeling service is started in a Docker on Amazon and accessible from anywhere with the address : ```IP: 13.38.65.157```  
[URL at Amazon](http://13.38.65.157:4000)  

You can test with the curl command: 
```bash
echo $(curl http://13.38.65.157:4000 -d 'Hello my friends.' -s)
```

To use the service, please read the README first  
[ML Service README](test-ml/README_ML.md)

## Database
We are using MongoDB as Sonoomod database, you can use it through [Docker](https://www.docker.com/).

Type ```docker-compose --profile seeds up --force-recreate --build``` to populate MongoDB with music data and type ```docker-compose up``` when you need to run MongoDB.

docker-composer version 1.28 or above is needed for "profiles" option to work.

### Run tests
To run tests type the following command in the root directory
```
yarn test
```

### Test UI (Endpoints)
[http://localhost:3000/FeedSongMood](http://localhost:3000/healthcheck)

[http://localhost:3000/GetMoodFromTweets](http://localhost:3000/healthcheck)


### Swagger - Open API
An Open API documentation is available at ```/api-docs``` endpoint.
