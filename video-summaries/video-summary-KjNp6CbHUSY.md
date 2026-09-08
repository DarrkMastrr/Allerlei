# "This NEW Claude Feature Is The Best Thing I've Used In 3 Years"

**Kanal:** AI Edge
**URL:** https://www.youtube.com/watch?v=KjNp6CbHUSY
**Länge:** 17:15
**Zusammenfassung erstellt:** 2026-09-08

**Fact-Check-Status: durchgeführt am 2026-09-08 per WebSearch. Die im Video gezeigte Kernfunktion ("Record a Skill" in Claude Cowork) ist real, am 21.07.2026 gelauncht und bereits zweimal unabhängig in diesem Repo dokumentiert (siehe Cross-Referenz) — dieses Video ist die dritte Demo derselben Funktion, liefert aber einige neue Detailtipps.**

---

*Siehe auch: [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) für das allgemeine Skill-Konzept inkl. "Record a Skill", [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md) und [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) für zwei frühere, ausführlichere Demos derselben Funktion.*

## Format des Videos

Talking-Head-Video (Kanal "AI Edge", Webcam-Bubble unten rechts) mit Screen-Recording-Demos der eigenen Claude-Desktop-App. Reißerischer Titel ("Best Thing I've Used In 3 Years") und deutliches Eigenmarketing: Am Ende wird ein kostenloses PDF ("The AI Employee Onboarding Plan") als Lead-Magnet für den Newsletter-Anmeldung beworben (im Frame bei ca. 16:49 sichtbar). Video erschien laut Websuche am 22.07.2026 — einen Tag nach dem offiziellen Feature-Launch (21.07.2026) und passt zu einem im Video selbst gezeigten Frame mit Datum "July 22, 2026".

## Die Funktion: "Record a Skill" in Claude Cowork

Deckt sich im Kern mit der bereits im Repo dokumentierten Funktion: In der Claude-Desktop-App den Tab **Cowork** wählen (nicht normaler Chat), über das Plus-Menü **"Record a Skill"** anklicken, Bildschirmaufnahme + Mikrofon starten, eine Aufgabe wie gewohnt am Bildschirm ausführen und dabei laut kommentieren ("erst mache ich dies, dann das..."). Claude verarbeitet Aufnahme und gesprochenen Kommentar danach zu einem wiederverwendbaren Skill, der per Slash-Trigger abrufbar ist und sich in der Skill-Bibliothek verwaltet, herunterladen und erneut anpassen lässt. Im Frame bei ca. 00:11 ist der zugehörige, im Video zitierte @claudeai-Tweet vom 21.07.2026 zu sehen ("Record your screen while you do a task, talk through it as you go, and Claude turns it into a skill it can run again... Available on Pro, Max, and Team plans").

## Neuer Tipp: Modellwahl zwischen Bauen und Ausführen

Der Host empfiehlt explizit, den Skill selbst mit dem stärksten verfügbaren Modell (im Video: **Fable 5**) aufnehmen/erstellen zu lassen, weil es Abläufe genauer destilliert und besseres kritisches Denken zeigt — für das spätere **Ausführen** des fertigen Skills reiche dagegen meist ein günstigeres Modell (**Opus 4.8** oder **Sonnet 5**), außer bei visuell/kreativ anspruchsvollen Aufgaben (Vibe-Coding, Grafikdesign). Dieser Kosten-/Nutzungssplit wird in den beiden bereits im Repo dokumentierten "Record a Skill"-Videos nicht erwähnt und ist damit der konkreteste neue Beitrag dieses Videos.

## Demo 1: Client-Onboarding-Prozess für eine Agentur

Der Host demonstriert (im Zeitraffer) seinen eigenen Agentur-Onboarding-Ablauf: Deal-Memo aus dem Notiz-Tool "Granola" öffnen, neuen Kundenordner anlegen, Dokument mit den Konditionen erstellen, Bestätigungsmail verschicken (laut Video kann Claude inzwischen per Connector direkt E-Mails versenden), Kundentracker-Tabelle aktualisieren, Zahlungseingang aus dem Postfach abgleichen und Meeting-Notizen ablegen. Claude beobachtet die komplette Sequenz und leitet daraus automatisch eine Schritt-für-Schritt-Skill-Datei ab (im Frame bei ca. 06:41 sichtbar als generiertes Markdown-Dokument "Client Onboarding — Deutscher Media"). Ein zweiter Testlauf mit einem fiktiven Kunden ("Focus Capital") ruft den gespeicherten Skill per Sprachbefehl (über die separate Diktier-App "WhisperFlow") ab.

## Demo 2: Content-Ideation-Pipeline (virale Outlier-Recherche)

