# "Hermes AI Just Learned to Read Books"

**Kanal:** Julian Goldie SEO
**URL:** https://www.youtube.com/watch?v=0sDKQMO23xE
**Länge:** 12:13
**Zusammenfassung erstellt:** 2026-08-14

**Hinweis zum Ablauf:** yt-dlp lieferte auf das adaptive Standardformat einen HTTP-403-Fehler (bekanntes PO-Token-Problem). Fallback auf das progressive kombinierte Format (`-f "best[ext=mp4]"`, hier Format 18) hat funktioniert, Auflösung niedriger, Text auf den gezeigten Screens blieb aber lesbar. Native englische Untertitel (yt-dlp) plus alle 100 Frames über die volle Länge gelesen.

---

*Siehe auch: [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) (Grundkonzept "Skill als portabler, Progressive-Disclosure-geladener Ordner" — die hier gezeigte Hermes-Funktion ist im Kern dieselbe Idee, nur für ganze Bücher/Dokumente statt einzelner Workflows). Cross-Checks siehe unten in "Zu prüfen".*

## Worum es geht: Hermes Agent lernt ganze Bücher

Kernthema: Der neue `/learn`-Befehl von **Hermes Agent** (Open-Source-Agent-Framework von **Nous Research**, Entwickler-Lead im Video als "Technium" bezeichnet — richtig geschrieben **Teknium**, Mitgründer/Lead Engineer) kann jetzt ganze Bücher, PDFs, Word-/PowerPoint-/EPUB-Dateien etc. verarbeiten und daraus eine dauerhafte "Skill" bauen, statt sie nur einmalig ins Kontextfenster zu laden. Laut Host: `/learn` + Dateipfad genügt, keine Programmierkenntnisse nötig.

Der Presenter nennt das eigene Marketing-Label **"Book Brain Engine™"** (mit Trademark-Symbol, durchgängig im Screen-Overlay "Get the Book Brain Engine™ inside the AI Profit Boardroom" sichtbar) — das ist **keine offizielle Nous-Research-/Hermes-Bezeichnung**, sondern ein vom Host selbst geprägter Begriff für seinen eigenen Kurs/seine Community.

## Wie das Feature technisch funktioniert (im Video gezeigt)

- Statt das Buch bei jeder Konversation neu ins Kurzzeitgedächtnis zu kippen, liest der Agent es einmal komplett, extrahiert Frameworks/Entscheidungsregeln/Fehler-Vermeidung und baut eine Ordnerstruktur: eine `SKILL.md`-Indexdatei, eine Referenzdatei pro Kapitel, ein Glossar und ein Cheat-Sheet.
- Bei einer neuen Frage öffnet der Agent gezielt nur das benötigte Kapitel statt das ganze Buch neu zu lesen ("Discovery Loop Tax" — im GitHub-Repo-Screenshot als offizieller Fachbegriff des Projekts sichtbar).
- Laut im Frame lesbarem X-Post von Teknium (Antwort auf eine Nutzerfrage): Die Haupt-Skill-Datei ist auf 100.000 Zeichen (~33.000 Token) gedeckelt, größere Inhalte wandern automatisch in kompakte Referenzdateien.
- Vorher waren Hermes-Skills laut einem weiteren im Frame gezeigten Teknium-Tweet auf max. 200 Zeilen ohne Referenzdateien begrenzt ("skills were built for little tasks") — die neue Version erlaubt für große Quellen (Bücher, Papers, Doku-Ordner) explizit umfangreichere, mehrteilige Skills.
- Unterstützte Formate laut Video: PDF, Word, PowerPoint, Excel, OpenDocument, RTF, EPUB — Konvertierung läuft laut gezeigtem Tweet lokal über das separate Open-Source-Tool `anydoc` (von Nicolas Camara, aufbauend auf @firecrawl).

## Live-Demo im Video: Sun Tzus "Die Kunst des Krieges"

Der Host führt `/learn` live an einem EPUB von Sun Tzus "The Art of War" vor (Terminal-Screenshot). Ergebnis: Ordnerstruktur mit `SKILL.md` und `references/`-Unterordner (u. a. Dateien zu Themen wie Verhandlung/Angriff-vs-Verteidigung). In einer neuen Chat-Session (kein erneuter Upload) beantwortet der Agent laut Demo eine Strategiefrage, indem er gezielt das passende Kapitel aus der gelernten Skill öffnet statt zu raten.

## Die genannten Zahlen — Herkunft geprüft

