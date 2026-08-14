# "Wie ANTHROPIC intern mit CLAUDE arbeitet und wie MCP zum Industriestandard wurde! 💬 🚀"

**Kanal:** AI to the DNA (Host: Christoph Magnussen, CEO von Blackboat)
**URL:** https://www.youtube.com/watch?v=1guudCDr0H4
**Länge:** 59:55
**Zusammenfassung erstellt:** 2026-08-14

**Hinweis zum Ablauf:** Nativer yt-dlp-Download scheiterte zunächst mit HTTP 403/429 (adaptive Formate, fehlender PO-Token). Funktioniert hat der empfohlene Workaround: `--extractor-args "youtube:player_client=android"` plus progressives Format 18 (360p). Dabei wurden direkt auch die deutschen Auto-Untertitel (video.de.vtt, 1598 bereinigte Segmente) mitgeladen — dadurch war kein Whisper-Fallback nötig, es handelt sich um echte YouTube-Auto-Captions, nicht um eine Transkription. Das komplette Transkript wurde vollständig gelesen. Zusätzlich 100 Frames über die volle Länge gesichtet: durchgehend ein reines Zwei-Personen-Sitzinterview im Hotelzimmer (Podcast-Branding "AI TO THE DNA" eingeblendet), keine Folien, keine Namens-Bauchbinden, kein Screensharing — die Frames liefern daher kaum zusätzliche Information über den Transkript-Inhalt hinaus.

---

## Rahmen: Gäste und Format

Christoph Magnussen (Gastgeber, Unternehmer, u. a. CEO von Blackboat, einer Beratung für KI-Einführung im Mittelstand) interviewt **David Soria Parra**, Member of Technical Staff bei Anthropic und Mitentwickler des Model Context Protocol (MCP). Per WebSearch verifiziert: David Soria Parra ist real, seit April 2024 bei Anthropic, davor u. a. Engineering Manager bei Meta (AR/VR-Infrastruktur) — deckt sich mit seiner Aussage im Video, "10 Jahre bei Meta" gewesen zu sein. MCP wurde laut unabhängigen Quellen von David Soria Parra **und** Justin Spahr-Summers entwickelt; Letzterer wird im Video nicht erwähnt.

## MCP-Entstehungsgeschichte bei Anthropic

David beschreibt den internen Ursprung: Ausgangspunkt war die Beobachtung, dass ein zentrales Developer-Tooling-Team immer langsamer wächst als der Rest der Firma — die einzige Skalierungsoption sei, Mitarbeitenden Werkzeuge zu geben, mit denen sie sich selbst Integrationen bauen können, weil sie ihren eigenen Workflow besser kennen als jedes zentrale Team. Ursprünglicher interner Arbeitstitel war **"Claude Connect"**. Weil es gleichzeitig mehrere Clients gab (Claude Desktop, IDEs wie Zed, VS Code), entstand das klassische N-Clients-×-M-Integrationen-Problem — daraus wurde die Idee, MCP als Protokoll zu bauen.

## MCP vs. API vs. CLI — der Vorteil des Protokolls

David ordnet MCP bewusst zwischen zwei Alternativen ein:
- **Gegenüber klassischen APIs:** API-Endpunkte sind ursprünglich für programmatischen Zugriff gedacht und oft zu granular (z. B. getrennte Endpunkte für Suche-nach-Name/-ID/-Keyword) — für Modelle schlecht nutzbar. MCP sei "nicht viel mehr als eine API mit einem semantischen Layer" für Dinge wie Authentifizierung, automatisches Nachfragen beim Nutzer, Human-in-the-loop-Bestätigungen.
- **Gegenüber CLI-Zugriff:** CLI sei für einzelne Entwickler und kleine Firmen gut geeignet. Für größere Organisationen, die keine Binärdatei auf jeden Laptop verteilen wollen, sondern einen zentralen Server mit Policy-Enforcement/Governance-Layer brauchen, sei ein Protokoll wie MCP die bessere Wahl.

## Claude Tag: Claude als "eigene Entity" in Slack

