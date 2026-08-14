# "Forscher knacken verschlüsselte KI-Gedanken – mit einer anderen KI"

**Kanal:** heise & c't
**URL:** https://www.youtube.com/watch?v=6YFN2GiGyHg
**Länge:** 08:47
**Zusammenfassung erstellt:** 2026-08-14

---

## Ausgangslage: Warum verschlüsselte Reasoning-Blöcke überhaupt existieren

Moderne Reasoning-Modelle (GPT-5, Claude, Gemini) "denken" intern in mehreren Schritten, bevor sie eine sichtbare Antwort ausgeben — Ansätze werden verworfen, andere ausprobiert. Diese internen Denkprozesse sind für die Anbieter wertvoll, weil sie viel über die Funktionsweise eines Modells verraten. OpenAI, Anthropic und Google zeigen sie Nutzern deshalb meist nicht im Klartext, sondern übertragen sie in verschlüsselter Form — ein "Reasoning-Block", der ohne den passenden Schlüssel nur wie Datenmüll aussieht.

## Der Trick: Entschlüsselung per schwächerem Modell

Die Forscher haben die Verschlüsselung nicht im klassischen Sinn geknackt (kein gestohlener Schlüssel, kein Brute-Force). Stattdessen fütterten sie einen abgefangenen, verschlüsselten Reasoning-Block eines starken Modells in ein **schwächeres Modell derselben Anbieter-Modellfamilie**. Da die Infrastruktur des Anbieters den fremden Block anstandslos akzeptiert und für das schwächere Modell wieder lesbar macht, mussten die Forscher das schwächere Modell nur noch dazu überreden bzw. per Jailbreak dazu bringen, den entschlüsselten Inhalt preiszugeben (im Video als Grafik bei t≈02:24 gezeigt: starkes Modell → verschlüsselter Block → schwächeres Modell + Jailbreak/Überreden → Inhalt wird ausgeplaudert).

## Die Studie: 315.000 gefundene Reasoning-Blöcke

Die Forscher sammelten über **315.000 verschlüsselte Reasoning-Blöcke** aus öffentlich zugänglichen Repositories (z. B. von Entwicklern veröffentlichte Session-Logs, Benchmarks, Bug-Hunting-Protokolle) und fanden darin hunderte sensible Informationen — u. a. persönliche Daten und Zugangsdaten (Passwörter, API-Keys). Besonders problematisch: Ein Teil dieser Informationen existierte offenbar **ausschließlich** im internen Denkprozess, tauchte also nie in der sichtbaren KI-Antwort auf. Wichtige Einschränkung, die im Video explizit betont wird: Das ist **kein Generalschlüssel** für die Chats aller ChatGPT-/Claude-/Gemini-Nutzer — untersucht wurden nur Reasoning-Blöcke, die durch Entwickler (z. B. beim Veröffentlichen von Agenten-Logs) öffentlich geworden waren.

## Warum Anbieter ihre Denkprozesse schützen: Distillation

Ein zweiter Grund für die Verschlüsselung ist der Schutz der eigenen Trainingsinvestition: Wer den Lösungsweg eines starken Modells sehr genau beobachten kann, kann diese Information nutzen, um ein eigenes (Konkurrenz-)Modell zu trainieren — Stichwort **Distillation**. Je mehr Einblick in den Lösungsweg, desto wertvoller die Trainingsdaten für Dritte. Damit wird aus dem Datenschutzproblem laut Video auch ein handfestes Geschäftsproblem für die Anbieter selbst — was laut Host tendenziell positiv ist, weil sie dadurch stärker motiviert sind, es zu lösen.

## Risiko: Prompt Injection über unsichtbare Inhalte

Die Forscher beschreiben zusätzlich ein Angriffsszenario über Prompt Injection: Verschlüsselte Reasoning-Blöcke könnten versteckte, für Nutzer unsichtbare Anweisungen enthalten. Das System verarbeitet damit Inhalte, deren Inhalt Nutzer selbst nicht überprüfen können — aus Sicherheitssicht eine unangenehme neue Angriffsfläche.

