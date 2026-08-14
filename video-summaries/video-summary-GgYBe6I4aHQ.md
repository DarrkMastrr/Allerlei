# "KI-AGENTEN richtig nutzen: Diese BASICS musst du kennen!"

**Kanal:** Christoph Magnussen (CEO Blackboat Internet GmbH)
**URL:** https://www.youtube.com/watch?v=GgYBe6I4aHQ
**Länge:** 22:48
**Zusammenfassung erstellt:** 2026-08-14

---

*Siehe auch: [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md), [claude-skills-ueberblick.md](../claude-skills-ueberblick.md), [mcp-ueberblick.md](../mcp-ueberblick.md), [ai-agent-workflow.md](../ai-agent-workflow.md) sowie die anderen Videos desselben Kanals: [video-summary-4m6qbh_aVY0.md](video-summary-4m6qbh_aVY0.md), [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md), [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md), [video-summary-6LVB3mpPvB4.md](video-summary-6LVB3mpPvB4.md). Cross-Checks siehe unten in "Zu prüfen".*

**Hinweis zum Ablauf:** Der Standard-Videodownload (adaptives Format) scheiterte mit HTTP 403 Forbidden. Behoben wie in ähnlichen Fällen zuvor über `--extractor-args "youtube:player_client=android"` kombiniert mit dem progressiven Format `best[ext=mp4]` — funktionierte beim zweiten Versuch. Die nativen Untertitel (Sprache "en") kamen dagegen sofort und vollständig durch. Auf den Frames ist die Bildschirm-UI aber durchgehend Deutsch (z. B. "Personalisierung", "Best Practices", "Hooks & Sandbox"), während das Transkript komplett auf Englisch vorliegt — vermutlich maschinelle Auto-Übersetzung der Plattform-Untertitel des tatsächlich auf Deutsch gesprochenen Videos. Diese Zusammenfassung basiert auf dem vollständig gelesenen Transkript (300 Segmente) plus allen 80 Frames und ist sinngemäß ins Deutsche zurückübertragen — Einzelformulierungen können vom Original-O-Ton abweichen.

## Worum es geht

Ein als Einsteiger-Grundlagenvideo angelegter Rundumschlag zu KI-Agenten (nicht Chatbots): Christoph erklärt Schritt für Schritt, welche Bausteine einen "Agent-Harness" (Claude Code, Codex, Cursor, ChatGPT-Apps) ausmachen und wie man kontrolliert, was ein Agent auf dem eigenen Rechner darf. Durchgehende Analogie: ein Auto mit Tempolimit-Schild (Text-Anweisung, freiwillig befolgt) vs. technischer Geschwindigkeitsbegrenzung (Hook, technisch erzwungen).

## Chatbot vs. Agent — die Grundunterscheidung

Ein Chatbot bekommt eine Aufgabe und liefert eine Antwort. Ein Agent arbeitet in Schleifen ("Loops"), prüft eigene Ergebnisse und bekommt Werkzeuge, um Aufgaben direkt auf dem Rechner zu erledigen — das sei der zentrale Shift dieses Jahres. Dargestellt als Dreieck **Modell – Prompt – Kontext** (Frame bei t≈01:47).

## Browser- vs. Desktop-App-Agenten

Wichtige Unterscheidung: Cloud-basierte Agenten (im Hintergrund beim Anbieter, z. B. ChatGPT-Web) fühlen sich anders an als lokal auf dem eigenen Rechner laufende Desktop-Apps (Codex, Claude Code, Cursor) mit Zugriff auf lokale Projekte. Bildliche Einordnung: ChatGPT sei "der Alltagswagen", Codex "eher ein Rennwagen" — mächtiger, aber ungewohnter zu bedienen. Anbieter versuchen laut Video, beide Welten zusammenzuführen, was aktuell noch nicht rund läuft.

## Memory-Dateien: CLAUDE.md, AGENTS.md, Auto-Memory