Zweite Demo: Der Host zeichnet seinen eigenen Recherche-Workflow zum Finden "viraler Ausreißer"-Videos auf anderen YouTube-Kanälen auf (als Beispielkanal genannt: laut Untertiteln uneinheitlich "Nate O'Brien" bzw. später "Nate Hurk" — siehe Zu prüfen, gemeint ist vermutlich der reale AI-YouTuber Nate Herk). Kernthese: Nicht große, etablierte Kanäle kopieren, sondern kleine Kanäle beobachten, die mit einem einzelnen Video stark viral gegangen sind — das sei ein stärkeres Signal für ein funktionierendes Thema/Packaging. Workflow: Auffällige Videos identifizieren, Transkript über NotebookLM ziehen, Claude analysieren lassen warum das Video funktionierte, und thematisch verwandte, aber nicht identische Spin-off-Ideen vorschlagen lassen. Ergebnis im Video: automatisch generierte Themenideen wie "Claude Code Explained — zero coding required" oder "6 months of Claude Code lessons in 27 minutes".

## Skill-Verwaltung: Bibliothek, Backup, Portabilität

- Fertige Skills lassen sich über Einstellungen → Skills verwalten, herunterladen (als `.skill`-Datei) und in eine lokale Ordnerstruktur (z. B. nach Business/Personal, dann nach Themenbereich) einsortieren — Empfehlung des Hosts als Absicherung, "falls dem eigenen Claude-Account etwas passiert".
- Claude Code/Claude Code Work kann laut Host beauftragt werden, den Downloads-Ordner selbstständig nach `.skill`/`SKILL.md`-Dateien zu durchsuchen und automatisch einzusortieren.
- Behauptung im Video: Die heruntergeladenen Skill-Dateien seien grundsätzlich auch mit anderen KI-Systemen (explizit genannt: GPT) nutzbar, funktionierten aber "wahrscheinlich besser" auf Claude, wenn sie dort erstellt wurden. Nicht selbst im Video demonstriert, nur behauptet — deckt sich aber inhaltlich mit der bereits in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) dokumentierten Einschätzung, dass die Skill-Definition selbst (reines Markdown) meist anbieterunabhängig übertragbar ist.

## Weitere Einsatzideen und die "Employee"-Analogie

Der Host listet weitere Kandidaten für Skills auf: Vertrieb (Angebote, Anrufvor-/nachbereitung anhand des Kalenders), Finanzen/Admin (Rechnungsabgleich, monatliche Buchhaltung), Content (Newsletter, Threads), E-Commerce (Ticket-Triage, Meta-Ads-Anpassungen), Ops/Recherche und Hiring. Durchgehende Kernanalogie des Videos (auch als Grafik bei ca. 03:14 gezeigt: "Treat Claude Like An Employee"): Wie beim Einarbeiten eines neuen Mitarbeiters solle man die Aufgabe einmal vorführen und erklären ("warum" man etwas so macht) statt nur Ergebnisse zu erwarten — Feedback und Nachschärfen verbessere den Skill iterativ, genau wie bei einem Menschen. Der Host zieht dabei explizit eine Parallele zu Metas realem "Model Capability Initiative"-Programm, bei dem Meta seit April 2026 Bildschirmaktivität, Klicks und Tastatureingaben von Mitarbeitenden aufzeichnet, um eigene KI-Modelle darauf zu trainieren — laut Host "die exakt gleiche Methodik", jetzt für Endnutzer verfügbar gemacht.

---

## Plausibilitätscheck (per WebSearch, 2026-09-08)

**Kernfunktion real und bereits mehrfach im Repo bestätigt.** "Record a Skill" in Claude Cowork wurde laut mehreren unabhängigen Quellen (Search Engine Journal, Android Authority, cybersecuritynews.com, AlphaSignal, AI Weekly) am 21.07.2026 für Pro-, Max- und Team-Abos gelauncht — exakt wie im Video behauptet und bereits in [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md) und [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) fact-gecheckt. Dieses Video ist damit eine dritte, unabhängige, korrekte Demo derselben realen Funktion, keine erfundene Behauptung.

**Meta-Keylogger-Vergleich ebenfalls real.** Die Behauptung, Meta zeichne seit April 2026 Bildschirm, Klicks und Tastatureingaben von Mitarbeitenden auf, um eigene KI-Modelle zu trainieren, ist gut belegt (u. a. TechSpot, Fortune, San.com) — das Programm heißt "Model Capability Initiative" (MCI), umfasst laut Berichten periodische Screenshots plus vollständige Tastatur-/Klick-Erfassung über hunderte Websites/Apps hinweg (inkl. teils privater Nutzung wie Gmail), es gibt laut CTO Andrew Bosworth kein Opt-out für US-Beschäftigte (EU-Beschäftigte ausgenommen wegen DSGVO). Der Vergleich des Hosts ist also sachlich zutreffend, wenn auch verkürzt (Metas Programm betrifft eigene Angestellte unternehmensweit und ohne Wahlfreiheit, "Record a Skill" ist ein freiwilliges Endnutzer-Feature).