- **"24 bis 51× weniger Token"** gegenüber dem Dumpen des ganzen Buchs in den Kontext: Diese Zahl stammt laut Video aus dem eigenen Benchmark-Test des zugrundeliegenden Open-Source-Projekts **`book-to-skill`** (GitHub-README im Frame sichtbar, MIT-Lizenz, Badges "#3 GitHub Trending" / "#1 Repository of the Day").
- **"Über 18.000 GitHub Stars"**: Auf der eigenen Landingpage des Hosts im Frame lesbar als "18k+ stars on the engine".

## Praxis-Use-Cases (laut Video)

Nicht nur Bücher: interne Dokumentation, Marken-/Voice-Guidelines, Forschungspapiere, Spezifikationen/Standards — alles, was man "oft genug wieder aufschlägt, dass man es sich wünscht, es wäre memoriert". Genannte Beispiele: Agentur-Onboarding-Dokument als Skill für konsistente Task-Ausführung, Coaching-Programm-Material für automatisierte Kundenantworten im eigenen Stil, Marken-Voice-Guide für konsistente Produkttexte/E-Mails.

## Werbliche Inhalte

Deutlicher Eigenwerbe-Anteil: Mehrfache Cross-Promotion für die eigene bezahlte Community **"AI Profit Boardroom"** (Skool-Gruppe, im Frame sichtbar: "MAKE MONEY WITH AI", 3.800+ Mitglieder, Flash-Sale-Banner "$59/Monat, normal $71/Jahr — Save $144/Jahr" [Preisangaben im Screenshot leicht widersprüchlich, siehe "Zu prüfen"]) sowie für eine eigene Dashboard-Anwendung "Agentic OS" / "Mission Control" (Multi-Agent-Übersicht, Obsidian-artiges Memory-Graph-Tool, Hermes-Chat-Integration). Der gesamte zweite Videohälfte-Teil ("Step 1-4 diese Woche") ist strukturiert als Lead-Funnel in Richtung dieses Kurses.

## Für den technischen Team-Lead: Relevanz

Der Kernmechanismus (Dokument → strukturierte, per Index/Kapitel-Datei abrufbare Agent-Skill statt wiederholtem Volltext-Upload) ist für einen Gruppenleiter mit Team-Dokumentation (SOPs, Spezifikationen, Hardware-Handbücher) direkt interessant: Es ist im Kern dieselbe **Progressive-Disclosure**-Idee, die bereits in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) als Claudes Skill-Grundkonzept dokumentiert ist — nur hier auf lange, unstrukturierte Quellen (Bücher, Handbücher) angewandt statt auf kurze Workflow-Anleitungen. Der im Video mehrfach betonte Punkt, dass das Skill-Format dem **"offenen Agent Skills Standard"** folgt und laut Aussage im Video über Hermes, Claude Code, GitHub Copilot CLI und Amp portabel ist, deckt sich mit der in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) diskutierten These, dass die Skill-Definition selbst anbieterunabhängig übertragbar ist — ein Plus-Punkt für die dort beschriebene Resilienz-/Anti-Vendor-Lock-in-Strategie. Praktisch nutzbar wäre der Ansatz z. B. für ein internes Hardware-Handbuch oder eine Normenreihe, die ein Agent dauerhaft griffbereit halten soll, ohne bei jeder Anfrage neu eingelesen zu werden.

---

## Fact-Check

**Kernfeature ist real und unabhängig bestätigt.** Per WebSearch verifiziert: Nous Research / Teknium haben den `/learn`-Befehl für Hermes Agent tatsächlich um die Verarbeitung ganzer Bücher erweitert, indem sie laut Tekniums eigenem X-Post das Open-Source-Projekt **`book-to-skill`** in den `/learn`-Befehl integriert haben ("Integrated the work of book-to-skill repo into our /learn command..."). Offizielle Hermes-Agent-Doku (hermes-agent.nousresearch.com) beschreibt `/learn` und die "expansive knowledge-base skill"-Struktur (Index-`SKILL.md` + eine Datei pro Kapitel + Glossar/Cheatsheet) nahezu wortgleich zu dem, was im Video als Screenshot gezeigt wird — Video-Inhalt deckt sich hier eng mit der Primärquelle.

Das zugrunde liegende `book-to-skill`-Projekt selbst existiert real auf GitHub (Original von Entwickler "Virgilio Jr", nicht von Nous Research), folgt laut mehreren unabhängigen Quellen tatsächlich dem offenen "Agent Skills"-Standard (funktioniert über Claude Code, GitHub Copilot CLI, Amp) und bewirbt selbst die "24-51× weniger Token"-Kennzahl. **Kleine Diskrepanz bei der Sternezahl:** Eine im Rahmen dieser Prüfung gefundene Sekundärquelle (CoddyKit-Blog) nennt "12.256 GitHub Stars", während Video und Host-eigene Landingpage "18k+" nennen — plausibel als zeitliche Differenz (GitHub-Sterne wachsen kontinuierlich, exakter Snapshot-Zeitpunkt unklar), aber nicht mit einer autoritativen Live-Quelle exakt gegengecheckt.

