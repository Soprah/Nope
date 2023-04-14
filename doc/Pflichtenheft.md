# Anforderungs- und Entwurfsspezifikation (“Pflichtenheft”)

# 1 Einführung
## 1.1 Beschreibung
Es soll das Kartenspiel "Nope" implementiert werden inklusive simulierte Spieler die automatisch strategische Züge ausführen
## 1.2 Ziele
- Das Spiel soll über eine Verteilte Systemarchitektur verfügen:
    - Dabei wird es aufgeteilt in Form einer Client-Server-Architektur
    - Mehrere Spieler können sich über das Netzwerk verbinden um gegeneinander zu spielen
    - Es können mehrere Runden des Spiels gleichzeitig gespielt werden
 - Zielbenutzergruppe:
    - Dozenten und Studenten, welche im Modul Softwareprojekt involviert sind
# 2 Anforderungen
## 2.1 Stakeholder
| Funktion / Relevanz | Name | Kontakt / Verfügbarkeit | Wissen | Interessen / Ziele |
| --- | --- | --- | --- | --- |
| Benutzer der Software | Name des Spielers |  |  |  |
| Benutzer der Software | Name der KI |  |  |  |
## 2.2 Funktionale Anforderungen
Aus dem Regelwerk von Nope lassen sich folgende Anforderungen ableiten:
- Ein Spieler schickt dem Server zur Anmeldung eine Nachricht. Als Antwort bekommt dieser eine Session ID. Anhand der Session ID ist zu erkennen ob der Spieler als erster an der Reiche ist. Alle Spieler mit einer gültigen Session ID können nun dem Server mitteilen dass Sie eine Karten ziehen möchte. Dies erfolgt einzeln für jede Karte. Wenn der erste Spieler genug Karten auf der Hand hat, kann er nun den Server mitteilen dass er die Oberste Karte auf dem Ablagestapel sehen möchte. Der Server schickt daraufhin die entsprechende Information und stoppt dabei die Zeit. Wenn der Spieler mehr als 10 Sekunden für seien Zug braucht ist diese ungültig und der Spieler hat verloren. Wenn der Zug innerhalb der Frist erfolgt dann prüft der Server ob dieser gültig ist. Bei einem ungültigen Zug hat der Spieler ebenfalls verloren. Bei einem gültigen Zug wandert die gelegte Karte auf die oberste Position des Ablagestapels. Dem folgenden Spieler, welcher anhand seiner Session ID im Wartezustand ist, wird nun die Oberste Karte im Ablagestapel mitgeteilt und der Server prüft alle weiteren Züge wie vorher beschrieben.
## 2.3 Nicht-funktionale Anforderungen
### 2.3.1 Rahmenbedingungen
### 2.3.2 Betriebsbedingungen
### 2.3.3 Qualitätsmerkmale
## 2.4 Graphische Benutzerschnittstelle
Die Kommunikation mit dem Server soll für den Client zuerst über eine Textbasiert Oberfläche erfolgen. Im späteren Verlauf kann eine Webseite gestaltet werden, welche die Funktionalitäten erweitert.
Das Anzeizen der Karten auf der Hand erfolgt mit dem Text für die Bezeichnung der Farben gefolgt von der Nummer. Die einzelnen Karten werden mit einem Komma getrennt.
Das Auswählen einer Karte erfolgt mit der Angabe der Position auf der Hand. Neue Karten werden zu der Hand hinten angefügt.
## 2.5 Anforderungen im Detail
| Als | möchte ich | so dass | Akzeptanz |
| --- | --- | --- | --- |
| Benutzer | mich mit dem Server verbinden | in der Warteschlange für Nope warten kann |  |
| Benutzer | einem Spiel beitreten | mit einem weiteren Spieler Nope spielen kann |  |
| Benutzer | Karten aus dem Kartenstapel ziehen | sodass ich diese auf meine Hand ablegen kann |  |
| Benutzer | am Anfang solange Karten ziehen bis meine Hand voll ist | das Spiel beginnen kann |  |
| Benutzer | die oberste Karte auf dem Ablagestapel sehen | damit ich meinen Zug planen kann |  |
| Benutzer | bei Sonderkarten weitere Karten auf dem Ablagestapel einsehen | damit ich meinen Zug planen kann |  |
| Benutzer | Karten auf dem Ablagestapel ablegen | der folgende Spieler seinen Zug machen kann |  |
# Technische Beschreibung
## Systemübersicht
## Softwarearchitektur
## Schnittstellen
### Ereignisse
## Datenmodell
## Abläufe
## Entwurf
## Fehlerbehandlung
## Validierung
# 4 Projektorganisation
## 4.1 Annahmen
- Verwendete Technologien:
    - Programmiersprachen: Java, Python
    - Frameworks: RabbitMQ
    - Verwaltung: Github

- Einschränkungen, Betriebsbedingungen und Faktoren, die die Entwicklung beeinflussen:
    - Jedes Mitglied arbeitet am eigenen PC, es muss Acht gegeben werden auf Betriebssystemspezifische Fehler und sonstige Eigenarten

- Interne Qualitätsanforderungen:
    - Ausgibige Tests
## 4.2 Risiken
- Gruppenmitglieder könnten spontan wegfallen aus gesundheitlichen oder persönlichen Gründen
- Der Workload von anderen Modulen kann dazu führen, dass weniger Zeit in das Projekt investiert wird
- Mitglieder könnten, trotz besten Willens, überfordert mit der Aufgabe sein
## 4.3 Verantwortlichkeiten
Aufgrund der geringen Anzahl an Teammitgliedern werden die Aufgaben größtenteils gemeinsam bearbeitet.
Somit sind Eric Neppert, Oskar Schaubert, Waldemar Schäfer, Jason Piper und Manuel Wiebe alle beteiligt an der implementierung der Server Logik.
Zusätzlich implementiert jedes Mitglied eigenständig einen KI-Spieler.
Sollten weitere Rollen im Verlauf des Implementierens nötig werden, werden einzelne Mitglieder dafür auserkoren.
Zum aktuellen Zeitpunkt ist dies nur die Rolle des Koordinators, übernommen von Oskar Schaubert
## 4.4 Grober Projektplan
Es wird sich größtenteils an die vorgegebenen Meilensteine gehalten:
- Mitte April: Abgabe der Spezifikationen
- Ende April: Grundlegende Spiel und Serverlogik implementiert
- Mitte Mai: Grundlagen der künstlichen Spieler fertig, können selbstständig eine Runde spielen
- Ende Mai: Fertiger Softwareprototyp und simple künstliche Spieler
- Mitte Juni: Projektabgabe, Software ausgearbeitet und Spieler kompetent
# Anhänge
## Glossar
## Referenzen
## Index

