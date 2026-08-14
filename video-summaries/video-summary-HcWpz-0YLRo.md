# "Claude-Skills wurden komplett NEU erfunden… (keine Prompts nötig)"

**Kanal:** Unfairer Vorteil | KI
**URL:** https://www.youtube.com/watch?v=HcWpz-0YLRo
**Länge:** 06:25
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) für das allgemeine Skill-Konzept, [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) für Cowork im Gesamtbild, [mcp-ueberblick.md](../mcp-ueberblick.md) für Connectors/MCP.*

## Das Problem, das die Funktion lösen soll

Ausgangsthese des Hosts: Bei KI-Automatisierung war bisher die Dokumentation der Flaschenhals — wer eine Aufgabe an eine KI übergeben will, musste jeden Schritt und jede Ausnahme aufschreiben, was oft länger dauert als die Aufgabe selbst ("Erklären dauert länger als machen"). Die neue Funktion soll das umgehen: Bildschirm aufnehmen, dabei reden — Claude baut daraus selbständig eine Fähigkeit (Skill).

## Die Funktion: "Record a Skill"

- Zu finden in der Claude-Desktop-App, Tab **Cowork**, über das Plus-Menü im Chatfenster → "Einen Skill aufnehmen" (engl. "Record a Skill")
- Ablauf laut Video-Grafik: **Aufnehmen + Erklären → Claude lernt → Skill jederzeit per `/mein-skill` abrufbar**
- Ein Einwilligungs-Dialog vor Start warnt ausdrücklich: keine Passwörter tippen oder sensible Bildschirminhalte zeigen, da alles aufgezeichnet und an Claude gesendet wird

## Die Demo: YouTube-Kommentare-Tracker als Skill

Der Host nimmt eine Aufgabe auf, die er laut eigener Aussage regelmäßig manuell macht: Kommentare aus YouTube Studio sichten, gute Ideen in eine Google-Sheets-Tabelle ("Comment Tracker") kopieren und in einer zweiten Spalte per Ja/Nein bewerten, ob sich daraus eine Video-Idee bauen lässt.

- Während der Aufnahme spricht er die Anweisung mündlich mit ("Hey Claude, das mache ich hier...") und führt die Aufgabe einmal normal am Bildschirm aus
- Ein Live-Zähler zeigt die erfassten Schritte ("Capturing · 28 steps", später 34 steps)
- Die eigentliche Bildschirmaufnahme dauert laut Cowork-Anzeige nur **68,8 Sekunden** — deutlich kürzer als die Länge des Video-Ausschnitts, der die Aufnahme zeigt
- Nach Stop verarbeitet Claude die Aufnahme sichtbar in mehreren Schritten: Screenshots werden in Einzelschritte zerlegt und analysiert, die gesprochene Erklärung wird transkribiert, anschließend sucht Claude passende Tools (u. a. wird laut Bildschirmtext eine **MCP-Registry-Integration** durchsucht)
- Claude stellt danach **drei gezielte Rückfragen** (Multiple Choice, mit einer jeweils empfohlenen Option), bevor der Skill fertiggestellt wird:
  1. Wer soll das Ja/Nein im Zweifel entscheiden — Claude selbst (mit Nutzerkorrektur, empfohlen), immer "Nein" oder eine zusätzliche Begründungsspalte?
  2. Welche Kommentare soll der Skill bei jedem Lauf holen — alle unbeantworteten (empfohlen), nur neue seit dem letzten Lauf, oder die letzten 30 Tage?
  3. Wie soll der Zugriff auf YouTube Studio/Sheet erfolgen — Claude in Chrome installieren (empfohlen), Computer Use aktivieren, oder beides?
- Ergebnis ist eine Markdown-Skill-Datei ("youtube-kommentare-tracker skill"), die der Host komplett einsehen, editieren und direkt als Skill abspeichern kann. Die Datei enthält laut gezeigtem Screenshot sehr konkrete "harte Regeln", die Claude selbst aus der Aufnahme abgeleitet hat (z. B. "Nur Werte einfügen" beim Einfügen in Google Sheets, weil normales Einfügen die YouTube-Formatierung mitzieht und die Datenvalidierung killt) — inklusive Fallback-Hinweisen, falls Chrome nicht verfügbar ist

## Wann sich das laut Host lohnt — zwei Kriterien

1. **Gibt es für die Ziel-App schon einen Connector (z. B. Gmail, Kalender)?** Dann diesen bevorzugen — ein Connector sei deutlich zuverlässiger als eine KI, die sich durch eine Browser-Oberfläche klickt, welche sich jederzeit ändern kann. "Record a Skill" eignet sich laut Host eher für Abläufe über mehrere Apps/Websites hinweg, die stark auf Claudes "Browser Use"-Fähigkeit setzen (Vergleich: wie das Einarbeiten eines neuen Praktikanten am Browser)
2. **Ist die Aufgabe extrem wiederholbar** — jede Woche exakt gleiche Schritte, gleiches Ergebnis (Reports zusammenbauen, Dateien verschieben/umbenennen)? Sobald im Ablauf eine Bauchentscheidung steckt, hilft die Aufnahme laut Host nicht mehr — dann sei ein normaler Chat schneller

