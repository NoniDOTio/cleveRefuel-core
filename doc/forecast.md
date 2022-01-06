> Zurück zur [Startseite](index.md)

# Forecasting

Die Forecasting Algorithmen bestimmten wie versucht werden soll den zukünftigen Preis vorherzusagen.

## Naive Forecasting
Beim Naive Forecasting werden alle Preise die über eine bestimmte Tankstelle bekannt sind kombiniert und der Durchschnitt wird berechnet. Dieser Ansatz ermöglicht die Einfachste Berechnung von Kosten nimmt aber nicht zukünftige Preissteigerungen, Tag/Nacht Preise und andere Faktoren.

## Brandwide Forecasting
Beim Brandwide Forecasting werden die Preise aller Tankstellen einer Bestimmten Marke zusammengerechnet und unter Verwendung der Tageszeit analysiert. Dabei werden die Tagespreise von den Nachtpreisen getrennt, wir gehen dabei davon aus das die "Nachtpreise" zwischen 18 und 6 uhr liegen.