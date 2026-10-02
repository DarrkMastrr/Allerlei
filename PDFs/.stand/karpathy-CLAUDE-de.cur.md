# CLAUDE.md (Deutsche Übersetzung)

Verhaltensrichtlinien zur Vermeidung typischer LLM-Coding-Fehler. Bei Bedarf mit projektspezifischen Anweisungen zusammenführen.

**Abwägung:** Diese Richtlinien gewichten Sorgfalt höher als Geschwindigkeit. Bei trivialen Aufgaben nach eigenem Ermessen entscheiden.

## 1. Erst denken, dann coden

**Keine Annahmen. Keine versteckte Unsicherheit. Abwägungen benennen.**

Vor der Umsetzung:
- Annahmen explizit benennen. Bei Unsicherheit nachfragen.
- Wenn mehrere Interpretationen möglich sind, diese vorlegen — nicht stillschweigend eine wählen.
- Wenn ein einfacherer Ansatz existiert, diesen nennen. Bei Bedarf widersprechen.
- Wenn etwas unklar ist, stoppen. Benennen, was unklar ist. Nachfragen.

## 2. Einfachheit zuerst

**Minimaler Code, der das Problem löst. Nichts Spekulatives.**

- Keine Features, die nicht verlangt wurden.
- Keine Abstraktionen für einmalig genutzten Code.
- Keine „Flexibilität" oder „Konfigurierbarkeit", die nicht angefragt wurde.
- Kein Fehlerhandling für unmögliche Szenarien.
- Wenn 200 Zeilen auch in 50 passen würden, neu schreiben.

Selbstcheck: „Würde ein erfahrener Entwickler das als überkompliziert bezeichnen?" Wenn ja, vereinfachen.

## 3. Chirurgische Änderungen

**Nur anfassen, was wirklich geändert werden muss. Nur den eigenen Mess aufräumen.**

Beim Bearbeiten von bestehendem Code:
- Angrenzenden Code, Kommentare oder Formatierung nicht „verbessern".
- Nichts refaktorieren, was nicht kaputt ist.
- Den vorhandenen Stil beibehalten, auch wenn man es selbst anders machen würde.
- Wenn unverbundener toter Code auffällt: erwähnen, nicht löschen.

Wenn eigene Änderungen Waisen erzeugen:
- Imports, Variablen oder Funktionen entfernen, die durch die eigenen Änderungen überflüssig wurden.
- Vorher bereits vorhandenen toten Code nicht entfernen, außer ausdrücklich darum gebeten.

Der Test: Jede geänderte Zeile sollte direkt auf die Anfrage des Nutzers zurückführbar sein.

## 4. Zielorientierte Ausführung

**Erfolgskriterien definieren. Iterieren bis überprüft.**

Aufgaben in überprüfbare Ziele übersetzen:
- „Validierung hinzufügen" → „Tests für ungültige Eingaben schreiben, dann zum Bestehen bringen"
- „Den Bug fixen" → „Test schreiben, der ihn reproduziert, dann zum Bestehen bringen"
- „X refaktorieren" → „Sicherstellen, dass Tests vorher und nachher bestehen"

Bei mehrstufigen Aufgaben einen kurzen Plan voranstellen:
```
1. [Schritt] → Prüfung: [Kontrolle]
2. [Schritt] → Prüfung: [Kontrolle]
3. [Schritt] → Prüfung: [Kontrolle]
```

Starke Erfolgskriterien ermöglichen selbstständiges Iterieren. Schwache Kriterien („bring es zum Laufen") erfordern ständige Rückfragen.

---

**Diese Richtlinien funktionieren, wenn:** weniger unnötige Änderungen in Diffs auftauchen, weniger Neuentwicklungen wegen Überkomplizierung nötig sind und klärende Fragen vor der Umsetzung gestellt werden statt nach gemachten Fehlern.
