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


Compilate la variabile `SECRET_KEY` con una stringa alfanumerica casuale
molto lunga.


Proseguite con:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


### DB

Attualmente non c'è bisogno di nessuna configurazione per il database. Il
progetto è configurato per utilizzare un db sqlite3 (vedi i settings).


## Modelli

### User

Il modello custom dell'utente (presente in `rtcb.authentication.models`) è
quello che rappresenta il nostro player.

Oltre ad avere uno username (e una password) ha anche altri due campi utili al
nostro progetto: `role` e `versatile`.

`role` specifica il ruolo preferito dal giocatore (che può essere Striker o
Defender) mentre `versatile` indica se il giocatore è disposto anche a giocare
nel ruolo opposto al preferito. Questi valori verranno usati nella generazione
automatica delle squadre.


## Script - comandi da poter utilizzare

### populate

Questo è uno script che popola il db con alcuni oggetti per testare l'applicativo.

    python manage.py populate


### blastdb

**Questo script server per resettare il db dell'applicativo!** Non usarlo se si
hanno dei dati che non si vogliono perdere.


È scritto specificatamente per eliminare solo il db sqlite3 (quindi un altro
database non verrebbe eliminato). Cancella anche tutti i file delle migrazioni
dell'applicazione `rtcb`! **Non è reversibile**.

    python manage.py blastdb


## TODO

[] Generazione automatica delle squadre in base ai ruoli preferiti
[] Generazione automatica dei turni
