# "NEW Claude Obsidian 2.0 Changes Everything"

**Kanal:** Julian Goldie SEO
**URL:** https://www.youtube.com/watch?v=UZr4lLHBKyo
**Länge:** 07:49
**Zusammenfassung erstellt:** 2026-08-14

---

*Siehe auch: [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md) ("Nie wieder verlorene Informationen – Das Claude Wiki System (Karpathy LLM)") — behandelt unabhängig dasselbe Karpathy-Konzept eines persistenten LLM-Wikis, aber als manuell instruierten CLAUDE.md-Workflow statt als konkretes Obsidian-Plugin. Ergänzend, kein Widerspruch, siehe „Zu prüfen".*

## Worum es geht: das Plugin „claude-obsidian"

Moderator ist laut Einblendung „Julian Goldie, Digital Avatar" (KI-Avatar/Double des realen Julian Goldie, SEO-Content-Marketers). Vorgestellt wird **claude-obsidian**, ein laut Video kostenloses, quelloffenes Plugin für Claude Code, das der Obsidian-Notizen-App (lokale Markdown-Notizen-App) ein „echtes Gedächtnis" gibt: Man legt Dateien in einen Inbox-Ordner, Claude liest sie, verlinkt sie und merkt sie sich dauerhaft — als wachsendes, vernetztes „Vault" statt einzelner, isolierter Chats.

Per WebSearch unabhängig verifiziert: Das Projekt existiert real auf GitHub unter `AgriciDaniel/claude-obsidian` (MIT-Lizenz), mit exakt der im Video gezeigten README-Formulierung „local-first knowledge system for Claude Code and compatible Agent Skills hosts" und dem Zusatz „Based on Karpathy's LLM Wiki pattern" — beides deckt sich wortgleich mit den gesichteten Frames. Sekundärquellen (u. a. skillsllm.com) nennen ca. 10.700 GitHub-Stars; dieser Wert stammt nicht aus dem Video selbst, sondern aus der eigenen Recherche.

## Der Loop: Capture → Ground → Connect → Use

Im Video als Grafik gezeigt (Frames ~t=00:52–02:15, GitHub-README-Screenshots):

1. **Capture** — Quellen kommen über eine sichtbare Inbox rein, eine unveränderliche Kopie des Originals wird zuerst gesichert, bevor irgendetwas verändert wird.
2. **Ground** — jede wichtige Behauptung behält einen Verweis zurück zur Quelle; das Vault verfolgt, wie stark/frisch eine Quelle ist und ob ihr etwas widerspricht.
3. **Connect** — statt loser Notizen entstehen verlinkte Seiten, Themenkarten (Maps of Content) und visuelle Boards (Obsidian Canvas); alles verdrahtet sich selbstständig.
4. **Use** — man stellt dem Vault eine Frage, und es antwortet nur aus dem, was tatsächlich enthalten ist.

Zentrales Design-Versprechen (Ehrlichkeits-Mechanismus): Wenn das Vault etwas nicht weiß, sagt es das explizit, statt eine plausibel klingende Antwort zu erfinden. Für besonders wichtige Aussagen verlangt das System laut Video zwei unabhängige Quellen, bevor eine Aussage als „belastbar" gilt.

## 15 Skills in einem System

Die GitHub-README (gesichtet in mehreren Frames, ca. t=03:34–03:50) listet exakt 15 Skills in drei Gruppen — deckt sich mit der im Transkript genannten Zahl:

**Wiki bauen/nutzen:** `wiki` (initialisiert/übernimmt ein Vault, prüft Bereitschaft, routet Arbeit), `save` (sichert **eine** gezielte Erkenntnis, kein automatischer Transkript-Dump), `wiki-ingest` (macht aus erfassten Quellen verlinkte Seiten + Herkunftsnachweise), `wiki-query` (beantwortet nur lesend aus vorhandener Vault-Evidenz), `wiki-lint` (meldet tote Links, Waisen, veraltete Indizes, leere Abschnitte)

**Workflow erweitern:** `autoresearch` (begrenzte Web-Recherche mit explizitem Zugriff und separatem, kanonischem Merge), `canvas` (Obsidian-Canvas-Erstellung/-Pflege), `draftsafe` (bereinigt Web-Inhalte vor der Aufnahme), `wiki-fold` (nachvollziehbare Zusammenfassung des Vorgangsprotokolls), `wiki-mode` (Generic/LYT/PARA/Zettelkasten-Ablagekonventionen), `wiki-retrieve` (kontextbezogenes Retrieval: BM25 + optionales Cosine-Reranking), `wiki-cli` (transaktionssichere Obsidian-CLI-Lese-/Schreibzugriffe)

