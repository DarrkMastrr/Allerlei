# "Automatisiere ALLES mit KI-Agenten: Der ultimative KOMPLETTKURS"

**Kanal:** Everlast AI
**URL:** https://www.youtube.com/watch?v=WHUBWM0JoDM
**Länge:** 2:19:18 (139 Min.)
**Zusammenfassung erstellt:** 2026-09-07

---

*Siehe auch: [ai-agent-workflow.md](../ai-agent-workflow.md) — behandelt die gleiche "Workflow vs. Agent"-Grundunterscheidung (dort mit Bezug auf Boris Cherny/Claude Code, hier mit Bezug auf Anthropics eigenes Agenten-Framework), allerdings für Solo-Coding-Workflows statt Geschäftsprozess-Automatisierung — kein Widerspruch, andere Domäne. [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md) und [team-ki-einstieg-notizen.md](../team-ki-einstieg-notizen.md) sind ebenfalls themenfremd (Coding-/Verifikationsdisziplin bzw. Team-Onboarding), decken aber keinen der hier gezeigten n8n/Vapi/Zapier/Make-Anwendungsfälle ab — dieses Video ist der erste Eintrag im Repo zu Business-Process-Automatisierung mit No-Code-Plattformen. [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md) dokumentiert bereits zwei Replicate-Whisper-Fehlermodi (429 Rate-Limit, 6-Minuten-Timeout) samt Chunking-Workaround — bei diesem Video trat ein dritter, dort noch nicht dokumentierter Fehlermodus auf (siehe "Zu prüfen").

## Format und Aufbau

Ein einzelner Sprecher (Talking-Head, Studio-Setting) präsentiert einen zusammenhängenden Kurs mit Whiteboard-artigen Miro/Board-Folien ("EverlastAI KI-Agenten MEGA-Kurs") und Live-Screensharing der tatsächlichen Tool-Konfiguration. Der Kurs gliedert sich klar in: (1) Grundlagenteil zu KI-Agenten, (2) fünf vollständig live gebaute Praxis-Use-Cases, (3) einen Abschlussteil mit Karriere-/Positionierungsratschlägen, der stark werblich für die eigene Firma (Everlast AI / kiberatung.de) gehalten ist.

## Grundlagenteil: Was ist ein KI-Agent? (ca. 0:00–29:56)

- Aufhänger: Aussagen von Nvidia-CEO Jensen Huang und Berichte über Einstellungsstopps bei Meta wegen KI-Agenten; gleichzeitig Beispiele für gescheiterte KI-Funktionen bei Apple (zurückgezogene Zusammenfassungsfunktion), Google (halluzinierte AI Overviews) und Amazon Alexa.
- Definition: Ein KI-Agent ist ein "digitaler Mitarbeiter", der ein Ziel eigenständig verfolgt, im Unterschied zu einem Chatbot, der nur antwortet, aber nicht handelt.
- **Zentrale Unterscheidung Workflow vs. Agent** — explizit unter Berufung auf Anthropic: Workflows sind fest definierte Wenn-Dann-Abläufe (stabil, planbar), Agenten entscheiden selbst, welche Tools sie wann in welcher Reihenfolge nutzen (flexibel, aber schwerer zu testen/kontrollieren). Kernaussage: Nicht jede Aufgabe braucht einen Agenten — oft reicht ein einfacher Workflow mit ein bis zwei LLM-Aufrufen, und Agentenkomplexität für einfache Probleme "verbaut oft den Erfolg".
- Fünf Bausteine eines Agenten: LLM (Gehirn), Prompt (Anleitung), Memory (Gedächtnis), externes Wissen (optional, z. B. RAG), Tools/APIs (erst diese machen aus einem Sprachmodell einen handelnden Agenten).
- Kurzer, korrekter API-Exkurs: GET (Daten abrufen) vs. POST (Daten ändern/erstellen) als Grundbausteine, über die Agenten mit anderer Software sprechen.
- Fünf Agenten-Kategorien: Conversational Agents (Chat-/Voice-Bots), spezialisierte Co-Piloten, Multi-Agent-Systeme (mit ausdrücklichem Warnhinweis unter Berufung auf Anthropic, dass diese oft unnötig komplex und weniger zuverlässig sind), Knowledge-Based/RAG-Agenten, Workflow-Agenten (prozessintegriert, z. B. Lead-Qualifizierung im CRM).

## Use Case 1 — Lead-Scraping-Agent (ca. 29:56–57:37)

