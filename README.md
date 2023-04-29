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
| Prüfer | Jörg Brunsmann | gemeinsame Meetings für die Angabe,<br>bei Fragestellungen via Mailverkehr | Anforderungen an das Projekt |Nachvollziehbarkeit der Arbeitsschritte,<br>Einsicht in die Produktdokumentation,<br>Leistungsbewertung der Studierenden|
| Studierende | Eric Neppert, <br>Oskar Schaubert,<br>Waldemar Schäfer,<br>Jason Piper,<br>André Ghazaryan,<br>Manuel Wiebe | gemeinsame Meetings, Discord | Projektmanagement,<br>Softwareentwicklung | Erfüllung der Leistungen für das <br>Studienfach Softwareprojekt<br>Anwendung von Projektmanagementmethoden,<br> Vertiefung in der Softwareentwicklung |
| Programmierer | Studierende | | Softwareentwicklung | Funktionsfähige Software |
| Benutzer| Prüfer,<br>Studierende |  | Spielregeln | Teilnahme am Turnier<br>Benutzung einer KI für die Spielzüge |
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
-   Set:
    - Anzahl und Farbe der Karten, die abgeworfen werden müssen.
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
Normen und Standards
Netzwerkprotokolle: Um die Kommunikation zwischen den Client-Geräten und dem zentralen Server zu ermöglichen, können Netzwerkprotokolle wie TCP/IP (Transmission Control Protocol/Internet Protocol) oder UDP (User Datagram Protocol) verwendet werden, um die Datenübertragung zu standardisieren.
Es sollten gängige Netzwerkprotokolle wie TCP/IP oder HTTP verwendet werden, um die Kommunikation zwischen den Client-Geräten und dem zentralen Server zu ermöglichen.
Sicherheitsstandards: 
Es können Sicherheitsstandards wie SSL/TLS (Secure Sockets Layer/Transport Layer Security) für die sichere Kommunikation zwischen den Clients und dem Server verwendet werden, um die Vertraulichkeit und Integrität der übertragenen Daten zu gewährleisten.
Protokolle:

Kommunikationsprotokolle: Es müssen Protokolle für die Kommunikation zwischen den Client-Geräten und dem zentralen Server definiert werden, um die Interaktion und den Austausch von Spielinformationen zu ermöglichen, z.B. für das Anmelden, Verbinden, Abmelden, Übermitteln von Spielzügen und Aktualisieren des Spielstatus.
Spielregelprotokolle: Es können Protokolle definiert werden, um die Spielregeln und Abläufe festzulegen, z.B. für das Austeilen der Karten, die Reihenfolge des Spielzugs, die Entscheidungsfindung der KI-Spieler und die Überprüfung der Siegbedingungen.

Verteilte Systeme: Es sollten Normen und Standards für verteilte Systeme wie z.B. das Message Passing Interface (MPI) oder das Java Remote Method Invocation (RMI) verwendet werden, um die Kommunikation zwischen den Client- und Serverkomponenten der Software zu ermöglichen.

Hardware

Server-Hardware: Ein leistungsfähiger Server ist erforderlich, um die Spiellogik, die Kommunikation mit den Clients und die Verwaltung der Spielinformationen zu unterstützen. Die Hardware-Anforderungen hängen von der Anzahl der Spieler und der Komplexität des Spiels ab.
Client-Hardware: Die Client-Geräte, von denen aus die Spieler dem Spiel beitreten, müssen über ausreichende Ressourcen verfügen, um die Spielanwendung auszuführen und die Kommunikation mit dem Server zu bewältigen.

Externe Vorgaben:

Datenschutzbestimmungen: Da Spielinformationen in einer Datenbank gespeichert werden, müssen geltende Datenschutzbestimmungen eingehalten werden, um sicherzustellen, dass die Spielerdaten geschützt und sicher verwaltet werden.
Netzwerkrichtlinien: Es können Netzwerkrichtlinien vorgegeben sein, die die Verwendung bestimmter Netzwerkprotokolle, Firewall-Konfigurationen oder andere Sicherheitsrichtlinien festlegen, um die Netzwerksicherheit zu gewährleisten.
Anwendungsrichtlinien: Es können Anwendungsrichtlinien definiert sein, die die Spielregeln, die Verwendung von KI-Spielern und andere Aspekte der Anwendung festlegen, um einheitliche Standards und Erwartungen für die Benutzer einzuhalten.

