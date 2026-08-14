# "Run DeepSeek V4 Flash Free Forever : Here's How"

**Kanal:** Julian Goldie SEO
**URL:** https://www.youtube.com/watch?v=SGyhrdkPO20
**Länge:** 08:24
**Zusammenfassung erstellt:** 2026-08-14

---

*Siehe auch: [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md) ("NEW Claude Obsidian 2.0 Changes Everything") — selber Kanal, selbes Format (KI-„Digital Avatar" von Julian Goldie) und exakt dasselbe werbliche Ökosystem („Agent OS", „AI Profit Boardroom", „AI Success Lab"/„AI Money Lab"). Details siehe „Zu prüfen".*

## Format des Videos

Moderator ist wie im bereits dokumentierten Schwestervideo laut Einblendung „Digital Avatar" von Julian Goldie (CEO der SEO-Agentur „Goldie Agency"), kein Live-Auftritt. Das Video wechselt durchgehend zwischen Talking-Head-Clips und Screen-Recordings: Produktseiten (DeepSeek-API-Dokumentation, Hugging Face, OpenCode), Drittanbieter-Blogartikel, die die DeepSeek-Ankündigung einordnen (u. a. „DigitalApplied", „DevDigest", „ofox.ai", Artificial Analysis, DataLearnerAI), sowie mehrere Screenshots aus Julians eigenem „Agent OS"-Dashboard und seiner „AI Profit Boardroom"-Community.

## Die eigentliche Neuigkeit: DeepSeek-V4-Flash-0731

Kern der Aussage: DeepSeek hat am 31. Juli 2026 sein kleines Modell **V4-Flash** neu post-trainiert (nicht neu architektiert) und als offiziellen „0731"-Build veröffentlicht:

- **Architektur unverändert:** 284 Mrd. Parameter gesamt, ca. 13 Mrd. aktiv (Mixture-of-Experts), 1‑Mio.-Token-Kontextfenster — dieselbe Größe wie beim April-Preview.
- **Fokus des Retrainings:** speziell Agenten- und Coding-Fähigkeiten.
- **Genannte Benchmark-Sprünge** (laut Video, im Frame als „vendor-stated … no third-party reproduction as of publish" gekennzeichnet): Terminal-Bench 2.1 von zuvor 56,9 auf 82,7; DeepSWE 54,4; „Two Lathlon verified" 70,3; Artificial Analysis Intelligence Index ca. +10 Punkte. Das kleinere Flash-Modell übertrifft laut Video auf mehreren hauseigenen Agenten-Benchmarks das größere V4-Pro-Preview.
- **Offene Gewichte:** MIT-lizenziert, laut Video am 31. Juli auf Hugging Face erschienen — ein im Video gezeigter Screenshot (Hugging-Face-Modellseite) bestätigt Link und Lizenz.
- **Wichtige Einschränkung, die das Video selbst nennt:** Das 0731-Update betrifft nur die V4-Flash-**API**. App, Web-Chat und die V4-Pro-API wurden nicht aktualisiert.
- **Preise laut gezeigtem DeepSeek-API-Dokument:** 0,0028 $/Mio. Token (Cache-Hit-Input), 0,14 $/Mio. (Cache-Miss-Input), 0,28 $/Mio. (Output). Auf demselben Screenshot steht zusätzlich ein Hinweis, den der Sprecher nicht erwähnt: DeepSeek kündigt dort selbst eine **bevorstehende, „signifikante" Preiserhöhung** für die API an.

## Der „kostenlose" Weg: OpenCode

Zentrale Setup-Anleitung: Die neue V4-Flash-0731 ist unter der Modell-ID `deepseek-v4-flash-free` kostenlos über **OpenCode** (Open-Source-Coding-Agent, opencode.ai) nutzbar — kein API-Key, keine Kreditkarte nötig, laut gezeigtem Terminal-Screenshot „no API key · cost $0". Der Sprecher weist selbst darauf hin, dass „free tiers can change" und man bei Bedarf auf DeepSeeks reguläre, „sehr günstige" API ausweichen könne.

## Hermes → OpenCode → DeepSeek: der Agenten-Stack

Vorgestellt wird ein Workflow, in dem der Orchestrierungs-Agent **Hermes** (über eine installierbare „OpenCode CLI"-Skill) Coding-Aufgaben an **OpenCode** delegiert, das wiederum DeepSeek V4-Flash als Modell im Hintergrund nutzt. Beispiel im Video: Ein an Hermes gegebener Auftrag („Content-Automatisierungssystem für Newsletter-Entwürfe bauen") wird von Hermes geplant, von OpenCode als Code umgesetzt und von DeepSeek inhaltlich befüllt — laut Sprecher fertig in unter 10 Minuten. Zusätzlich gezeigt: ein „DeepSeek Coder"-Fenster innerhalb von Julians eigenem „Agent OS"-Dashboard (Chat links, Live-Vorschau rechts) für spontane Bau-Aufträge.

## Werblicher Rahmen: Agent OS und AI Profit Boardroom

Wie im bereits dokumentierten Schwestervideo nimmt ein erheblicher Teil der Laufzeit Eigenwerbung ein:
- **„Agent OS"** — Julians eigenes Multi-Agenten-Dashboard, hier mit vorkonfiguriertem DeepSeek/OpenCode-Setup beworben, als herunterladbares Zip.
- **„AI Profit Boardroom"** — kostenpflichtige Community (Banner: „join 4.000+ founders"), beworben mit 30-Tage-Fahrplan, täglichen Tutorials, vier Live-Coaching-Calls pro Woche. Eine separate Landingpage im Video zeigt abweichende Zahlen („1.420 Mitglieder", „$2,4 Mio.+ Profit", „93 % Retention") — nicht miteinander abgeglichen, wirkt wie unterschiedliche Marketing-Snapshots derselben Community.
- **„AI Success Lab"** — kostenlose Einstiegs-Community (laut Frame „85,8k Mitglieder"), im Video als „87.000 Mitglieder" genannt — konsistent mit der im Schwestervideo dokumentierten Zahl (85.200), plausibles Wachstum.

---

## Kernbotschaft

Der Kern der Meldung — DeepSeek hat am 31. Juli 2026 sein kleines Flash-Modell (284B/13B aktiv, MIT-lizenziert, offene Gewichte auf Hugging Face) gezielt für Agenten-/Coding-Aufgaben nachtrainiert und dabei starke Benchmark-Sprünge erzielt, teils über das größere V4-Pro hinaus — ist durch mehrere unabhängige Quellen bestätigt und lässt sich tatsächlich kostenlos (wenn auch mit Limits) über OpenCodes `deepseek-v4-flash-free` nutzen. Der reißerische Titel „Free Forever" ist dabei irreführend: OpenCode selbst beschreibt sein Gratis-Kontingent als zeitlich begrenztes Promo-Angebot mit reduziertem Kontextfenster, und selbst der Sprecher relativiert das im Video. Wie im bereits im Repo dokumentierten Schwestervideo desselben Kanals dient ein Großteil der Laufzeit letztlich dem Verkauf von Julian Goldies eigenem „Agent OS"-Wrapper und seiner kostenpflichtigen „AI Profit Boardroom"-Community — die DeepSeek-Neuigkeit selbst ist der Aufhänger.

## Themen-Tags
DeepSeek V4-Flash-0731, MIT-Lizenz, Open Weights, Hugging Face, OpenCode, OpenCode Zen, Hermes Agent, Agent OS, AI Profit Boardroom, AI Success Lab, Terminal-Bench, Artificial Analysis, Julian Goldie, Digital Avatar, Coding-Agenten

## Zu prüfen

- **Release, Architektur, MIT-Lizenz/Hugging-Face-Verfügbarkeit, Terminal-Bench-Kopfzahl (82,7): per WebSearch bestätigt.** Mehrere unabhängige Quellen (MarkTechPost, DigitalApplied, deepseek.ai-Blog, datanorth.ai, Hugging-Face-Blog, opensourceforu.com) bestätigen Datum (31.07.2026), Architektur (284B total/13B aktiv), MIT-Lizenz und Terminal-Bench-2.1-Wert 82,7 unabhängig vom Video.
- **Kleine Zahlen-Diskrepanz beim Terminal-Bench-Vorher-Wert:** Das Video nennt für den April-Preview „56,9", eine unabhängige Quelle (MarkTechPost) nennt „61,8" als Vorher-Wert für denselben Vergleich. Nicht aufgelöst, ob unterschiedliche Terminal-Bench-Versionen (2.0 vs. 2.1) oder unterschiedliche Messbasis dahinterstecken — keine grobe Falschangabe, aber nicht exakt deckungsgleich.
- **Alle Balkendiagramm-Benchmarks (Cybergym, xBench-FullStack usw.) im Video selbst als „vendor-stated … no third-party reproduction as of publish" gekennzeichnet** — DeepSeeks eigene Zahlen, nicht unabhängig reproduziert; das Video übernimmt sie unkommentiert.
- **„Free Forever"-Titel vs. tatsächliche Bedingungen:** Per WebSearch bestätigt, dass OpenCodes `deepseek-v4-flash-free` real existiert, aber laut mehreren Drittquellen (ayautomate.com, ofox.ai, GitHub-Issues bei anomalyco/opencode) auf 200K statt 1M Kontext gedeckelt, ratenlimitiert und explizit als „zeitlich begrenztes Promo-Angebot" markiert ist; ein GitHub-Issue dokumentiert bereits reale „Free usage exceeded"-Fehler. Der Titel „Free Forever" ist damit eine Übertreibung, die der Sprecher im Video selbst relativiert („free doesn't mean unlimited forever").
- **Preiserhöhungs-Hinweis auf dem gezeigten DeepSeek-Doku-Screenshot** (Ankündigung einer „signifikanten" künftigen API-Preissteigerung) wird im Video gezeigt, aber vom Sprecher nicht erwähnt oder eingeordnet.
- **Testimonials und Umsatzzahlen der „AI Profit Boardroom"** (Sarah K., Marcus R., Elena V.; „$2,4 Mio.+ Profit") — reine Marketingaussagen, nicht verifizierbar/nicht geprüft.
- **Cross-Referenz zu [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md):** Bestätigt dasselbe Muster (Digital-Avatar-Format, Agent-OS/AI-Profit-Boardroom-Funnel, „AI Success Lab" als Gratis-Einstieg) bei einem anderen, unabhängigen Thema desselben Kanals — kein Widerspruch, sondern wiederkehrendes Geschäftsmodell.
- **Relevanz für die Team-/Gruppenleiter-Rolle:** Der harte Kern (kleines, MIT-lizenziertes 13B-aktiv-Coding-Modell mit stark verbesserten Agenten-Benchmarks, günstiger API und einem echten, wenn auch limitierten Gratis-Zugang über OpenCode) ist eine konkret nutzbare, kostengünstige Option zur Evaluierung als Coding-Agent-Backend — unabhängig vom werblichen Rahmen um „Agent OS"/„AI Profit Boardroom" zu bewerten, der für diese Rolle keinen eigenständigen Mehrwert bietet.

**Hinweis zum Ablauf:** Native englische YouTube-Untertitel wurden erfolgreich per yt-dlp geladen (227 Segmente), kein Whisper-Fallback nötig. Alle 80 extrahierten Frames wurden gesichtet; bei diesem bildschirmlastigen Format lieferten die Frames (Preistabellen, Lizenzangaben, Terminal-Screenshots) deutlich mehr belastbare Details als das reine Transkript.
