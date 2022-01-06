# Tankstrategien



## Naive Tankstrategie

Die naive Tankstrategie beschreibt einen simplen, unoptimierten Ansatz zu Tanken. Hierbei wird immer dann vollgetankt, wenn der Treibstoff nicht mehr bis zur nächsten Tankstelle reichen würde. Wenn das Ziel mit weniger als einer vollen Betankung erreichbar ist, wird nur so viel getankt um am Zielort anzukommen.
Dieser Algorithmus soll das Tankverhalten einer Person, welche sich keine Gedanken über eine kosteneffiziente Betankung ihres Fahrzeugs macht, repräsentieren.

## Fixed Path Gas Station Algorithmus

Das Fixed Path Gas Station Problem beschreibt die Aufgabenstellung, für einen festgelegte Route die günstigste Art zu Tanken zu berechnen. Gegeben ist eine limitierte Tankgröße und Kraftstoffpreise and den Knotenpunkten des Pfads.
Weitere Informationen und verschiedene Lösungsansätzen zu dem Problem sind [hier]() weiter erläutert.

In unserem Fall, werden die möglichen Tankstops einer Fahrzeugroute rückwärts durchlaufen, beginnend mit dem letzten Stop, also dem Ziel der Route. Hiervon ausgehend werden alle folgenden Tankstops analysiert, bis sie nicht mehr mit der aktuellen Tankfüllung erreicht werden können. Aus den untersuchten Tankstops, wird dann jener, mit dem günstigsten Kraftstoffpreis angefahren. Ausgehend von neuen Stop wiederholt sich der Algorithmus dann immer wieder - solange, bis die Fahrzeugoute abgeschlossen ist.