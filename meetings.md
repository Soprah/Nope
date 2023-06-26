# Scrum Meetings

## 11.04.2023
- 14.30Uhr | 90min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Jason Piper
- Manuel Wiebe

### Themen

#### Softwarespezifikation
In diesem Meeting sollen Abschnitte der Softwarespezifikation auf die
Teammitglieder aufgeteilt werden.

Für das Zusammenführen der Spezifikation als Dokument wurde Githubs Rich Text Funktion vorgeschlagen,
so kann die Spezifikation direkt über das Repo gefunden werden.

Folgende Bereiche wurden eingeteilt:
- Einführung - Oskar
- Anforderungen - Eric, Waldemar
- Technische Beschreibung - Jason, Manuel
- Projektorganisation - Oskar
- Anhänge - Werden im nächsten Meeting zusammen bearbeitet

Die Zweierteams teilen die Überschriften nochmals unter sich auf.

Am Freitag ist ein Meeting organisatorisch schwierig, aber im Verlauf des Tages wird jeder im Discord Server über den eigenen Fortschritt berichten.
Am Montag den 17.04 um 18:00 Uhr findet ein letztes Meeting statt (online), um direkt vor der Abgabe das Dokument bereit zu machen.

#### Weiterer Inhalt

Bezüglich der Programmiersprachen in denen die KIs programmiert werden, 
plant Manuel ebenfalls Python zu benutzen.

Das Projekt kann ein gemeinsames Repo benutzen für die Serverlogik, da wir gemeinsam an ihr arbeiten werden.
Eric zeichnet ein Diagramm für unseren geplanten Github Workflow für die Serverlogik.

Wir arbeiten mit 3 Branches, Master, Dev und Feature.
Wir planen ein Kanban Board. Die Abgabetermine sind unsere Milestones.
Wir wollen die Serverlogik prioritisieren um alles für die Entwicklung der KIs vorzubereiten.
Außerdem werden wir Prinzipien von CI und CD anwenden.

Im Repo wird Englisch geschrieben.

Für die individuellen KIs legt jeder nochmal sein eigenes Repo an.

-------------------------------------------------------------------

## 17.04.2023
- 18.00Uhr | 90min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Jason Piper
- Manuel Wiebe
- André Ghazaryan

### Themen

Wir gingen die Spezifikation ein letztes mal gemeinsam durch um sie für die Abgabe fertig zu stellen.

Morgen ansprechen:
-André ist dem Team beigetreten, Aufgaben wurden für ihn verteilt
-Frage: Läuft das Turnier nur innerhalb der Teams ab oder auch Teamübergreifend?

-------------------------------------------------------------------

## 18.04.2023
- 14.30Uhr | 90min

### Teilnehmer
- Jörg Brunsmann
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Jason Piper
- Manuel Wiebe
- André Ghazaryan

#### Verbesserungsvorschläge des Stakeholders

- KI und Server sind keine Stakeholder sondern Akteure welche in bei den Funktionalen Anforderungen auftauchen sollten
- Weitere Funktionale Anforderungen erarbeiten und zu Unterpunkten zusammenfassen
- Die Abfrage der Anzahl der Karten des Gegenspielers muss vorhanden sein und bei den Schnittstellen aufgeführt werden. Die Möglichkeit keine Karte abzulegen (Nope) ebenso.
- Fachbegriffe im Glossar dokumentenweit verwenden und gegebenenfalls neu eintragen (session)
- Wir sollten uns darauf einigen welche JDK Version wir verwenden werden damit jeder an dem Projekt mitarbeiten kann. Eventuell Make nutzen damit jeder die gleichen Voraussetzungen haben kann und wir nicht an eine bestimmte Entwicklungsumgebung gebunden sind
- User Storrys und Funktionalitäten erweitern sodass der Inhalt beider übereinstimmt (matchen)
- Unautorisierte Spieler können keine Spielzüge machen. User Storys und Funktionalitäten dementsprechend anpassen
- User Story für das Ablegen keiner Karte hinzufügen (Nope)
- Weitere Ablaufdiagramme hinzufügen. Wichtig ist es dass wir den Turnierbetrieb (zwei Spieler) abbilden und uns Gedanken machen wie die Kommunikation mit dem Server stattfinden soll
- In der Dokumentation die Schnittstellen korrekt angeben (bei JSON die Klammern)
- Die Software in verschiedene Bausteine unterteilen und die Abhängigkeiten besser darstellen (Schichtenmodell).
- Zeitpuffer in der Projektplanung einbeziehen
- Pair Programming in die Projektorganisation aufnehmen. Einiges in der Organisation könnte in den Rahmenbedingungen der Nichtfuntionalen Anforderungen stehen
- Turnierregeln sollten festgelegt werden. Da ein Spiel nur wenige Minuten dauern könnte, sollten wir überlegen welchen Zeitrahmen wir benötigen um den Sieger zu ermitteln. Es könnte ein best of 100 werden

