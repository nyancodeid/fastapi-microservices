# Microservice in Python using FastAPI + Postgresql
Building simple microservices with Python

[https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc](https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc)

## Running on Docker
Running on docker using docker-compose

```shell
$ sudo docker-compose up -d
```

## Development
by default this project using `vertualenv` so first, setup env.

```shell
$ virtualenv env
# activate `virtualenv`
$ source ./env/bin/activate
# install pip requirements
$ pip install -r requirements.txt
```

Start development server

```shell
$ uvicorn app.main:app --reload
```

## cURL Tests
### Create Casts
```shell
curl --request POST \
  --url http://localhost:8080/api/v1/casts \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"Ryan Aunur","nationality":"Indonesia"}'
```

### Create Movie
```shell
curl --request POST \
  --url http://localhost:8080/api/v1/movies \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"name":"Iron Man: 1","plot":"This is dummy plot","genres":["Action","Adventure","Fantasy"],"casts_id":[1]}'
```

### Get All Movies
```shell
curl --request GET \
  --url http://localhost:8080/api/v1/movies \
  --header 'accept: application/json'
```