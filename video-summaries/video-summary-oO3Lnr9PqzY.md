# "Die 3 Wellen der KI-Revolution: Nur 0,04% sind in Welle 3"

**Kanal:** Garrit Wilson (KI-Pionier Akademie)
**URL:** https://www.youtube.com/watch?v=oO3Lnr9PqzY
**Länge:** 50:19
**Zusammenfassung erstellt:** 2026-08-14

---

*Hinweis zum Ablauf: Native YouTube-Untertitel scheiterten mit HTTP 429. Die Transkription lief automatisch über den Replicate-Whisper-Fallback des watch-Skills mit Auto-Chunking (10 Segmente à ca. 5:30 Min., 785 Segmente gesamt, siehe [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md)) — kein manuelles Eingreifen nötig. Zwei kurze Passagen im Transkript (ca. 4:55–5:30 und 24:50–25:20) sind erkennbar Whisper-Aussetzer mit eingestreuten koreanischen/chinesischen Schriftzeichen und Wortsalat — vermutlich Musik/Stille/Übergang im Original. Die Zusammenfassung stützt sich dort auf die umliegenden Folienframes statt auf das Transkript. Gleicher Kanal/Sprecher wie bereits in [video-summary-PJnR0AbJZeA.md](video-summary-PJnR0AbJZeA.md) dokumentiert (dort: "Der einzige Claude-Code-Kurs"), Bio und mehrere Zahlen stimmen zwischen beiden Videos überein — siehe "Zu prüfen".*

## Worum es geht

Garrit Wilson (Psychologe, seit ~3 Jahren selbstständiger KI-Berater, Gründer der KI-Pionier-Akademie) präsentiert ein reines Talking-Head-Video mit Folienwechseln (kein Screen-Recording, keine Live-Demo): eine dreistufige Taxonomie der bisherigen KI-Nutzung (Chatbots → Assistenten → Agenten), garniert mit der These, dass fast alle Nutzer noch in Stufe 1 oder 2 feststecken, gefolgt von einem eigenen Rahmenkonzept ("KI-Betriebssystem") für den produktiven Einsatz von Agenten im Unternehmen, und mündet in einem Pitch für die eigene Akademie/Coaching.

## Die drei Wellen der KI-Revolution

**Welle 1 — Chatbots (ab ChatGPT-Release):** Reines Frage-Antwort-Muster ("conversational prompting"). Nützlich für Texte, Ideen, Recherche, Zusammenfassungen — kann aber nichts ausführen. Laut Wilson "vom Business Value her relativ begrenzt". ChatGPT sei laut Video am "31. November 2022" veröffentlicht worden (dieses Datum existiert nicht, gemeint ist vermutlich der 30. November 2022) und "schnellste Applikation jemals auf 100 Millionen Nutzer" — ein zum Zeitpunkt Anfang 2023 zutreffender, inzwischen aber überholter Rekord (siehe Fact-Check).

**Welle 2 — Assistenten (ab 2023, Wilsons eigene "Nische" laut Video):** Hochoptimierte, oft mehrseitige Single-Shot-Prompts/Megaprompts, Custom GPTs, Prompt-Templates, Claude Projects. Erstmals planbarer statt zufälliger Mehrwert, aber weiterhin stark manuell: Ergebnisse müssen kopiert und selbst weiterverarbeitet werden ("10-20% der Wertschöpfungskette"). Wilson zeigt hier Fotos von einem eigenen, stark überbuchten Prompt-Engineering-Workshop (Contra-KI-Messe: 40 Plätze geplant, ~140 Personen erschienen) als Beleg für seine damalige Positionierung als "professioneller Prompt Engineer" und Hochschuldozent für Prompt Engineering.

**Welle 3 — Agenten (laut Video seit Februar 2026):** Der zentrale Unterschied: Man gibt ein Ziel statt einer Instruktion, der Agent plant, handelt (Dateien lesen/schreiben, Code ausführen, Browser/APIs/Datenbanken nutzen), erkennt Blockaden und korrigiert sich selbst. Wilson beschreibt Februar 2026 als persönlichen Wendepunkt ("tektonische Plattenverschiebung"), bei dem er kurzfristig die komplette Agenda eines bereits geplanten Live-Events neu aufgesetzt habe. Zeitliche Einordnung deckt sich mit dem in mehreren anderen Repo-Notizen dokumentierten "Februar-2026-Schub" (Claude Opus 4.6).

