# Anforderungs- und Entwurfsspezifikation (“Pflichtenheft”)

# 1 Einführung
## 1.1 Beschreibung
Es soll das Kartenspiel "Nope" über Verteilte Systeme implementiert werden. Spieler können von verschiedenen Geräte aus einer Partie beitreten die auf einen zentralen Server läuft. Das Kartenspiel selbst wird von simulierten Spielern gesteuert, die automatisch strategische Züge ausführen.
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
### 2.2.1 STRUKTURIERUNG DER ANFORDERUNGEN IN FUNKTIONALE GRUPPEN
-	Spielregeln:
    -  	Festlegung der Regeln & Abläufe
        - Siegbedingungen
        - Austeilen der Karten
        - Reihenfolge des Spielzugs
        - Etc.
-	KI-Spieler:
    -  Algorithmen, die den simulierten Spieler reflektieren
        - Entwicklung von Strategien
        - Kartenverteilung
        - Entscheidungsfindung
-	Server
    - Schnittstelle zwischen den KI-Spielern
        - Verwaltet Kommunikation zwischen Spielern
        - Stellt sicher, dass die Regeln eingehalten werden
        - Speichert Spielinformationen in Datenbank
-	Datenbank
    - Speichert Daten des Spiels
        - Informationen zu einem Spielzug 
            - Welche Karte liegt auf dem Ablagestapel
            - Welche Karte spielt KI-1
            - Wie antwortet KI-2
            - Welche Karten besitzen KI-1 / KI-2 in der Hand
            - Welche Karten liegen noch im Deck
            - Gewinner und Verlierer eines Matches
### 2.2.2 AKTEURE
-	KI-Spieler/Spieler 1: 
    - Spielersimulation 1, die eine Partie mitspielt
    - KI-Spieler/Spieler 2:
    - Spielersimulation 2, die eine Partie mitspielt
-	Mensch:
    - Startet das Spiel
- Server: 
    - Verbindet Spieler
    - Steuert das Spiel
    - Speichert wichtige Informationen in Datenbank
### 2.2.3 WEITERE ENTITÄTEN/BEGRIFFE INNERHALB DER FACHDOMÄNE
-	Spielregeln:
    - Regeln & Abläufe des Kartenspiels, die von dem Kartenspiel festgelegt und von uns ggf. angepasst wurden (z.B. gibt es keinen Kartengeber)
-	Karten:
    - Spielkarten, die die Spielregeln vorgeben und im System umgesetzt wurden
    - Spielkarten befinden sich entweder im Ablagestapel, Nachziehstapel oder in der Hand eines Spielers
-	Deck:
    - Umfasst alle Karten des Spiels
-	Nachziehstapel:
    - Sammlung an Karten, die umgedreht bzw. verdeckt übereinander liegen und vom Spieler bei Bedarf gezogen werden können/müssen
-	Ablagestapel:
    - Die Sammlung an Karten, die vom Spieler abgeworfen wurden
    - Zu Anfang des Spiels wird die oberste Karte des Nachziehstapels den Anfang des Ablagestapels bilden
    - Die oberste Karte definiert eine Menge von Karten, die im Spielzug erlaubt sind
-	Spielzug:
    - Die Summe aus
        - Die oberste Karte des Nachziehstapels
        - Die abgeworfenen Karten eines Spielers
-	Spielerhand:
    - Die Summe der Karten, die eine KI bzw. Spieler in der Hand hält
-	Spielverlauf:
    - Wie sich das Spiel über die Spielzüge entwickelt
