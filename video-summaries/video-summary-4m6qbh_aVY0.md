# "Mein ARBEITSTAG mit KI 2026: ChatGPT, Claude & Co.!"

**Kanal:** Christoph Magnussen (Gründer von Blackboat)
**URL:** https://www.youtube.com/watch?v=4m6qbh_aVY0
**Länge:** 29:11
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [ai-agent-workflow.md](../ai-agent-workflow.md) für die destillierten Agent-Workflow-Prinzipien (starke inhaltliche Überschneidung mit Christophs "Intent/Judgment/Responsibility"), [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) für die Claude-Code-vs-Cowork-Einordnung, [mcp-ueberblick.md](../mcp-ueberblick.md) für MCP.*

Christoph (Blackboat, seit 20 Jahren im Tech-Bereich, seit 10 Jahren KI-fokussiert) zeigt als Nachfolger eines Videos von vor anderthalb Jahren einen kompletten Arbeitstag mit KI-Tools. Kernthese direkt zu Beginn: Der größte Unterschied zum letzten Mal ist das Thema **Agents** — von reinem Chat hin zu Systemen, die selbstständig Aufgaben erledigen statt nur Text zu produzieren.

## Morgens: Laptop statt Handy, Agent statt Übersicht

- Größte Verhaltensänderung: Vor anderthalb Jahren war das Smartphone das einzige Arbeitsgerät, jetzt fast ausschließlich der Laptop — Grund: Coding- und Agentic-Tools laufen primär dort
- Speech-to-Text bleibt aber konstant der erste Schritt jeden Morgens
- Erstes geöffnetes Tool: **Codex bzw. ChatGPT for Work**. Beispiel-Prompt (im Video wörtlich gezeigt): Agent soll E-Mails/Slack sichten, Termine der kommenden Woche vorbereiten, dabei nichts an Externe verschicken ohne vorherige Freigabe
- Wichtiger Unterschied zu vor einem Jahr: Ein Agent *tut* Dinge (erledigt die Aufgabe im Rahmen der vorgegebenen Guideline), ein reiner Chat hätte nur eine Zusammenfassung produziert

## Datenschutz- und Governance-Vorkehrungen (explizit erwähnt, nicht nur nebenbei)

- Interne Vorfilterung: hochvertrauliche Themen werden von der KI ferngehalten, Kunden werden nur mit internen Kürzeln referenziert statt Klarnamen
- Auftragsverarbeitungsverträge (AVV) mit OpenAI, Anthropic, Microsoft, Google für alle eingesetzten KI-Dienste
- Regeln liegen technisch in einer **Agent-MD**-Datei (Analogon zu `CLAUDE.md`/`agents.md`) hinterlegt — was der Agent darf und nicht darf
- Bei kritischen E-Mails: maximal ein KI-Entwurf, den er immer selbst noch liest, bevor etwas rausgeht ("Supervisor-Reviewer"-Prinzip)
- Unternehmensweite Leitplanken: das "Blackboat Operating System" läuft im Hintergrund bei allen Mitarbeitenden mit, überschreibt aber nicht individuelle Agent-Regeln, sondern ergänzt sie nur

## Skills und Sub-Agents

- Skill-Konzept wird direkt im Prompt demonstriert ("nutze bitte meinen Skill") — ein Skill ist laut Christoph "eine Fähigkeit, die der Agent schon mal gemacht hat"
- Neu seit wenigen Wochen: Modelle können selbst Sub-Agents launchen, ohne dass das manuell orchestriert werden muss
- Drei Dinge, die sich laut Christoph beim Arbeiten mit Agents *nicht* ändern, unabhängig von Modellfortschritt: **Intent** (was gebt ihr rein), **Judgment/Taste** (in welche Richtung geht der Agent, ist es gut oder schlecht), **Responsibility** (hängt an der Beziehung/Verantwortung im Unternehmen)

## Während der Agent arbeitet: mehr Zeit für Dinge mit echtem Input-Bedarf