Zentrales Praxisbeispiel im Gespräch, mit dem der Podcast auch einsteigt: **Claude Tag**, die neue Slack-Integration. Per WebSearch verifiziert: real, ging am 23. Juni 2026 in die Public Beta für Claude-Enterprise/Team-Kunden — passt zeitlich zum Video (Upload 31. Juli 2026, "vor Kurzem veröffentlicht"). Anders als der reine Claude-Code-Modus (Mensch sitzt davor, Modell arbeitet an der einen konkreten Aufgabe) beschreibt David Claude Tag als "wirklich zum ersten Mal ein Produkt, das eine eigene Entity ist" — mit eigenen Zugriffsrechten (z. B. auf GitHub-Repos), asynchron arbeitend, und in der Lage, **proaktiv** zu agieren: Beispiel im Video ist eine Observability-Plattform (Datadog/Sentry), die nach einem Deployment erhöhte Fehlerraten in einen Slack-Channel postet — Claude untersucht das eigenständig und meldet sich mit Diagnose-Vorschlägen, bevor jemand es explizit bittet. David beschreibt das als qualitativen Sprung gegenüber "Claude Code, wo du davorsitzt".

## Ultracode: Modellsprünge und weniger Scaffolding

David beschreibt einen von Anthropic intern beobachteten "Capability Jump" beim Sprung von Opus 4.1 zu Sonnet 4.5 (Transkript nennt die Zahlen verkürzt "41" und "45") — insbesondere darin, wie lange ein Agent an einer Aufgabe eigenständig weiterarbeiten kann (10–30 Minuten statt kurzer Turns), was mehr asynchrone interne Tooling-Architektur ermöglicht habe. Als konkretes Beispiel nennt er **"Ultra Code"**: ein Modus, in dem Claude Code sich selbst orchestriert (mehrere Subagenten aufmacht, die parallel suchen, daraus einen Index baut). Per WebSearch verifiziert als real existierendes Feature: **"ultracode"**, seit 28. Mai 2026 in Claude Code verfügbar, kombiniert maximale Reasoning-Tiefe ("xhigh") mit automatischer Orchestrierung paralleler Subagenten-Workflows (per `/effort ultracode`).

David vertritt die These, dass mit steigender Modellfähigkeit **weniger** manuell gebautes Scaffolding/Werkzeuge nötig werden — bei Anthropic intern seien deshalb bereits Dinge wieder aus Claude Code entfernt worden, weil das Modell sie inzwischen ohne Hilfsmittel selbst kann. Einschränkung: In Firmen mit anderem Risikoprofil könnten engere, restriktivere "Harnesses" weiterhin sinnvoll bleiben — bei Anthropic selbst sei "weniger mehr", weil das Modell besser geworden sei.

## Governance: Wie MCP zum offenen Industriestandard wurde

Dieser Abschnitt ist der inhaltlich wertvollste Teil aus Sicht von [mcp-ueberblick.md](../mcp-ueberblick.md), da er dort bislang fehlt: David beschreibt bewusste Governance-Entscheidungen von Anfang an, damit MCP "wirklich" offen bleibt:
1. **Lizenzwahl:** MIT-Lizenz (per WebSearch verifiziert: korrekt, MCP-Hauptrepository steht unter MIT), bewusst **ohne Contributor License Agreement (CLA)** — laut David, damit Anthropic die Lizenz später nicht mehr ändern kann, ohne alle jemals beteiligten Mitwirkenden fragen zu müssen. (Die CLA-Angabe selbst stammt nur aus dem Video/von David als Erstquelle, wurde nicht unabhängig gegengeprüft.)
2. **Übertragung an eine neutrale Stiftung:** Auf Nachfrage des Hosts bestätigt David die Übertragung an die **Linux Foundation**. Per WebSearch verifiziert und **stimmt**: Anthropic übergab MCP im Dezember 2025 an die neu gegründete **Agentic AI Foundation (AAIF)** unter dem Dach der Linux Foundation — mit acht Platin-Mitgliedern (AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI) und einem Technical Steering Committee. Das deckt sich exakt mit Davids Begründung im Video: Firmen sollen auf MCP aufbauen und Dependencies bilden können, ohne dass eine einzelne Firma es theoretisch zurückziehen könnte.

