run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

user:
	python manage.py createsuperuser
	python manage.py runserver

push:
	git add .
	git commit -m "update" 
	git push origin main --force
	python manage.py runserver

pull:
	git pull origin main
	python manage.py runserver