# "Karpathys CLAUDE.md macht Claude Code 10x cleverer (Tutorial)"

**Kanal:** Jonas | KI Workflows
**URL:** https://www.youtube.com/watch?v=5DuHZrtmwoY
**Länge:** 12:07
**Zusammenfassung erstellt:** 2026-07-04

---

## Hintergrund: Der virale Tweet

- Andrej Karpathy hat in einem viral gegangenen Tweet typische Fehler von LLM-Coding-Agents gesammelt: falsche Annahmen ohne Nachfrage, überkomplizierte Lösungen, Anfassen von Code, der gar nicht geändert werden sollte, fehlende klare Erfolgskriterien
- Ein GitHub-Nutzer hat daraus eine einzige `CLAUDE.md`-Datei gebaut, die diese Beobachtungen in konkrete Regeln für Claude Code übersetzt

## Die vier Prinzipien der Datei

- **Think Before Coding** — Annahmen explizit machen, mehrere Interpretationen abwägen, bei Unklarheit nachfragen
- **Simplicity First** — so wenig Code wie nötig, keine Overengineering-Tendenz
- **Surgical Changes** — nur den Code anfassen, der wirklich geändert werden muss
- **Goal-Driven Execution** — ein übergeordnetes, überprüfbares Ziel festlegen, sodass Claude Code so lange iteriert, bis das Ziel nachweislich erreicht ist

## Installation (ca. 10–15 Sekunden)

- **Option A – Claude Code Plugin:** Marketplace hinzufügen, dann Plugin installieren
- **Option B – CLAUDE.md pro Projekt:** Datei per `curl` herunterladen bzw. an bestehende CLAUDE.md anhängen
- Auch für Cursor nutzbar über eine mitgelieferte Cursor-Regel-Datei

## Der Praxistest: Habit-Tracker-Erweiterung

Jonas testet die Wirkung an einem selbstgebauten Habit-Tracker. Auftrag an zwei parallele Claude-Code-Instanzen (identischer Prompt): Statistik-Seite ergänzen mit 7-Tage-Heatmap, Wochenfortschritts-Ring, Streak-Ranking und Kalenderansicht.

- **Mit CLAUDE.md (Karpathy-Guidelines):** ~7,5 Minuten, ca. 0,70 $ Kosten. Ergebnis sauber umgesetzt, einziger kleiner Mangel: Kalendertage nicht anklickbar
- **Ohne Guidelines (Standard Claude Code):** ~17 Minuten, ca. 1,42 $ Kosten. Ergebnis funktional ähnlich, aber unsauberer (alter Toggle-Bereich blieb bestehen, seitenverkehrtes Layout, inkonsistente Berechnungslogik, unerwünschte Pulsanimation)
- Fazit: Die CLAUDE.md-Version gewinnt bei erstem Versuch in Geschwindigkeit, Kosten und Sauberkeit

---

## Kernbotschaft
Eine einzige, frei verfügbare CLAUDE.md-Datei mit vier von Karpathy inspirierten Prinzipien macht Claude Code spürbar effizienter: schneller, günstiger und mit saubereren Ergebnissen als ohne diese Guidelines.

## Themen-Tags
Claude Code, Agentic Coding, CLAUDE.md, Andrej Karpathy, Prompt Engineering, Produktivitäts-Tools

## Zu prüfen — GEPRÜFT (2026-07-04)
- Repo-Attribution "GitHub-Nutzer Herobrine19"/"ferrettechang", Repo "multica-ai/andrej-karpathy-skills" — **teilweise falsch.** Das Repo wurde real von **Forrest Chang** erstellt (27.01.2026), Herobrine19 ist nur Mit-Committer. Der im Video genannte Install-Befehl (`ferrettechang/...`) existiert so nicht — vermutlich Verwechslung/Verhörer von "forrestchang". Der Repo-Pfad `multica-ai/andrej-karpathy-skills` selbst stimmt aber tatsächlich.
- Sternezahl "über 165.000" — **stimmt ungefähr** (Stand Anfang Juli 2026: ca. 165.000–187.000 Stars je nach Quelle), im Gegensatz zu Video [x-Jqu_WlEI4](video-summary-x-Jqu_WlEI4.md), das mit "über 26.000" einen veralteten Wert nennt. Vollständiger Abgleich in [karpathy-claude-md-guidelines.md](karpathy-claude-md-guidelines.md).
- Konkrete Kosten-/Zeitangaben aus dem Test (0,70 $ / ~7,5 Min. vs. 1,42 $ / ~17 Min.) — projektspezifisches Einzelbeispiel, keine belastbare allgemeine Benchmark-Aussage
- Zuschreibung "Karpathy war Head of AI bei Tesla" — genaue Jobbezeichnung/Zeitraum ggf. gegenprüfen
