# "HÖR AUF Skills zu prompten: Das neue Claude Update verändert alles!"

**Kanal:** Sascha Hoffmann | KI ohne Team
**URL:** https://www.youtube.com/watch?v=tK9C3Skskws
**Länge:** 15:18
**Zusammenfassung erstellt:** 2026-08-14

---

*Siehe auch: [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md) für eine frühere ausführliche Demo derselben "Record a Skill"-Funktion (dort: YouTube-Kommentare-Tracker als Skill), [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) für das allgemeine Skill-Konzept.*

## Ausgangsthese: Skill Engineering als vierter Baustein von Agent-Workflows

Sascha (gibt laut eigener Aussage regelmäßig Agent-Workshops) ordnet Agent-Arbeit in vier Bereiche ein: **Harness Engineering** (Umgebung), **Context Engineering** (Wissen), **Tool Engineering** (MCP) und **Skill Engineering** (Prozesse, wie Agenten arbeiten). Um den vierten Bereich soll es im Video gehen — konkret um das neue Claude-Feature, mit dem sich Skills nicht mehr mühsam beschreiben/iterieren lassen müssen, sondern per Bildschirmaufnahme entstehen.

## Die zwei alten Wege, Skills zu bauen (Vergleichsfolie vor der Demo)

1. **Direkt `/skill-creator` anschmeißen** und beschreiben, was man will ("Bitte baue mir ein Report und draft eine Email") — Output laut Host meist "relativ bescheiden", weil zu wenig Kontext mitgegeben wird.
2. **Besserer bisheriger Weg:** die Aufgabe zunächst Schritt für Schritt im normalen Chat lösen und iterieren (Beispiel im Video: Daten per API/MCP als Liste holen → auf Tabelle umstellen → Auswertung/Prediction machen → E-Mail-Entwurf ableiten), und erst wenn der Output nahezu perfekt ist, den fertigen Chatverlauf per Skill-Creator in einen Skill umwandeln lassen ("Bitte auf folgenden Chatverlauf erstelle einen Skill, der das abbildet").

Dieser zweite Weg deckt sich praktisch wortgleich mit der bereits in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) dokumentierten Best Practice ("nie abstrakt planen, aus einer bereits geführten Konversation heraus bauen", Prompt-Muster *"Based on this conversation, build me a skill"*) — dieses Video zeigt sie hier explizit als bisher besten, aber durch das neue Feature nun überholten Ansatz.

## Der neue Weg: "Record a Skill" in Claude Cowork

- Zu finden in der Claude-Desktop-App, Tab **Cowork**, über das Plus-Menü → "Skill aufnehmen"/"Record a Skill" — funktioniert laut Host ausdrücklich **nicht** im normalen Chat, nur im Cowork-/Desktop-Umfeld.
- Consent-Dialog vor Aufnahmestart (im Frame lesbar, wortgleich zur bereits im Repo dokumentierten Version): *"Your screen, clicks, typing, and voice are recorded, then sent to Claude and turned into a repeatable skill. Don't type passwords or secrets, or display sensitive information or private conversations while recording."*
- Während der Aufnahme läuft unten ein Live-Zähler ("Capturing X steps"); der spätere Chat zeigt die Aufnahme als Objekt "Recorded demonstration (405.6s)" an.

## Die Demo: YouTube-Sponsor-Report für Hostinger

Konkrete, selbst genutzte Aufgabe: In YouTube Studio (Erweiterter Modus, Zeitraum letzte 365 Tage) die Analytics-Daten als CSV herunterladen, in einen benannten lokalen Ordner ("Youtube August 2026") sortieren/entpacken, dann die Daten in Bezug auf einen konkreten Sponsor (hier: Hostinger.com) auswerten — welche Video-Titel/Themen gut performt haben, welche Sponsor-Produkte dazu passen, welche Video-Ideen sich anbieten — und das Ergebnis in ein neues Google Doc ("Hostinger Sponsor Dokument") schreiben. Sascha kommentiert die ganze Aufnahme laut mit ("ich möchte jetzt …", "das heißt, er soll …"), was als Anweisungsspur an Claude dient.

## Nach der Aufnahme: zwei Rückfragen, dann Skill-Erstellung

Frame-bestätigt stellt Claude nach der Aufnahme genau zwei Rückfragen mit jeweils vorgeschlagener Option:
1. Wo soll das fertige Sponsor-Dokument landen? → gewählt: Google Doc (wie in der Demo)
2. Soll der Skill am Ende auch gleich einen E-Mail-Entwurf an den Sponsor vorbereiten? → gewählt: Ja, als Gmail-Entwurf