Eine live gezeichnete Excalidraw-Skizze visualisiert den Unterschied: Chatbot- und Assistenten-Pfade enden jeweils mit einem X (Sackgasse ohne echte Autonomie), der Agenten-Pfad zeigt eine Schleife aus Planen → Blockade → neuer Versuch → Ziel erreicht.

## Die 99,6%/0,04%-Studie: Wer steht wo?

Zentrale Zahlen des Videos: "99,6% der Menschen hängen noch in Welle 1 oder 2 fest" (Intro) versus die im Titel und bei ~22:05 genannte Zahl "0,04% der Menschheit nutzt aktuell Coding-Agenten wie Claude Code oder Codex". Gezeigt wird eine Dot-Grid-Grafik ("Each dot is ~3.2 million people") mit vier Kategorien (nie KI genutzt / kostenfreier Chatbot-Nutzer / zahlender Nutzer / Coding-Agent-Nutzer), wobei die letzte Kategorie nur als winziger, kaum sichtbarer Punktanteil erscheint. Wilson selbst weist mehrfach darauf hin, dass die feinere Aufschlüsselung (Anteil Assistenten- vs. Agenten-Nutzer unter den zahlenden Nutzern) "seine eigene Schätzung" und nicht Teil der Original-Studie sei.

**Wichtig — Zahlen-Inkonsistenz im Video selbst:** "99,6% in Welle 1/2" würde bedeuten, dass 0,4% in Welle 3 sind — die im Titel und an anderer Stelle genannte Zahl ist aber 0,04%, also eine Zehnerpotenz kleiner. Das Video vermischt hier zwei unterschiedlich enge Definitionen von "Welle 3" (Agenten allgemein vs. spezifisch Coding-Agenten), ohne das explizit zu klären. Die 0,04%-Zahl selbst ist plausibel und deckt sich mit unabhängiger Berichterstattung (siehe Fact-Check), die 99,6%-Eröffnungszahl ist intern nicht ganz konsistent mit dem Rest des Videos.

## Warum Agenten allein nicht reichen

Drei von Wilson genannte Haupthindernisse, warum Menschen trotz Zugang zu Agenten nicht wirklich profitieren:
1. **Fehlender Einstieg:** Keine Anleitung, welche Use Cases überhaupt sinnvoll sind, wirkt "spooky" (Sorge um Datenzugriff, Kontrolle).
2. **Fehlende Schutzmechanismen:** Ohne Guardrails werden versehentlich Dateien gelöscht, sensible Daten freigegeben oder Systeme beschädigt, bevor es auffällt.
3. **Wildwuchs bei Power-Usern:** "Agenten, Vollgas" ohne Struktur führt zu Dutzenden zusammenhangslosen Projekten, keiner Wiederverwendbarkeit, keiner Verbesserung über Zeit — verglichen mit "einem Supergenie mit Amnesie", das jede Session bei null beginnt.

Daraus leitet er drei Konsequenzen ab: keine Kontinuität, keine Verbesserung über Zeit, nichts wird wiedergefunden — visualisiert mit einem Vergleichsdiagramm "einzelne Projekte" (mehrere kleine Glockenkurven) gegen "integriertes System" (eine exponentiell wachsende Kurve).

## Das KI-Betriebssystem: vier Schichten

Wilsons Lösungsvorschlag ist ein selbst entwickeltes Rahmenkonzept — ein "digitaler Zwilling" des Unternehmens (zwei lokale Ordnerstrukturen, kein Code nötig), in den der Agent "einzieht":