## Agent Identity — das nächste große Standardisierungsthema

David beschreibt seinen aktuellen Arbeitsschwerpunkt als "Agent Identity": Wie identifizieren/autorisieren sich Agenten gegenüber anderen Systemen, wie kommunizieren Agenten unterschiedlicher Firmen miteinander in einer gemeinsamen "Sprache", und (unter Bezug auf ein Gespräch mit Johannes Otterbach, laut David vorher bei OpenAI und Palantir) ob Agenten perspektivisch eine eigene **rechtliche Identität** bräuchten. Wird als aktuell "langweilig wirkendes, aber sehr wichtiges" Standardisierungsthema mit potenziell rechtlichen Konsequenzen beschrieben — nicht weiter im Detail ausgeführt, nicht unabhängig geprüft.

## Anthropics interne Kultur

- **"Member of Technical Staff"** als einheitlicher Titel ohne Hierarchie-Kennzeichnung — laut David eine Praxis mit Wurzeln bei Facebook/Google: Kompetenz soll durch Arbeit entstehen, nicht durch Titel. Der Host vergleicht das mit seinem eigenen Versuch bei Blackboat ("Crewmember" für alle), räumt aber ein, dass Kunden trotzdem wissen wollen, wer welche Rolle hat.
- **Persönlichkeitsarbeit an Claude:** David erwähnt ein Team um "Amanda Skel" (Transkript-Fehlschreibung; per WebSearch verifiziert als **Amanda Askell**, real — Philosophin, leitet bei Anthropic das Team für Claudes Charakter/"Constitution", 2024 auf der TIME100-AI-Liste), das an Freundlichkeit, Ton und Vertrauensaufbau arbeitet — mit Verweis darauf, dass Anthropic Claudes System-Prompts öffentlich macht.
- **Anthropic Economic Index:** kurz erwähnt als internes Forschungsformat, um den wirtschaftlichen Wandel durch KI-Systeme zu verstehen (real existierendes Anthropic-Forschungsprojekt, nicht im Detail vertieft).

## USA vs. Deutschland: Kulturunterschiede in Tech-Firmen

David (lange in den USA, vorher München) nennt auf Nachfrage des Hosts zwei Beobachtungen: (1) ein grundsätzlicher amerikanischer Technologie-Optimismus ("net positive, wenn man es richtig einsetzt") kombiniert mit starker Selektion auf **"High Agency"**-Mitarbeitende, denen viel Vertrauen und wenig Struktur gegeben wird ("wenn was passiert, räumen wir danach auf"); (2) dass US-Spitzenfirmen im SaaS/Tech-Bereich von oben bis unten technisch geprägt seien (viele CEOs/CTOs mit Research- oder Engineering-Hintergrund), was schnellere interne Adaption neuer Tools begünstige. Als Positivbeispiel für deutsche Firmen, die früh experimentierten, nennt er ohne Namen zu nennen den Ansatz, den besten Entwicklern früh eine Kreditkarte und Freiraum zu geben, bestehende Regeln testweise zu verschieben.

## Historische Analogien

Ein längerer Gesprächsteil ordnet die aktuelle Entwicklung historisch ein: Unix als Davids persönliches Wunsch-Projekt ("hätte ich gerne mitgebaut") wegen seines "outsized influence" als generelle, pragmatische statt technisch perfekte Plattform; der C++-Erfinder Bjarne Stroustrup (im Transkript nur "der dänische Entwickler", korrekt: Stroustrup ist Däne) und Grace Hopper/der erste Compiler als Beispiele für Pragmatismus, der sich gegen anfängliche Kritik durchsetzt; Postgres als weiteres "zufällig" entstandenes Standard-Beispiel. Auf die zugespitzte Frage, ob Anthropic "die neuen Bell Labs" seien, antwortet David bewusst ausweichend ("History will tell") und verweist auf oft vergessene Vorläufer wie Xerox PARC (Erfinder des User Interface). Seine Einordnung: Compute-Architektur, Compiler und Betriebssysteme hätten sich historisch immer additiv statt disruptiv entwickelt — er erwartet dasselbe Muster für die aktuelle KI-Welle.