Mögliche Sicherheitsrisiken und Sicherheitsschwachstellen:

Datenlecks: Unzureichende Sicherheitsmaßnahmen bei der Speicherung von Spielinformationen in der Datenbank können zu Datenlecks führen und die Vertraulichkeit von Spielerdaten gefährden.
Netzwerkangriffe: Unzureichende Absicherung der Kommunikation zwischen den Clients und dem Server kann zu Netzwerkangriffen wie Man-in-the-Middle-Angriffen oder Denial-of-Service-Angriffen führen, die die Verfügbarkeit und Integrität des Spiels

Unsichere Kommunikation: Wenn die Kommunikation zwischen den Client-Geräten und dem Server nicht ausreichend abgesichert ist, könnten Daten abgefangen oder manipuliert werden. Um dies zu verhindern, sollte eine sichere Kommunikation wie SSL/TLS verwendet werden.
Unzureichende Authentifizierung: Wenn die Benutzer Identifikation und Authentifizierung nicht ausreichend umgesetzt ist, könnten unbefugte Benutzer auf das Spiel und die Spielinformationen zugreifen. Eine starke Authentifizierung sollte implementiert werden, um sicherzustellen, dass nur autorisierte Benutzer auf das System zugreifen können.
### 2.3.2 Betriebsbedingungen
Hardwareanforderungen:

Server-Hardware: Der zentrale Server, auf dem die Software läuft, sollte über ausreichende Rechenleistung, Speicher und Netzwerkfähigkeiten verfügen, um die Anforderungen des Spiels und der Spielerzahl zu bewältigen.
Client-Hardware: Die Client-Geräte, von denen aus die Spieler dem Spiel beitreten, sollten über ausreichende Rechenleistung und Netzwerkkonnektivität verfügen, um die Spielanwendung und die Kommunikation mit dem Server effizient auszuführen.

Externe Vorgaben:

Webbrowser-Versionen: Die Software sollte auf gängigen Webbrowsern wie Google Chrome, Mozilla Firefox, Microsoft Edge oder Safari lauffähig sein, wobei die aktuellsten stabilen Versionen bevorzugt werden.
Betriebssystem-Versionen: Die Software sollte auf gängigen Betriebssystemen wie Windows, macOS oder Linux lauffähig sein, wobei die aktuellsten stabilen Versionen bevorzugt werden.

### 2.3.3 Qualitätsmerkmale
<img width="504" alt="image" src="https://user-images.githubusercontent.com/92401495/232754853-a1548f7a-cc3b-40dc-bbe2-8a2fca1982e9.png">

