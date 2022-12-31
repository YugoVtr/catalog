.PHONY: run

default: run

run:
	scrapy crawl -L WARNING r44goiania

requirements:
	pip freeze > requirements.txt

venv:
	python -m venv .venv
	source .venv/bin/activate
	pip install --no-cache-dir -r requirements.txt

mongo:
	docker-compose up -d mongo-express
