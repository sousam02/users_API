

﻿
# Users API

This API was built using a great python framework: `Flask`, together with a `PostgreSQL` database.

The API main sections are `Models/`, `Controllers/` and `Repositories/`

## This API was built with
- Python 3.11 (https://www.python.org/downloads/release/python-3116/)

# Steps to configure enviroment

## Clone the repository with this command:
	git clone https://github.com/sousam02/users_API.git

## Creating virtual enviroment
After you clone, go to users_API folder with command line and set the virtual enviroment to avoid dependencies conflicts

    python -m venv .venv
    
## Activating virtual enviroment 
	(WINDOWS) .venv\Scripts\activate
	(LINUX) source .venv/bin/activate

## Installing dependencies

    pip install -r requirements.txt

# Configuring Docker and PostgreSQL

## Download docker
- https://docs.docker.com/compose/

## Download Postgres Image
After the Docker download, you are able to use docker commands. For the api, we need to download the PostgreSQL image. Go to command prompt and execute:

    docker pull postgres

## Create a new container

    docker run --name pg -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres

## Activating container

    docker start pg

## Connect to bash

    docker exec -it pg bash

## Connect to PostgreSQL
- After you connected to bash, you will see something like this:
- `root@8b288ff4a8e8:/#`
- Now you need to connect to PostgreSQL, execute this command:

		psql -U root
- You will see this:
- `root=#`

## Create `registrations` database and UUID extension
Now you can execute SQL queries to PostgreSQL, you will create the database that API will use.

    CREATE  DATABASE  registrations;


## Connect to the new database

    \c registrations

## Create table `users`
We will use UUID, so we need to use the extension that implements it, and then create users table. Paste this code on command prompt:

    CREATE EXTENSION IF  NOT  EXISTS "uuid-ossp";

    CREATE  TABLE  users (
    	id UUID NOT NULL  UNIQUE  DEFAULT uuid_generate_v4(),
    	name  VARCHAR  NOT NULL,
    	cpf VARCHAR  NOT NULL,
    	age VARCHAR  NOT NULL
    );

## Now you are able to consume the API
- Navigate to users_API folder and execute `flask run`

# Code structure
## The project is separated in 3 main folders
- `controllers/` is the folder that is responsible for the API business rules. For example, verify if a CPF already exists when trying to create a new user, or verify if all required fields are set.
- `models/` is the folder where is stored the classes that represent the API entities and logic. In our case we have Users and Database models.
- `repositories/` is the folder responsible to interact with the database, if we need to change the database, the business rules will be protected of these changes.
- `app.py` is in the root of project, and contains the API endpoints to users (Create, Read, Update, Delete and Get user by id)

# REST API

The REST API to the example app is described below.

## Get list of users

### Request

`GET /users`

    curl -X GET http://127.0.0.1:5000/users

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:43:39 GMT
    Content-Type: application/json
    Content-Length: 86
    Connection: close

    []

## Create a new user

### Request

`POST /users`

    (WINDOWS) curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Moises\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users
	
	(LINUX) curl -X POST -H "Content-Type: application/json" -d '{"name":"Moises", "cpf":"99999999999", "age":21}' http://127.0.0.1:5000/users


### Response

    HTTP/1.1 201 CREATED
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:22:57 GMT
    Content-Type: application/json
    Content-Length: 70
    Connection: close

    {"age": 28, "cpf": "10316782807", "id": dab9edf5-f3e1-4888-8c45-80f63542bd45, "name": "Maria"}

## Get user by id

### Request

`GET /users/id`

    curl -X GET http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:26:47 GMT
    Content-Type: application/json
    Content-Length: 70

    {"age": 28,"cpf": "10316782807","id": dab9edf5-f3e1-4888-8c45-80f63542bd45, "name": "Maria"}

## Get a non-existent user

### Request

`GET /users/id`

    curl -X GET http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:29:37 GMT
    Content-Type: application/json
    Content-Length: 32

    {"error":"User not found"}

## Update user informations

### Request

`PUT /users/:id`

    (WINDOWS) curl -X PUT -H "Content-Type: application/json" -d "{\"name\":\"Moises Ferreira\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45
    
    (LINUX) curl -X PUT -H "Content-Type: application/json" -d '{"name":"Moises Ferreira", "cpf":"99999999999", "age":21}' http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45


### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:34:17 GMT
    Content-Type: application/json
    Content-Length: 82

    {"age": 21,"cpf": "99999999999","id": dab9edf5-f3e1-4888-8c45-80f63542bd45,"name": "Moises Ferreira"}

## Attempt to change a user that don't exists

### Request

`PUT /thing/:id`

    curl -X PUT -H "Content-Type: application/json" -d "{\"name\":\"Moises Ferreira\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:37:39 GMT
    Content-Type: application/json
    Content-Length: 32
    Connection: close

    {"error": "User not Found"}

## Delete a user

### Request

`DELETE /user/id`

    curl -X DELETE http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45

### Response

    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:40:03 GMT
    Content-Type: application/json
    Connection: close

## Try to delete same user again

### Request

`DELETE /user/id`

    curl -X DELETE http://127.0.0.1:5000/users/dab9edf5-f3e1-4888-8c45-80f63542bd45

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:41:06 GMT
    Content-Type: application/json
    Content-Length: 32
    Connection: close

    {"error": "User not Found"}