**Referenz-Skills:** `obsidian-markdown` (korrektes Obsidian-Markdown inkl. Links/Embeds/Callouts), `obsidian-bases` (native `.base`-Tabellen/Karten/Filter/Formeln), `think` (strukturierte Beobachten-Zuhören-Verbinden-Erstellen-Wachsen-Review-Schleife)

Julians im Video verwendete Spitznamen ("der Bibliothekar", "das ehrliche Orakel", "der Kartenmacher", "der Finder", "der Historiker") entsprechen erkennbar `wiki-ingest`, `wiki-query`, `canvas`, `wiki-retrieve` bzw. `wiki-fold` — im Video selbst werden die technischen Skill-Namen nicht ausgesprochen, nur die Screenshots zeigen sie.

## Vier Ablage-Modi

Laut README (Frame ~t=04:00) legt ein einstellbarer Modus fest, wie **neue** Notizen einsortiert werden (bestehende Notizen werden beim Wechsel nicht neu organisiert):
- **Generic** (Standard) — Quellen, Konzepte, Entitäten, Sessions
- **LYT** — Maps of Content und verlinkte atomare Notizen
- **PARA** — Projects, Areas, Resources, Archives
- **Zettelkasten** — stabile Kennungen, atomare Notizen, dichte Verlinkung

## Sicherheit bei paralleler Nutzung

Wenn mehrere Agenten gleichzeitig am Vault arbeiten, schreiben sie laut Video nicht direkt in die Dateien, sondern geben Entwürfe zurück; ein einzelner Controller prüft die Gesamtänderung und wendet sie in einem einzigen, transaktionssicheren Schritt an. Bricht etwas mittendrin ab, wird das Vault auf den vorherigen Stand zurückgerollt — nichts bleibt halb geschrieben. Das Tool ist laut Video nicht auf Claude beschränkt, sondern funktioniert auch mit Codex, Gemini und anderen Open-Source-Setups. Voraussetzung: Obsidian (kostenlose Notizen-App) + Claude Code.

## Werblicher Rahmen: Agent OS und AI Profit Boardroom

Ein erheblicher Teil der Bildschirmzeit gehört nicht dem freien Plugin selbst, sondern Julians eigenem, kommerziellem Ökosystem:
- **„Agent OS"** — Julians eigenes Multi-Agenten-Dashboard („Mission Control") mit benannten Agenten (Claude, OpenClaw, Hermes, Gemini, Antigravity, Codex u. a.) — ein eigenes Wrapper-Produkt, nicht Teil von claude-obsidian selbst.
- **„AI Profit Boardroom"** — kostenpflichtige Community (laut einem Frame $59/Monat, „24 hour flash sale", über 4.000 Mitglieder), beworben mit fertigem „Agent OS"-Zip inkl. vorinstalliertem claude-obsidian, 30-Tage-Fahrplan und Coaching-Calls.
- **„AI Success Lab" / „AI Money Lab"** — zusätzlich beworbene kostenlose Community (laut Frame 85.200 Mitglieder) als Einstiegs-Funnel.

Das eigentliche Werkzeug (claude-obsidian) ist frei und quelloffen; das Video funktioniert aber strukturell vor allem als Verkaufsvideo für Julians kostenpflichtiges Angebot darum herum — ähnliches Muster wie in anderen bereits im Repo dokumentierten Videos mit Eigenwerbung (vgl. „Zu prüfen" unten).

---

## Kernbotschaft

claude-obsidian v2 ist ein reales, quelloffenes (MIT-lizenziertes, ~10.700 GitHub-Stars) Claude-Code-Plugin, das einen lokalen Markdown-Ordner nach Andrej Karpathys „persistentem LLM-Wiki"-Prinzip in eine sich selbst organisierende, quellenbelegte Wissensbasis verwandelt — über einen Capture-Ground-Connect-Use-Loop und 15 kleine, kombinierbare Skills. Bemerkenswert sind vor allem die explizite Anti-Halluzinations-Haltung (lieber „weiß ich nicht" als erfunden, Zwei-Quellen-Regel für wichtige Aussagen) und die transaktionssichere Mehrfach-Agenten-Nutzung. Der Großteil der Videolänge dient jedoch dem Verkauf von Julian Goldies eigenem „Agent OS"-Wrapper und seiner kostenpflichtigen „AI Profit Boardroom"-Community — das eigentliche Tool ist nur der Aufhänger.

## Themen-Tags
Claude Obsidian, claude-obsidian (GitHub), Obsidian, Second Brain, Karpathy LLM-Wiki-Pattern, PARA/Zettelkasten, Agent Skills, Claude-Code-Plugin, Wissensmanagement, Compounding Vault, Julian Goldie/AI Profit Boardroom

## Zu prüfen