**Nicht geprüft/nicht prüfbar:** Die konkreten Demo-Ergebnisse (Sun-Tzu-Test, Antwortqualität) sind reine Bildschirmaufnahmen des Hosts, nicht unabhängig nachvollziehbar. Die "18.000 Personas" / "3.800 Business Owner" / "flash sale"-Zahlen zur eigenen Community sind unbelegte Eigenangaben des Hosts.

**Werbliche Vermischung als Kritikpunkt:** Der reißerische Titel ("Just Learned to Read Books") beschreibt eine reale, dokumentierte Produkt-Funktion korrekt im Kern — das Video nutzt sie jedoch fast durchgehend als Aufhänger für die eigene bezahlte Community, inklusive eines selbst erfundenen Markenbegriffs ("Book Brain Engine™") für eine Funktion, die eigentlich kostenlos und quelloffen (Nous Research + `book-to-skill`) ist.

## Kernbotschaft

Das im Video beschriebene Feature ist real: Hermes Agent (Nous Research, Open Source) hat seinen `/learn`-Befehl tatsächlich um die Fähigkeit erweitert, ganze Bücher/Dokumente in eine dauerhafte, kapitelweise abrufbare Agent-Skill zu verwandeln — basierend auf dem quelloffenen Projekt `book-to-skill` und dessen eigener "24-51× weniger Token"-Kennzahl, unabhängig per WebSearch bestätigt. Inhaltlich ist das Video eine im Kern korrekte, aber stark werblich verpackte Erklärung einer echten, kostenlosen Open-Source-Funktion — der Host verkauft sie unter einem selbst erfundenen Markenbegriff ("Book Brain Engine™") als Aufhänger für seine bezahlte "AI Profit Boardroom"-Community. Für technische Team-Leads ist der zugrunde liegende Mechanismus (Dokument → strukturierte, indexierte Skill statt wiederholtem Volltext-Kontext) unabhängig vom Marketing-Rahmen ein reales, nützliches Muster für interne Dokumentation/SOPs.

## Themen-Tags
Hermes Agent, Nous Research, Teknium, /learn-Befehl, book-to-skill, Agent Skills Standard, Progressive Disclosure, SKILL.md, Token-Effizienz, Claude Code, GitHub Copilot CLI, Amp, AI Profit Boardroom, Fact-Check

## Zu prüfen

- **Cross-Check mit claude-skills-ueberblick.md:** Starke inhaltliche Überschneidung — das dort dokumentierte Claude-Skill-Grundkonzept (echter Ordner mit Markdown, Progressive Disclosure, anbieterunabhängig übertragbares Format als Anti-Vendor-Lock-in-Argument) ist praktisch identisch mit dem hier gezeigten Hermes-`/learn`-Mechanismus, nur auf lange unstrukturierte Quellen statt kurze Workflows angewandt. Kein Widerspruch, eher eine Bestätigung/Erweiterung der dortigen These, dass das Skill-*Format* (nicht der Anbieter) der eigentliche portable Wert ist.
- **GitHub-Sternezahl `book-to-skill`:** Video/Host-Landingpage nennen "18k+", eine gefundene Sekundärquelle "12.256" — nicht mit einer Live-GitHub-Abfrage exakt zum Videozeitpunkt (8. August 2026, laut `upload_date` im Metadaten-JSON) gegengecheckt, plausibel als Wachstum über Zeit.
- **"Book Brain Engine™"** ist erkennbar eine Eigenschöpfung des Hosts für seinen Kurs, keine offizielle Nous-Research-/Hermes-Bezeichnung — im Video selbst nicht transparent als solche gekennzeichnet, wird in dieser Zusammenfassung entsprechend getrennt dargestellt.
- **Preisangaben "AI Profit Boardroom"** im Frame leicht inkonsistent lesbar ("$59/Monat" vs. "Normal price $71 → NOW $59 (Save $144 per year!)" — Monats- und Jahrespreis wirken im Screenshot vermischt); bei 512px-Framebreite nicht zweifelsfrei zu entziffern, hier nur als Unsicherheit vermerkt, nicht als harte Zahl übernommen.
- Einzelne Community-Zahlen des Hosts (3.800+ Mitglieder, "18.000 Personas" im Transkript vs. sichtbare Mitgliederzahl im Frame) wurden nicht unabhängig verifiziert, da es sich um unbelegte Eigenangaben eines Drittanbieters handelt.