- Zeitersparnis fließt laut Christoph explizit in mehr Arbeit an Tools, Coding, Konzepten und Kundenbeziehungen — Dinge, für die er keine KI alleine losschicken will
- Praxisbeispiel Büroeinrichtung: Prompt an den Agent, USM-Regale zu recherchieren und Angebote vorzubereiten, ausdrücklich mit der Einschränkung "noch nichts kaufen, noch nichts abschicken" — der Agent bereitet nur bis zur Entscheidungsreife vor
- Konzeptioneller Punkt: zielbasierte Agents ("kümmere dich um die komplette Büroeinrichtung") könnten theoretisch autonom laufen, bis ein prüfbares Ziel erreicht ist — Christoph nennt das als kommenden Trend, aber mit der Einschränkung, dass der Agent bei nicht überprüfbaren Zielen selbst meldet, dass er das nicht bewerten kann
- **Compounding**: nach jeder Interaktion dem Agent explizit sagen, was er sich fürs nächste Mal merken soll ("das merkt sich bitte für das nächste Mal") — Agent lernt so kontinuierlich Präferenzen dazu

## Von 15 Terminalfenstern zu aufgeräumten Agent-Apps

- Schmerzpunkt aus Februar 2026 explizit benannt: 15 parallele Terminalfenster, mehrere Git-Worktrees, keine Persistenz — Terminal versehentlich geschlossen, Arbeit weg
- Diese Reibung sei der Auslöser für die schnelle Entwicklung vernünftiger Agent-Apps (raus aus dem nackten Terminal) gewesen
- Ausblick auf noch mehr Autonomie: Budget-basierte Prompts ("dieses Thema ist mir 100 € an Tokens wert, entscheide selbst welches Modell, bleib aber sparsam")
- **Codex Micro** wird gezeigt (Produktseite, 230 €) — ein von OpenAI mit Work Louder entwickeltes physisches Eingabegerät (Makropad mit Tasten/Dial/Joystick) zur Steuerung von Codex-Agents. Per Websuche verifiziert: real existierendes, im Juli 2026 gelauntes Produkt, kein Fake

## Terminvorbereitung als Beispiel-Workflow (komplett in einer App)

- Konkretes Beispiel: Termin mit Kollege Hanno zur Videoaufnahme vorbereiten — Agent soll (1) Kontext in den Kalendereintrag schreiben, (2) eine erarbeitete Modell-Matrix als Bild per Mail schicken, (3) die meistgesehenen YouTube-Videos zum Thema heraussuchen und verlinken
- Bewusste Modellwahl: für diese vergleichsweise einfache Aufgabe wird explizit *nicht* das stärkste (teuerste) Modell verwendet ("Luna Max" laut Transkript — Modellname unsicher, siehe Zu-prüfen-Abschnitt), sondern ein günstigeres, passendes Modell
- Explizit genannter Fehler großer Einsteiger: immer das beste Modell nutzen, obwohl die Aufgabe das nicht braucht → verbrennt unnötig Tokens
- Kompletter Workflow bleibt in einer einzigen App (hier Codex) — funktioniert laut Christoph genauso in Claude, Claude Cowork oder Cursor

## Mobile Fernsteuerung

- Codex und Claude lassen sich laut Video seit wenigen Wochen per QR-Code-Scan vom Smartphone aus fernsteuern, während der eigentliche Agent lokal auf dem Rechner weiterläuft (Settings → Computernutzung → Verbindungen)
- Bewusste Transparenz-Praxis erwähnt: intern wird jede von einem Agent verschickte Slack-Nachricht markiert ("Sent by ChatGPT"/von Codex verschickt), Christoph bemerkt live, dass diese Markierung bei einer Mail fehlte und will das nachprüfen

## Wo Christoph unterwegs arbeitet — und warum zwei Haupttools

