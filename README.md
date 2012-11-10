# My Walkthrough of Django REST Framework Tutorial

Going through the [django-rest-framework][tut] tutorial.

   $ mkvirtualenv djangoRESTFramework
   $ workon djangoRESTFramework
   $ pip install markdown
   $ pip install pyyaml
   $ pip install -r ./virtualenv_rf_requirements.txt 
   $ pip install -r ./virtualenv_rf_optionals.txt 

   $ pip install -r ./virtualenv_tut_requirements.txt

   $ python ./manage.py startapp snippets

   $ curl -X GET http://localhost:8000/snippets/1/ -H "Accept: application/json; indent=4"
[tut]: http://django-rest-framework.org/tutorial/1-serialization.html