## Django project that uses:
- Django Rest Framework
- Redis
- Celery
- Docker
- Postgres

## How to run:
- Clone the repo
- Run `docker-compose up -d --build`
- Go to [http://localhost:8000/](localhost:8000)

## TODO:
- [ ] Add tests
- [ ] Migration to Postgres must be done automatically.
- [ ] Add cron job to update and save stock prices to the database.