- Unterwegs nutzt er ChatGPT, Claude (Chat) und Perplexity eher zum Brainstormen/Ideen spiegeln, mit Export-Möglichkeit in die Agent-Tools
- Begründung für Dual-Nutzung Claude + ChatGPT: "das sind die beiden Führenden, die möchte ich beide gut beherrschen" — plus Erwartung, dass 2026 weitere Anbieter mit anderen Ansätzen in diese Kategorie vordringen

## Design-Aufgabe → gezielt Claude statt Codex/ChatGPT

- Für eine spontane Design-Aufgabe (Landingpage für ein fiktives "Summer School Alumni"-Event) wechselt Christoph bewusst zu **Claude Design**, Modell Opus 4.8 — Begründung: "Anthropic hat deutlich das bessere Design meistens"
- Wichtiger Konzeptpunkt: ein einmal hinterlegtes Blackboat-Designsystem greift automatisch in allen Tools (Claude, Codex-App, ChatGPT-for-Work-App) — zentrale Style-Vorgaben lohnen sich firmenweit, statt dass jeder neu erfindet
- Betonter Effekt: nicht in erster Linie Zeitersparnis, sondern verkürzte Distanz von Idee zu einem zeigbaren Entwurf — laut Christoph "kraftvoller als schnelle Kommunikation, als mehr Effektivität"

## Wo bewusst *keine* KI eingesetzt wird

- E-Mails werden inzwischen wieder häufiger selbst beantwortet — bessere Filter, weniger Notwendigkeit für Agent-Triage, "Freude an E-Mails wiedergefunden"
- Bewusste Fallunterscheidung bei jeder Suche: klassische Google-/Dateisuche selbst durchführen vs. an einen Agent delegieren — explizit **nicht** entweder/oder
- Ausdrückliche Warnung vor Vollautomatisierung: "Large Language Models halluzinieren... ihr dürft euch bei Google darauf verlassen, dass es präziser funktioniert" als bei einer LLM-Antwort

## Calls: Transkription als Standard, mit rechtlichem Hinweis

- Meeting-Transkription ist inzwischen bei vielen Tools (Teams, Google) Standard-Voreinstellung
- Rechtlicher Hinweis (von Christoph selbst als Nicht-Rechtsberatung gerahmt): Widerspruch gegen Aufnahme in Deutschland ist keine reine Datenschutzfrage, sondern Strafrecht — heimliche Aufnahme ohne Zustimmung ist strafbar
- Praxis: bewusst entscheiden, wann *nicht* aufgenommen wird ("off the record"), aktiv nachfragen bei Tools wie Plaud
- Nutzen der Transkription: Christoph kann sich im Call auf zwischenmenschliche Nuancen konzentrieren ("was kann ein LLM nicht raushören"), während die KI Fakten mitschreibt — Nachbereitung inkl. Follow-up-Mail danach automatisiert, aber mit eigenem "Gefühl" ergänzt
- Rückbezug auf Kritik am Vorgängervideo (vor 1,5 Jahren): Nutzer bemängelten damals "Wall of Text"/Datenmüll — Christoph: Transkripte werden inzwischen routinemäßig wieder gelöscht (Datenminimierung), der Wert liegt nicht im Aufbewahren, sondern im **Compounding** (was daraus fürs nächste Mal gelernt wird)

## Workshops bleiben bewusst analog

- Workshops finden laut Video weiterhin komplett physisch mit Post-its an der Wand statt, kein digitales Whiteboard im Einsatz
- Nachbereitung trotzdem KI-gestützt: ein Foto der beschrifteten Post-its wird von multimodalen Modellen (genannt: Gemini, ChatGPT, Claude) zuverlässig genug erkannt und strukturiert übernommen — Begründung für den bewussten Verzicht auf digitale Tools: mehr Fokus auf die Menschen im Raum statt auf ein Gerät

## Wo KI keine Rolle spielt

Kinder von der Schule/Kita abholen bleibt laut Video vollständig menschliche Aufgabe — KI hilft höchstens bei der Terminlogistik drumherum, nicht beim Abholen selbst.

## Fazit-Trend: Konsolidierung zu "Super-Apps"

