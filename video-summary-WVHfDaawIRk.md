# "Fable 5 ist ZURÜCK! Alles was du jetzt wissen musst"

**Kanal:** Julian Ivanov | KI-Automatisierung
**URL:** https://www.youtube.com/watch?v=WVHfDaawIRk
**Länge:** 15:18
**Zusammenfassung erstellt:** 2026-07-04

---

## Rückkehr nach Sperrung
Claude Fable 5 — laut Video das leistungsstärkste bisher veröffentlichte Anthropic-Modell — war rund zwei Wochen gesperrt, nachdem Amazon-Forscher gezeigt hatten, dass sich das Modell dazu bringen ließ, Sicherheitslücken in Software aufzuspüren. Die US-Regierung reagierte mit Exportkontrollen. Jetzt ist das Modell zurück, mit verschärften Filtern und eingeschränkter Verfügbarkeit.

**Vollständiger Fact-Check inkl. Quellen:** [fable-5-modell-sperre.md](fable-5-modell-sperre.md) — die Geschichte ist real, in den Kern-Fakten sehr genau bestätigt.

## Zugang und Kosten
- Bis 7. Juli: Pro-, Max- und Team-Nutzer können bis zu 50% ihres wöchentlichen Limits für Fable 5 nutzen, ohne Aufpreis
- Fable 5 verbraucht das Kontingent deutlich schneller als andere Modelle
- Nach dem 7. Juli nur noch über separat abgerechnete "Usage Credits"
- Freeplan: kein Zugang. API-Preise: 10 $ / 1 Mio. Input-Tokens, 50 $ / 1 Mio. Output-Tokens — doppelt so teuer wie Opus 4.8
- Verfügbar in Claude Desktop, Web, Claude Code, Cowork und Claude Design

## Die drei neuen Filterbereiche
Fable 5 ist technisch identisch mit "Mythos 5", läuft aber hinter zusätzlichen Klassifizierungsmodellen, die bei Verdacht auf Opus 4.8 zurückschalten:
- **Cybersecurity** — Aufspüren/Ausnutzen von Schwachstellen
- **Biologie/Chemie** — breiter Filter (Dual-Use-Risiko bei gentechnischer Virenanalyse)
- **Distillation** — Schutz gegen Auslesen des Modells zum Training von Konkurrenzmodellen (Anthropic wirft Alibaba vor, dies über tausende Fake-Accounts versucht zu haben)

Anthropic räumt ein, dass der neue Klassifikator auch harmlose Programmier-/Debugging-Anfragen häufiger fälschlich blockiert.

## Praxistest: Landingpage im Apple-Stil
Fable 5 baut eine komplette Landingpage für ein fiktives Smartphone im Apple-Stil (Scraping via Firecrawl, KI-Bilder/Videos). Ergebnis nach ~30 Minuten: 9/10, Scroll-Animationen fehlten zunächst.

## Weitere Tests: Wo die Filter greifen
- Login mit Passwort-Hashing bauen: kein Filter, eigenständig umgesetzt
- Code auf Sicherheitslücken analysieren: Filter griff, Wechsel zu Opus 4.8
- Heimnetzwerk-Port-Scanner: Wechsel zu Opus 4.8
- mRNA-Technologie erklären / Aspirin-Synthese: beide harmlosen Fragen lösten Wechsel zu Opus 4.8 aus
- Distillation-Versuch (30 Beispieldialoge generieren): auch von Opus 4.8 verweigert

## Fazit des Hosts
Für die meisten Aufgaben kein spürbarer Unterschied. Beispiel für reine Modellstärke: Stripe soll mit Fable 5 eine 50-Mio-Zeilen-Codebasis an einem Tag migriert haben, wofür ein Team sonst über zwei Monate gebraucht hätte.

---

## Kernbotschaft
Fable 5 ist zurück und in der Modellqualität weiterhin top, kommt aber mit spürbar strengeren, dreigleisigen Sicherheitsfiltern (Cyber, Bio/Chemie, Distillation), die bei sensiblen Anfragen automatisch auf Opus 4.8 zurückfallen. Verfügbarkeit ist bis 7. Juli befristet günstig, danach nur noch kostenpflichtig.

## Themen-Tags
Claude Fable 5, Anthropic, KI-Sicherheit/Guardrails, Agentic Coding, Claude Code, Modellvergleich, Preismodell/API-Kosten

## Zu prüfen — GEPRÜFT (2026-07-04)
- API-Preise (10$/50$ pro 1M Tokens), 50%-Nutzungslimit bis 7. Juli, Stripe-Beispiel — **alle bestätigt real**, siehe [fable-5-modell-sperre.md](fable-5-modell-sperre.md)
- Alibaba-Vorwurf: Zahlen im Video (~25.000 Accounts, ~28 Mio. Anfragen) — **bestätigt, exakter Wert 28,8 Mio.**
- Behauptung, Fable 5/Mythos 5 performe bei Bio-/Gentherapie-Aufgaben besser als Spezialmodelle — laut Anthropics Launch-Post plausibel, aber nicht unabhängig verifiziert
