# Intelitank

[Aufgabenstellung](intellitank.pdf)

> Abgabe von Nils Schulz und Arne Perschke

# Installation dieser Implementierung

Zur Verwendung der Implementierung wird Python3 mit einigen zusätzlichen Modulen verwendet. Zur Installation als aller erstes Python3 Von der Website herunterladen:

https://www.python.org/downloads/

Nachdem Python installiert ist müssen wir noch die Zusätzlichen Module installieren. Dafür einfach eine Eingabeaufforderung im Projektverzeichnis öffnen und den folgenden Befehl ausführen:

`pip install -r requirements.txt`

Danach sollten alle benötigten dependencies installiert sein und das Programm kann ausgeführt werden.

## Installation des Erweiterten Datensatzes
Das Repo kommt mit einem minimierten Datensatz der das ausführen der Anwendung ermöglicht. Bei Bedarf kann der komplette Datensatz der Informaticup Aufgabe (~3.5Gb) heruntergeladen werden. Mit dem größeren Datensatz ist die Ermittelte Tankstrategie genauer allerdings hat der Algorithmus je nach Optimierungsstrategie auch eine deutlich längere Laufzeit.

Zum Herunterladen den root ordner öffnen und den folgenden Befehl ausführen:

`git submodule update --init`

Das Programm verwendet Beim ausführen dann automatisch den erweiterten Datensatz.

Wenn der Erweiterte Datensatz wieder deinstalliert werden soll kann `git submodule deinit --all` benutzt werden

## Zusätzliche Routen hinzufügen
Das Repository kommt mit zwei vorgefertigten Routen, bei bedarf können weitere Routen im Ordner `data/Fahrzeugrouten` hinzugefügt werden. Die Routen werden beim ausführen des Programms automatisch eingelesen und können dann vom Nutzer ausgewählt werden.

# Programm Ausführen

Zum Staren des Programms eine Eingabeaufforderung im geklonten Ordner öffnen und das Programm wie folgt starten:

`python clever-refuel-core`

Nach dem Start wird dir ein Menu angezeigt in welchem du die zu verarbeitende Route sowie die Vorhersagemethode auswählen kannst.


# Weitere Dokumentation
Tiefere Dokumentation kann [hier](doc/index.md) gefunden werden

