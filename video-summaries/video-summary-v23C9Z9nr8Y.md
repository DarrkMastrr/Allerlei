# "Warum nutzt kaum jemand dieses ChatGPT Tool!?"

**Kanal:** Christoph Magnussen
**URL:** https://www.youtube.com/watch?v=v23C9Z9nr8Y
**Länge:** 14:24
**Zusammenfassung erstellt:** 2026-09-08

---

*Siehe auch: [video-summary-8hBXDntBQaQ.md](video-summary-8hBXDntBQaQ.md) (selber Kanal, späterer Live-Deepdive desselben Sprechers) und [video-summary-6LVB3mpPvB4.md](video-summary-6LVB3mpPvB4.md) (früheres Magnussen-Video) — beide bereits im Repo. Dieses Video ist der erste Eintrag im Repo, der ChatGPT Sites und WebMCP konkret behandelt.*

## Format des Videos

Talking-Head-Video (Christoph Magnussen im Blackboard-Loft, gleiches Studio-Setting wie in anderen bereits im Repo dokumentierten Magnussen-Videos) mit eingeschobenem Live-Screen-Recording einer dunklen Codex/ChatGPT-Oberfläche. Kein Sponsoring laut expliziter Aussage im Video selbst ("das ist weder ein gesponsertes Video noch Werbung für irgendetwas"); am Ende (ca. 13:51) blendet YouTube dennoch automatisch ein "Werbung"-Label ein, während Magnussen für die hauseigene "Blackboard Academy" wirbt.

## Einleitung: Tempo der KI-Updates

Magnussen eröffnet mit der These, dass die Update-Geschwindigkeit bei allen großen KI-Anbietern so hoch sei, dass viele scheinbar kleine Neuerungen unterschätzt werden. Als Beleg für Tempo bei OpenAI nennt er Effizienzsteigerungen der Modelle: das günstigste Modell sei zuletzt nochmals deutlich billiger geworden, das Flaggschiff-Modell rund 20 % günstiger. Ergänzend zeigt ein eingeblendeter Screenshot (t≈00:56) die OpenAI-Ankündigungsseite "Premium-Benutzerlizenzen kommen zu ChatGPT Business", datiert auf den 25. August 2026 — passend zur gesprochenen Aussage über ein neues Business-Lizenzmodell mit Flatrate statt reiner API-Token-Abrechnung.

## ChatGPT Sites: mehr als nur "Artifacts"

Magnussen führt das eigentliche Thema ein: ChatGPT Sites, verglichen mit Claudes Artifacts-Feature (interaktive HTML-Ausgaben statt PDF/PowerPoint). Sein Kernpunkt: Sites sei kein bloßes Artifact-Klon, sondern "eine kleine Engine für Mini-Apps" mit eigener Datenbank und Authentifizierung im Hintergrund, direkt aus dem Chat heraus veröffentlichbar.

## Live-Demo: Firmenwebsite bearbeiten, Kontaktformular + Datenbank bauen

Zentraler Teil des Videos (ca. 03:37–08:14), Screen-Recording einer Codex-Oberfläche mit Tab "Sites": Eine zuvor von einem Teammitglied ("Hanno") gebaute Demo-Firmenwebsite ("MAG Metall GmbH") wird per Prompt weiterentwickelt — Farbschema auf Firmen-Orange umgestellt, ein Kontaktformular mit DSGVO-konformer Einwilligung ergänzt. Codex baut dafür automatisch eine Datenbank (laut Magnussen ein "echtes" Datenbank-Backend, von OpenAI zusammen mit Cloudflare entwickelt, global skalierbar). Nach dem Absenden eines Test-Kontaktformulars über die veröffentlichte Seite ist der Eintrag live im Datenbank-Tab sichtbar (Tabelle `contact_requests` mit Zeitstempeln). Magnussens Einordnung: nützlich vor allem für interne Team-Mini-Apps (Kontaktformulare, Event-Anmeldungen, Workshop-Einladungen), die bisher zu aufwendig oder zu teuer für eine externe Beauftragung waren.

