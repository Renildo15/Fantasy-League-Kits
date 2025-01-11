#formata o código
format:
	black .
	isort .
#roda as migrations
migrate:
	python manage.py makemigrations
	python manage.py migrate
#executa o servidor
server:
	python manage.py runserver 192.168.1.13:8000

admin:
	python manage.py initadmin

add-dependencies:
	pip freeze > requirements.txt

dependencies:
	pip install -r requirements.txt

#rodar os testes com o pytest e gerar relatório de cobertura
coverage:
	coverage run -m pytest
	coverage report
	coverage html