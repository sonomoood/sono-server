# Sonomood server

## Install
First, clone this repository.
```
git clone https://github.com/sonomoood/sono-server.git
```
### Yarn
Sonomood uses [yarn](https://classic.yarnpkg.com/en/) as its dependency management tool so you need to install it and then run ```yarn install``` in the root directory of the project.
### Twitter API
Sonomood uses Twitter API so you need to get your own credential to use Sonomood, go to [Twitter API documention](https://developer.twitter.com/en/docs) for more.

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

### Run
To run the server type the following command in the root directory
```
yarn dev
```
## Database
We are using MongoDB as Sonoomod database, you can use it through [Docker](https://www.docker.com/).

Type ```docker-compose --profile seeds up``` to populate MongoDB with music data and type ```docker-compose up``` when you need to run MongoDB.
## Run tests
To run tests type the following command in the root directory
```
yarn test
```

## Swagger - Open API
An Open API documentation is available at ```/api-docs``` endpoint.