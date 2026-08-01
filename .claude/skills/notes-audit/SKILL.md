---
name: notes-audit
description: Health-Check für die Markdown-Notizen und Video-Zusammenfassungen dieses Repos. Prüft auf Widersprüche zwischen Artikeln, unbelegte Behauptungen und wiederkehrende Themen ohne eigenen Übersichtsartikel. Nutzen bei "Health Check", "Wiki-Audit", "Notizen prüfen" oder wenn regelmäßig gepflegt werden soll.
allowed-tools: Glob, Grep, Read, Write
user-invocable: true
---

# /notes-audit — Health-Check für die Notizen

Dieses Repo sammelt Notizen (Video-Zusammenfassungen unter `video-summaries/`, Themen-Artikel im Wurzelverzeichnis) nach dem Inbox→Wiki-Prinzip. Dieser Skill übernimmt den in der Zusammenfassung von `video-summaries/video-summary-meZirzrbqXM.md` beschriebenen **Health-Check-Schritt**: regelmäßig prüfen, ob sich Widersprüche eingeschlichen haben, ob Behauptungen unbelegt im Raum stehen, und ob ein Thema in mehreren Notizen auftaucht, ohne je einen eigenen Übersichtsartikel bekommen zu haben.

## Schritt 1 — Notizen einsammeln

Scope ist das gesamte Repo, mit Ausnahme von Tooling/Config:

```
Glob: **/*.md
```

Ausschließen: alles unter `.claude/`, `claude-skills/`, `node_modules/`, sowie der Report dieses Skills selbst (`notes-audit-report.md`, siehe Schritt 4).

Lies jede verbleibende Datei vollständig (`Read`). Bei vielen/langen Dateien: gruppiere sinnvoll (z.B. erst alle `video-summaries/*.md`, dann die Themen-Artikel im Root) statt alles auf einmal zu laden, wenn das Kontextfenster knapp wird.

## Schritt 2 — Drei Prüfungen

**a) Widersprüche zwischen Artikeln**
Suche nach Aussagen zum selben Thema/Tool/Konzept in verschiedenen Dateien, die sich widersprechen (z.B. unterschiedliche Funktionsbeschreibungen desselben Features, widersprüchliche Zahlen/Daten). Notiere Datei + Zeile/Abschnitt beider Fundstellen.

**b) Unbelegte Behauptungen**
Viele Zusammenfassungen haben bereits einen Abschnitt `## Zu prüfen` mit offenen Verifikationspunkten — sammle diese. Suche zusätzlich nach neuen unbelegten Behauptungen (Marketing-Aussagen, Statistiken ohne Quelle, Zitate ohne Fundstelle), die noch nicht als "zu prüfen" markiert sind.

**c) Wiederkehrende Themen ohne eigenen Artikel**
Sammle Themen-Tags/Kernkonzepte, die in mehreren Notizen auftauchen (z.B. "Agent Loop", "MCP", "Skills", "Progressive Disclosure"). Prüfe pro Thema, ob es bereits eine eigene, fokussierte Datei dazu gibt (nicht nur Erwähnungen innerhalb anderer Zusammenfassungen). Themen, die in **3 oder mehr** Notizen vorkommen, aber keinen eigenen Artikel haben, sind Kandidaten für einen neuen Übersichtsartikel.

## Schritt 3 — Report schreiben

Schreibe/überschreibe `notes-audit-report.md` im Repo-Root mit diesem Aufbau:

```markdown
# Notes Health Check — {Datum}

## Widersprüche
- ...

## Unbelegte Behauptungen
- ...

## Themen-Kandidaten für einen eigenen Artikel
- **{Thema}** — erwähnt in: {Datei1}, {Datei2}, {Datei3}
```

Leere Abschnitte explizit als "Keine gefunden" kennzeichnen statt wegzulassen — das macht den Report über die Zeit vergleichbar.

## Schritt 4 — Kurzfassung im Chat

Nach dem Schreiben des Reports: fasse die drei Abschnitte in 3-5 Sätzen im Chat zusammen, nicht den ganzen Report wiederholen. Verlinke auf `notes-audit-report.md` für Details.

Wenn ein klarer Top-Kandidat für einen neuen Übersichtsartikel existiert, biete an, ihn zu entwerfen — aber lege ihn nicht ungefragt an.

## Hinweis zur Wiederholung

Dieser Skill ist für regelmäßige, manuell oder per Cron ausgelöste Durchläufe gedacht (z.B. wöchentlich über den `schedule`-Skill). Er selbst richtet keinen Cron-Job ein — falls gewünscht, das explizit über `/schedule` einrichten.
