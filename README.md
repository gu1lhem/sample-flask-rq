# sample-flask-rq

Sample Flask project with redis queue and a logger. Written from [this tutorial](https://realpython.com/flask-by-example-implementing-a-redis-task-queue/) and [this StackOverflow thread](https://stackoverflow.com/questions/63824888/how-to-use-python-logging-with-redis-worker).

## Installation

Create a simple Heroku app.

Define `SONAR_TOKEN` for the CI, and `HEROKU_API_KEY`, `HEROKU_APP_NAME` and `HEROKU_EMAIL` in the repo's secrets for the CD.

Install [Redis To Go](https://elements.heroku.com/addons/redistogo) to the app.

Clone, crete a virtual environment and install the dependencies.

``` bash
python3 -m venv env
. env/bin/activate
pip install wheel setuptools
pip install -r requirements.txt
```

For development, create .env file from .env.sample and configure it

``` bash
cp .env.sample
```

The environment variable REDISTOGO_URL is automatically set up by Heroku when getting the add-on.

## TODO

https://stackoverflow.com/questions/39924325/redis-management-on-heroku
 or https://elements.heroku.com/addons/heroku-redis (the fre-tier of the second is better but I am currently using Redis to go).