#### Klärung einiger Details
- Es  spielen jeweils immer nur zwei Spieler gegeneinander
- Das Turnier findet nur unter uns statt
- Die Ausgabe der Spielverlauf ist Pflicht und keine Option für die Grafische Oberfläche. Diese Sollte gut getestet werden.
- Der Spielablauf sollte gut automatisiert werden, sodass der Server nicht unnötig auf die Spieler warten soll
- Der Server kennt alle Daten des Clients sodass dieser mit einer gültigen Identifikation neu Starten kann und das Spiel fortsetzen kann

-------------------------------------------------------------------

## 24.04.2023
- 18.00Uhr | 80min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Manuel Wiebe
- André Ghazaryan

#### Themen

- Oskar ist vorraussichtlich vom 04.05 - 08.05 abwesend

- Die Software in Module zu unterteilen, dass wir das Team auf die Module aufteilen:
	- Schichten aufteilen, TCPIP Protokoll:
		- unterste Schicht: Netzwerk (Web Sockets)
		- drüber: Authentifizierung (Überprüfung der Authentizität einer Nachricht)
		- drüber: Spielerverwaltung (Zuweisung von Daten zu Spieler und Session)
		- drüber: Spiellogik
	- Schnittstellen abklären, dann kann Individuell an den Modulen gearbeitet werden
	- Waldemar zeichnet eine Skizze um den Aufbau zu verdeutlichen
		- link: (wird noch hinzugefügt)

- Es wurde sich entschieden den Server lieber in Python zu implementieren
	- Als Framework wurde SQLalchemy und Flask vorgeschlagen
	- Waldemar hat bischer keine Erfahrung mit Python, ist bereit die Sprache zu lernen

- Die Spezifierung muss noch mit den neuen Änderungen angepasst werden

- Die Spieleranzahl pro Partie ist maximal 2

- Polling verhindern, alternative finden
	- link: https://discord.com/channels/1092803319166160937/1094255471789092884/1100105018650136586

- Nächstes Meeting: 25.04.23 Dienstag 14:30 Uhr
	- Agenda:
		- Dienstag Meetings eventuell später anfangen
		- Die Spiellogik muss als erstes besprochen werden
		- TDD, Test Driven Development. Ein Team schreibt Code, das andere die Tests
		- Konsistente Begriffe gemeinsam definieren und in die Spezifizierung ergänzen
		- Github: Issues gemeinsam bestimmen und aufteilen

-------------------------------------------------------------------

## 25.04.2023
- 14.30Uhr | 80min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Manuel Wiebe
- Jason Piper

#### Themen
- Meetings können Dienstags um 15:30 erst anfangen, ausnahme nächste Woche treffen mit Brunsmann

- Diskussion zur Implementierung
	- Einzelheiten der Spiellogik werden besprochen
		- Eric zeichnet Diagramme
	- Untergruppen um mit der Implementierung anzufangen:
		- Spiellogik: Eric und Oskar
		- JSON: Waldemar und Manuel
		- Jason und André sind momentan abwesend, aber werden sich auf diese Teams aufteilen

- Zwischenmeeting Samstag 29.04.23 um 15:00 Uhr
	- sehr kurze Besprechung über den Progress

-------------------------------------------------------------------

## 02.05.2023
- 14.30Uhr | 30min

### Teilnehmer
- Jörg Brunsmann
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Manuel Wiebe
- André Ghazaryan
- Jason Piper

#### Inhalt
- Zukünftige wöchentliche Sprint Meetings am Dienstag finden um 15:30 statt

- Meeting mit Brunsmann über den Fortschritt
- Spezifikation:
	- ersichtlich machen, dass wir in 3 Teams aufgeteilt sind
	- Schichtenmodell in der Spezifikation muss angepasst werden
	- Schichtenmodell eventuell "auf den Kopf stellen" für das Client-Server System, Netzwerk zuerst
		- Spiellogik ist fest und größtenteils unveränderlich, Netzwerk kann sich mehr ändern
		- Schnittstelle zwischen Spiellogik / Spielerverwaltung können mit Unit Tests getestet werden
	- unseren Workflow für die Source Code Verwaltung einfügen
	- readMe unbenennen zu Spezifikation

- bis zum 16.05:
	- Clients können sich mit dem Server verbunden
	- Clients können Spielzüge durchführen
- bis zum 13.06 muss das Turnier durchgeführt sein
- zwei wochen später Abgabe der individuellen Projektdokumentation

- sobald vorhanden, die Repos der Clients im Repo des Servers verlinken