## Custom Domain, Freigabe und Analytics

Weitere gezeigte Funktionen im Einstellungsbereich der Site: eigene Domain hinterlegen (DNS-Einträge beim Domain-Registrar), granulare Freigabe (nur der Ersteller, bestimmte eingeladene Personen, alle im Workspace, oder öffentlich im Internet — analog zu Google-Docs-Freigaben), Umgebungsvariablen für Secrets/Passwörter/API-Keys (explizite Warnung, Passwörter nie direkt im HTML-Code zu hinterlegen), sowie ein eingebautes Analytics-Tab (im Beispiel 57 Aufrufe, 3 eindeutige Besucher).

## Weitere Feature-Erwähnungen: Computer History und WebMCP

Kurzer Exkurs zu zwei weiteren aktuellen Codex/ChatGPT-Funktionen: (1) "Computer History" — Codex kann bei Aktivierung die komplette Nutzungshistorie am Computer einsehen, um Erinnerungen/Kontext zu bilden; standardmäßig deaktiviert, Magnussen nutzt es bewusst nicht aktiv ("wir haben eine andere Verantwortung bei den Dingen, die wir tun"). (2) WebMCP — laut Magnussen ein neuer, von "Google" vorangetriebener Standard, der Websites für Agenten besser verständlich/nutzbar machen soll (Analogie: nicht nur Menschen, sondern zunehmend auch Agenten besuchen Websites und müssen verstehen, was dort möglich ist). Ein eingeblendeter Screenshot (t≈12:47) zeigt eine OpenAI-Seite "Das Web mit Agenten nutzbar machen" mit Partnerlogos Vercel, Cloudflare, Render, Netlify und OpenAI selbst.

## Ausblick: Wer gewinnt das "Arbeits-Interface" für Agenten?

Abschließend offene Einschätzung, dass noch niemand wisse, wie das zentrale Arbeits-Interface für Agenten am Ende aussehen wird — eigene kleine Apps pro Prozess, alles in Slack, oder ein komplett neues Tool. OpenAI (Codex/ChatGPT) nähere sich dem laut Magnussen von der einen Seite, Anthropic (im Transkript durch Auto-Untertitel-Fehler als "Tropic" wiedergegeben) von der anderen mit Fokus auf Code und Modelloptimierung. Erwähnt wird zudem ein angeblicher interner OpenAI-"Ultra Fast Mode", der 13–14× schneller als der normale Modus sein soll — explizit als Erwartung/Gerücht formuliert, nicht als bestätigte Tatsache.

## Für den technischen Team-/Gruppenleiter

Konkret nützlich für den Alltag eines Hardware-Teams: ChatGPT Sites senkt laut Demo die Schwelle für kleine interne Werkzeuge (Kontaktformulare, einfache Anmelde-/Erfassungsseiten, kleine interne Dashboards mit Datenbank-Backend) auf "ein Prompt" — ein Muster, das sich auf einfache interne Verwaltungsaufgaben (z. B. Muster-/Prototypen-Anfrageformulare, kleine Checklisten-Tools) übertragen lässt, ohne dass dafür ein separates Web-App-Projekt aufgesetzt werden muss. Zwei Punkte sind für die Praxis wichtig: (1) die im Video demonstrierte Freigabesteuerung (privat/Workspace/öffentlich) und Secrets-Handling (Umgebungsvariablen statt Klartext-Passwörter im Code) ist eine direkt übertragbare Basis-Sicherheitsregel für jede Art von KI-generierten internen Tools; (2) die per WebSearch geprüfte Einschränkung, dass ChatGPT Sites zum Start explizit **nicht** im EWR/der Schweiz/UK verfügbar war (siehe Plausibilitätscheck) — falls das aktuell noch gilt, ist das für ein in Deutschland tätiges Team ein praktisch relevanter Blocker, den das Video nicht erwähnt.

---

## Plausibilitätscheck (per WebSearch, 2026-09-08)

