# RedTurtle Calcio Balilla

- python3
- django 2


    virtualenv .
    . bin/activate
    pip install -r requirements.txt

    cd rtcbproj

    cp rtcbproj/config/omissis.py.template rtcbproj/config/omissis.py


    vi rtcbproj/config/omissis.py


Compilate la variabile `SECRET_KEY` con una stringa casuae molto lunga.


Proseguite con:

    python manage.py makemigrations rtcb
    python manage.py migrate
    python manage.py runserver
