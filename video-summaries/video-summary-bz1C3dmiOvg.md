# "Anthropic Engineers Just Fixed Claude Code's Biggest Problem"

**Kanal:** Oleg Melnikov
**URL:** https://www.youtube.com/watch?v=bz1C3dmiOvg
**Länge:** 07:50
**Zusammenfassung erstellt:** 2026-08-14

---

## Worum es geht: Cross-Session-Messaging in Claude Code

Oleg Melnikov stellt ein neues Claude-Code-Feature vor, mit dem parallel laufende Claude-Code-Sessions auf demselben Rechner sich gegenseitig Nachrichten schicken können, ohne dass der Nutzer manuell zwischen Terminals kopieren/einfügen muss. Eine Session kann eine andere von sich aus (oder auf Zuruf) informieren, fragen oder Ergebnisse übergeben — "wie zwei Mitarbeiter im selben Büro, die kurz an die Tür der/des anderen klopfen", so die im Video verwendete Analogie.

Der Titel ("Biggest Problem") ist Zuspitzung des Hosts, aber die Kernbehauptung — es gibt jetzt eingebautes Session-zu-Session-Messaging in Claude Code — ist real und stammt aus einem tatsächlichen, aktuellen Anthropic-Feature-Rollout (siehe Fact-Check unten).

## Demo 1: Zwei Sessions grüßen sich (ca. 1:20–1:44)

Gezeigt wird eine browserbasierte Claude-Code-Oberfläche mit zwei offenen Tabs/Sessions ("X" und "Y"). Der Host prompted in Session X: *"send message hi to another recently created session"*. Im Tool-Output ist zu sehen, wie Claude zunächst **ListAgents** aufruft (listet erreichbare Peer-Sessions, im Frame sichtbar: `dantane-35 [eb89d9]`, `twitter-spy [fbd0el]`) und danach **SendMessage** nutzt, um "hi" an die Zielsession zu schicken. In Session Y erscheint daraufhin die Nachricht ("A peer session said hi. Nothing to act on — what do you need?"), ohne dass der Nutzer dort etwas eingegeben hat.

## Reisebeispiel als Aufhänger (0:36–1:20)

Eingeführt über eine Grafik ("The trip" → Rome/Paris/Lisbon, "all three at the same time"): Statt eine Session eine komplexe Aufgabe (Reise mit drei Städten, gemeinsames Budget) abarbeiten zu lassen, schlägt der Host vor, eine Master-Session plus eine Session pro Stadt zu betreiben, die sich per Messaging über den gemeinsamen Reise-/Budget-Stand abstimmen.

## Kontextfenster-Problem und die vorgeschlagene Lösung (1:51–3:58)

Zentrales Argument: Das Kontextfenster (im Video mit 1 Million Token beziffert, per `/context`-Befehl abrufbar — im Frame sichtbar: "claude-opus-5 [1m], 56.6k / 1.0M tokens (6%)") wird mit steigender Füllung sowohl teurer als auch "dümmer" in der Modellleistung. Konkretes Kostenbeispiel des Hosts: Wer nach einer Stunde Pause mit "Fable 5" eine kurze Nachricht schickt, zahlt laut ihm rund 10 $, weil der Cache für rund eine halbe Million Token neu aktiviert werden muss; mit "Opus 5" sei das etwa halb so teuer. Als günstigere Alternative zu `/compact` (das laut Host das gesamte Gespräch durchgeht und dadurch selbst viele Token kostet) schlägt er vor: neue, "leichte" Session starten und die alte Session per Cross-Session-Message nur eine kurze Zusammenfassung des relevanten Kontexts schicken lassen. Visualisiert über die Grafik "Send the short version. Start fresh." (rote "too full"-Box → Pfeil → grüne "light again"-Box).

## Weitere gezeigte Anwendungsfälle

