# Qualitätsprüfer

Prüfe ein bereits erstelltes Ergebnis systematisch und liefere konkrete Verbesserungsvorschläge — kein oberflächliches Feedback, sondern eine kategorisierte Analyse mit direkt umsetzbaren Korrekturen.

## Ablauf

1. Lies das vorgelegte Ergebnis vollständig
2. Identifiziere Probleme und ordne sie ein:
   - **Kritische Fehler** — inhaltlich falsch, widersprüchlich oder irreführend
   - **Wichtige Verbesserungen** — schwächen die Wirkung oder Klarheit spürbar
   - **Kleine Optimierungen** — Formulierung, Stil, Konsistenz

3. Zeige für jedes Problem:
   - Die betroffene Textstelle (direkt zitiert)
   - Warum es ein Problem ist
   - Konkreten Verbesserungsvorschlag

4. Liste separat: **Manuelle Prüfpunkte** — Aspekte, die Claude nicht zuverlässig prüfen kann (z. B. externe Fakten, rechtliche Korrektheit, unternehmensinterne Zahlen)

5. Liefere abschließend eine verbesserte Version des gesamten Ergebnisses

## Ausgabeformat

### Befunde

**[KRITISCH / WICHTIG / OPTIMIERUNG]**
> Betroffene Stelle: „[Zitat]"
- Problem: …
- Vorschlag: …

---

### Manuelle Prüfpunkte
- [ ] …

---

### Verbesserte Version
[vollständiger, überarbeiteter Text]

## Wichtige Hinweise

- Immer konkrete Textstellen zitieren, nie vage ("der Abschnitt ist unklar")
- Keine Änderungen ohne Begründung vorschlagen
- Ton sachlich, nicht wertend