- **ChatGPT Sites als reales Feature bestätigt:** Laut OpenAI Help Center, OpenAI Academy und mehreren unabhängigen Berichten (u. a. theaicareerlab.com, playcode.io) wurde Sites am 2. Juni 2026 auf OpenAIs "Intelligence at Work"-Event für Business/Enterprise angekündigt, seit 9. Juli 2026 auch für Plus/Pro im Public Beta verfügbar — inklusive Hosting, Zugriffskontrollen, Speicher und Datenbank-Unterstützung (D1/SQLite für Datensätze, R2 für Datei-Uploads). Deckt sich mit der Demo im Video.
- **Wichtige, im Video nicht erwähnte Einschränkung:** Laut denselben Quellen war ChatGPT Sites zum Start **nicht im Europäischen Wirtschaftsraum, der Schweiz oder UK verfügbar**. Ob diese Einschränkung im September 2026 noch besteht, ließ sich nicht abschließend klären.
- **WebMCP als reales, aber falsch zugeordnetes Konzept:** WebMCP ist laut OpenAI Developer Community und mehreren Fachartikeln ein experimenteller offener Web-Standard (`navigator.modelContext`, Entwurf bei der W3C Web Machine Learning Community Group), **initiiert von OpenAI** zusammen mit sechs Launch-Partnern: Google Chrome, Cloudflare, Shopify, Vercel, Render und Netlify. Die Aussage im Video, das sei "von Google" vorangetrieben bzw. als Standard etabliert worden, ordnet die Urheberschaft leicht falsch zu — Google (genauer: Chrome) ist einer von mehreren Partnern, nicht der Initiator.
- **"Ultra Fast Mode 13–14× schneller":** nicht unabhängig auffindbar, im Video selbst nur als Magnussens eigene Erwartung/Gerücht dargestellt — nicht verifizierbar.

## Zu prüfen

- **EU/CH/UK-Verfügbarkeit von ChatGPT Sites** zum aktuellen Zeitpunkt (nicht abschließend geklärt, ob die Einschränkung vom Juni-2026-Launch im September 2026 noch gilt) — relevant, falls das Team die Funktion selbst nutzen möchte.
- **WebMCP-Zuschreibung im Video ("von Google")** ist laut Recherche eine leichte Fehlzuordnung — tatsächlich ein OpenAI-geführtes Multi-Partner-Projekt (siehe Plausibilitätscheck).
- **Auto-Untertitel-Artefakte:** Die Transkription stammt aus automatisch generierten englischen YouTube-Untertiteln (nicht manuell erstellt) und enthält erkennbare Phonetik-Fehler bei Produkt-/Firmennamen (u. a. "Chat GPD"/"JGBD"/"CHGBT" für ChatGPT, "Tropic" für Anthropic, "Luna" für das günstigste Modell, "Soll" für das Flaggschiff-Modell). Die exakten, korrekten Modellnamen ließen sich daraus nicht zweifelsfrei rekonstruieren und wurden in dieser Zusammenfassung bewusst nicht geraten, sondern umschrieben.
- **"Ultra Fast Mode" (13–14× schneller):** unbestätigtes internes OpenAI-Gerücht laut eigener Aussage des Sprechers, keine externe Quelle gefunden.
- **Kein inhaltlicher Widerspruch zu bestehenden Repo-Notizen gefunden** — ChatGPT Sites und WebMCP sind neue Themen, die vorher im Repo nicht vorkamen (Grep über alle Dateien ergab keine Treffer). [video-summary-8hBXDntBQaQ.md](video-summary-8hBXDntBQaQ.md) (selber Kanal) dokumentiert bereits einen verwandten, aber anderen OpenAI-Standard (den "Plugin"-Standard für Skills/MCP-Bündel) — keine Redundanz, ergänzt sich thematisch.

**Hinweis zum Ablauf:** Transkript basiert auf nativen (automatisch generierten) englischen YouTube-Untertiteln, 418 Segmente. Alle 80 automatisch verteilten Frames (Vollvideo-Modus, 0,093 fps über die volle Länge) wurden gesichtet.