- **Globale Agent-/Memory-Dateien** (in Claude Code: `CLAUDE.md`) enthalten Wissen über den Nutzer und Arbeitsweise-Regeln, liegen zunächst lokal in versteckten Ordnern auf dem Rechner (Mac: Shift+Cmd+Punkt zum Sichtbarmachen).
- Eine im Frame (t≈02:51) vollständig lesbare Vergleichstabelle "CLAUDE.md-Dateien vs. Auto-Memory": Wer schreibt es (Nutzer vs. Claude selbst), Umfang (Projekt/Nutzer/Organisation vs. pro Repository geteilt), Ladezeitpunkt (jede Sitzung vs. Sitzungen mit ca. 200 Zeilen/25 KB), Verwendungszweck (Coding-Standards/Workflows/Projektarchitektur vs. Build-Befehle/Debugging-Erkenntnisse/Vorlieben).
- Kernbotschaft: Diese Dateien muss man nicht selbst schreiben — man lässt den Agenten sie aus vergangenen Chats destillieren und sich das z. B. alle vier Wochen wiederholt vornehmen lassen.
- Unterschied zwischen Anbietern explizit angesprochen: Anthropic und OpenAI wollten laut Christoph bewusst sehr persönliche, sich merkende Modelle, Google/Microsoft seien zurückhaltender.
- Wichtiger Praxis-Hinweis: LLMs häufen Memory-Einträge tendenziell nur an, Modelle können selbst nicht gut einschätzen, was gelöscht werden sollte — Aufräumen bleibt Nutzerverantwortung.
- Codex-Pendant: `AGENTS.md` als globaler Arbeitsrahmen, im Frame (t≈01:51) mit Beispielinhalt gezeigt ("Globaler Codex-Arbeitsrahmen", "System-, Entwickler- und aktuelle Nutzeranweisungen haben Vorrang").
- Eigene Regel als Beispiel genannt: Für extern gehende Texte immer zweistufige Freigabe verlangen, bei wichtigen Punkten eine bestimmte Kennzeichnung nutzen, aber nie allein entscheiden.

## Skills

Ein Skill wird als "erweiterte, einmal definierte Anweisung" beschrieben, die das Modell aus dem Training als Format erkennt — statt bei jedem Prompt dieselbe Anleitung neu zu schreiben, wird sie einmal fest hinterlegt. Der Agent entscheidet selbst, ob ein passender Skill zur aktuellen Aufgabe existiert, auch ohne expliziten Trigger im Prompt. Im Frame gezeigt: Claude-Skills-Verwaltung ("Persönlich"/"Organisation"), Anthropic-Doku-Seite "Agent Skills" samt "Best Practices"-Liste (Fähigkeiten vor Bereitstellung testen, auf Gruppen beschränken, aussagekräftige Namen, klare Beschreibungen, Standardstatus bewusst setzen, Freigabeschritte bewusst wählen). Warnung: Skills aus offenen Verzeichnissen vor Nutzung immer selbst durchlesen und prüfen, was sie tun — sie folgen dem "Tempolimit" freiwillig, nicht zwingend. Anthropic habe das Konzept zuerst etabliert, andere Anbieter (u. a. OpenAI) seien mit eigenen, inkompatiblen Skill-Standards nachgezogen — Umformatierung zwischen den Formaten lässt der Agent selbst erledigen.

## MCP (Model Context Protocol)

Analogie: Ein Skill ist die Anweisung "fahr durch die Stadt, max. 50 km/h", MCP ist das "Handbuch", das dem Agenten erst beibringt, wie er das Auto überhaupt bedient (Gas, Lenkung). MCP-Server sollten laut Video von vertrauenswürdigen Quellen stammen, da im Prinzip jeder einen MCP-Server bauen kann. Praxisbeispiele im Frame: Gmail-MCP-Server-Konfigurationsseite (Google-Doku), eigene Blackboat-MCP-Server. Verweis auf ein (im Video verlinktes) Interview mit MCP-Mitschöpfer David Soria Parra von Anthropic für Vertiefung.

## Plugins

Ein Plugin bündelt mehrere Skills, MCP-Server und Tools zu einem Paket — Beispiel im Frame (t≈14:37): Codex-"Security"-Plugin mit 13 Skills (u. a. "Attack Path Analysis", "Deep Security Scan", "Define Security Policy") plus einem MCP-Server. Grund für die Kategorie: Bei 100-200 einzelnen Skills wird die Auswahl für das System unübersichtlich, ein Plugin schafft eine Organisationsebene. Praxis-Tipp: Nicht alles in ein Riesenplugin packen, sondern sinnvoll abgrenzen — "wie ein guter Mitarbeiter braucht es einen klaren Verantwortungsbereich". OpenAI habe kürzlich (laut Video "vor Wochen oder Monaten") eigene Plugins veröffentlicht, gemeinsam mit Vercel, Cursor und weiteren Firmen als offenen Standard.

**Record & Replay** (Codex-Feature, Frame t≈16:32-16:53): Man lässt Codex bis zu 30 Minuten bei einer Aufgabe zusehen, danach erzeugt es daraus automatisch eine Skill-Datei, die den Ablauf beschreibt und wiederholbar macht.