- Werkzeug: n8n (Automatisierungsplattform, live aufgebaut), LLM GPT-4.1 Nano (Kostenabwägung live anhand der OpenAI-Pricing-Seite demonstriert: 4o-mini vs. 4.1-mini vs. 4.1-nano), Google Maps-Suche über serper.dev als HTTP-Tool, Google Sheets als Zieltabelle.
- Ablauf: Chat-Anfrage ("100 Leads aus der Möbelbranche") → Agent recherchiert über Google Maps → schreibt Ergebnisse (Adresse, Name, Telefon, Website, Bewertung) automatisch in ein Google Sheet über ein n8n-Sub-Workflow-Tool.
- Live gezeigt: erster Testlauf schlägt fehl (Tool wird nicht aufgerufen), durch Anpassung des System-Prompts (explizite Anweisung, das Speicher-Tool zu nutzen) funktioniert es beim zweiten Versuch — als Beispiel für iteratives Prompt-Engineering.

## Use Case 2 — Voice-Agent zur Lead-Reaktivierung (ca. 57:37–83:23)

- Werkzeuge: Vapi (Voice-Agent-Plattform), ElevenLabs (Stimme, Modell "Flash 2.5"), Deepgram als Transcriber (mit explizitem Hinweis, unbedingt Deutsch einzustellen), Make.com als Orchestrierung, Google Sheets als Lead-Liste.
- Ablauf: Alle Leads mit Status "offen" werden automatisiert angerufen, der Voice-Agent spricht Kunden mit Vornamen/Nachnamen an (dynamische Variablen), vermerkt Ergebnis (Interesse ja/nein, Rückruf gewünscht) zurück im Sheet; End-of-Call-Report per Webhook.
- Live-Demo eines tatsächlichen Anrufs mit dem gebauten Agenten (Sprecher hält Handy in die Kamera) — Agent führt ein kurzes, kohärentes deutsches Verkaufsgespräch.
- Genannte Zahl: Unternehmen mit systematischer Lead-Reaktivierung machen laut Sprecher im Schnitt "30% mehr Jahresumsatz" — als eigene Erfahrungs-/Kundenzahl dargestellt, nicht extern belegt.

## Use Case 3 — Sales-Call-Preparation-Agent (ca. 83:26–101:35)

- Werkzeuge: n8n, Telegram-Bot als Interface, Sub-Agent für Recherche (SerpAPI/Google-Suche, Wikipedia, Website-zu-Markdown-Konverter, Apify LinkedIn-Company-Scraper als Workaround für LinkedIn-Zugriff), OpenAI Text-to-Speech (Alternative: ElevenLabs) für die Sprachantwort.
- Ablauf: Mitarbeiter schreibt/spricht "Erzähl mir was über [Firma]" an den Telegram-Bot → Haupt-Agent ruft Sub-Agenten für Website-/LinkedIn-Recherche und Produktdatenbank-Abgleich auf → fasst Ergebnis zusammen → sendet Sprachnachricht mit Firmen-Infos und passender Produktempfehlung zurück.
- Demonstriert explizit Multi-Agent-Kollaboration (ein Agent ruft einen Sub-Agenten als Werkzeug auf) und dass der Agent bei Rückfragen ("wie finde ich den Bedarf raus?") kontextbezogen mit Zugriff auf die vorherige Recherche weiterantwortet.

## Use Case 4 — Call-Upload & Analyse-Agent (ca. 101:37–118:50)

- Werkzeuge: Zapier (bewusst als dritte Plattform neben n8n/Make gezeigt, um Bandbreite an Tools zu vermitteln), Zoom-Cloud-Recording als Trigger, Google Drive als Ablage, Zapier-Agents (ChatGPT-Conversation-Modul) für die eigentliche Analyse.
- Ablauf: Zoom-Call-Recording wird automatisch abgefangen, Video + VTT-Transkript in Google Drive abgelegt (mit explizitem Hinweis, dass vorher die Einwilligung der Gesprächspartner nötig ist — "wir machen hier keine Rechtsberatung"), ein Zapier-Agent liest neue VTT-Dateien, lässt sie per ChatGPT auf Redeanteil (%), Füllwörter, Gesprächsphasen, Pausen und "wurde der Termin max. 2-3 Tage in die Zukunft gelegt" auswerten und speichert das Ergebnis als Google Doc.
- Live-Demo mit fiktivem Beispieldialog liefert plausible, nachvollziehbare Kennzahlen (Redeanteil Verkäuferin ca. 61%, Kunde 39%, berechnet aus Wortanteilen).
- Genannter Nutzen: Zeitersparnis bei manueller Call-Analyse; eigene Zahl "hunderte bis tausende Stunden im Jahr" ist unternehmenseigene, nicht extern verifizierbare Angabe.

## Use Case 5 — Angebots-Follow-Up-Voice-Agent (ca. 118:50–129:45)

