# "Higgsfield MCP in Claude Code: Ein Prompt baut mein ganzes Visual-Paket"

**Kanal:** IAmFabian
**URL:** https://www.youtube.com/watch?v=JDebq_fxLlw
**Länge:** 15:19
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [mcp-ueberblick.md](../mcp-ueberblick.md) für das allgemeine MCP-Konzept — dieses Video ist ein konkretes Anwendungsbeispiel dafür, diesmal nicht Smart Home, sondern KI-Bild-/Videogenerierung für die eigene Content-Produktion.*

## Ausgangslage

Fabian zeigt live an einem leeren Projektordner für sein nächstes YouTube-Video sein bisheriges Problem: Thumbnail in Photoshop, Grafiken in einem anderen Tool, Stock-Footage für Zwischenschnitte woanders suchen — mehrere Tabs, mehrere Abos, viel manuelle Arbeit, bevor überhaupt geschnitten wird. Sein neuer Workflow soll das komplett im Terminal über Claude Code lösen, ohne ein einziges anderes Tool zu öffnen.

## Was Higgsfield ist

Higgsfield wird als Plattform für KI-Bilder und KI-Videos vorgestellt, die kein eigenes Modell trainiert, sondern über 30 bestehende Modelle an einem Ort bündelt (u. a. Nano Banana, Google Veo, Gemini, ByteDances Seedance, Kling) und über ein gemeinsames Credit-System abrechnet. Fabian betont ausdrücklich: "Higgsfield ist ein Bündel und kein Zauberstab" — die Ausgabequalität hängt vom jeweils gewählten Basismodell ab, Higgsfield liefert nur eine einheitliche, bequeme Oberfläche/Schnittstelle statt vieler Einzel-Abos.

Higgsfield bietet dafür sowohl einen MCP-Server als auch ein eigenes CLI-Tool an; das Video fokussiert sich auf MCP.

## Einrichtung des MCP-Servers in Claude Code

Installation über einen einzelnen Terminal-Befehl (`claude mcp add --transport http higgsfield <URL>`), danach Login per Browser-OAuth-Flow — kein API-Key, keine Secrets manuell nötig. Über `/mcp` in Claude Code lässt sich der verbundene Server einsehen; laut Video stellt er 77 einzelne Tools bereit (Bilder generieren, Videos generieren, Hintergrund entfernen, Upscaling, Bild erweitern, 3D-Generierung, "Shorts Studio"/Reels-Content, Re-Frame, Explainer-Video, Motion Control, Voice Change, Dubbing).

## Praxis-Demo 1: Thumbnails per Prompt

Prompt-Beispiel aus dem Video: vier Thumbnail-Konzepte im 16:9-Format für ein Video "Lokale KI auf dem Mac", Stilvorgaben (dunkler Hintergrund, gelbes Akzentelement, viel Kontrast, kein Text im Bild), mit expliziter Zielordner-Angabe (`/Thumbnails`) und der Anweisung, den Higgsfield MCP zu nutzen. Claude Code prüft zuerst das Higgsfield-Guthaben, sucht dann passende Modelle und wählt selbstständig **Nano Banana Pro** aus ("Ultimate Quality Text and Diagrams"). Ergebnis: vier PNG-Dateien direkt im Projektordner. Fabian erklärt, dass er bewusst nur den visuellen Kern (Hintergrund/Motiv) generieren lässt — Text, wiederkehrende Grafikelemente (gelbe Box, Pfeil, Schriftart) baut er weiterhin selbst in Photoshop ein, um einen Wiedererkennungswert über alle Thumbnails hinweg zu behalten. Einzelne Nachbesserungen (z. B. "mach das Gehirn pink") lassen sich per Chat-Anweisung an Claude Code weitergeben, ohne das Bild komplett neu zu würfeln.

## Praxis-Demo 2: B-Roll-Video per Prompt

