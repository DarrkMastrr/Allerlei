# "Du MUSST Home Assistant MCP JETZT nutzen!! (Claude baut dein Smart Home)"

**Kanal:** simon42
**URL:** https://www.youtube.com/watch?v=AL391nkWGIc
**Länge:** 35:51
**Zusammenfassung erstellt:** 2026-07-04

---

*Siehe auch: [mcp-ueberblick.md](../mcp-ueberblick.md) für das allgemeine MCP-Konzept über dieses Video hinaus.*

## Was ist MCP und warum ist es relevant für Home Assistant?
Home Assistant hat eine API, über die normalerweise Apps zugreifen. Das Model Context Protocol (MCP) setzt sich dazwischen und öffnet diese API strukturiert für KI-Modelle — nicht nur lesend, sondern auch schreibend/erstellend.

## Eingebauter MCP-Server vs. Community-Projekt "ha-mcp"
- **Eingebauter Server:** kontrolliert nur Entities/Geräte, Szenen/Automationen abfragen; Entity-Scope beschränkt auf für "Assist" freigegebene Entities; kein Automationen-/Szenen-Editing, keine Dashboards, kein Debugging über Traces
- **ha-mcp:** voller Zugriff auf alle Entities, kann Automationen/Skripte/Szenen erstellen und bearbeiten, Dashboards bauen, Automationen anhand von Traces/Logs debuggen, Helper/Areas/Zones/Labels/Groups verwalten, sowie Backups, Add-ons, HACS und die Geräte-/Entity-Registry ansteuern
- Faustregel: eingebauter Server reicht für Sprachsteuerung bereits freigegebener Geräte; für aktives Bauen/Konfigurieren/Debuggen braucht es ha-mcp

## Einrichtung
- Installation von "Home Assistant MCP Server" über HA App-Store/HACS, inkl. Tool Security Policies, Allow-/Deny-Listen, automatisches Backup vor Änderungen
- Für Fernzugriff: "Nabu Casa Webhook Proxy for HA MCP", damit externe KI-Clients ohne Portfreigabe zugreifen können

## MCP-Server mit KI verbinden
- Demo mit LM Studio (lokales Modell, z.B. Gemma) als MCP-Client via Webhook-Proxy-Endpunkt
- Testfrage nach Entities erfolgreich beantwortet mit realen Daten aus der Hausinstallation

## Claude als Automatisierungs-Assistent + "Best Practices"-Skill
- Agent Skill "home-assistant-best-practices" (installierbar via `npx skills add` oder Plugin-Marketplace) mit Entscheidungsworkflows, Namenskonventionen und sicheren Vorgehensweisen

## Praxisbeispiele
- **Regen-heute-Sensor:** Claude erkennt, dass der vorhandene Niederschlagssensor ein kumulativer Zähler ist, und legt per MCP-Tool einen Utility-Meter-Helper mit täglichem Reset an
- **Baby-Dashboard-Badge:** Anbindung von Baby Buddy per REST API, Templates für Trinkmengen-Badges
- **Kinderzimmer-Lichtautomation debuggen:** Bug (Helligkeit/Farbe blieb nach Dimmen nicht erhalten) über Automations-Trace analysiert, Claude liefert Fix-Vorschlag

---

## Kernbotschaft
MCP öffnet Home Assistant für KI-Assistenten nicht nur zur Steuerung, sondern zur aktiven Mitgestaltung: Entities lesen, Helper und Automationen erstellen, Dashboards bauen und Fehler über Traces debuggen. Die Community-Lösung "ha-mcp" geht dabei deutlich über den eingebauten HA-MCP-Server hinaus.

## Themen-Tags
Home Assistant, MCP (Model Context Protocol), Claude, KI-Hausautomation, Smart Home, Lokale KI (LM Studio), Agentic Coding / Agent Skills

## Zu prüfen
- Feature-Vergleich eingebauter MCP-Server vs. "ha-mcp" gegen aktuelle Dokumentation verifizieren (beide Projekte entwickeln sich schnell weiter)
- Gezeigte Versionsnummer der HA-MCP-Tools-Integration gegen aktuell tatsächliche Version prüfen
- Funktionsweise/Kostenmodell des Nabu-Casa-Webhook-Proxy für HA-MCP

**Hinweis:** Native Audiospur/Untertitel waren nicht abrufbar, Whisper-Fallback (Replicate) scheiterte mit HTTP 429 ("less than $5.0 in credit"). Zusammenfassung basiert auf 80 Frames und On-Screen-Texten, nicht auf gesprochenem Inhalt. Siehe [whisper-replicate-rate-limit.md](whisper-replicate-rate-limit.md).
