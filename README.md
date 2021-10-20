# Comex Backend

A REST API to access data from the Exterior Commerce from Brazil for the last 3 years.

## Setting up the database

We convert the 3 csv files to a postgres database. Check the makefile and change the command according to your files paths.
To setup the development database:
```bash
make setup-dev-db
```

## Download new comex data

The app command `download` downloads data from the last 3 years and saves it to a csv file.

```bash
python -m app download <output-file-path>
```

## Running the app

After everything is setup, run the command and access the url <http://localhost:8000/docs>:
```bash
make run-dev
```

## Development

A `devcontainer` is available with all the configurations for the development environment.

## Deploy
To setup the app for the first time, do the following:

Create the heroku app:
```bash
heroku create <app-name>
```
Configure the following environment variables
Set the environment to production:
```bash
heroku config:set APP_ENV=prod
```
Add the database, also created database url:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```
Add the heroku remote:
```bash
heroku git:remote -a <app-name>
```
Push the app to heroku:
```
git push heroku main
```

After the app is setup, run the command to populate the database. Check the makefile and change the command according to your files paths:
```bash
make setup-heroku-db
```
