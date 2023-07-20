## Django project that uses:
- Django Rest Framework
- Redis
- Celery
- Docker
- Postgres
- yfinance library (unofficial Yahoo Finance API)

## How to run:
- Clone the repo
- Run `docker-compose up --build`
- Run `docker-compose exec django python manage.py makemigrations stock_price`
- Run `docker-compose exec django python manage.py migrate stock_price`
- Go to [http://localhost:8000/](localhost:8000)

## TODO:
- [ ] Add tests
- [ ] Migration to Postgres must be done automatically.
- [ ] Add cron job to update and save stock prices to the database.