## Warnhinweis zu sensiblen Daten

Ausdrücklicher Rat: Die Funktion nicht für Logins in Banking-Apps oder zum Auslesen von Kontoständen nutzen — was man nicht in einer Bildschirmaufnahme zeigen möchte, gehört grundsätzlich nicht in die Aufnahme.

---

## Kernbotschaft
"Record a Skill" (Claude Cowork) senkt die Einstiegshürde für Skill-Erstellung radikal: statt Prompt-Dokumentation reicht eine einmalige, kommentierte Bildschirmaufnahme einer Aufgabe, aus der Claude eine wiederverwendbare, editierbare Skill-Datei ableitet — inklusive gezielter Rückfragen zu Grenzfällen. Sinnvoll vor allem für hoch wiederholbare, mehrere Apps/Websites umspannende Browser-Workflows ohne Connector und ohne sensible Daten; bei vorhandenem Connector oder Aufgaben mit Bauchentscheidungen bleiben Connector bzw. normaler Chat laut Host die bessere Wahl.

## Themen-Tags
Claude Skills, Claude Cowork, Record a Skill, Browser Use, Computer Use, MCP-Registry, Workflow-Automatisierung, Google Sheets, Datenschutz

## Zu prüfen (falls zutreffend)
- **Feature-Existenz per Websuche bestätigt:** "Record a Skill" ist eine real am 21.07.2026 von Anthropic für Claude Cowork gelaunchte Funktion (mehrere unabhängige Tech-Medien-Quellen, u. a. Android Headlines, Android Authority, Search Engine Journal, Enterprise DNA). Verfügbarkeit laut Recherche auf Pro-/Max-/Team-Abos beschränkt — diese Abo-Einschränkung wird im Video selbst nicht erwähnt und wurde nicht separat auf der Anthropic-Seite gegengecheckt.
- **Cross-Check gegen [claude-skills-ueberblick.md](../claude-skills-ueberblick.md):** Kein Widerspruch gefunden. Der Übersichtsartikel dokumentiert bereits mehrere Wege, Skills zu bauen (`/skill-creator`, "Based on this conversation, build me a skill", Faustregel "nervt es 1-2x → Skill-Kandidat"). "Record a Skill" ist eine sinnvolle Ergänzung dieser Liste um einen vierten, noch nicht dokumentierten Weg (Bildschirmaufnahme statt Text-Prompt) und passt zur dortigen Kernbotschaft, Skills "aus einer bereits geführten Konversation heraus" statt abstrakt zu bauen — hier eben aus einer geführten *Aktion* heraus. Empfehlung: bei nächster Pflege des Übersichtsartikels als fünften Punkt unter "Wie man gute Skills baut" ergänzen.
- **Cross-Check gegen [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md):** Passt zur dortigen Einordnung von Cowork als Werkzeug für "Alltags-Workflows" mit "Computer Use" für mehrstufige Aufgaben — keine Widersprüche.
- Die im Video gezeigte "68,8s"-Aufnahmedauer und die genauen Rückfrage-Optionen sind Screenshot-Ablesungen, nicht selbst nachgestellt/getestet.
- Whisper-Transkript (Replicate) enthält an einer Stelle (ca. 04:22-04:24) einen erkennbar unsinnigen/verrauschten Absatz ("...ich bagiere jetzt die Antwort auf. Dasension der lamentiert vom Büro...") — vermutlich ein Transkriptions-Artefakt, hat die inhaltliche Zusammenfassung an dieser Stelle nicht beeinflusst, da die Bildschirmgrafik ("Wann nutzen — kommt drauf an, zwei Gründe") den Kontext eindeutig macht.
- **Relevanz für Team-/Gruppenleiter-Rolle:** Die Funktion senkt die Hürde, dass auch nicht-technische Teammitglieder repetitive Verwaltungs-/Reporting-Workflows selbst zu Skills machen können, ohne Prompts zu schreiben — nützlich als Werkzeug-Idee für Teamprozesse. Gleichzeitig relevant als Risiko: Bildschirmaufnahmen können unabsichtlich sensible Daten (Kundennamen, interne Zahlen, Logins) erfassen, wenn Mitarbeitende die Warnung im Consent-Dialog übersehen — ggf. als Hinweis in Team-Guidelines aufnehmen, analog zum PII-Anonymisierungs-Skill aus [video-summary-qZRftXozT3M.md](video-summary-qZRftXozT3M.md).

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429, der Whisper-Fallback lief über Replicate (in 2 Chunks, siehe [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md) zum bekannten Timeout-Problem bei diesem Backend) und lieferte diesmal erfolgreich 67 Segmente. Die Zusammenfassung basiert auf allen 80 extrahierten Frames plus vollständigem Transkript.
