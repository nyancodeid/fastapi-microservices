## Install PIP
pip install -r requirements.txt

## Development Run
uvicorn app.main:app --reload

## Using Env
source ./env/bin/activate

## Exit Env
deactivate

## Compose Up
docker-compose up -d 

## Compose Down
docker-compose down

## Compose Log
docker-compose logs