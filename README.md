# Project Title

Django REST API for fetching soccer data.

## Description

An API built using DRF to scrape Football players and teams statistics from Api-Football-Beta and save it into a Postgres database. It uses a customized scraper to fetch and save the data; Uses Celery task scheduler, with Redis as a broker, for fetching and saving these data. Also, the project has a logging and Redis cache setup; in addition to, Sentry error tracking system. The main purpose of the project was to provide a Python Django interface, for fetching soccer statistics, to be used as a backend in custom projects.
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
docker-compose exec web python manage.py makemigrations api
```
* run 
```
docker-compose exec web python manage.py migrate
```
* use django project shell to run scraping tests using scraping-example.py


## Scraper UML Class Diagram

![scraper UML](https://github.com/MohAyman3600/soccer_data_DRF/blob/master/Scraper_UML_Class_Diagram.png)


## Authors

[@Mohamed Ayman](https://www.linkedin.com/in/mohayman3600/)


## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details


