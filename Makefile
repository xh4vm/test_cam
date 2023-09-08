# define standard colors
ifneq (,$(findstring xterm,${TERM}))
	BLACK        := $(shell printf "\033[30m")
	RED          := $(shell printf "\033[91m")
	GREEN        := $(shell printf "\033[92m")
	YELLOW       := $(shell printf "\033[33m")
	BLUE         := $(shell printf "\033[94m")
	PURPLE       := $(shell printf "\033[95m")
	ORANGE       := $(shell printf "\033[93m")
	WHITE        := $(shell printf "\033[97m")
	RESET        := $(shell printf "\033[00m")
else
	BLACK        := ""
	RED          := ""
	GREEN        := ""
	YELLOW       := ""
	BLUE         := ""
	PURPLE       := ""
	ORANGE       := ""
	WHITE        := ""
	RESET        := ""
endif

define log
	@echo ""
	@echo "${WHITE}----------------------------------------${RESET}"
	@echo "${BLUE}[+] $(1)${RESET}"
	@echo "${WHITE}----------------------------------------${RESET}"
endef

.PHONY: interactive build grad services
run: poetry-install-build collectstatic build-dockers

.PHONY: clean all docker images and pyc-files
clean-all: clean-pyc clean-all-dockers

.PHONY: django migrations
migrate: poetry-install-build migrate-run 

.PHONY: potery install build to venv
poetry-install-build:
	$(call log,Poetry installing packages)
	poetry install

.PHONY: interactive build docker services
build-dockers:
	$(call log,Build containers)
	docker-compose up --build

.PHONY: collect static files
collectstatic:
	poetry run python3 app/manage.py collectstatic --noinput

.PHONY: clean-pyc
clean-pyc:
	$(call log,Run cleaning pyc and pyo files recursively)
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: run django migrations
migrate-run:
	$(call log,Run django migrations)
	docker exec -it app python3 /opt/app/manage.py migrate

.PHONY: clean all docker images
clean-all-dockers:
	$(call log,Run stop remove and cleaning memory)
	T=$$(docker ps -q); docker stop $$T; docker rm $$T; docker container prune -f