Sichtbarer Fortschritt danach: "Entwerfe den Skill" → "Skill paketieren (.skill) und an Sascha senden" → fertige Datei **`youtube-sponsor-report.skill`**, Benachrichtigung "Skill gespeichert".

## Test: Skill abrufen — und plattformübergreifende Ambition

- In einem neuen Chat ruft Sascha den Skill per `/youtube-sponsor-report bitte für claude.com erstellen` auf; die Skill-Datei hängt als Kontext am Chat.
- Der Host erwähnt zusätzlich (nicht selbst live gezeigt, nur behauptet), dass sich derselbe Skill — sofern die Connectoren es hergeben — auch außerhalb des lokalen Cowork-Setups nutzen ließe, z. B. in ein GitHub-Repo gepackt und über geplante Routinen in Claude Code wieder ausgeführt. Ein gezeigter Screenshot passt dazu: eine Claude-Code-artige Oberfläche mit einer "Routinen"-Liste und Modellauswahl "Opus 5".
- Dabei fallen beiläufig die Begriffe **"Hermes"** und **"OpenClaw"** als mögliche Cloud-Infrastruktur-Optionen für einen solchen wiederkehrenden Lauf — nur akustisch erwähnt, nicht im Bild gezeigt oder erklärt (siehe Zu-prüfen-Abschnitt).

## Grenzen, die der Host selbst benennt

- **Kein reiner One-Shot:** Beim eigenen Nachtest hat das automatische Einfügen der Ergebnisse in den E-Mail-Entwurf laut Host "nicht ganz korrekt" funktioniert — er musste nachiterieren. Ausdrückliche Warnung, nicht davon auszugehen, dass die Aufnahme-Funktion sofort perfekte Skills liefert.
- **Sicherheit/Datenschutz** (inhaltlich identisch zur bereits im Repo dokumentierten Warnung): Aufgezeichnet wird nicht nur der fachlich relevante Ausschnitt, sondern der komplette Bildschirm. Passwörter, sensible Kundendaten oder nicht-öffentliche Zahlen dürfen während der Aufnahme nicht sichtbar sein; Alternativen laut Host: Abstraktion/Platzhalterdaten verwenden oder in einer Testumgebung aufnehmen und Details erst textlich nachtragen.

## Handlungsempfehlung des Hosts

Eigene Liste wiederkehrender manueller Prozesse aufschreiben (falls noch nicht vorhanden), direkt mit der Aufnahme-Funktion ein bis zwei Skills bauen und eine Woche lang im echten Alltag testen.

---

## Kernbotschaft
"Record a Skill" senkt laut Host die technische Einstiegshürde für Skill-Engineering weiter: Statt wie bisher empfohlen eine Aufgabe erst manuell im Chat zu iterieren und danach den Chatverlauf per Skill-Creator umzuwandeln, reicht jetzt eine einmalige, laut kommentierte Bildschirmaufnahme, aus der Claude — nach ein bis zwei gezielten Rückfragen — eine paketierte, wiederverwendbare `.skill`-Datei baut, die sich auch plattformübergreifend (z. B. via Claude Code/Routinen) weiterverwenden lassen soll. Kein Selbstläufer: Nachiterieren bleibt laut eigenem Test des Hosts nötig, und wegen der Vollbildschirmaufzeichnung gelten dieselben Datenschutz-Einschränkungen wie im bereits dokumentierten Pendant-Video.

## Themen-Tags
Claude Skills, Claude Cowork, Record a Skill, Skill Engineering, Skill Creator, Harness/Context/Tool Engineering, Google Workspace, YouTube Analytics, Claude Code, Datenschutz