1. **Onboarding:** Der Agent versteht das Unternehmen "in Sekunden" (Mitarbeiter, laufende Projekte, Roadmap, Kennzahlen).
2. **Wissen/interne Bibliothek:** Zugriff auf alles, was das Unternehmen je dokumentiert hat — zentraler Punkt: aktives Kuratieren/Warten nötig, sonst "Second Brain" voller Datenmüll, das die Ergebnisqualität über Zeit verschlechtert. Wilson nennt das explizit **Context Engineering statt Prompt Engineering**.
3. **Fähigkeiten:** Standardisierte, hochqualitative Prozesse statt Ad-hoc-Chats — hier entsteht laut Wilson der eigentliche ökonomische Mehrwert.
4. **Grenzen/Governance:** Klare Leitplanken (z. B. Anonymisierung von E-Mails vor der Verarbeitung, keine Namen/Adressen im Agentenzugriff).

Illustriert mit einer wiederkehrenden Einstein-Bildsprache ("Supergenie als Praktikant") und einem IQ-Vergleich: Mensch im Schnitt IQ 100, Claude Opus 4.6 (Stand Februar 2026) IQ 133, "bestes Modell" mittlerweile (Stand August 2026) IQ 145 auf dem Mensa-Norwegen-Test.

## Praxisbeispiele aus dem eigenen Unternehmen

- **Content-Zuschnitt:** Mitarbeiterin "Sophie" braucht für das Zuschneiden von Podcast-Ausschnitten in Kurzvideos jetzt 2 statt vorher 8 Stunden (vorher: Opus Clips-Software).
- **Kurserstellung:** Wilsons eigene "KI-Betriebssystem-Masterclass" (11,5 Std. Videoinhalt) habe ihm rund 40 Stunden operative Zeit gespart — inkl. vollautomatischem Video-Upload, Transkription, Beschreibungserstellung und Vorlagen-Upload durch den Agenten, ohne menschliches Zutun.
- **Decision Intelligence:** Vor Geschäftsentscheidungen holt sich Wilson routinemäßig eine "zweite Meinung" vom Agenten, der auf alle Unternehmensdaten Zugriff hat.
- Weitere genannte Bereiche: interne/externe Kommunikation, Präsentationserstellung, Lead-Scoring/-Qualifizierung im Vertrieb, automatisierte Call-Vor-/Nachbereitung.

## Werblicher Rahmen

Das Video ist strukturell ein Sales-Funnel: Der eigene Kurs zum KI-Betriebssystem wird explizit nicht mehr frei verkauft ("weil viele es falsch einsetzen"), sondern nur noch über die Akademie mit Coaching-Begleitung. Gegen Ende: Kundenstimmen (Bewertung 4,91, "100+ zufriedene Kunden", "100% Weiterempfehlung" — unbelegte Eigenangaben), Einladung zu einem unverbindlichen Kennenlerngespräch sowie Werbung für einen KI-Retreat auf Bali. Kein "Werbung"-Label im Player sichtbar.

## Relevanz für technische Team-Leiter

Die "vier Schichten"-Struktur (Onboarding/Wissen/Fähigkeiten/Grenzen) ist im Kern eine plausible, auf Unternehmens-/Teamebene gedachte Blaupause für Agent-Rollouts — inhaltlich deckt sie sich stark mit dem in [ai-agent-workflow.md](../ai-agent-workflow.md) und [video-summary-4m6qbh_aVY0.md](video-summary-4m6qbh_aVY0.md) bereits dokumentierten "Blackboat Operating System"-Ansatz (Agent-MD-Datei, Datenminimierung, Supervisor-Review). Besonders die "drei häufigsten Fehler" (fehlende Einstiegsanleitung, fehlende Schutzmechanismen, unstrukturierter Power-User-Wildwuchs) und die Warnung vor unkontrolliertem Context-Wachstum ("Second Brain" wird zu Datenmüll) sind konkret verwertbare Warnsignale für die Einführung von Agenten in einem Team — unabhängig vom werblichen Rahmen um Wilsons eigenes Coaching-Angebot.

---

## Fact-Check

