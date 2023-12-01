# Users API

This API was built using a great python framework: `Flask`, together with a `PostgreSQL` database.

The API main sections are `Models/`, `Controllers/` and `Repositories/`

## Creating virtual enviroment

    python -m venv .venv
    .venv\Scripts\activate

## Installing dependencies

    pip install -r requirements.txt

# Configuring Docker and PostgreSQL

## Download Postgres Image

    docker pull postgres

## Create a new container

    docker run --name pg -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres

## Activating container

    docker start pg

## Connect to bash

    docker exec -it pg bash

## Connect to PostgreSQL

    psql -U root

## Create `registrations` database and UUID extension

    CREATE  DATABASE  registrations;
    CREATE EXTENSION IF  NOT  EXISTS "uuid-ossp";

## Connect to the new database

    \c registrations

## Create table `users`

    CREATE  TABLE  users (
    	id UUID NOT NULL  UNIQUE  DEFAULT uuid_generate_v4(),
    	name  VARCHAR  NOT NULL,
    	cpf VARCHAR  NOT NULL,
    	age VARCHAR  NOT NULL
    );

## Now you are able to consume the API

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

    curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Moises\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users

### Response

    HTTP/1.1 201 CREATED
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:22:57 GMT
    Content-Type: application/json
    Content-Length: 70
    Connection: close

    {"age": 28, "cpf": "10316782807", "id": 1, "name": "Maria"}

## Get user by id

### Request

`GET /users/id`

    curl -X GET http://127.0.0.1:5000/users/1

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:26:47 GMT
    Content-Type: application/json
    Content-Length: 70

    {"age": 28,"cpf": "10316782807","id": 1, "name": "Maria"}

## Get a non-existent user

### Request

`GET /users/id`

    curl -X GET http://127.0.0.1:5000/users/9999

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

    curl -X PUT -H "Content-Type: application/json" -d "{\"name\":\"Moises Ferreira\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users/1

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:34:17 GMT
    Content-Type: application/json
    Content-Length: 82

    {"age": 21,"cpf": "99999999999","id": 1,"name": "Moises Ferreira"}

## Attempt to change a user that don't exists

### Request

`PUT /thing/:id`

    curl -X PUT -H "Content-Type: application/json" -d "{\"name\":\"Moises Ferreira\", \"cpf\":\"99999999999\", \"age\":\"21\"}" http://127.0.0.1:5000/users/9999

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

    curl -X DELETE http://127.0.0.1:5000/users/1

### Response

    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:40:03 GMT
    Content-Type: application/json
    Connection: close

## Try to delete same user again

### Request

`DELETE /user/id`

    curl -X DELETE http://127.0.0.1:5000/users/1

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.1 Python/3.12.0
    Date: Thu, 30 Nov 2023 22:41:06 GMT
    Content-Type: application/json
    Content-Length: 32
    Connection: close

    {"error": "User not Found"}
