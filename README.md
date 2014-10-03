survivalguide
=============
Basic django app following 
http://gswd-a-crash-course-pycon-2014.readthedocs.org/


NOTE: I'm using here Django 1.7 and Python 3.3.

- no __unicode__ definition: use __str__

- no south install

- after creating the model of the talks app
    add 'talks' to INSTALLED_APPS
- run
    ./manage.py makemigrations talks
- and
    ./manage.py migrate
