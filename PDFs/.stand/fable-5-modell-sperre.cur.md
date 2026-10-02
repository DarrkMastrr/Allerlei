# Fable 5 / Mythos 5 — die Exportkontroll-Sperre (Juni/Juli 2026)

Quellen: [video-summary-6LVB3mpPvB4.md](video-summary-6LVB3mpPvB4.md) ("Fable 5 gesperrt!"), [video-summary-WVHfDaawIRk.md](video-summary-WVHfDaawIRk.md) ("Fable 5 ist ZURÜCK!"), Kontext auch in [video-summary-5Tj88qDPrFw.md](video-summary-5Tj88qDPrFw.md) ("Lokale KI ist endlich brauchbar")

**Fact-Check-Status: durchgeführt am 2026-07-04 per Web-Recherche. Die Geschichte ist real und in den Kern-Fakten sehr genau — keine Erfindung oder Übertreibung der Videos.**

Drei von 14 angeschauten Videos behandeln unabhängig voneinander dasselbe Ereignis — deshalb als eigenes Thema zusammengefasst statt in den Einzel-Summaries verstreut.

## Was passiert ist (chronologisch)

1. **9. Juni 2026** — Anthropic launcht öffentlich **Claude Fable 5** (Teil der "Mythos"-Modellklasse), plus das noch stärkere **Mythos 5** für einen engen Partnerkreis (Project Glasswing / US-Regierung). Preise: 10 $ / 1 Mio. Input-Tokens, 50 $ / 1 Mio. Output-Tokens — exakt doppelt so teuer wie Opus 4.8 Standard (5 $ / 25 $).
2. **12. Juni 2026** — Amazon-Sicherheitsforscher zeigen einen Jailbreak, der Fable 5 dazu bringt, Exploits für bekannte Software-Schwachstellen zu liefern. Amazon-CEO Jassy meldet dies ans Weiße Haus. Das US-Handelsministerium (Commerce/BIS) verhängt per "deemed export rule" eine weltweite Sperre für alle Nicht-US-Bürger — auch für im Ausland lebende Anthropic-Mitarbeiter selbst. Anthropic konnte Nutzerherkunft technisch nicht sauber genug filtern, daher traf die Sperre faktisch alle Nicht-Amerikaner.
   - Umstritten: Über 100 Cybersecurity-Experten (u.a. Katie Moussouris) widersprachen der Einstufung als "Guardrail-Bypass" — sahen darin kein einzigartiges neues Risiko.
3. **~1. Juli 2026** (nach ca. 18-20 Tagen) — BIS hebt die Kontrolle wieder auf. Modell kehrt zurück mit verbessertem Cybersecurity-Klassifikator (blockiert die Amazon-Technik in >99% der Fälle).

## Die drei Filterschichten (seit Relaunch verschärft)

- **Cybersecurity** — Aufspüren/Ausnutzen von Schwachstellen
- **Biologie/Chemie** — Dual-Use-Risiko bei gentechnischer Virenanalyse (Fable 5 soll hier laut Anthropic sogar spezialisierte Bio-Modelle übertreffen)
- **Distillation** — Schutz gegen Modell-Diebstahl

Bei Verdacht schaltet ein Klassifikator automatisch auf Opus 4.8 zurück. Nebeneffekt: auch harmlose Coding-/Debugging-Anfragen werden häufiger fälschlich blockiert.

## Weitere bestätigte Einzelfakten

- **Alibaba-Distillation-Vorwurf:** Anthropic beschuldigt Alibaba, zwischen April und Juni 2026 ca. 25.000 Fake-Accounts und **28,8 Mio.** Anfragen genutzt zu haben, um Qwen per Distillation aufzuwerten.
- **Stripe-Beispiel:** Migration einer 50-Mio-Zeilen-Ruby-Codebasis in einem Tag statt über zwei Monaten Teamarbeit — bestätigt durch Anthropics Launch-Post und ein Statement von Stripe-Entwickler Nate Berkopec.
- **Nutzungslimit:** Pro-/Max-/Team-Nutzer konnten bis 7. Juli 2026 bis zu 50% ihres wöchentlichen Limits für Fable 5 nutzen, danach nur noch über separat abgerechnete Usage Credits.

## Quellen (aus der Fact-Check-Recherche)
- [Anthropic: Fable/Mythos Launch](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Anthropic: Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)
- [Anthropic: Statement zur Sperre](https://www.anthropic.com/news/fable-mythos-access)
- [CNBC, 30.06.2026](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)
- [CyberScoop — Kritik der Security-Community](https://cyberscoop.com/cybersecurity-experts-anthropic-fable-5-not-unique-ai-threat/)
- [Tom's Hardware — Alibaba-Vorwurf](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude)
- [Nate Berkopec (Stripe) auf X](https://x.com/nateberkopec/status/2064449418196340874)

## Einordnung für die eigene Praxis
Der Vorfall ist ein reales Beispiel für das Risiko, das [video-summary-6LVB3mpPvB4.md](video-summary-6LVB3mpPvB4.md) und [video-summary-5Tj88qDPrFw.md](video-summary-5Tj88qDPrFw.md) beide ansprechen: Wer sich vollständig auf ein einzelnes, fremdes KI-Modell verlässt, kann über Nacht den Zugriff verlieren — aus politischen, nicht aus technischen Gründen. Beide Videos leiten daraus ab, in Tool-Unabhängigkeit (mehrere Harnesses/Modelle testen), eigene toolagnostische Wissensbasis und ggf. lokale/quelloffene Alternativen (siehe [lokale-ki.md](lokale-ki.md)) zu investieren.