## Sicherheitsebenen: Hooks und Sandbox — Kernabschnitt für den Zielleser

Die zentrale Sicherheitsfrage des Videos: Kann ein Agent theoretisch außer Kontrolle geraten und z. B. Dateien löschen? Antwort: Ja, sofern man es nicht verhindert. Zwei Ebenen werden unterschieden:

- **Textebene** (Prompts in Skills, Agent-Dateien, CLAUDE.md, Memory) — reine Anweisungen, die der Agent freiwillig befolgt, wie ein Tempolimit-Schild. Kann theoretisch überschritten werden.
- **Code-Ebene / Hooks** — technisch erzwungene Regeln, vergleichbar mit einer technischen Geschwindigkeitsbegrenzung im Auto: Egal wie stark man aufs Gas drückt, es geht technisch nicht schneller. Beispiel: ein Hook, der besonders destruktive Befehle wie `rm` (Dateien/Ordner löschen, im Extremfall das Root-Verzeichnis) blockiert. Codex-Doku im Frame (t≈17:51) zeigt Hooks als "deterministische Skripte während des Codex-Lifecycles" — u. a. zum Blockieren versehentlich eingefügter API-Keys, automatischem Zusammenfassen bei Chat-Turns, Validierung vor Commits. Wer nicht weiß, wie man einen Hook schreibt, soll den Agenten selbst danach fragen ("welche Hooks brauche ich, kannst du sie einrichten und erklären, warum").
- **Sandbox** — der Agent darf innerhalb eines abgegrenzten Bereichs alles tun, aber ihn nicht verlassen. Im Frame gezeigt: Claude-Code-Doku "Sandboxing-Ansätze vergleichen" (t≈18:33-18:39) mit einer Vergleichstabelle verschiedener Ansätze (Sandboxed Bash Tool, Sandbox Runtime, Dev Container, VS Full Access, Claude on the Web). Genannter Philosophie-Unterschied: Anthropic gibt Modellen tendenziell mehr direkten Zugriff (mehr Entscheidungsspielraum beim Modell selbst), OpenAI arbeitet werkzeugorientierter mit häufiger separaten Sandboxes pro Agent.

## Permission-Level (ChatGPT/Codex-Einstellungen, Frame t≈20:16)

Im Frame gezeigte "Allgemein"-Einstellungsseite mit Reglern für Standard-Berechtigungen, Auto-Review und Vollzugriff:
- **Standard**: Agent fragt bei jeder Aktion nach Freigabe — bremst frühe Nutzung, aber sicher.
- **Auto Review** (laut Video "dieses Jahr" eingeführt): funktioniert inzwischen sehr gut, birgt aber mehr Risiko.
- **Vollzugriff/Full Access**: keine Befehlsfreigabe mehr nötig, Modell entscheidet allein. Ausdrückliche Empfehlung des Hosts: Vollzugriff deaktiviert lassen, außer man ist sich absolut sicher.

## Abschluss

Aufruf zum YouTube-Livestream am 19. August um 19 Uhr (u. a. Datenschutz-Thema angekündigt) sowie zum Teilen des Videos.

---

## Kernbotschaft

Das Video ordnet die Bausteine eines modernen Agent-Harness sauber ineinander: Memory-/Kontextdateien (CLAUDE.md/AGENTS.md/Auto-Memory) geben dem Modell Wissen über Nutzer und Projekt, Skills bündeln wiederholte Anweisungen, MCP übersetzt Absicht in konkrete Werkzeugnutzung, Plugins bündeln beides zu größeren Paketen — und zwei technische Schutzebenen (Hooks als harte, code-basierte Grenzen; Sandbox als abgegrenzter Handlungsraum) verhindern, dass reine Text-Anweisungen (die ein Agent theoretisch ignorieren könnte) die einzige Sicherheitsebene bleiben. Für den technischen Team-Leiter ist der Hooks-/Sandbox-/Permission-Level-Abschnitt der praktisch wertvollste Teil: Er liefert eine klare, leicht vermittelbare Sprache (Tempolimit-Schild vs. technische Begrenzung), um im Team zu erklären, warum reine Prompt-Regeln nicht als alleinige Sicherheitsmaßnahme reichen, und eine konkrete Handlungsempfehlung (Vollzugriff/Full Access meiden, Hooks für destruktive Befehle wie `rm` einrichten lassen).

