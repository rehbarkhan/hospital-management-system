.PHONY: run
run:
	python manage.py init_group
	python manage.py runserver 0.0.0.0:8080