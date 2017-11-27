.PHONY: help bootstrap clean-pyc clean lint test coverage docs

help:
	@echo "api - run the api"
	@echo "front - run the frontend"

api:
	apistar run