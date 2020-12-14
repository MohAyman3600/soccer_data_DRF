# Project Title

Django REST API foor fetching soccer data.

## Description

An API which was built using DRF to scrape Football players and teams statitics from [Api-Football-Beta](https://rapidapi.com/api-sports/api/api-football-beta) and save it into a Postgres database.
It uses a customized scraper to fetch and save the data; Uses Celery task scheduler, with Redis as broker, for fetching and saving these data.
Also, the project has logging and redis cache setup; in addition to, Sentry error tracking system.
The main purpose of the project was to provide a Python Django interface, for fetching soccer statistics, to be used as backend in custom projects.

## Getting Started

### Dependencies

* Docker & Docker Compose
* Python 3

### Installing

* Clone the project
* define the environment variables in .env file

### Executing program

* run 
```
docker-compose up --build -d
```
* run 
```
docker-compose exec web python manage makemigrations api
```
* run 
```
docker-compose exec web python manage migrate
```
* use django project shell to run scraping tests using scraping-example.py


## Authors

Contributors names and contact info

Mohamed Ayman


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [mit] License - see the LICENSE.md file for details