**Channel- und Titel-Check:** "AI Edge" als Kanal und die exakte Video-Veröffentlichung (22.07.2026, einen Tag nach Feature-Launch) ließen sich über die Suche bestätigen. Der reißerische Titel ("Best Thing I've Used In 3 Years") ist unüberprüfbare persönliche Übertreibung, aber die inhaltliche Beschreibung der Funktion selbst ist zutreffend — kein Fall von Clickbait mit falschem Kerninhalt.

**Kleine Unstimmigkeit im Transkript, nicht inhaltsrelevant:** Die (dieses Mal aus echten YouTube-Untertiteln stammende) Transkription nennt den Beispielkanal für virale Recherche einmal "Nate O'Brien" und wenig später "Nate Hurk" — vermutlich beides Verschreibungen des real existierenden AI-YouTubers **Nate Herk** (per Websuche bestätigt: bekannter Kanal für KI-Automatisierungs-Workflows). Betrifft nur den Eigennamen, nicht die inhaltliche Aussage.

## Cross-Referenz zu bestehenden Notizen

**Deutliche Themenüberlappung, kein Widerspruch.** [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) dokumentiert "Record a Skill" bereits als eigenen Abschnitt, gestützt auf zwei unabhängige frühere Demos mit wortgleichem Consent-Dialog ([video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md), [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md)). Dieses Video ist die **dritte** Demo derselben Funktion im Repo — keine der drei widerspricht sich, alle bestätigen dieselben Kernmechanik-Details (Cowork-Tab, Plus-Menü, Consent-Dialog, Skill-Bibliothek). Neu gegenüber den beiden bestehenden Videos sind: (1) der Modell-Split-Tipp (starkes Modell zum Bauen, günstigeres zum Ausführen), (2) die konkrete Empfehlung, Skills lokal als `.skill`-Dateien zu sichern und thematisch zu organisieren, sowie (3) die (unbelegte, aber plausible) Behauptung plattformübergreifender Portabilität — Letzteres bestätigt tendenziell die bereits in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) unter "Spannungsfeld: Skills als Produktivitätsgewinn vs. Vendor-Lock-in" gezogene Schlussfolgerung, dass die reine Skill-Definition anbieterunabhängig übertragbar sei. Keine inhaltlichen Widersprüche zu den beiden Auswahlkriterien aus [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md) (Connector bevorzugen, wenn vorhanden; nur bei extrem repetitiven Multi-App-Aufgaben aufzeichnen) — dieses Video äußert sich dazu einfach nicht.

---

## Für den technischen Team-/Gruppenleiter

Der praktisch nützlichste, in diesem Video neue Punkt ist der **Kosten-/Qualitäts-Split zwischen Skill-Erstellung und Skill-Ausführung**: Beim einmaligen Aufnehmen/Destillieren eines Workflows lohnt sich das stärkste verfügbare Modell (im Video Fable 5), weil hier die Qualität der destillierten Anleitung über die gesamte spätere Nutzungsdauer des Skills entscheidet — für die wiederholte Ausführung reicht danach oft ein günstigeres Modell. Übertragen auf ein Hardware-/Entwicklungsteam: Skills für wiederkehrende, aber gut abgrenzbare Abläufe (Testprotokoll-Auswertung, Report-Zusammenstellung, Onboarding-Checklisten für neue Teammitglieder) einmal mit dem besten verfügbaren Modell sauber aufnehmen lassen, danach im Alltag mit einem günstigeren Modell ausführen. Zweitens: Die Empfehlung, Skills lokal als Dateien zu sichern statt sie nur im Cloud-Account vorzuhalten, ist eine sinnvolle, einfache Absicherung gegen Anbieterausfall/-Sperre — passt zur bereits in [fable-5-modell-sperre.md](../fable-5-modell-sperre.md) dokumentierten Empfehlung, sich nicht vollständig auf einen einzigen KI-Anbieter zu verlassen. Wichtig gegenüber dem Team zu kommunizieren, falls "Record a Skill" eingesetzt wird: Der Consent-Dialog warnt ausdrücklich vor Passwörtern/sensiblen Bildschirminhalten während der Aufnahme (siehe bereits dokumentiert in [video-summary-HcWpz-0YLRo.md](video-summary-HcWpz-0YLRo.md)) — bei Hardware-/Firmen-internen Workflows mit vertraulichen Daten (Kundendaten, Zugangsdaten, unveröffentlichte technische Spezifikationen) ist das eine reale Stolperfalle, die dieses Video selbst nicht thematisiert.

