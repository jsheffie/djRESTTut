# My Walkthrough of Django REST Framework Tutorial

Going through the [django-rest-framework][tut] tutorial.

## Set up VirtualEnv
- $ mkvirtualenv djangoRESTFramework
- $ workon djangoRESTFramework
- $ pip install markdown
- $ pip install pyyaml
- $ pip install -r ./virtualenv_rf_requirements.txt 
- $ pip install -r ./virtualenv_rf_optionals.txt 

- $ pip install -r ./virtualenv_tut_requirements.txt

- $ python ./manage.py startapp snippets

## A sample Query
- [snippets][snip1]
- [snippets/1/][snip2]
- [snippets/1/?format=json][snip3]
- $ curl -X GET http://localhost:8000/snippets/1/ -H "Accept: application/json; indent=4"

[snip1]: http://localhost:8000/snippets/
[snip2]: http://localhost:8000/snippets/1/
[snip3]: http://localhost:8000/snippets/1/?format=json
[tut]: http://django-rest-framework.org/tutorial/1-serialization.html