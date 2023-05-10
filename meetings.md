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