## Kernbotschaft

Das Video ist eine dritte, sachlich zutreffende Demo der bereits im Repo dokumentierten, real am 21.07.2026 gelaunchten Anthropic-Funktion "Record a Skill" (Claude Cowork): Bildschirm aufnehmen und einen Arbeitsablauf laut kommentieren, statt ihn manuell zu beschreiben, wodurch Claude selbstständig einen wiederverwendbaren Skill ableitet. Über die bereits bekannten Mechanik-Details hinaus liefert es zwei praktisch nützliche neue Tipps (starkes Modell zum Bauen, günstiges zum Ausführen; lokale Skill-Sicherung als Backup-Strategie) sowie einen sachlich zutreffenden, wenn auch verkürzten Vergleich zu Metas realem Mitarbeiter-Tracking-Programm. Der reißerische Videotitel ist unbelegbare Übertreibung, verzerrt aber nicht die im Kern korrekte Funktionsbeschreibung.

## Themen-Tags

Claude Cowork, Record a Skill, Claude Skills, Skill-Bibliothek, Fable 5, Opus 4.8, Sonnet 5, Workflow-Automatisierung, Client Onboarding, Content Ideation, Vendor-Lock-in, Skill-Portabilität, Meta, Model Capability Initiative, Mitarbeiter-Tracking, AI Edge, Nate Herk

## Zu prüfen

- **"Nate O'Brien" vs. "Nate Hurk" im Transkript:** Uneinheitliche Schreibweise innerhalb desselben (dieses Mal aus echten YouTube-Untertiteln stammenden) Transkripts — vermutlich beides Verschreibungen von **Nate Herk**, einem real per Websuche bestätigten AI-Automatisierungs-YouTuber. Nicht mit letzter Sicherheit anhand der Frames verifizierbar (kein Kanalname im Bild lesbar).
- **Cross-Plattform-Portabilität der `.skill`-Dateien** (Nutzung auch mit GPT) wird im Video nur behauptet, nicht selbst demonstriert oder mit einer Quelle belegt — plausibel, da Skills im Kern reine Markdown-Dateien sind, aber nicht unabhängig gegengeprüft.
- **Bereits dreifache Redundanz im Repo:** Dieses Video ist nun die dritte Zusammenfassung, die im Kern dieselbe "Record a Skill"-Funktion demonstriert (siehe Cross-Referenz oben). Für einen Leser, der die beiden anderen Zusammenfassungen bereits kennt, sind vor allem die zwei oben hervorgehobenen neuen Details (Modell-Split, Backup-Empfehlung) der Mehrwert dieses Videos — der Rest ist Wiederholung.
- Die genaue Zahl/Länge der "Recorded demonstration" (in den Frames z. B. "454.6s", "159.7s") wurde nicht separat nachgerechnet oder mit der tatsächlichen Aufnahmedauer im Video abgeglichen.

## Quellen der Plausibilitätschecks

- [Search Engine Journal — Anthropic's Claude Can Now Watch A Video And Learn Your Job](https://www.searchenginejournal.com/anthropics-claude-can-now-watch-a-video-and-learn-your-job/583053/)
- [Android Authority — Forget prompts: Claude can now learn your workflow by watching your screen](https://www.androidauthority.com/claude-cowork-record-skills-feature-3689919/)
- [cybersecuritynews.com — Now You Can teach a Skill to Claude by Just Recording your Screen](https://cybersecuritynews.com/teach-skill-claude/)
- [TechSpot — Meta will record employee screens, clicks, and keystrokes to train AI that may replace them](https://www.techspot.com/news/112143-meta-record-employee-screens-clicks-keystrokes-train-ai.html)
- [Fortune — Meta will start tracking employees' screens and keystrokes to train AI tools](https://fortune.com/2026/04/21/meta-will-start-tracking-employees-screens-and-keystrokes-to-train-ai/)
- [WION — Meta CEO Mark Zuckerberg says 'smart' employees used to train AI models in viral audio](https://www.wionews.com/world/meta-zuckerberg-leaked-audio-ai-training-employee-tracking-layoffs-1779376862572)

**Hinweis zum Ablauf:** Native YouTube-Untertitel (captions) waren diesmal verfügbar und wurden vollständig genutzt (567 Segmente, keine Whisper-Fallback nötig, trotz anfänglicher HTTP-429-Warnung bei einem parallelen Subtitle-Download-Versuch im Log). Alle 80 automatisch verteilten Frames (0,077 fps über die volle Länge von 17:15) wurden gesichtet, davon 10 gezielt stichprobenartig gegen den Transkripttext geprüft.
