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