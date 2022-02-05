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

### Config file
rename ```src/configs/template.json``` to ```development.json``` and update the file with your data.

For the twitter section you must add your own bearer token in order to use the Twitter API.

### Run
To run the server type the following command in the root directory
```
yarn dev
```

## Run tests
To run tests type the following command in the root directory
```
yarn test
```

## Swagger - Open API
An Open API documentation is available at ```/api-docs``` endpoint.