## Rat an junge Entwickler und an Führungskräfte

- **An junge Leute:** Systemwissen (wie Computer/Programme funktionieren) bleibt wichtig; in dem arbeiten, was man wirklich liebt, statt einer Trend-Karriereplanung zu folgen.
- **An Entscheider/CEOs:** Den wirtschaftlichen Wandel durch KI ernst nehmen, Mitarbeitenden explizit Raum zum Experimentieren geben, und vor allem verinnerlichen, dass Veränderung kein einmaliger Punkt, sondern ein dauerhaftes Organisationsprinzip ist ("ich weiß nicht, wie es in einem Jahr aussieht — nur, dass es anders aussieht als heute").
- **Schlusspointe:** Man solle regelmäßig gedanklich extrapolieren, was der jeweils nächste Modell-Capability-Sprung (nach dem Muster Opus 4.1 → Sonnet 4.5 → "Fable") für die eigenen Systeme und Möglichkeiten bedeutet — dieses "Weiterdenken" werde laut David oft vergessen.

---

## Plausibilitätscheck / Fact-Check

Kein reißerisches Video im Stil der Everlast-AI-Kanäle im Repo — ruhiges Zwei-Personen-Fachgespräch, entsprechend wenig zu entzaubern. Die überprüften Kernfakten halten durchweg stand:
- **David Soria Parra:** real, Member of Technical Staff bei Anthropic, MCP-Mitentwickler, vorher bei Meta — verifiziert.
- **Claude Tag:** real, Public-Beta-Start 23. Juni 2026, passt zeitlich zum Upload-Datum — verifiziert.
- **Ultracode/"Ultra Code":** real, seit 28. Mai 2026 in Claude Code — verifiziert.
- **MCP-Übertragung an die Linux Foundation/Agentic AI Foundation (Dezember 2025):** verifiziert, deckt sich exakt mit Davids Darstellung.
- **Amanda Askell/Claude-Persönlichkeitsteam:** verifiziert, real.
- **MIT-Lizenz von MCP:** verifiziert. Die CLA-Aussage stammt nur von David selbst im Video, nicht unabhängig gegengeprüft.
- Historische Nebenfakten (Stroustrup als Däne, Grace Hopper/Compiler, Xerox PARC/UI) sind allgemein bekannte, unstrittige Fakten — nicht einzeln nachrecherchiert.

Insgesamt eine glaubwürdige, mit Primärquelle (MCP-Miterfinder) geführte Folge ohne erkennbare Übertreibungen — im Gegenteil, David formuliert an mehreren Stellen bewusst zurückhaltend ("History will tell", "man weiß nie, wie es in 12 Monaten aussieht").

## Wert für den technischen Team-Lead

Mehrere Punkte sind für eine Rolle als Gruppenleiter/technischer Entscheider direkt relevant:
- Der **MCP-vs-API-vs-CLI-Vergleich** ist eine klare Entscheidungshilfe für die Frage "brauchen wir für Tool X einen MCP-Server oder reicht die bestehende API/CLI?" — abhängig davon, ob ein Governance-/Policy-Layer für mehrere Teams/Clients gebraucht wird.
- Die **Governance-Lektion** (frühe Lizenzwahl ohne Rücknahmemöglichkeit, Übertragung an eine neutrale Stiftung) ist ein übertragbares Muster für eigene interne Standards/Tools, die firmenübergreifend Vertrauen brauchen sollen.
- Die wiederholte These "je besser das Modell, desto weniger Scaffolding nötig" ist eine konkrete, gegenläufige Position zu vielen anderen im Repo dokumentierten Videos, die aufwendige Agent-Harnesses/Skill-Sammlungen empfehlen (siehe [claude-skills-ueberblick.md](../claude-skills-ueberblick.md)) — wichtig als Gegengewicht, mit der eigenen Einschränkung, dass das je nach Risikoprofil der Organisation variiert.
- Der Führungsratschlag zu kontinuierlicher statt punktueller Veränderung und zu bewusst gegebenem Experimentierraum für die besten Leute ist unmittelbar auf eine Gruppenleiter-Rolle übertragbar.

