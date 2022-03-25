-include .env
export

dev.install:
	@poetry install
lint:
	@mypy frontend
	@flake8 frontend
run:
	@python -m frontend

db.run:
	@docker-compose up -d db

db.create:
	@python -m frontend.models

db.stop:
	@docker-compose stop db

stop:
	@docker-compose stop -t 1

clean:
	@docker-compose down
