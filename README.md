# LernplatzReservierer

Ein kleines Skript, welches einem den lieblings UB Lernplatz in der Klausurenphase garantieren soll.

## Benutzung

pass arguments as callparameter from a terminal:
<br>
<br>
py script.py $UB_NUMMER $PASSWORT_KOMBINATION $VORNAME $NACHNAME $TELEFONUMMER
<br>

login data via launch.json args:
<br>
<br>
"args": [<br>
>$UB_NUMMER, $PASSWORT_KOMBINATION,<br>
>$VORNAME, $NACHNAME,<br>
>$TELEFONUMMER<br>
]