## Reaktion der Unternehmen / Fazit

Die betroffenen Anbieter wurden informiert; laut Video ist zumindest ein Teil der beschriebenen Angriffe inzwischen entschärft — das gezeigte Verfahren zum Extrahieren privater Informationen soll laut den Forschern nicht mehr funktionieren. Teile der Reasoning-Traces sollen aber weiterhin rekonstruierbar sein. Kernlehre laut Host: eine klassische IT-Security-Lektion in neuem Gewand — Verschlüsselung allein macht Daten nicht automatisch sicher; entscheidend ist auch, wer sie andernorts wieder entschlüsseln kann. Für Nutzer bleibt die alte Grundregel bestätigt: keine Passwörter/API-Keys/sensiblen Daten an KI-Tools weitergeben — auch wenn es in diesem Fall "nur" eine Studie war.

## Werbe-Hinweis (im Video)

Von ca. 02:47 bis 03:47 folgt ein als "WERBUNG" gekennzeichneter, thematisch unabhängiger Sponsoring-Block für den KI-Aggregator-Dienst "Mammouth" (Zugriff auf mehrere KI-Modelle über ein Abo). Laut Videobeschreibung: Starterpaket ab 9,92 €/Monat (jährliche Zahlung) bzw. 11,90 €/Monat (monatlich). Für die inhaltliche Kernaussage des Videos ohne Relevanz.

## Einordnung für Organisation/Sicherheit

Für die Team-/Prozessperspektive besonders relevant, auch wenn im Video primär allgemein an Endnutzer gerichtet:
- **Bestätigt und verschärft bestehende interne Regel:** Das im Repo bereits dokumentierte Prinzip "keine vertraulichen Daten in öffentliche KI-Tools" (siehe [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md), Abschnitt 6) bekommt hier einen konkreten technischen Grund obendrauf: Selbst wenn eine sensible Eingabe nie in der sichtbaren Chat-Antwort auftaucht, kann sie trotzdem im internen (eigentlich verschlüsselten) Reasoning-Block landen und von dort potenziell wieder auslesbar sein.
- **Konkret handlungsrelevant beim Veröffentlichen von Agenten-Logs:** Wer im Team KI-Agenten-Sessions, Benchmark-Ergebnisse oder Debugging-Protokolle veröffentlicht oder in Bugtrackern/Repositories teilt, sollte nicht nur die sichtbare Konversation, sondern auch enthaltene verschlüsselte Reasoning-Blöcke als potenziell sensibel behandeln — genau dieser Fall war laut Studie die Hauptquelle der 315.000 gefundenen Blöcke.
- **Neue Angriffsfläche bei Agentic-Workflows:** Die beschriebene Prompt-Injection-Variante über unsichtbare Reasoning-Inhalte ist für Teams relevant, die zunehmend mehrstufige KI-Agenten einsetzen (vgl. Themen in [ai-agent-workflow.md](../ai-agent-workflow.md)) — ein weiterer Grund, Agenten-Ausgaben/-Aktionen nicht blind zu vertrauen.

---

## Kernbotschaft

Forscher zeigen, dass sich die verschlüsselten internen "Denkprozesse" von Reasoning-Modellen (GPT-5, Claude, Gemini) nicht durch Kryptoanalyse, sondern durch einen Architektur-Trick auslesen lassen: Ein abgefangener Reasoning-Block wird einem schwächeren Modell derselben Modellfamilie vorgelegt, dessen Anbieter-Infrastruktur ihn klaglos entschlüsselt — das schwächere Modell muss dann nur noch überredet werden, den Inhalt preiszugeben. An über 315.000 öffentlich gefundenen Reasoning-Blöcken fanden die Forscher hunderte sensible Daten (Passwörter, API-Keys, persönliche Informationen), teils ausschließlich im unsichtbaren Denkprozess versteckt. Kein Generalschlüssel für alle Nutzerchats, aber ein klarer Beleg, dass Verschlüsselung allein nicht reicht, wenn sie an anderer Stelle im System klaglos wieder aufgehoben werden kann — und ein zusätzlicher Grund, keine sensiblen Daten in KI-Tools einzugeben.

