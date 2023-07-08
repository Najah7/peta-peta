.PHONY:
	app test migrate pro admin django react 

app:
	docker-compose run --rm app sh -c "python manage.py startapp api"

migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations --settings app.dev_settings"
	docker-compose run --rm app sh -c "python manage.py migrate --settings app.dev_settings"

admin:
	docker-compose run --rm app sh -c "python manage.py createsuperuser --settings app.dev_settings"

django:
	docker-compose run --rm app sh -c "django-admin startproject app ."

next:
	docker-compose run --rm next sh -c "npx create-next-app . --ts"

django-test:
	docker-compose run --rm app sh -c "python manage.py test --settings app.dev_settings"