**0,04%-Zahl (Coding-Agent-Nutzung):** Per WebSearch bestätigt — eine im Februar 2026 kursierende Analyse (u. a. via "God of Prompt" auf X, aufgegriffen von mehreren Branchenmedien) schätzt 2-5 Millionen aktive Nutzer von KI-Coding-Tools weltweit bei 8,1 Mrd. Menschen, was ziemlich genau den obersten ~0,04% entspricht. Die Titel-Kernzahl ist also keine Übertreibung, sondern deckt sich mit unabhängiger Berichterstattung.

**METR-Verdopplungszeit "196 Tage":** Per WebSearch bestätigt als reale, aber inzwischen leicht veraltete METR-Zahl. Die ursprüngliche METR-Studie (März 2025) nannte tatsächlich ~7 Monate/196 Tage Verdopplungszeit für den "Time Horizon" von KI-Agenten. METRs eigenes Update "Time Horizon 1.1" (Januar 2026) korrigierte das aber bereits auf ~130,8 Tage (4,3 Monate) für den Post-2023-Trend — das Video nutzt also die ältere, konservativere Zahl und unterschätzt damit tendenziell das tatsächliche Tempo der jüngsten Entwicklung.

**IQ-Werte (Mensa-Norwegen-Test, TrackingAI.org/Maxim Lott):** Per WebSearch bestätigt als reales, laufendes Projekt mit nachvollziehbarer Methodik. Die genannte Obergrenze von 145 entspricht laut unabhängigen Quellen tatsächlich der Testobergrenze selbst (Skala endet bei 145) — Modelle, die "145 erreichen", schöpfen also eher die Skala aus, als dass 145 ihre "wahre" Obergrenze wäre. Aktuelle Frontier-Modelle lagen laut Suchergebnissen Mitte 2026 tatsächlich im Bereich 140+ auf diesem Test — die Größenordnung passt.

**"ChatGPT: schnellste App aller Zeiten auf 100 Mio. Nutzer":** Stimmte zum Zeitpunkt Anfang 2023, ist aber inzwischen überholt — Metas Threads erreichte im Juli 2023 100 Mio. Anmeldungen in nur 5 Tagen (ChatGPT brauchte ~2 Monate). Wilson wiederholt hier eine mittlerweile veraltete, wenn auch weit verbreitete Behauptung.

**GPT-3.5 "~36 Sekunden" Zeithorizont / METR-Grundthese:** Nicht in einer Primärquelle einzeln nachgerechnet, aber durch internen Repo-Abgleich gestützt: [video-summary-PJnR0AbJZeA.md](video-summary-PJnR0AbJZeA.md) — ein früheres Video **desselben Kanals/Sprechers** — nennt exakt dieselbe Zahl (GPT-3.5, Nov. 2022, ~36 Sekunden) im Vergleich zu Claude Opus 4.6 (~15 Std.). Das ist zumindest interne Konsistenz über zwei Videos hinweg, keine unabhängige externe Bestätigung des genauen Zahlenwerts.

**"Claude Mithos"/"Claude Mythos":** Im Whisper-Transkript als "Mithos" verschriftlicht, im Video als gesprochene Alternativbezeichnung zu "Fable" erwähnt. [video-summary-lKHUKXp-nOA.md](video-summary-lKHUKXp-nOA.md) dokumentiert unabhängig denselben Modellnamen als "Claude Mythos" (Mitte 2026) — das bestätigt, dass es sich um eine Whisper-Fehltranskription von "Mythos" handelt, kein neuer/anderer Modellname.

---

## Kernbotschaft

Die Kernthese — ein Großteil der KI-Nutzer steckt noch bei Chatbots oder optimierten Prompts fest, während eine winzige Minderheit bereits mit autonom handelnden Agenten arbeitet — ist im Kern plausibel und die zentrale 0,04%-Zahl unabhängig belegbar; die im Video selbst verwendete Eröffnungszahl "99,6%" ist damit aber nicht ganz konsistent (Verwechslung von "Agenten allgemein" mit "spezifisch Coding-Agenten"). Der inhaltlich wertvollste Teil ist nicht die Wellen-Taxonomie selbst (Chatbot → Assistent → Agent ist mittlerweile eine im Repo mehrfach dokumentierte Standard-Erzählung), sondern das "KI-Betriebssystem"-Rahmenkonzept mit seinen vier Schichten und den drei konkret benannten Rollout-Fehlern — inhaltlich nah an bereits dokumentierten Unternehmensansätzen (Blackboat Operating System), hier aber explizit als Verkaufsargument für Wilsons eigene, nicht mehr frei verkaufte Akademie-Mitgliedschaft verpackt.