## Themen-Tags

KI-Sicherheit, Reasoning-Modelle, Verschlüsselung, GPT-5, Claude, Anthropic, Gemini, Google, Prompt Injection, Distillation, Datenschutz, API-Keys, IT-Security, heise/c't

## Zu prüfen

- **Kernmechanismus und 315.000-Zahl (durchgeführt, bestätigt):** Eine Websuche bestätigt, dass diesem Video eine reale Forschungsarbeit zugrunde liegt: "Stealing Reasoning Traces from Proprietary LLM APIs" (arXiv 2608.09867, veröffentlicht ca. 10. August 2026, Autoren u. a. von MATS Research, ELLIS Institute Tübingen, Max Planck Institute for Intelligent Systems und der Sicherheitsfirma Snyk). Die Kernaussagen passen zusammen: ein von Anbietern verwendeter, modellfamilien-weiter statt session-spezifischer Verschlüsselungsschlüssel ermöglicht das im Video beschriebene Entschlüsseln über ein schwächeres Geschwistermodell; unabhängige Quellen (u. a. heise.de selbst, thehackernews.com) nennen exakt die Zahl 315.320 rekonstruierte Reasoning-Blöcke aus rund 6.708 öffentlichen Agent-Trajektorien — deckt sich mit der im Video gezeigten "315.000 Blöcke".
- **Genaue Aufschlüsselung der gefundenen Zugangsdaten (nicht abschließend geklärt):** Sekundärquellen zur Studie nennen uneinheitliche Detailzahlen für gefundene Credentials/PII (z. B. "704 Artefakte inkl. 62 API-Keys/33 Passwörter/24 Access-Tokens/30 E-Mails" in einer Quelle, "367 PII-Artefakte und 182 Credentials" in einer anderen) — die Zahlen widersprechen sich zwischen den referierenden Artikeln und wurden nicht am Original-Paper selbst verifiziert. Das Video selbst nennt hier ohnehin nur "hunderte" ohne genaue Aufschlüsselung, diese vagere Aussage ist also unproblematisch.
- **Aussage, betroffene Angriffe seien bereits entschärft:** Stammt direkt aus dem Video/den Forschern, wurde nicht unabhängig gegengeprüft (z. B. keine eigene Bestätigung von OpenAI/Anthropic/Google eingeholt).
- **Kreuzcheck gegen bestehende Notizen:** Thematische Überschneidung mit [video-summary-WVHfDaawIRk.md](video-summary-WVHfDaawIRk.md), das bereits "Distillation" als Anthropic-Schutzmechanismus nennt (Alibaba-Vorwurf, tausende Fake-Accounts) — kein Widerspruch, sondern dieselbe Grundmotivation (Schutz vor Modell-Abkupfern) aus zwei verschiedenen Blickwinkeln. Ebenfalls thematisch verwandt: [video-summary-XEbR5qmxGQ0.md](video-summary-XEbR5qmxGQ0.md) (unsichtbare Reasoning-Tokens, dort aus Kostenperspektive) und die bestehende Vertraulichkeits-Richtlinie in [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md) Abschnitt 6, die durch dieses Video eine konkrete technische Begründung bekommt. Kein inhaltlicher Widerspruch zu bestehenden Notizen gefunden.

**Hinweis zum Ablauf:** Native YouTube-Untertitel (Englisch, automatisch generiert bzw. vom Kanal bereitgestellt) waren verfügbar und wurden verwendet; kein Whisper-Fallback nötig. Die deutschsprachigen On-Screen-Grafiken (Diagramm, Kapitel-Zwischentitel) stammen aus den gelesenen Frames.