- **Neue Idee bekommt eigenes Fenster** (4:00–4:44, Grafik "A new idea gets its own window"): Wenn während der Arbeit an einem Projekt eine neue, unabhängige Idee aufkommt, lässt sich der relevante Kontext per natürlichsprachlicher Anweisung an eine neue, sich selbst startende Session übergeben, statt Kontext manuell auszuwählen und zu kopieren. Als Beispiel nennt der Host eine selbst gebaute Chrome-Extension (Ersatz für eine bezahlte Extension, die Social-Media-Zugriff blockiert), mit der Begründung, die niedrigere Baubarriere führe dazu, dass er "viele Dinge gleichzeitig" baue.
- **Zwei Sessions an derselben Google-Sheet-Datenbank** (4:52–5:50, Grafik "Two windows, one Google Sheet"): Zwei parallele Sessions, die an derselben Tabelle arbeiten, können sich per Messaging synchronisieren ("I take the top rows" / "ok, I take the rest"), um sich nicht gegenseitig zu überschreiben.
- **Keine manuelle Freigabe nötig** (5:53–6:21, Grafik "Nobody has to type in there"): Laut Host braucht es standardmäßig keine Bestätigung, damit eine Session eine Nachricht an eine andere schicken/empfangen kann — das läuft automatisch.

## Session-Namensgebung als Praxistipp (6:21–7:45)

Der Host empfiehlt, jeder neuen Session sofort per `/rename`-Befehl einen sprechenden Namen zu geben (Demo: Umbenennung von "X" zu "Feature Form For New Users"). Begründung: Beim späteren Wiederaufnehmen über die Sessions-/Resume-Liste (im Frame sichtbar: Einträge wie "twitter-spy", "yt-vid-cc-talk-sessions", "Feature Form For New Users") lässt sich mit klaren Namen die richtige Session sofort finden, statt sich durch generische/kryptische Bezeichnungen zu wühlen. Das ist zugleich Voraussetzung dafür, eine Zielsession im Prompt gezielt ansprechen zu können.

## Fact-Check: Ist das Feature real?

**Ja, per WebSearch und offizieller Anthropic-Dokumentation bestätigt.** Die Doku-Seite `code.claude.com/docs/en/cross-session-messaging` beschreibt exakt das im Video gezeigte Feature ("Cross-Session Messaging"), inklusive der beiden Tools `ListAgents` und `SendMessage`. Wichtige Details aus der Doku, die das Video nicht erwähnt bzw. leicht vereinfacht:

- **Setup:** Ausgerollt mit Claude Code v2.1.224 (Anthropic-Ankündigung datiert auf den 7. August 2026, also nur wenige Tage vor Erstellung dieses Videos) — passt zeitlich sehr gut.
- **Plattform-Einschränkung, im Video nicht erwähnt:** Das Feature läuft laut Doku nur auf **macOS und Linux (inkl. WSL2)** — **nicht auf nativem Windows**. Für dieses Repo (das offensichtlich in einer Windows-Umgebung geführt wird) ist das ein relevanter Praxis-Punkt: Wer Claude Code direkt unter Windows nutzt (nicht via WSL2), kann dieses Feature aktuell nicht verwenden.
- **Nicht auf allen Anbieter-Plattformen:** laut Doku nicht verfügbar auf Amazon Bedrock, AWS Claude Platform, Google Cloud Agent Platform oder Microsoft Foundry.
- **Kein automatisches Freigabe-Verhalten in jedem Fall**, wie im Video suggeriert ("no, you don't need to approve nothing"): Die Doku beschreibt ein Regelwerk (`crossSessionInbound`: `accept`/`hold`/`refuse`), das je nach Permission-Mode der sendenden/empfangenden Session automatisch zwischen sofortiger Zustellung und Bestätigungsdialog unterscheidet. Für zwei gewöhnliche interaktive Sessions mit Standardeinstellungen (wie im Video gezeigt) stimmt die Aussage des Hosts im Kern, ist aber nicht pauschal für jede Konfiguration richtig.
- **Nachrichteninhalt:** laut Doku ausdrücklich **nur reiner Text**, nie Konversationsverlauf oder Dateien — passt zum im Video gezeigten Verhalten (kurze Zusammenfassungen statt Dateiübertragung).
- Die im Video gezeigten Befehle/Tool-Namen (`ListAgents`, `SendMessage`, `/rename`) stimmen mit der Doku überein.