- Früher: viele Einzeltools (ChatGPT, NotebookLM, Kalender, Perplexity), jetzt zunehmend Bündelung in einer App — jeder Anbieter versucht, zur "Super-App" zu werden
- Christophs Einschätzung: aktuell liegt OpenAI knapp vorn, Claude ist aber deutlich stärker im Unternehmenseinsatz verankert — beides unabhängig vom Video nicht gegengecheckt, reine persönliche Einschätzung
- Schlussverweis auf MCP als Standard für Tool-Anbindung, mit Ankündigung eines vertiefenden MCP-Deep-Dives im "AI to the DNA"-Podcast (Cross-Show-Werbung, kein eigenständig prüfbarer Fakt)

---

## Kernbotschaft
Der zentrale Wandel gegenüber dem Vorgängervideo (vor 1,5 Jahren) ist der Sprung von reinem Chat zu handelnden Agenten, die über den ganzen Tag verteilt E-Mails triagieren, Termine vorbereiten, recherchieren und sogar Designentwürfe liefern — bei klarer, immer wiederkehrender Tool-Wahl-Logik: Codex/ChatGPT for Work für schnelle, günstige Agent-Workflows, Claude gezielt für Design/Kreativaufgaben, plus feste unternehmensweite Guardrails (Agent-MD, Datenminimierung, AVV) und die bewusste Entscheidung, wo Mensch statt Agent bleibt (Beziehungsarbeit, Kinderabholung, komplett analoge Workshops). Die Konstanten bleiben laut Video Intent, Judgment und Responsibility — die Technologie ändert sich schneller als diese drei Prinzipien.

## Themen-Tags
Agentic AI, ChatGPT/Codex, Claude/Claude Design, Arbeitsalltag mit KI, Agent-Guardrails, Compounding, Modellwahl/Kostenbewusstsein, Remote-Steuerung, Meeting-Transkription/Datenschutz, Super-App-Konsolidierung, MCP

## Zu prüfen
- Modellname "Luna Max" (Transkript, Whisper-generiert) — klingt nicht wie ein bekannter offizieller OpenAI-Modellname, möglicherweise Whisper-Fehltranskription eines anderen Begriffs; nicht gegengecheckt
- "Codex Micro" (physisches Eingabegerät von OpenAI x Work Louder, 230 €) — per Websuche bestätigt real und im Juli 2026 gelauncht (u. a. TechCrunch, Tom's Hardware, The New Stack); auf dem gezeigten Frame stand "Nicht verfügbar" — vermutlich nur eine ausverkaufte Variante, nicht das gesamte Produkt
- Einschätzung "Claude deutlich größer bei Unternehmen, OpenAI aktuell knapp vorn" — unbelegte persönliche Einschätzung Christophs, nicht mit Marktdaten unterlegt
- Konkrete rechtliche Aussage zu heimlichen Meeting-Aufnahmen in Deutschland als Strafrecht — plausibel und mit gängigen Presseeinordnungen vereinbar, aber im Video selbst ausdrücklich als "keine Rechtsberatung" gekennzeichnet und hier nicht juristisch verifiziert
- Interner Blackboat-Workflow-Details (Agent-MD, "Blackboat Operating System") sind firmeninterne Praxis, keine allgemein verifizierbaren Fakten — als Praxisbeispiel, nicht als Industriestandard zu lesen

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429 (bekanntes Muster, siehe [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md)). Die Transkription lief automatisch über den im watch-Skill bereits eingebauten Replicate-Whisper-Fallback mit Auto-Chunking (6 Segmente à ca. 5:30 Min., 504 Segmente gesamt) — kein manuelles Eingreifen nötig, kein Timeout. Die Zusammenfassung basiert auf diesem vollständigen Transkript plus 80 sparsam verteilten Frames (Standardwarnung des Skripts bei 29 Minuten Länge: Frame-Abdeckung ist dünn, aber bei diesem überwiegend redend-vor-der-Kamera-Format mit wenigen UI-Screenshots ausreichend für die inhaltliche Einordnung).