Zweiter Test: Prompt für einen 5-Sekunden-B-Roll-Clip (Kamerafahrt über einen dunklen Schreibtisch, leuchtender Mac im Hintergrund, Codezeilen), mit Zielordner `/B-Roll`. Claude Code wählt dafür **Kling 3.0 Turbo** (5 Sekunden, 1080p, 16:9, Text-to-Video) und liefert nach einigen Minuten Wartezeit eine fertige MP4-Datei inklusive Soundeffekten direkt in den Projektordner.

## Vom Einzel-Prompt zum wiederverwendbaren Skill

Kernpunkt des Videos: Fabian lässt sich den gesamten gezeigten Ablauf (vier Thumbnails + ein B-Roll-Clip, feste Ordnerstruktur) von Claude Code als wiederverwendbaren Skill namens "Visual-Paket" abspeichern. Ab dann reicht für künftige Videos der Skill-Name plus Thema als Prompt. Das Video macht damit implizit denselben Punkt wie das MCP-Grundlagen-Video im Repo (sQBinJA_zxU): MCP liefert den Werkzeugzugriff, ein Skill macht daraus einen wiederholbaren Prozess.

## MCP vs. CLI, insbesondere für Claude Cowork

Fabian weist darauf hin, dass Claude Cowork MCP-Server in der Regel nicht direkt unterstützt ("nur über Workarounds"), während die Higgsfield-CLI dort über das Terminal installiert und genutzt werden kann. Als Grund für die generelle CLI-vs-MCP-Empfehlung bei Vielnutzung nennt er den Kontextverbrauch: MCP ziehe bei jedem Aufruf vergleichsweise viel Kontext (= Tokens = Kosten), die CLI sei "schlanker". Für Claude Code selbst empfiehlt er dagegen weiterhin MCP, da es dort mehr Funktionsumfang biete.

## Kosten und Credits

Konkrete Zahlen aus dem Video: vier Thumbnails plus ein B-Roll-Clip verbrauchten rund 45 Credits (von 5.940 auf ca. 5.895/5.080 — die genaue Restzahl wechselt im Video leicht). Videos seien deutlich teurer als Bilder (laut Fabian 20- bis 50-fache Kosten pro Clip). Wichtiger Hinweis: Ein "Unlimited"-Schalter für Modelle gilt laut Fabian nicht für die Nutzung über Terminal/MCP/CLI — dort wird immer das normale Credit-Guthaben verbraucht.

## Fazit des Hosts

Empfehlung für alle, die regelmäßig Thumbnails, Zwischenschnitte oder Grafiken brauchen und nicht mehrere Einzel-Tools/Abos pflegen wollen — in Kombination mit Claude Code sei das ein klarer Zeitgewinn. Für Gelegenheitsnutzer (z. B. zwei Bilder im Monat) lohne sich dagegen kein eigenes Abo.

---

## Einordnung für Organisation/Sicherheit

Für die Team-/Prozessperspektive relevant, auch wenn im Video nicht explizit thematisiert:
- **Zugriffsmodell:** Die Anbindung läuft über OAuth-Login des persönlichen Higgsfield-Accounts, nicht über einen verwalteten API-Key — für Teameinsatz heißt das, jeder Nutzer bräuchte einen eigenen (bezahlten) Account bzw. es braucht eine klare Regelung, wessen Account/Guthaben ein Agent nutzt.
- **Kostenkontrolle bei Automatisierung:** Da ein Agent selbstständig Modelle auswählt und mehrere Aufrufe parallel/nacheinander tätigen kann (im Video wird explizit erwähnt, dass sich z. B. acht Thumbnails und fünf Videos gleichzeitig generieren ließen), ist ohne Aufsicht ein schneller, ungeplanter Credit-Verbrauch möglich — ähnlich der Fahrlässigkeits-Warnung zu MCP-Berechtigungen im Home-Assistant-Beispiel in [mcp-ueberblick.md](../mcp-ueberblick.md).
- **Datenfluss an Drittanbieter:** Prompts (und ggf. anfangs auch Firmenkontext/Bildmaterial) gehen an einen externen Cloud-Dienst (Higgsfield, der wiederum mehrere weitere KI-Anbieter im Hintergrund orchestriert) — für sensible/interne Visuals ist das ein Datenabfluss-Punkt, den man vor Team-Rollout prüfen sollte.
- **Übertragbarkeit über Content-Produktion hinaus:** Das gezeigte Muster (MCP-Tool anbinden → einmal per Prompt austesten → als wiederverwendbaren Skill fixieren) ist unabhängig von Higgsfield als generelles Vorgehen für andere Agentic-Coding-Automatisierungen im Team interessant, nicht nur für Marketing/Video.

