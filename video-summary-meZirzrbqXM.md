# "Nie wieder verlorene Informationen – Das Claude Wiki System (Karpathy LLM)"

**Kanal:** Designers Inn | Apps, KI, Automation fürs Business
**URL:** https://www.youtube.com/watch?v=meZirzrbqXM
**Länge:** 16:38
**Zusammenfassung erstellt:** 2026-07-04

---

## Das Problem: Chaos aus Notizen und Dateien
Verstreute Artikel, Notizen, Bookmarks, Screenshots und Transkripte ohne System — "Kein System. Kein Überblick."

## Die Lösung: Ein Wiki, das Claude selbst pflegt
- Kein Vektor-Datenbank-Setup, kein Code nötig — nur Ordner plus eine Steuerdatei
- Zitiert wird Andrej Karpathy: Statt bei jeder Anfrage nur Rohdaten abzurufen, baut das LLM fortlaufend ein persistentes Wiki aus verlinkten Markdown-Dateien auf, das zwischen Nutzer und Rohquellen sitzt
- Grundprinzip: **Inbox → Wiki → Output**

## Die 5 Schritte des Systems

**1. Setup** — Hauptordner (Inbox/Wiki/Output) anlegen, zentrale `CLAUDE.md` mit Fokus-Themen, Inbox-Regeln, Antwort-Format

**2. Informationen sammeln** — "Wirf alles rein. Kein Aufräumen." Die Organisation übernimmt Claude. Beispiel: automatisiertes Clipping von YouTube-Videos inkl. Key-Talking-Points und Kapiteln

**3. Wiki aufbauen** — Ein Prompt genügt: "Lies alles in der Inbox und bau ein Wiki im Wiki-Ordner. Erstell zuerst einen Index, dann eine Datei pro Hauptthema, und verknüpfe zusammenhängende Themen." Ergebnis als Graph-Ansicht (Obsidian-artig) gezeigt

**4. Compounding Loop** — Claude liest Wiki → generiert Antwort → schreibt Output. Zusätzlicher Memory-Ordner mit Daily Notes sorgt für sitzungsübergreifendes Wissen

**5. Pflege (Health Check)** — Audit-Prompt: "Prüf auf Widersprüche zwischen Artikeln. Such nach Behauptungen ohne Quelle. Identifiziere Themen, die häufig erwähnt werden, aber noch keinen eigenen Artikel haben." Empfehlung: als wöchentliche Scheduled Task einrichten

## KI-Team als Erweiterung
Mehrere spezialisierte Agenten (u.a. "William – Writingstyle") übernehmen Teilaufgaben, während der Nutzer nur noch Aufträge vergibt.

## Wachstumskurve (Tag 1 – Tag 100)
- Tag 1: Ordner + CLAUDE.md stehen
- Tag 7: erste Dutzend Einträge, erste Zusammenfassungen
- Tag 30: Präsentationen, Briefings, Auswertungen ohne lange Erklärungen
- Tag 100: jedes Meeting verknüpft, persistentes Gedächtnis — "Business-Asset"

*Im Video eingebettet ist ein Werbeblock für ein Kurs-/Produktangebot ("KI-Mitarbeiter", businesserfolg.de).*

---

## Kernbotschaft
Statt Informationen einfach abzulegen, soll Claude aus einer simplen Inbox automatisch ein strukturiertes, verlinktes Markdown-Wiki bauen und pflegen — nach Andrej Karpathys Konzept eines "persistenten LLM-Wikis". Durch einen sich selbst verstärkenden Kreislauf (Inbox → Wiki → Output → Memory) und regelmäßige Selbst-Audits entsteht ein wachsendes, individuelles "Second Brain".

## Themen-Tags
Second Brain, Claude Wiki System, Wissensmanagement, Agentic Workflows, KI-Automatisierung, Business-Coaching/Produktwerbung

## Zu prüfen
- Das gezeigte Karpathy-Zitat zum "persistenten Wiki" — Originalquelle (Tweet/Blogpost) verifizieren
- Marketing-Behauptungen des beworbenen Drittanbieter-Kurses sind Werbeaussagen, nicht unabhängig verifiziert

*Hinweis: Für dieses Video waren keine Untertitel verfügbar und der Whisper-Fallback ist an einem Rate-Limit (HTTP 429) gescheitert. Die Zusammenfassung basiert daher ausschließlich auf 80 extrahierten Frames und Video-Metadaten. Siehe [whisper-replicate-rate-limit.md](whisper-replicate-rate-limit.md) für die Ursache.*
