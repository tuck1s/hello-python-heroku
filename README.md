# Python: Hello World

A barebones app, which can easily be deployed to Heroku, using Flask / Gunicorn.

This application is based on [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article, but using Flask instead of Django.

Your app can be run locally using `flask` directly:

```sh
export FLASK_APP=hello.py
flask run
```

and will by default serve [localhost:5000](http://localhost:5000/)

## Deploying to Heroku

Heroku serves Flask via gunicorn.

```sh
heroku create
git push heroku master
heroku open
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