**Nicht unabhängig geprüft:** die konkreten Kostenzahlen des Hosts ("$10 für eine Nachricht nach einer Stunde Pause bei Fable 5, halb so teuer bei Opus 5") — das ist eine plausible, aber nicht belegte persönliche Schätzung/Erfahrung zur Funktionsweise von Prompt-Caching (Cache-Reaktivierungskosten bei langer Inaktivität), keine offiziell zitierte Zahl.

## Kernbotschaft

Claude Code hat ein reales, kürzlich (Anfang August 2026) ausgerolltes Feature erhalten, mit dem parallel laufende Sessions sich über zwei neue Tools (`ListAgents`, `SendMessage`) gegenseitig kurze Textnachrichten schicken können — nützlich für Handoffs zwischen parallelen Arbeits-Sessions, zur Vermeidung von manuellem Copy-Paste und als günstigere Alternative zu `/compact`, wenn ein Kontextfenster voll wird. Der Host zeigt mehrere plausible Anwendungsfälle (Trip-Planung über mehrere Sessions, neue Ideen in eigenen Fenstern, gemeinsame Arbeit an einer Google-Tabelle) und empfiehlt disziplinierte Session-Benennung per `/rename` als Voraussetzung dafür, das Feature im Alltag nutzbar zu halten. Wichtigste Einschränkung, die im Video selbst nicht erwähnt wird: Das Feature läuft laut offizieller Anthropic-Doku nur auf macOS/Linux (inkl. WSL2), nicht auf nativem Windows.

## Themen-Tags

Claude Code, Cross-Session Messaging, ListAgents, SendMessage, Kontextfenster, Prompt Caching, /compact, /rename, Session-Management, Multi-Session-Workflow, Claude Opus 5, Claude Fable 5, Agentic Coding

## Zu prüfen

- **Plattform-Lücke Windows** ist der wichtigste praktische Punkt für dieses Repo und wurde im Video selbst nicht thematisiert — vor Rollout im eigenen (laut Arbeitsverzeichnis Windows-basierten) Team-Setup unbedingt prüfen, ob/wie WSL2 dafür genutzt werden müsste.
- Kostenbeispiel ("$10 pro Nachricht nach 1h Pause bei Fable 5") ist unbelegte persönliche Erfahrung des Hosts, keine offizielle Zahl — plausibel als Illustration von Prompt-Cache-Reaktivierungskosten, aber nicht nachgerechnet.
- Kein Widerspruch zu bestehenden Repo-Notizen gefunden: Eine gezielte Grep-Suche nach verwandten Begriffen (Sessions, Multi-Agent, Kontextfenster, /compact, ListAgents, SendMessage, Cross-Session) über alle Markdown-Dateien im Repo ergab keine bisherige Dokumentation dieses konkreten Features — inhaltlich neu für das Repo, keine Überschneidung mit z. B. [ai-agent-workflow.md](../ai-agent-workflow.md) (dort geht es um Loop-/Review-Workflows innerhalb einer Session, nicht um Session-zu-Session-Kommunikation) oder [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) (erwähnt das Kontextfenster nur allgemein, ohne dieses Feature). Die dort dokumentierten Modellnamen "Fable 5" und "Opus 5" sowie deren Preisverhältnis (Fable 5 ≈ doppelt so teuer wie die jeweilige Opus-Generation, siehe [fable-5-modell-sperre.md](../fable-5-modell-sperre.md)) passen konsistent zur Kostenaussage in diesem Video.
- **Hinweis zum Ablauf:** Der Video-Download über yt-dlp scheiterte zunächst mit HTTP 403 bei den regulären adaptiven Videoformaten (YouTube verlangt dafür einen PO-Token, der auf diesem Rechner nicht eingerichtet ist). Als Workaround wurde auf das progressive Kombi-Format (360p) ausgewichen — die Bildqualität der Frames ist dadurch etwas niedriger als sonst üblich (640×360 statt höherer Auflösung), Text auf den Screenshots war aber durchgehend gut lesbar. Das Transkript stammt regulär aus nativen YouTube-Untertiteln (217 Segmente, keine Whisper-Nutzung nötig) und ist vollständig.