## Zu prüfen
- **Feature-Existenz per Websuche bestätigt:** "Record a Skill" wurde real am 21.07.2026 für Claude Cowork gelauncht, verfügbar für Pro-/Max-/Team-Abos (u. a. Android Headlines, Android Authority, Search Engine Journal, Enterprise DNA, AI Weekly) — deckt sich mit der bereits in [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md) dokumentierten Recherche, keine neuen Widersprüche.
- **Kanal "Sascha Hoffmann | KI ohne Team" per Websuche bestätigt real** (YouTube @saschthetasch, zusätzlich aktive Präsenz auf the-autopilot.com/LinkedIn zu AI-Agent-Themen) — Video-Inhalt passt zum sonstigen Themenfokus des Kanals.
- **Cross-Check gegen [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md):** Starke inhaltliche Überschneidung — gleiches Feature, wortgleicher Consent-Dialog, gleiche Kernkriterien (wiederholbare Prozesse, keine sensiblen Daten). Kein Widerspruch, aber neue Details ergänzen das Bild: (1) jenes Video nannte das Ergebnis "eine Markdown-Skill-Datei", dieses zeigt konkret eine gepackte `.skill`-Datei — vermutlich zwei Blickwinkel auf dieselbe zugrundeliegende Struktur, die für die Distribution paketiert wird, kein echter Widerspruch; (2) dieses Video zeigt zusätzlich den "Vorher"-Zustand (Skill-Creator direkt vs. iterieren-dann-Skill-bauen) und ordnet Record-a-Skill explizit als dritten, überlegenen Weg ein; (3) dieses Video nennt eine konkrete Limitation aus eigenem Nachtest (fehlerhafte automatische E-Mail-Befüllung), was das andere Video nicht tat.
- **Cross-Check gegen [claude-skills-ueberblick.md](../claude-skills-ueberblick.md):** Bestätigt 1:1 die dort dokumentierte Best Practice "nie abstrakt planen, aus einer Konversation heraus bauen" (Prompt "Based on this conversation, build me a skill") als weiterhin gültigen, aber laut diesem Video nun "alten" zweiten Weg. Die "vier Bereiche" (Harness/Context/Tool/Skill Engineering) sind ein neues, in keinem anderen Repo-Artikel dokumentiertes Ordnungsschema — Ergänzungskandidat für den Übersichtsartikel.
- Modellnamen "Fable 5" (UI-Screenshot, Auswahl "Fable 5 Hoch") und "Opus 5" (Claude-Code-artiger Screenshot) sind bereits an mehreren Stellen im Repo als reale, aktuelle Anthropic-Modellnamen dokumentiert (siehe [fable-5-modell-sperre.md](../fable-5-modell-sperre.md)) — kein Widerspruch, eher zusätzliche Bestätigung.
- Unklare Begriffe **"Hermes"** und **"OpenClaw"** als genannte Cloud-Infrastruktur-Optionen (ca. 12:19–12:23 im Transkript) — nur akustisch erwähnt, nicht im Bild gezeigt, nicht per Websuche verifiziert. Könnten Whisper-Fehltranskriptionen anderer Produktnamen sein oder real existierende, dem Zusammenfasser aber unbekannte Tools/Deployment-Plattformen. Nicht aufgelöst — für den Leser als offene Frage markiert.
- Aussage, das Record-Feature tauche "jetzt auch bei Codex" auf — unbelegte, beiläufige persönliche Beobachtung des Hosts, nicht selbst gegengecheckt.
- Whisper-Transkript enthielt bei ca. 02:22–02:23 einen offensichtlichen Transkriptionsfehler: derselbe Satz "Ich kann das nicht machen" 12x hintereinander wiederholt — eindeutiges Artefakt, hat die inhaltliche Zusammenfassung an dieser Stelle nicht beeinflusst, da der zugehörige Frame (Skill-Creator-Prompteingabe im Chat) eindeutig war.
- **Relevanz für Team-/Gruppenleiter-Rolle:** Direkt anschlussfähig an die bereits im Repo dokumentierte Risiko-Einschätzung zur Vollbildschirmaufzeichnung (mögliches unbeabsichtigtes Erfassen sensibler Firmendaten). Neu und zusätzlich nützlich: das "4-Bereiche"-Ordnungsschema (Harness/Context/Tool/Skill Engineering) als Vokabular, um im Team zu strukturieren, an welcher Stelle ein Agent-Workflow gerade hakt — brauchbar für Onboarding/Schulung. Ebenso die praktische Warnung, auch aufgenommene Skills nicht "one-shot" zu vertrauen, sondern wie jeden Prozess vor produktivem Team-Einsatz zu testen und zu iterieren.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten erneut mit HTTP 429 (siehe [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md)). Der Whisper-Fallback lief über Replicate in 3 Chunks à ca. 330s (Video mit 15:18 knapp über der 6-Minuten-Grenze pro Chunk) und lieferte 283 Segmente ohne manuelles Eingreifen. Der Video-Download lief diesmal problemlos über das reguläre adaptive Format (398+251), kein HTTP-403-Fallback nötig. Die Zusammenfassung basiert auf allen 80 extrahierten Frames plus vollständigem Transkript.