- **Repo-Existenz und Kernangaben unabhängig bestätigt:** WebSearch fand `github.com/AgriciDaniel/claude-obsidian`, MIT-Lizenz, README-Formulierung und „Based on Karpathy's LLM Wiki pattern" stimmen wortgleich mit den Video-Frames überein — kein Fake-Produkt. Die ~10.700-Stars-Zahl stammt aus einer Sekundärquelle (skillsllm.com), nicht aus einer eigenen Live-Prüfung der GitHub-Seite selbst.
- **Name des Entwicklers:** Transkript sagt „developer called Agresti Daniel"; der tatsächliche GitHub-Handle laut Suche ist „AgriciDaniel" — vermutlich phonetische Lesart des Handles (das evtl. kein echter Vor-/Nachname ist), nicht gegengecheckt, welcher Name korrekt/real ist.
- **Versionsnummer „2.0":** Das Video spricht durchgehend von „Claude Obsidian 2" bzw. „version two just dropped". Eine Suchergebnis-Kurzfassung erwähnte dagegen „Version 1.7" für die „Compound Vault"-Architektur. Ob „2.0" ein Marketing-Name oder die tatsächliche SemVer-Version zum Video-Zeitpunkt ist, wurde nicht abschließend anhand der echten Release-Tags geprüft.
- **Zwei ähnlich benannte Repos:** Es existieren sowohl `efslabs/claude-obsidian` als auch `AgriciDaniel/claude-obsidian`; laut einer Sekundärquelle ist Letzteres „die aktiver gepflegte Version" und passt zu den Video-Frames — nicht vollständig unabhängig entwirrt, ob beide zusammenhängen (Fork?) oder unabhängige Projekte sind.
- **Starke Eigenwerbung:** Große Teile der Bildschirmzeit gehören Julians eigenem „Agent OS" (Mission Control, benannte Agenten wie Hermes/OpenClaw/Antigravity) und der kostenpflichtigen „AI Profit Boardroom"-Community — als Julians eigenes Zusatzprodukt zu lesen, nicht als Teil des freien claude-obsidian-Tools selbst. Vergleichbares Muster wie bei anderen bereits im Repo dokumentierten, stark werblichen Videos (z. B. [video-summary-qtte0zpnGks.md](video-summary-qtte0zpnGks.md), Everlast-AI-Eigenwerbung).
- **Cross-Check gegen [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md):** Beide Videos berufen sich unabhängig auf dasselbe Karpathy-Zitat/-Konzept eines persistenten LLM-Wikis („Inbox → Wiki → Output" dort vs. „Capture → Ground → Connect → Use" hier) — kein Widerspruch, aber deutliche inhaltliche Nähe. Der dortige Ansatz ist ein manuell per Prompt instruierter Workflow ohne festes Tool; dieses Video zeigt dagegen ein konkretes, fertiges Open-Source-Plugin mit Obsidian als tatsächlicher Notizen-App. Die Karpathy-Originalquelle selbst wurde auch dort schon als ungeprüft markiert und bleibt es hier.
- **Bezug zu [video-summary-qtte0zpnGks.md](video-summary-qtte0zpnGks.md):** Jenes Video fordert für Unternehmen eine zentrale „Company Brain"/Ontologie „statt verstreuter PDFs/Markdown-Dateien in Obsidian" — claude-obsidian adressiert genau diesen Kritikpunkt direkt (verlinktes, gepflegtes Vault statt lose verstreuter Dateien), ist aber ein Einzelnutzer-/Team-Tool, kein unternehmensweites Ontologie-System. Erwähnenswerte Ergänzung, kein Widerspruch.
- **Relevanz für die Team-/Gruppenleiter-Rolle:** Da die Zielperson bereits mit Claude Code arbeitet, ist claude-obsidian ein konkret nutzbares, kostenloses, lokal bleibendes Werkzeug für eigenes Wissensmanagement (Projektnotizen, Entscheidungen, wiederkehrende Recherchen) — im Unterschied zu den meisten anderen in diesem Repo dokumentierten Cloud-/Abo-Tools bleiben die Daten dabei als reines Markdown auf dem eigenen Rechner (git-freundlich, kein Vendor-Lock-in laut Video). Der PARA-Modus dürfte für strukturierte Team-/Projektarbeit die naheliegendste Wahl sein.

**Hinweis zum Ablauf:** Native englische YouTube-Untertitel wurden erfolgreich geladen (264 Segmente über yt-dlp), kein Whisper-Fallback nötig. Die Zusammenfassung basiert auf dem vollständigen Transkript plus allen 80 extrahierten Frames — bei diesem stark bildschirmlastigen Format (GitHub-README, Skill-Tabellen, Graph-Ansichten) lieferten die Frames deutlich mehr verwertbare Detailinformation (exakte Skill-Namen, Modi, Zitate) als das Transkript allein.
