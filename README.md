# RedTurtle Calcio Balilla

Il Progetto si basa su:
- python 3
- django 2
- GraphQL


## Start working on the project

    virtualenv .
    . bin/activate
    pip install -r requirements.txt

    cd rtcbproj

    cp rtcbproj/config/omissis.py.template rtcbproj/config/omissis.py

    vi rtcbproj/config/omissis.py


Compilate la variabile `SECRET_KEY` con una stringa casuae molto lunga.


Proseguite con:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


### DB

Attualmente non c'è bisogno di nessuna configurazione per il database. Il
progetto è configurato per utilizzare un db sqlite3 (vedi i settings).