## Themen-Tags

KI-Wellen-Taxonomie, Chatbots vs. Assistenten vs. Agenten, Coding-Agenten-Adoption, METR Time Horizon, Mensa-IQ-Test/TrackingAI, Context Engineering, KI-Betriebssystem, Digitaler Zwilling, Agent-Guardrails, Second Brain/Context-Wartung, Decision Intelligence, KI-Pionier-Akademie, Garrit Wilson, Business-Pitch/Funnel

## Zu prüfen

- **Zahlen-Inkonsistenz 99,6% vs. 0,04%** (siehe oben) — im Video selbst nicht aufgelöst, hier als eigenständiger Kritikpunkt dieser Zusammenfassung markiert, nicht aus einer externen Quelle übernommen.
- **METR-196-Tage-Zahl ist die ältere, bereits von METR selbst überholte Version** (aktuell ~130 Tage) — Video zitiert damit eine im Vergleich zum Erstellungszeitpunkt (August 2026) bereits veraltete Verdopplungsrate.
- **"Schnellste App auf 100 Mio. Nutzer"** — seit Juli 2023 durch Threads widerlegt, im Video unkommentiert als aktuell gültiger Rekord dargestellt.
- **Cross-Check mit [video-summary-PJnR0AbJZeA.md](video-summary-PJnR0AbJZeA.md):** Gleicher Kanal, überlappende Bio-Details (Psychologiestudium, seit 2022/2023 selbstständig, Prompt-Engineering-Hintergrund) und identische METR-Vergleichszahl (GPT-3.5 ~36 Sek.) — hohe interne Konsistenz zwischen beiden Videos, aber das ist Konsistenz des Sprechers mit sich selbst, keine unabhängige externe Verifikation.
- **Cross-Check mit [ai-agent-workflow.md](../ai-agent-workflow.md) / [video-summary-4m6qbh_aVY0.md](video-summary-4m6qbh_aVY0.md):** Das "KI-Betriebssystem"-Konzept (4 Schichten: Onboarding, Wissen, Fähigkeiten, Grenzen) deckt sich inhaltlich stark mit dem dort dokumentierten "Blackboat Operating System" (Agent-MD, Datenminimierung, Supervisor-Review) — kein Widerspruch, eher ein Hinweis, dass dieses Strukturmuster branchenübergreifend zum Standard-Vokabular für Agent-Governance wird. Auch der Begriff "KI-Betriebssystem" selbst taucht bereits unabhängig in [video-summary-wZeOwqmSw84.md](video-summary-wZeOwqmSw84.md) auf (dort: Claude als "vollwertiges KI-Betriebssystem") — vermutlich ein inzwischen generisch gewordener Marketingbegriff, nicht Wilsons Alleinstellungsmerkmal, auch wenn das Video es so framt.
- **"Über 80.000 Euro in Coaches investiert", Kundenzahlen (4,91/100+/100%):** Unbelegte Eigenangaben, nicht überprüfbar.
- **Whisper-Transkript-Aussetzer bei ca. 4:55–5:30 und 24:50–25:20:** Erkennbar korrupt (Fremdschriftzeichen, Wortsalat) — Zusammenfassung stützt sich dort auf Folienframes statt Transkript; kleine inhaltliche Lücke möglich, falls in diesen ~1-2 Minuten zusätzliche gesprochene Punkte gemacht wurden, die weder im Transkript noch auf einer Folie sichtbar sind.
- **Chatbot-vs-Assistent-vs-Agent-Vergleichskarte (Frame ~12:35):** Jahresangaben "2022-2023"/"2023-2024" für die Wellen sind Wilsons eigene, im Video nicht weiter belegte Datierung.