- Werkzeuge: n8n + Vapi (wie Use Case 2), Gmail-Suche nach Angebotsnummer im Betreff (als Workaround, wenn das Angebotssystem keine API hat), Google Sheets mit Formel-Filter (Status "offen" UND Angebotsdatum ≥ 3 Tage alt).
- Ablauf: Trigger alle 10 Minuten, Mo–Fr; Agent ruft Kunden mit offenem, unbestätigtem Angebot an, erinnert freundlich, beantwortet Rückfragen anhand der aus der E-Mail extrahierten Angebotsdetails (Menge, Preis, Lieferzeit, Zahlungsbedingungen).
- Live-Demo eines echten Anrufs, in dem der Kunde das Angebot am Telefon mündlich bestätigt.
- Genannte Zahl: konsequentes Nachfassen steigert die Abschlussquote laut Sprecher "im Schnitt um 20 bis 30 Prozent" — wieder unbelegte Eigenangabe.

## Abschlussteil: Positionierung und Werbung (ca. 129:45–139:12)

Der Sprecher gibt getrennte Ratschläge für Angestellte (KI-Kompetenz intern zeigen, sonst wechseln), Selbstständige/Gründer (großer, angeblich "fast leerer" Markt für seriöse KI-Agentur-Dienstleistungen in Deutschland) und Unternehmer (zuerst Engpässe analysieren, nicht blind Tools einbauen). Der Abschnitt ist stark werblich für die eigene Firma gehalten: staatlich akkreditierter Bildungsträger, TÜV-Süd-zertifizierte Ausbildung, "1.500+ beratene Unternehmen", "Millionenumsätze", KI-Champions-Community mit kostenlosen Ressourcen, Bewerbungsaufruf für offene Stellen. Ein kurzer Transkriptabschnitt (ca. 137:50–138:10) ist erkennbar Whisper-Kauderwelsch (unverständliche Wortfetzen) — vermutlich Musik/Jingle-Übergang ohne klare Sprache, inhaltlich ohne Bedeutungsverlust für die Zusammenfassung.

## Für den technischen Team-/Gruppenleiter

- Die **Workflow-vs.-Agent-Unterscheidung** (fest orchestrierter Ablauf vs. selbstentscheidender Agent) ist als Denkraster direkt nützlich, um interne Automatisierungsideen oder Anbieterversprechen realistisch einzuordnen — deckt sich mit Anthropics eigener Empfehlung, zuerst die einfachere Workflow-Lösung zu prüfen, bevor man Agentenkomplexität einführt.
- Die **Fünf-Bausteine-Struktur eines Agenten** (LLM, Prompt, Memory, Wissen, Tools) eignet sich als Scoping-Raster für jedes eigene Automatisierungsvorhaben, unabhängig von der konkreten Plattform.
- Use Case 4 (automatisierte Gesprächs-/Protokollanalyse mit definierten Kriterien wie Redeanteil, Vollständigkeit, Einhaltung eines Leitfadens) lässt sich konzeptionell auf andere strukturierte interne Reviews übertragen (z. B. Auswertung von Design-Review- oder Abnahme-Protokollen auf definierte Pflichtpunkte) — nicht 1:1 nachbaubar ohne eigene Anpassung, aber als Muster interessant.
- Die live gezeigte, bewusste Modellwahl nach Kosten/Leistung (z. B. GPT-4.1-nano statt eines größeren Modells für eine einfache Aufgabe) ist ein allgemein übertragbares Prinzip für jeden eigenen KI-Einsatz mit Kostenverantwortung.
- Der Großteil der fünf Use Cases ist jedoch klar auf Vertrieb/Kundengewinnung zugeschnitten und für ein Hardware-Entwicklungsteam nicht direkt anwendbar — der Wert liegt vor allem im übertragbaren Denkraster, nicht in den konkreten Vertriebs-Workflows selbst.

---

## Kernbotschaft
Das Video ist ein vollständiger, praxisorientierter Kurs, der anhand von fünf live gebauten Geschäftsanwendungen (Lead-Scraping, Voice-Agent zur Lead-Reaktivierung, Sales-Call-Vorbereitung, Call-Analyse, Angebots-Follow-Up) zeigt, wie man mit No-Code-Plattformen wie n8n, Make.com, Zapier und Vapi funktionsfähige KI-Agenten für Vertriebsprozesse baut. Fundiert ist vor allem der Grundlagenteil (Workflow-vs.-Agent-Unterscheidung, fünf Bausteine eines Agenten, Warnung vor unnötiger Multi-Agent-Komplexität — alles erkennbar an Anthropics eigenem Agenten-Framework orientiert), während der Rahmen (reißerischer Aufhänger, umfangreicher Werbeteil für die eigene Firma, mehrere unbelegte eigene Erfolgszahlen) mit entsprechender Skepsis zu lesen ist.

## Themen-Tags
KI-Agenten, n8n, Make.com, Zapier, Vapi, ElevenLabs, Voice-Agent, Lead-Scraping, Google Sheets, Prompt Engineering, Workflow vs. Agent, Multi-Agent-System, RAG, Vertriebsautomatisierung, Everlast AI

