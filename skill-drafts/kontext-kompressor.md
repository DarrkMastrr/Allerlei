# Kontext-Kompressor

Verdichte einen langen, unübersichtlichen Chat oder ein Projekt zu einem kompakten "Context Pack", das in einem neuen Chat als vollständiger Einstiegspunkt dient.

## Ablauf

Arbeite in drei Stufen:

### Stufe 1 — Behalten (unverändert)
- Projektziel und Auftragsformulierung
- Getroffene Entscheidungen inkl. Begründungen
- Definierte Anforderungen und Constraints
- Aktueller Projektstand (letzter bekannter Zustand)
- Offene Fragen und ungelöste Probleme

### Stufe 2 — Verdichten
- Lange Diskussionen → Kernaussage in 1–2 Sätzen
- Mehrere ähnliche Anfragen → einmal zusammenfassen
- Zwischenergebnisse, die in ein finales Ergebnis gemündet sind → nur Endergebnis behalten

### Stufe 3 — Entfernen
- Smalltalk und Begrüßungen
- Veraltete Zwischenstände, die durch spätere Versionen ersetzt wurden
- Verworfene Ideen ohne Relevanz für den aktuellen Stand
- Wiederholungen

## Ausgabeformat

```
# Context Pack — [Projektname / Thema]
Erstellt: [Datum]

## Projektziel
[1–3 Sätze]

## Hintergrund & Kontext
[Komprimiert auf das Wesentliche]

## Getroffene Entscheidungen
- [Entscheidung] — Begründung: [kurz]

## Anforderungen & Constraints
- …

## Aktueller Stand
[Wo stehen wir gerade, was ist fertig, was nicht]

## Offene Punkte
- [ ] …

---
## Start-Prompt für neuen Chat

"[Fertiger Prompt, den man direkt in einen neuen Chat einfügen kann, um den Kontext zu übergeben]"
```

## Wichtige Hinweise

- Kontext-Kompressor spart primär **Input-Tokens** (im Gegensatz zum Kompaktmodus, der Output-Tokens spart)
- Den Start-Prompt immer als direkt kopier- und einfügbaren Text formulieren
- Nichts erfinden oder interpretieren — nur was explizit im Chat steht