- das Deployment des Servers automatisieren

- Meeting am 16.05 ist in präsenz

-------------------------------------------------------------------

## 09.05.2023
- 15.30Uhr | 60min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Manuel Wiebe
- Jason Piper

#### Inhalt:

- Datenbank
	- Grundlegend fertig
	- Tabellen müssen noch erstellt werden mit Daten, die die anderen Teams noch absprechen werden

- Spiellogik
	- Arbeit läuft gut
	- Einfach Funktionen zum senden und empfangen von Daten sind vorhanden
	- Daten müssen mit dem Netzwerk Team abgesprochen werden

- Netzwerk
	- Grundlegend am laufen
	- Testen ist ein Problem da die Clients noch nicht vorhanden sind
	- Daten müssen mit Eric abgesprochen werden

- Spiellogik und Netzwerk Team werden in den nächsten Tagen sich zusammensetzen
- danach hat das Datenbank Team die nötigen Daten für die Tabellen
- Die einzelnen Komponenten werden in den nächsten Tagen zusammen

-------------------------------------------------------------------

## 15.05.2023
- 16.30Uhr | 60min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Jason Piper

#### Inhalt:
- Meeting bezüglich der morgigen Abgabe

- Waldemar:
- im Makefile muss der Pfad zum Projekt angegeben werden
- Spiel kann noch nicht starten, weil der zweite Spieler nicht der Partie beitreten kann

- Eric:
- Spiellogik fast komplett fertig
- Konnte einen ersten Spielzug simulieren (mit vorgemachter JSON)
- jedoch klappte es nur mit einer älteren Version vom Code
- die aktuellste Version wurde mit dem Backend verbunden, dieser Funktioniert jedoch noch nicht ganz

- Wir merken an, dass unsere kleine Teamgröße die Aufgabenteilung sehr schwierig macht
- Dadurch, dass jeder am Server und am Client arbeitet, ist es schwer uns intensiv auf ein Modul zu konzentrieren im Gegensatz zu den größeren Gruppen

- Eric schlägt vor, dass das Datenbankteam dem Netzwerkteam aushilft
- Das Datenbankteam hat sonst nicht viel zu tun, bis das Netzwerkteam bereit ist
- Das Thema bei dem das Netzwerkteam helfen soll: Bilaterale Kommunikation in Flask mit Websockets
- Zeit bis zum 23.05 zum einlesen

-------------------------------------------------------------------

## 16.05.2023
- 14.30Uhr | 60min

### Teilnehmer
- Eric Neppert
- Oskar Schaubert
- Waldemar Schäfer
- Jason Piper

#### Inhalt:
- Wir präsentieren unseren Fortschritt

- die Spiellogik ist soweit fertig
- wir haben aber noch Schwierigkeiten die Schnittstellen zu verbinden

- der Code wird durchgegangen und erklärt

- Arbeit wird in der nächsten Arbeitsphase neu verteilt, damit das Netzwerkteam mehr Unterstützung hat um die Schnittstellen bereit zu machen

- wir erläutern die Probleme, auf die wir gestoßen sind und wie wir planen sie zu beheben

- Ab hier schlechte Verbindung:
	- Brunsmann spricht über Websockets(?)
	- Brunsmann fragt wegen den KI Clients(?)
	- Brunsmann spricht über die Kommunikationsschicht(?)
	- Brunsmann spricht an wie wichtig es ist, dass das Turnier am Ende durchführbar ist(?)
	- Brunsmann spricht über das Format der Tournierergebnisse(?)
	- Brunsmann ist wichtig, dass das Tournier stattfinden kann und jeder eine fertige KI Logik hat(?)

-------------------------------------------------------------------

## 23.05.2023
- 14.30Uhr | 60min

### Teilnehmer
- Gesamte Team

#### Inhalt:
- Datenbank ist bereit
	- Es muss noch ein Format für die Tournierergebnisse gefunden werden
- Daten sollten bei jedem Zug an die Datenbank geschickt werden
	- ist sicherer und erlaubt das weiterführen einer pausierten Partie

- Netzwerk Team guckt, wie man Flask auf einen Server ausführen kann
- Websockets wurden durchschaut, nur noch das genaue Format der Daten muss bestimmt werden

- Es gibt immer noch unklarheiten zu den Spielregeln, diese klären wir endgültig bevor die Arbeit weitergehen kann
- Waldemar wird Eric bei der finalisierung der Spiellogik helfen müssen um unseren Zeitplan möglichst einzuhalten

- André und Oskar werden die Clients startklar machen, um möglichst bald die Spiellogik testen zu können

- wir haben uns entschlossen die täglichen Meetings beizubehalten

-------------------------------------------------------------------