## Zu prüfen
- **McKinsey-Zahl irreführend wiedergegeben:** Der Sprecher sagt, McKinsey zeige, dass "bis 2030 rund die Hälfte aller heutigen Tätigkeiten zumindest teilweise automatisiert werden können". Per WebSearch geprüft: McKinseys tatsächliche Aussage ist, dass 50% der Arbeitsaktivitäten *technisch* zwischen 2030 und 2060 automatisierbar sind (Mittelwert 2045) — die tatsächlich bis 2030 automatisierte Zeit liegt laut McKinsey im Mittelwert-Szenario eher bei ca. 15%, nicht 50%. Die Video-Aussage verkürzt/verzerrt die Quelle in Richtung eines dramatischeren, näheren Zeithorizonts.
- **Goldman-Sachs-Zahl leicht zugespitzt:** "300 Millionen Stellen ersetzen" — per WebSearch bestätigt, dass Goldman Sachs (März 2023) tatsächlich von "300 Millionen Jobs, die von KI betroffen/exponiert sind" spricht — der GS-Bericht selbst spricht von "betroffen" (teilweise oder vollständig automatisierbare Aufgabenanteile), nicht generell von vollständigem Ersatz der Stelle. Die Video-Formulierung "ersetzen" ist eine Verschärfung der Originalaussage.
- **n8n als "deutsches Unternehmen":** Per WebSearch bestätigt — n8n GmbH ist tatsächlich in Berlin registriert (Handelsregistereintrag 27.11.2019, Gründer Jan Oberhauser), diese Aussage im Video ist korrekt.
- **World Economic Forum "40% planen Belegschaft wegen KI zu verkleinern":** nicht separat verifiziert — plausibel im Bereich bekannter WEF-Future-of-Jobs-Umfragen, aber nicht gegengeprüft.
- **Zahlreiche unternehmenseigene Erfolgszahlen unverifizierbar:** "30% mehr Jahresumsatz durch Lead-Reaktivierung", "20-30% höhere Abschlussquote durch Follow-Up", "sechsstellige Mehrumsätze", "Millionenumsätze", "1.500+ beratene Unternehmen" — alles Eigenangaben des Sprechers/seiner Firma ohne externe Quelle, hier bewusst nicht als verifizierte Fakten übernommen.
- **Anthropic-Bezug (Workflow-vs.-Agent-Unterscheidung, Warnung vor Multi-Agent-Komplexität):** nicht einzeln neu verifiziert, deckt sich aber inhaltlich mit Anthropics bekanntem, öffentlichem Agenten-Framework (vgl. bereits im Repo dokumentierte Anthropic-Quellen in [video-summary-sIWwBfiuEsU.md](video-summary-sIWwBfiuEsU.md) und [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md), wenngleich dort ein anderer Anthropic-Blogpost zitiert wird).
- **Whisper-Transkription — neuer, bisher nicht dokumentierter Fehlermodus:** Der reguläre `watch`-Skill-Lauf scheiterte bei diesem 139-Min.-Video mit `HTTP 413 Payload Too Large` beim einmaligen Upload der kompletten ~65 MB-Audiodatei an Replicate (kein Rate-Limit, kein 6-Minuten-Timeout — die in [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md) bereits dokumentierten Fehlermodi). Das im Aufgabenauftrag genannte automatische Chunking existiert im installierten `whisper.py` nicht. Workaround (manuell durchgeführt, gleiches Prinzip wie in der genannten Datei beschrieben): Audio mit `ffmpeg -f segment -segment_time 300` in 28 Fünf-Minuten-Segmente zerlegt, jedes einzeln per Replicate-Whisper transkribiert (2159 Segmente, 0 Fehler) und mit Zeitversatz zusammengeführt. Diese 413-Variante sollte bei Gelegenheit in `whisper-replicate-rate-limit.md` ergänzt werden (hier nicht editiert, da nur die neue Datei angelegt werden sollte).
- **Parallel-Lauf im selben Scratchpad:** Während dieser Session liefen erkennbar mindestens zwei weitere, unabhängige `/watch`-Läufe für andere Videos (u. a. "Automatisiere ALLES mit Claude Code: Das ultimative Tutorial auf Deutsch" [Lu95f1ZBIos] und "KI-Deepdive mit Christoph Magnussen" [8hBXDntBQaQ, bereits als eigene Datei im Repo vorhanden]) parallel im selben Session-Scratchpad — deren Log-Ausgabe wurde anfangs mit dem eigenen `watch_output.log` vermischt, was zunächst zu Verwirrung über die Video-ID führte. Nach Prüfung der `video.info.json` in den jeweiligen Arbeitsverzeichnissen wurde bestätigt, dass der hier zusammengefasste Inhalt korrekt zu WHUBWM0JoDM gehört (Titel, Dauer 8358,1s und URL stimmen überein).
