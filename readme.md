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

## Endpoints:
- [http://localhost:8000/](localhost:8000) - Home page
- [http://localhost:8000/coin-list/](localhost:8000/coin-list/) - List of coins in database
- [http://localhost:8000/add-coin/?symbol=ETH](localhost:8000/add-coin/?symbol=ETH) - Add coin to track and save to database.
- [http://localhost:8000/show-price/?symbol=ETH](localhost:8000/show-price/?symbol=ETH) - Get price of coin from database.
## TODO:
- [ ] Add tests
- [x] Migration to Postgres must be done automatically.
- [x] Add cron job to update and save stock prices to the database.
- [ ] Add redis cache for stock prices. 