## 2.4 Graphische Benutzerschnittstelle
Die Kommunikation mit dem Server soll für den Client zuerst über eine Textbasiert Oberfläche erfolgen. Im späteren Verlauf kann eine Webseite gestaltet werden, welche die Funktionalitäten erweitert.
Das Anzeizen der Karten auf der Hand erfolgt mit dem Text für die Bezeichnung der Farben gefolgt von der Nummer. Die einzelnen Karten werden mit einem Komma getrennt.
Das Auswählen einer Karte erfolgt mit der Angabe der Position auf der Hand. Neue Karten werden zu der Hand hinten angefügt.
## 2.5 Anforderungen im Detail
| Als | möchte ich | so dass | Akzeptanz |
| --- | --- | --- | --- |
| Benutzer | mich mit dem Server verbinden | in der Warteschlange für Nope warten kann | bestätigte Verbindung mit dem Server |
| Benutzer | einem Spiel beitreten | mit einem weiteren Spieler Nope spielen kann | bestätigte Verbindung einer Session |
| Benutzer | Karten aus dem Kartenstapel ziehen | sodass ich diese auf meine Hand ablegen kann | Erhöhung der Anzahl meiner Karten auf der Hand |
| Benutzer | am Anfang solange Karten ziehen bis meine Hand voll ist | das Spiel beginnen kann | höchste Anzahl Karten auf der Hand |
| Benutzer | die oberste Karte auf dem Ablagestapel sehen | damit ich meinen Zug planen kann | bestätigte Angabe des Servers der angefragten Karte |
| Benutzer | bei der Durchblick-Karte weitere Karten auf dem Ablagestapel einsehen | damit ich meinen Zug planen kann | bestätigte Angabe des Servers der angefragten Karte |
| Benutzer | die Anzahl der Karten der Anderen Spieler sehen | eine passende Karte legen kann | bestätigte Angabe des Servers der Anzahl der Karten |
| Benutzer | Karten auf dem Ablagestapel ablegen | der folgende Spieler seinen Zug machen kann | bestätigte Angabe des Servers meines Zuges und der Angabe der Gültigkeit |
| Benutzer | keine Karte auf dem Ablagestapel ablegen (Nope) wenn ich kein passendes Set habe | der folgende Spieler seinen Zug machen kann | bestätigte Angabe des Servers meines Zuges und der Angabe der Gültigkeit |
# 3 Technische Beschreibung
## 3.1 Systemübersicht
![image](https://user-images.githubusercontent.com/16638925/232320881-4d456764-6f20-4220-ae09-21d2f35ec7e5.png)

## 3.2 Softwarearchitektur
![image](https://user-images.githubusercontent.com/16638925/232320130-c0bc9c59-227b-49a3-9b15-089be27c06ef.png)

## 3.3 Schnittstellen
"" = nicht sicher ob es gebraucht wird 

GET \
(Top Card)"letzte offenliegende Karte\
(New Card)\
(Hand Cards)\
"(Opponents Cards number)"\
(Current Player)\
(Standing) "teile der Tabelle des Turniers printen"\
(History)\
(Opponent)\
(Own Player Stats)

POST\
(Playable Cards)\
"(Give Up)"\
"(Start Game)"\
(Player stats) "daten des eigenen Spieler"


JSON:\

Farbe der Karte: (blue, yellow, red, green,blue yellow, blue red, blue green, yellow red,yellow green, red green ,black, multi)\
multi steht für Zahlen mit allen farben\
Zahl der Karte(1,2,3,4,5,6) 4 5 6 Ereigniskarten\
Am Zug( True, False)\
Anzahl der Handkarten(Int)\
 (um zu wissen ob man bestimmte Karten legen kann. Wenn der gegner 2 Karten hat kann die 3 nicht mehr gelegt werden)\

Beispiel JSON\
blue, 2; yellow, 1; green, 1; blue red, 3; red green,3;black, 5; True;\

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

## 3.9 Verwendete Technologien
- Programmiersprachen: Java, Python
- Frameworks: Werden noch bestimmt
- Verwaltung: Github

# 4 Projektorganisation
## 4.1 Annahmen
- Verwendete Technologien:
    - Programmiersprachen: Java, Python
    - Frameworks: Werden noch bestimmt
    - Verwaltung: Github

- Einschränkungen, Betriebsbedingungen und Faktoren, die die Entwicklung beeinflussen:
    - Jedes Mitglied arbeitet am eigenen PC, es muss Acht gegeben werden auf Betriebssystemspezifische Fehler und sonstige Eigenarten

- Interne Qualitätsanforderungen:
    - Ausgiebige Integrationstests
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
- 02.05.23: Aktueller Stand - Digitales Zoom Meeting (Link im Ilias)
- Mitte Mai (16.05.2023) : Grundlagen der künstlichen Spieler fertig, können selbstständig eine Runde spielen
- Ende Mai: Fertiger Softwareprototyp und simple künstliche Spieler
- Mitte Juni: Projektabgabe, Software ausgearbeitet und Spieler kompetent

