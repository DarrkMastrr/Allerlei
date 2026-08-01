# MCP (Model Context Protocol) — das Grundkonzept im Überblick

Quellen: [video-summary-sQBinJA_zxU.md](video-summaries/video-summary-sQBinJA_zxU.md), [claude-oekosystem-ueberblick.md](claude-oekosystem-ueberblick.md), [video-summary-B_OqkMRFonM.md](video-summaries/video-summary-B_OqkMRFonM.md), [video-summary-AL391nkWGIc.md](video-summaries/video-summary-AL391nkWGIc.md)

MCP wird in mehreren Videos am Rand erwähnt, aber nur in einem einzigen konkret vorgeführt (Home Assistant). Dieser Artikel bündelt das allgemeine Konzept mit dem praktischen Beispiel (siehe [notes-audit-report.md](notes-audit-report.md)).

## Was MCP ist

Model Context Protocol ist die offene Schnittstelle, die KI-Absichten in konkrete API-Aufrufe übersetzt — Analogie: MCP ist der Autoschlüssel, ein [Skill](claude-skills-ueberblick.md) ist die Fahrstunde (sQBinJA_zxU). B_OqkMRFonM beschreibt es als die offene Schnittstelle hinter den Connectors (Gmail, Google Calendar, Notion, Slack) — vergleichbar mit einem einheitlichen USB-Anschluss für KI-Tools: verschiedene Anbieter/Dienste stellen ihre Funktionen über dasselbe Protokoll bereit, statt dass jedes Tool eine eigene Integration bräuchte.

## Praxisbeispiel: MCP für Home Assistant (AL391nkWGIc)

Home Assistant hat eine eigene API, über die normalerweise nur Apps zugreifen. MCP setzt sich dazwischen und öffnet diese API strukturiert für KI-Modelle — nicht nur lesend, sondern auch schreibend/erstellend.

**Zwei Varianten mit sehr unterschiedlichem Umfang:**

| | Eingebauter MCP-Server | Community-Projekt "ha-mcp" |
|---|---|---|
| Entities | nur für "Assist" freigegebene | alle |
| Automationen/Szenen | nur abfragen | erstellen und bearbeiten |
| Dashboards | nein | bauen |
| Debugging | kein Zugriff auf Traces | Automationen anhand von Traces/Logs debuggen |
| Weiteres | — | Helper/Areas/Zones/Labels/Groups, Backups, Add-ons, HACS, Geräte-/Entity-Registry |

**Faustregel:** Der eingebaute Server reicht für Sprachsteuerung bereits freigegebener Geräte. Für aktives Bauen, Konfigurieren oder Debuggen braucht es die Community-Lösung.

**Einrichtung:** Installation über HA App-Store/HACS, inklusive Tool Security Policies, Allow-/Deny-Listen und automatischem Backup vor Änderungen. Für Fernzugriff ohne Portfreigabe: ein Webhook-Proxy (Nabu Casa), über den auch lokale KI-Clients (z. B. LM Studio) zugreifen können.

**Was das in der Praxis ermöglicht** (Beispiele aus dem Video): Claude erkennt, dass ein vorhandener Regensensor ein kumulativer Zähler ist, und legt selbstständig einen passenden Utility-Meter-Helper an; eine Kinderzimmer-Lichtautomation wird über die Automations-Trace analysiert und der Bug per Fix-Vorschlag behoben — beides wäre über den eingebauten Server (kein Trace-Zugriff, kein Helper-Erstellen) nicht möglich gewesen.

## Praktische Einordnung

Der generelle Lehrsatz aus dem Beispiel: MCP selbst ist nur das Protokoll/die Leitung. Wie viel ein Agent damit wirklich tun kann, hängt vollständig davon ab, was der jeweilige MCP-Server tatsächlich freigibt — ein "dünner" offizieller Server und ein "dicker" Community-Server können für dieselbe Anwendung völlig unterschiedliche Fähigkeiten bedeuten. Das lohnt sich vor der Einrichtung eines neuen MCP-Servers für ein anderes Tool zu prüfen, statt automatisch von voller Kontrolle auszugehen.

---

## Kernbotschaft
MCP ist die Übersetzungsschicht zwischen KI-Absicht und konkreten API-Aufrufen — technisch vergleichbar mit einem einheitlichen Anschluss, über den unterschiedliche Dienste ihre Funktionen bereitstellen. Wie viel Handlungsspielraum ein Agent dadurch bekommt, entscheidet aber nicht das Protokoll selbst, sondern der Funktionsumfang des jeweiligen MCP-Servers — offizielle Server sind oft bewusst eingeschränkt, Community-Server oft deutlich mächtiger.

## Themen-Tags
MCP, Model Context Protocol, Connectors, Home Assistant, Smart Home, Agentic Coding

## Zu prüfen
Offene Verifikationspunkte zum Home-Assistant-Beispiel (Feature-Vergleich, Versionsnummern, Kostenmodell des Webhook-Proxy) sind bereits in [video-summary-AL391nkWGIc.md](video-summaries/video-summary-AL391nkWGIc.md) erfasst.
