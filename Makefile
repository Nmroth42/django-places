DEV_COMPILATION_PATH:="requirements/compilation/dev.txt"
PROD_COMPILATION_PATH:="requirements/compilation/prod.txt"

DEV_IN_PATH:="requirements/dev.in"
PROD_IN_PATH:="requirements/prod.in"

define br
		@echo ""
endef

define freezeprod
		pip freeze | grep -v "pkg-resources" > requirements.txt
endef

define freezedev
		pip freeze | grep -v "pkg-resources" > requirements.dev.txt
endef

help:
		@echo "devenv        - switch to dev env"
		@echo "prodenv       - switch to prod env"
		@echo "run           - python manage.py runserver"
		@echo "cast path=    - run flake8, autopep8, docformatter, unify, isort"
		@echo "mmigrate      - run makemigrations and migrate"

run:
		python manage.py runserver

devenv:
		pip install pip-tools
		$(br)
		pip-compile --output-file $(DEV_COMPILATION_PATH) $(DEV_IN_PATH)
		$(br)
		pip-sync $(DEV_COMPILATION_PATH)
		$(br)
		$(freezedev)
		$(br)
		pip list
		$(br)
		@echo "Venv has been switched to development mode!"

prodenv:
		pip install pip-tools
		$(br)
		pip-compile --output-file $(PROD_COMPILATION_PATH) $(PROD_IN_PATH)
		$(br)
		pip-sync $(PROD_COMPILATION_PATH)
		$(br)
		$(freezeprod)
		$(br)
		pip list
		$(br)
		@echo "Venv has been switched to production mode!"

cast:
		flake8 --exit-zero --count $(path)
		$(br)
		autopep8 $(path) --recursive -a -d
		$(br)
		autopep8 $(path) --recursive --in-place -a
		$(br)
		docformatter --in-place -r $(path)
		$(br)
		unify --in-place -r $(path)
		$(br)
		isort -rc $(path)

mmigrate:
	python manage.py makemigrations
	python manage.py migrate

static:
	python manage.py collectstatic --noinput --settings=settings.prod
