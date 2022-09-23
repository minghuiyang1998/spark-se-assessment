# Flask JWT Auth

## Quick Start

### Basics

1. Activate a virtualenv : 
   1. python3 -m venv venv
   2. . venv/bin/activate
   3. pip install Flask
2. Install the requirements: 
   1. install postgresql frist: brew install postgresql
   2. pip install -r requirements.txt

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export FLASK_APP=project.server
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export FLASK_APP=project.server
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

Create the tables and run the migrations:

```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```
deactivate
pip uninstall flask
source venv/bin/activate

### Run the Application

```sh
$ flask run
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ flask run --host=0.0.0.0 --port=5000
> ```