## Themen-Tags
KI-Agenten, Agent-Harness, CLAUDE.md, AGENTS.md, Memory-Dateien, Claude Skills, Skill-Marktplatz, MCP, Model Context Protocol, David Soria Parra, Plugins, Codex Security Plugin, Record & Replay, Hooks, Sandbox, Permission-Level, Auto Review, Full Access, Claude Code, Codex, ChatGPT, Blackboat, Christoph Magnussen

## Zu prüfen

- **Schließt eine im Repo bereits dokumentierte Lücke:** [video-summary-PJnR0AbJZeA.md](video-summary-PJnR0AbJZeA.md) vermerkte explizit "Hooks werden nicht erwähnt — auch in diesem Repo bisher kein eigener Hooks-Artikel". Dieses Video ist damit die erste Zusammenfassung im Repo, die Hooks und Sandbox inhaltlich erklärt (nicht nur als Stichwort nennt, wie in [video-summary-TP73qyFWDcY.md](video-summary-TP73qyFWDcY.md): "Hooks, Schedule, Loops" als mächtigste Automatisierungs-Features laut Boris Cherny).
- **Konsistent mit bestehender Notiz:** Das `rm -rf`-Gefahrenbeispiel deckt sich fast wörtlich mit [video-summary-sQBinJA_zxU.md](video-summary-sQBinJA_zxU.md) ("Voller Terminalzugriff ist gefährlich, Beispiel `rm -rf`; nötig sind Guardrails, Sandboxes/isolierte Container") — kein Widerspruch, eher Bestätigung aus unabhängiger Quelle.
- **Mögliche Begriffsverwechslung:** Der im Video verwendete Begriff "Auto Review" (ChatGPT/Codex-Berechtigungsstufe, die Aktionen ohne Einzelbestätigung laufen lässt) ist nicht dasselbe wie der "Autoreview-Loop" aus [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 2 (dort: der Agent reviewt wiederholt sein eigenes Code-Ergebnis). Gleicher Name, unterschiedliches Konzept — beim Weitergeben an Kolleg:innen lohnt sich eine klare Unterscheidung.
- **Plausibilitätscheck durchgeführt (WebSearch), alle drei bestätigt:** (1) OpenAIs "Agent Plugins"-Standard — laut mehreren unabhängigen Quellen (The Next Web, AlphaSignal, The New Stack, the-decoder.com) am 6. August 2026 tatsächlich gemeinsam mit AWS, Cursor, GitHub, Microsoft und Vercel veröffentlicht, ChatGPT/Codex sowie Cursor, GitHub Copilot, Kiro und VS Code unterstützen es zum Start — deckt sich mit der Videoaussage. (2) Codex "Record & Replay" ist real, laut Community-/Presseeinordnung (u. a. eesel.ai, azukiazusa.dev, developers.openai.com) seit 18. Juni 2026 verfügbar, mit exakt der im Video genannten 30-Minuten-Aufnahmegrenze. (3) David Soria Parra ist real als Mitschöpfer des Model Context Protocol bei Anthropic bestätigt (zusammen mit Justin Spahr-Summers).
- **Nicht unabhängig gegengecheckt:** Die genaue Zahl "13 Skills" im gezeigten Codex-Security-Plugin (nur aus dem Frame abgelesen), die Detail-Vergleichstabelle "Sandboxing-Ansätze" aus der Claude-Code-Doku (Frame bei niedriger Auflösung teils schwer lesbar), sowie die pauschale Einordnung "Anthropic gibt Modellen mehr Zugriff, OpenAI ist werkzeugorientierter mit mehr separaten Sandboxes" — plausible, aber nicht im Detail verifizierte High-Level-Architektureinschätzung des Hosts.
- **Cross-Check mit [video-summary-4m6qbh_aVY0.md](video-summary-4m6qbh_aVY0.md)** (selber Kanal, gleicher Sprecher): Dort wird eine unternehmensinterne "Agent-MD"-Datei als CLAUDE.md/AGENTS.md-Analogon beschrieben — konsistent mit der hier gegebenen allgemeinen Erklärung dieser Dateien, keine Widersprüche gefunden.
- **Sprache/Übersetzung:** Wie oben im Ablauf-Hinweis beschrieben, spricht der Host sichtbar Deutsch (Bildschirm-UI komplett deutsch), das geladene Transkript liegt aber komplett auf Englisch vor — vermutlich automatische Plattformübersetzung. Einzelformulierungen in dieser Zusammenfassung sind sinngemäß zurückübertragen, keine wörtlichen Zitate des Originaltons.