---

## Kernbotschaft
Higgsfield bündelt über 30 KI-Bild-/Videomodelle hinter einem einheitlichen Credit-System und stellt diese über einen MCP-Server (und alternativ eine CLI) direkt in Claude Code bereit. Im Video entsteht so aus einem einzigen Prompt ein komplettes Visual-Paket (Thumbnails + B-Roll) direkt im Projektordner, ohne Tool-Wechsel — und der gesamte Ablauf lässt sich als wiederverwendbarer Skill fixieren, sodass aus einem Einmal-Prompt ein wiederholbares Werkzeug wird. Der Nutzen hängt aber am Credit-Verbrauch (Videos deutlich teurer als Bilder) und daran, dass "Unlimited"-Pläne im Terminal-Workflow nicht greifen.

## Themen-Tags
MCP, Model Context Protocol, Higgsfield, Claude Code, Claude Cowork, KI-Bildgenerierung, KI-Videogenerierung, Agentic Coding, Skills, Content-Produktion, Credits/Kostenmodell

## Zu prüfen
- **77 Tools / Modellzahl "über 30"** — Angaben stammen direkt aus der Claude-Code-Oberfläche bzw. Fabians Aussage im Video, nicht unabhängig nachgezählt.
- **"Kleinster Plan startet bei 1.000 Credits"** (Fabians Aussage bei ca. 14:02) — eine Web-Recherche zu aktuellen Higgsfield-Preisplänen fand stattdessen einen Basic-Tarif mit ca. 120 Credits für ca. 9 $/Monat sowie einen Plus-Tarif mit ca. 1.000 Credits für ca. 39–49 $/Monat; das passt nicht exakt zur Aussage im Video. Möglicherweise meint Fabian einen anderen/aktuelleren Plan, oder die Tarife haben sich seit der Recherche geändert — nicht abschließend geklärt.
- **Konkrete Credit-Verbrauchszahlen** (5.940 → 5.080/5.897, "45 Credits für 4 Thumbnails + 1 Video") — Bildschirm-Screenshot aus dem Video, nicht selbst nachvollzogen.
- Das Video ist als **bezahltes Werbevideo** ("Werbung"-Label im Player durchgehend sichtbar, siehe Frames) für Higgsfield gekennzeichnet — Fabian benennt selbst offen Einschränkungen (Kosten für Video, Unlimited-Falle), trotzdem bei einer Sponsor-Produktion generell mit Blick auf Einordnung lesen.
- Grundplausibilität von Higgsfield als Produkt, MCP-Server-Existenz und Installationsbefehl (`claude mcp add ... higgsfield`) wurde per Websuche gegengecheckt und bestätigt (u. a. higgsfield.ai/mcp, higgsfield.ai/cli) — Detailfunktionen (z. B. genaue Modellliste, Auflösungsgrenzen) wurden nicht einzeln verifiziert.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; die Zusammenfassung basiert auf dem Whisper-Fallback (Replicate, in 3 Chunks) plus 80 Frames. Ein kurzer Transkript-Abschnitt bei ca. 08:14–08:21 enthält deutlich erkennbare Whisper-Aussetzer/Sprachmix-Artefakte (unverständliche Wortfetzen); der Sinn der Stelle (Fabian erklärt, warum er Text/Wiedererkennungsmerkmale nicht von Higgsfield generieren lässt) ließ sich aber aus dem Kontext und den Frames zweifelsfrei rekonstruieren.