## Kernbotschaft

Ein ruhiges, fachlich dichtes Gespräch mit MCP-Miterfinder David Soria Parra: MCP entstand aus einem internen Skalierungsproblem bei Anthropic ("Claude Connect") und wurde bewusst als offener Standard gebaut — mit früher Lizenzentscheidung (MIT, keine CLA) und der inzwischen tatsächlich vollzogenen Übertragung an die Linux Foundation/Agentic AI Foundation. Parallel zeigt das Gespräch, wie sich Anthropics interne Nutzung von Claude verändert hat: von reinem Claude-Code-Pairing hin zu "Claude Tag" als eigenständig und proaktiv agierender "Entity" in Slack, ermöglicht durch längere autonome Agenten-Laufzeiten (Ultracode) und die These, dass bessere Modelle tendenziell weniger, nicht mehr Scaffolding brauchen. Alle zentralen, überprüfbaren Fakten (Person, Produkte, Governance-Übertragung) halten der Prüfung stand.

## Themen-Tags
MCP, Model Context Protocol, David Soria Parra, Anthropic, Claude Tag, Ultracode, Agent Identity, Linux Foundation, Agentic AI Foundation, Open Source Governance, Claude Code, Amanda Askell, Christoph Magnussen, AI to the DNA, Blackboat, High Agency, Unternehmenskultur

## Zu prüfen
- **Verhältnis zu [mcp-ueberblick.md](../mcp-ueberblick.md):** Dieses Video liefert **genuin neue, bislang nicht im Übersichtsartikel enthaltene Information** — insbesondere die interne Entstehungsgeschichte ("Claude Connect"), die MCP-vs-API-vs-CLI-Abgrenzung aus Sicht des Mitentwicklers, und vor allem die verifizierte Governance-Übertragung an die Linux Foundation/Agentic AI Foundation (Dezember 2025) — Letzteres ist ein wichtiger, faktisch bestätigter Fortschritt gegenüber dem bisherigen Stand ("der generelle Lehrsatz... MCP ist nur das Protokoll") und sollte in den Übersichtsartikel eingearbeitet werden. Kein Widerspruch zum bisherigen Inhalt, nur Ergänzung.
- Die CLA-Aussage (keine Contributor License Agreement) stammt ausschließlich von David selbst im Video und wurde nicht unabhängig in den offiziellen MCP-Repo-Unterlagen gegengeprüft.
- MCP wurde laut unabhängigen Quellen von David Soria Parra **und** Justin Spahr-Summers mitentwickelt; Spahr-Summers wird im Video nicht erwähnt — keine falsche Aussage, aber eine unvollständige Zuschreibung.
- Die "Agent Identity"-Diskussion (inkl. Verweis auf ein Gespräch mit "Johannes Otterbach") wurde inhaltlich nicht weiter vertieft und hier nicht separat fact-gecheckt.
- Die automatischen deutschen YouTube-Untertitel enthalten an mehreren Stellen erkennbare Fehlhörungen bei Eigennamen/Fachbegriffen (u. a. "Cloud Tag"/"Claw Tag" für "Claude Tag", "Amanda Skel" für "Amanda Askell", "54"/"41 zu 45" für Modellversionen) — im Text oben jeweils korrigiert und kenntlich gemacht, aber vereinzelte weitere kleinere Fehltranskriptionen sind nicht auszuschließen.
- Modellversion-Bezeichnungen ("Fable" als Nachfolgegeneration) folgen der in diesem Repo bereits etablierten Namenskonvention (siehe [fable-5-modell-sperre.md](../fable-5-modell-sperre.md)), wurden hier nicht erneut eigenständig verifiziert.