## 30.05.2023
- 14.30Uhr | 60min

### Teilnehmer
- Oskar Schaubert
- Waldemar Schäfer
- Eric Neppert
- Manuel Wiebe

#### Inhalt:
- Wir hängen im Zeitplan hinterher, weder Server noch Spiellogik noch Clients sind bereit
- Netzwerk und Client müssen Websockets abklären, treffen dafür wahrscheinlich am Donnerstag
- Eric wird ab morgen öffentlich an der Spiellogik arbeiten, man soll dazustoßen wenn man kann um sie möglichst schnell zu beenden
- Server läuft noch nicht, das Thema stellt sich als komplexer als erwartet heraus. Wir besprechen beim morgigen arbeiten ob er unterstützt werden kann

-------------------------------------------------------------------

## 06.06.2023
- 14.30Uhr | 60min

### Teilnehmer
-Oskar Schaubert
-Eric Neppert
-Waldemar Schäfer
-Manuel Wiebe
-André Ghazaryan

#### Inhalt:
Der Client wurde vorgestellt, die meisten Features sind vorhanden nur noch die Einsicht der Spielverläufe muss implementiert werden. Zusätzlich sollte der Code noch kommentiert werden.

Die Kommunikationsschicht des Servers ist ebenfalls fertig, es fehlt hier ebenfalls nur noch die Einsicht der Spielverläufe.

Das Client Team trifft sich morgen und beendet die History Features, zusätzlich wird die Client-Server Verbindung im Localhost getestet.

Jason verlässt das Projekt, André wird die Aufgaben der Datenbank übernehmen

Die Spiellogik Ebene fehlen noch ein paar Features, welche Eric in den nächsten Tagen fertigstellen wird.

Nächstes Meeting am Samstag um 14:30 Uhr.

Letztes Meeting am Montag um 19:00 Uhr, da wird das Tournier durchgeführt + letzte Besprechung vor der Abgabe.

-------------------------------------------------------------------

## 10.06.2023
- 14.30Uhr | 60min

### Teilnehmer
-Oskar Schaubert
-Eric Nepert
-Waldemar Schäfer
-André Ghazaryan
-Manuel Wiebe

#### Inhalt:
- Server konnte nicht zum laufen gebracht werden, Docker konnte das Problem nicht lösen
- Wir versuchen im Internet einen alternativen Server zu holen als letzte Notlösung

- Der Client hatte Probleme mit dem Zugreifen auf Daten vom eigenen Projekt, dies konnte gelöst werden

- Spiellogik noch nicht bereit, GameManagement fast bereit

- Im Falle dass der Server nicht fertig wird, werden wir das Tournier im Localhost durchführen müssen

- Wir haben entschlossen, die Spiellogik gemeinsam zuende zu bringen

-------------------------------------------------------------------

## 12.06.2023
- 19.00Uhr | 60min

### Teilnehmer
-Oskar Schaubert
-Eric Nepert
-Waldemar Schäfer
-André Ghazaryan
-Manuel Wiebe

#### Inhalt:
- Spezifikation muss etwas angepasst werden (welche Programmiersprachen werden benutzt, Jason ist weggefallen etc.)
- Server ist bereit
- Spiellogik braucht nur noch das State Pattern
- Server wird noch mit der Datenbank verbunden
- Die Main Methode des Clients befindet sich in der Netzwerkschicht

-------------------------------------------------------------------

## 13.06.2023
- 14.30Uhr | 60min

### Teilnehmer
-Oskar Schaubert
-Eric Nepert
-Waldemar Schäfer
-André Ghazaryan
-Manuel Wiebe

#### Inhalt:
Offen stehende Aufgaben:
1) 4 KI Clients	(*6 Tage)
	- Spiellogik berechnen
	- testen: kann ein Spiel durchgeführt werden?
2) Datenbank (4 Tage)
	- mit den Server verbinden
	- auf den Server aufsetzen
3) Kommunikationsschicht des Servers:
	- Circular import error beheben (3 Tage)
	- IDs der Aktionskarten umstrukturieren, Initialkarte mitschicken (4 Tage)
4) Spielresultate in der Datenbank speichern, Tourniertabelle (4 Tage)
	- vorhandene Planung mit history_list nutzen
	- Tourniertabelle braucht nur Resultate
	
Aufwandsschätzung:
15 Tage
*(Arbeit an KI Clients wird von jedem parallel ausgeführt)
	
Priorität (höhste bis tiefste):
3) Kommunikationsschicht als erstes gemeinsam beenden
Ab hier kann jeder parallel an der KI arbeiten
2), 4)


Nächstes Meeting: Dienstag, der 20.06 um 14:30 über Zoom
Finale Abgabe: 	Dienstag, der 27.06 um 14:30 Präsent