-	Gewinnergebnis:
    - Welcher Spieler gewonnen hat
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
| Benutzer | bei der Durchblick-Karte weitere Karten auf dem Ablagestapel einsehen | damit ich meinen Zug planen kann |  |
| Benutzer | Karten auf dem Ablagestapel ablegen | der folgende Spieler seinen Zug machen kann |  |
# 3 Technische Beschreibung
## 3.1 Systemübersicht
![image](https://user-images.githubusercontent.com/16638925/232320881-4d456764-6f20-4220-ae09-21d2f35ec7e5.png)

## 3.2 Softwarearchitektur
![image](https://user-images.githubusercontent.com/16638925/232320130-c0bc9c59-227b-49a3-9b15-089be27c06ef.png)

## 3.3 Schnittstellen
"" = nicht sicher ob es gebraucht wird 

GET 
(Top Card)"letzte offenliegende Karte
(New Card)
(Hand Cards)
"(Opponents Cards number)"
(Current Player)
(Standing) "teile der Tabelle des Turniers printen"
(History)
(Opponent)
(Own Player Stats)

POST
(Playable Cards)
"(Give Up)"
"(Start Game)"
(Player stats) "daten des eigenen Spieler"

## 3.4 Datenmodell

![image](https://user-images.githubusercontent.com/94369843/232548974-5414b3a7-bfd0-4a57-aa05-b387aaf2d8d7.png)


## 3.5 Abläufe
![image](https://user-images.githubusercontent.com/16638925/232319950-0b657fda-6b5a-4cce-8d31-021692439868.png)
![image](https://user-images.githubusercontent.com/16638925/232320009-4600e969-0e75-4b19-9e32-5760fb7e3929.png)

## 3.6 Entwurf
![image](https://user-images.githubusercontent.com/16638925/232320905-1058536c-f408-4fad-9b08-93b6e4419b67.png)

## 3.7 Fehlerbehandlung
### Mögliche Fehler:
- Interface
    - Button funktioniert nicht
    - Server nicht erreichbar
    - Authentifizierung schlägt fehl
    - Es wird zweimal das gleiche Profil authentifiziert
- Client
    - Verbindung zum Server wird unterbrochen
    - Ungültiger Spielzug wird ausgeführt (falsche Anzahl oder Farben)
    - Offene Karte kann nicht abgerufen werden, oder wird falsch ausgelesen
    - Handkarten stimmen nicht mit den vom Server gegebenen Karten überein
    - Spielzug wird ausgeführt, obwohl der andere Spieler an der Reihe ist
    - Kommunikationsfehler mit dem Server (Fehlerhafte JSON)
- Server
    - Verbindung zum Client wird während eines Spiels unterbrochen
    - Korrekter Spielzug wird als ungültig erkannt - Spieler wird fälschlicherweise disqualifiziert
    - Ungültiger Spielzug wird nicht erkannt - Spieler kann unbemerkt schummeln
    - Aktuell offene Karte, aktueller Spieler oder nächste Karte vom Stapel wird nicht korrekt geupdatet oder an Clients weitergegeben
    - Karte wird gezogen, obwohl der Stapel leer ist
    - Spieler können verdeckte Karten einsehen

## 3.8 Validierung
### Mögliche Integrations- und Unit-Tests:
- Testen der Verbindung zwischen Server und Clients
- Datenmodell
    - Test für korrekte Initialisierung und Beibehaltung des Kartendecks
    - Abspeichern und Auslesen der Spielhistorie
    - Zuordnung der User (richtige Handkarten / richtige Tabellenplätze)
    - Korrekte Modellierung der Spielregeln zur Überprüfung 
- API
    - Korrektes Generieren und Auslesen von JSON-Dateien
    - Korrekte Antworten auf API-Anfragen
    - Autorisierung bei sensiblen Anfragen (eigene Handkarten oder verdeckter Stapel / Identität beim Ausführen eines Zuges)
    - Fehlerabfangen bei fehlerhaften Anfragen vom Client
- User Interface
    - Korrekte Anzeige und Aktualisierung der Handkarten
    - Übergabe auszuspielender Karten an API

# 4 Projektorganisation
## 4.1 Annahmen
- Verwendete Technologien:
    - Programmiersprachen: Java, Python
    - Frameworks: RabbitMQ
    - Verwaltung: Github

- Einschränkungen, Betriebsbedingungen und Faktoren, die die Entwicklung beeinflussen:
    - Jedes Mitglied arbeitet am eigenen PC, es muss Acht gegeben werden auf Betriebssystemspezifische Fehler und sonstige Eigenarten

- Interne Qualitätsanforderungen:
    - Ausgiebige Tests
## 4.2 Risiken
- Gruppenmitglieder könnten spontan wegfallen aus gesundheitlichen oder persönlichen Gründen
- Der Workload von anderen Modulen kann dazu führen, dass weniger Zeit in das Projekt investiert wird
- Mitglieder könnten, trotz besten Willens, überfordert mit der Aufgabe sein
## 4.3 Verantwortlichkeiten
Aufgrund der geringen Anzahl an Teammitgliedern werden die Aufgaben größtenteils gemeinsam bearbeitet.
Somit sind Eric Neppert, Oskar Schaubert, Waldemar Schäfer, Jason Piper, André Ghazaryan und Manuel Wiebe alle beteiligt an der implementierung der Server Logik.
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

