---
name: research-verify
description: Klärt offene oder widersprüchliche Behauptungen per paralleler Recherche-Subagents (einer pro Frage/Quellentyp) und lässt einen eigenständigen, skeptischen Prüf-Agent die Funde unabhängig gegenchecken. Nutzen bei "recherchiere das", "prüfe das im Internet", bei offenen "Zu prüfen"-Punkten aus einer Video-Zusammenfassung oder einem Notes-Health-Check, oder bei einem gefundenen Widerspruch zwischen zwei Dateien.
allowed-tools: Agent, Read, Edit, Grep, Glob
user-invocable: true
---

# /research-verify — Recherche mit unabhängiger Gegenprüfung

Für Fälle, in denen eine einzelne Websuche nicht reicht: mehrere offene oder widersprüchliche Behauptungen, die echte Primärquellen brauchen, plus eine zweite, unabhängige Instanz, die die Recherche nicht einfach glaubt, sondern selbst nachprüft. Dieses Muster hat sich zweimal bewährt (Wasserzeichen-Übersetzungs-Widerspruch zwischen zwei Video-Zusammenfassungen; drei offene Fragen aus `loop-engineering-ueberblick.md`) und wurde deshalb hier als eigener Skill festgehalten, statt es jedes Mal neu zu improvisieren.

## Wann passt das (und wann nicht)

Passt: 2-4 klar abgrenzbare, per Websuche prinzipiell klärbare Fragen — z. B. widersprüchliche Zahlen zwischen zwei Dateien, ein Datum, eine Preis-/Tarif-Behauptung, eine Zitat-Zuschreibung.

Passt nicht: Fragen ohne mögliche externe Quelle (z. B. eine unscharfe Zahl aus einem privaten Video-Frame, eine rein persönliche Meinungsäußerung eines Hosts ohne Faktenanspruch) — die gehören als dauerhaft offen markiert, nicht in diesen Skill gesteckt. Auch nicht für eine einzelne, simple Faktenfrage, die eine normale `WebSearch` in derselben Antwort klärt — der Mehraufwand von Subagents + Prüf-Agent lohnt sich erst ab mehreren parallelen Fragen oder bei einem Fund, der eine bestehende Notiz korrigieren würde (dort will man vor dem Ändern einer Datei besonders sicher sein).

## Schritt 1 — Fragen zuschneiden

Jede Frage bekommt einen eigenen Agent. Zuschnitt entweder nach **Einzelfrage** (z. B. "stimmt Datum X", "gilt Preis Y", "sind Zahl A und Zahl B derselbe Test") oder nach **Quellentyp**, wenn es um eine einzelne, aber vielschichtige Behauptung geht (z. B. offizielle Herstelleraussage vs. akademische Literatur vs. unabhängiger Praxistest). Nicht künstlich weiter aufteilen als die Fragen es hergeben — 2-4 Agents sind der Regelfall.

## Schritt 2 — Recherche-Agents parallel im Hintergrund starten

Pro Frage ein `Agent`-Aufruf (`subagent_type: general-purpose`, `run_in_background: true`), alle im selben Antwort-Turn. Jeder Prompt braucht:

- **Die konkrete Behauptung im Wortlaut**, inkl. Dateiverweis(e) im Repo, aus denen sie stammt — der Agent kennt den bisherigen Chat-Verlauf nicht.
- **Explizite Anweisung, Primärquellen selbst zu fetchen** (`WebSearch` + `WebFetch`), nicht nur Suchergebnis-Snippets zu zitieren.
- **Ausdrücklich: keine Erfindung, keine geratene Auflösung.** Wenn nichts Eindeutiges gefunden wird, das offen so berichten statt eine plausibel klingende, aber unbelegte Versöhnung der Zahlen/Fakten zu konstruieren.
- **Kompaktes Berichtsformat** (unter 200-300 Wörter): gefundene Quellen mit URL, exakte Zahlen/Zitate, eigene Konfidenz-Einschätzung.

## Schritt 3 — Warten, bis alle Recherche-Agents fertig sind

Nicht vorzeitig synthetisieren. Jede Fertigmeldung kurz quittieren (ein Satz), aber erst nach der letzten den nächsten Schritt starten — der Prüf-Agent braucht alle Funde auf einmal.

## Schritt 4 — Einen skeptischen Prüf-Agent starten

Ein weiterer `Agent`-Aufruf (`run_in_background: true`), der die Funde aller Recherche-Agents bekommt — als Behauptungen mit Quellen-URLs, nicht als Weiterleitung der rohen Subagent-Transkripte. Instruiere ihn ausdrücklich:

- **Primärquellen selbst erneut fetchen**, nicht den Recherche-Agents einfach glauben.
- **Aktiv nach Fehlern suchen**: falsch zitierte Zahlen, eine Schlussfolgerung, die die Quelle nicht wirklich hergibt, ein Link, der nicht existiert oder etwas anderes zeigt als behauptet.
- **Pro Frage ein Verdikt**: CONFIRMED / PARTIALLY CONFIRMED (mit genauer Angabe, was falsch war) / UNABLE TO VERIFY (nicht einfach dem Recherche-Agent das Feld überlassen, wenn der Prüf-Agent selbst nicht zugreifen konnte).
- Kompakt (unter 400 Wörter für alle Fragen zusammen).

## Schritt 5 — Synthese im Chat

Pro Frage in 1-2 Sätzen: Ergebnis, Konfidenz, Quelle. Kein Rohdump der Agent-Berichte.

## Schritt 6 — Nur nach Zustimmung in Dateien nachtragen

Ergebnisse, die eine bestehende Notiz korrigieren oder eine offene Frage auflösen, **nicht automatisch einpflegen** — fragen, ob nachgetragen werden soll. Bei Zustimmung: bestehenden Inhalt nicht löschen/überschreiben, sondern als datierten Zusatz ("Nachtrag"/"Korrektur", mit Datum, Quellen-Links und Konfidenz-Einschätzung) an der betroffenen Stelle (meist `## Zu prüfen`) ergänzen — in **allen** betroffenen Dateien, falls der Widerspruch mehrere Dateien betraf, mit Querverweisen aufeinander.

## Hinweis zur Wiederholung

Kein eigenständiger Cron-/Wiederholungs-Anwendungsfall — wird typischerweise aus `notes-audit` (offene Punkte aus einem Health-Check) oder `watch-playlist` (ein während der Video-Auswertung gefundener Widerspruch) heraus manuell angestoßen.
