# "Opus 5 ist anstrengend. So behebst du es!"

**Kanal:** Alex Sprogis
**URL:** https://www.youtube.com/watch?v=VKMNP_5vOmM
**Länge:** 06:15
**Zusammenfassung erstellt:** 2026-08-14

---

*Siehe auch: [karpathy-claude-md-guidelines.md](../karpathy-claude-md-guidelines.md) — "Over-Engineering" ist dort als Code-Fehlermuster dokumentiert (aus einer einfachen Funktion wird eine überkomplizierte Abstraktion). Dieses Video zeigt eine verwandte, aber eigene Ausprägung desselben Grundmusters: Claude "over-engineert" nicht Code, sondern Text/Anweisungen — sowohl in normalen Antworten als auch, ironischerweise, beim Befolgen der eigenen Output-Style-Konfiguration (siehe unten).*

## Das Problem: Claude Opus 5 antwortet unnötig kompliziert

Der Host beschreibt ein bekanntes Ärgernis: Claude Opus 5 antwortet oft mit langen, verschachtelten Textwänden voller Fachjargon, bei denen man selbst einzelne Wörter nachschlagen muss. Als Beleg zeigt er einen (echten, siehe Plausibilitätscheck) viralen Blogpost eines Kölner Entwicklers mit dem Titel "Don't be a meat proxy" (gruhn.me, 03.08.2026), der KI-Output als "absolute Extraarbeit" beschreibt — "umständlich formuliert, enthält oft nur plausiblen Unsinn und ist vollgestopft mit Fachjargon". Im Frame ist ein Beispielsatz zu sehen: *"NATS control-plane events: stream leader election / R3 quorum re-form during pod churn"* — als Beispiel für kaum verständlichen KI-Output.

## Die Lösung: eigene Output-Styles definieren

Als Lösung stellt der Host **Output-Styles** in Claude Code vor — eine Konfiguration, die nicht festlegt, *was* Claude inhaltlich tut, sondern *wie* es antwortet (Tonfall, Satzlänge, Struktur). Standardmäßig bringt Claude Code laut gezeigtem `/config`-Menü vier Styles mit: **Default**, **Proactive**, **Explanatory** und **Learning** (Learning pausiert zwischendurch und lässt den Nutzer aktiv mitcoden — praktisch zum Lernen). Zwischen ihnen kann jederzeit gewechselt werden, zusätzlich lassen sich eigene Styles anlegen.

## Praxis-Demo 1: Der "Explain Me Like I'm 5"-Style von Lydia Hallie

Der Host greift einen konkreten, von **Lydia Hallie** (laut Frame Mitarbeiterin im Claude-Code-Team bei Anthropic) auf X geteilten Custom-Style auf: `ELI5.md` mit u. a. den Anweisungen "It's been a long day and my brain is fried, talk to me like I'm 5", kurze Sätze/Wörter/Absätze, bei Entscheidungen maximal zwei Optionen, exakte Pfade/Befehle. Der Host lässt Claude Code per Prompt einen neuen Output-Style mit diesem Inhalt anlegen — und bemerkt dabei einen ironischen Treffer ins eigene Kernthema: Claude übernimmt die Vorgabe nicht eins zu eins, sondern "dichtet noch einiges mit dazu" (Over-Engineering, diesmal beim Befolgen der Anweisung selbst statt bei der eigentlichen Konfigurationsdatei). Er korrigiert die Datei danach manuell.

Nach Neustart von Claude Code ist der neue Style unter `/config → Output Style` sichtbar. Mit `/rewind` dreht der Host eine vorherige Konversation eine Nachricht zurück und schickt denselben Prompt erneut ab — diesmal mit aktivem ELI5-Style. Ergebnis laut Video: deutlich kürzere Sätze, weniger Text insgesamt, mehr Absätze, übersichtlicher.

## Praxis-Demo 2: Mehrere Output-Varianten per Branch vergleichen

Zweiter Tipp: Eine Konversation lässt sich mit **Branch** aufspalten, um denselben Sachverhalt in mehreren Stilen parallel generieren zu lassen, ohne die ursprüngliche Konversation zu beeinflussen. Am Beispiel eines Stripe-Webhook-/Gutschein-Betrugsszenarios (E-Commerce-Projekt in VS Code, Themen: `checkout.session.completed`, `invoice.paid`, 100-%-Rabattcode-Missbrauch) zeigt der Host drei parallel erzeugte Varianten:
1. Ein einfacher, bildhafter Erklärstil für einen Brief an technisch unversierte Kunden/Testleser
2. Eine technische Variante für Entwickler mit deutlich mehr Detailtiefe
3. Eine "Entscheidungsvorlage" — eine kompakte Zusammenfassung für Entscheider

## Output-Style als Projektstandard festlegen

Abschließend zeigt der Host, dass sich ein Output-Style nicht nur pro Konversation/Nachricht, sondern auch projektweit als Standard setzen lässt: im `.claude`-Ordner des Projekts, Datei `settings.local.json`, über den Eintrag für den Standard-Output-Style. Claude hatte dort im Beispiel bereits automatisch den zuvor angelegten ELI5-Style eingetragen; dieser Wert lässt sich frei überschreiben.

## Eigenwerbung am Ende

Der letzte Videoabschnitt bewirbt den "AI Engineering Accelerator" des Hosts (Launch laut Einblendung am 17.08.2026, Warteliste mit Launch-Rabatt, 12 Module, 80+ Video-Lektionen, eigenes Framework, geschlossene Community) — inhaltlich nicht Teil des Output-Style-Themas, hier bewusst als Werbeblock markiert.

---

## Einordnung für Organisation/Team

Für einen Gruppenleiter/technischen Lead ist besonders der letzte Praxis-Teil relevant: Output-Styles lassen sich **projektweit** in `.claude/settings.local.json` festlegen — d. h. ein Team könnte pro Projekt einen einheitlichen Antwortstil erzwingen (z. B. knapp und handlungsorientiert für erfahrene Entwickler, "Explanatory"/"Learning" für Onboarding neuer Teammitglieder). Die Demo mit den drei parallelen Branch-Varianten (technischer Deep-Dive für Entwickler vs. kompakte Entscheidungsvorlage für Management) zeigt zudem ein direkt übertragbares Muster: dieselbe Analyse einmal durchführen lassen und für unterschiedliche Zielgruppen (Team vs. Führungsebene) in passender Form ausgeben lassen, statt manuell zwei Versionen zu schreiben.

## Kernbotschaft
Claude Opus 5 antwortet häufig unnötig verschachtelt und jargonlastig — Abhilfe schafft laut Video nicht ein anderes Modell, sondern selbst definierte **Output-Styles** in Claude Code, die festlegen, *wie* (nicht *was*) Claude antwortet. Neben den vier mitgelieferten Styles (Default, Proactive, Explanatory, Learning) lässt sich ein eigener Style anlegen (Beispiel: Lydia Hallies "Explain Me Like I'm 5"), per `/rewind` an bestehenden Konversationen testen, per `Branch` in mehreren Varianten parallel vergleichen (z. B. technisch vs. Entscheidungsvorlage) und schließlich projektweit in `.claude/settings.local.json` als Standard festlegen. Bemerkenswert: Selbst beim Erstellen der Style-Konfiguration zeigt Claude dasselbe Over-Engineering-Verhalten, gegen das der Style eigentlich helfen soll.

## Themen-Tags
Claude Code, Output Styles, Claude Opus 5, Lydia Hallie, Anthropic, Context Engineering, Prompt-Design, Over-Engineering, Rewind, Branch, Explain Me Like I'm 5, settings.local.json

## Zu prüfen
- **Lydia Hallie als Anthropic-Mitarbeiterin und Urheberin des ELI5-Styles:** per WebSearch bestätigt — ihr X-Post "btw Claude Code lets you configure your own output style! ... this is the one I like to use after a long day lol" (x.com/lydiahallie/status/2080378470111256907) sowie weitere Posts von ihr zu Claude-Code-Features (u. a. Learning-Mode-Empfehlung) sind auffindbar; sie wird an anderer Stelle als Teil des Claude-Code-Teams bei Anthropic beschrieben. Im Whisper-Transkript wird ihr Name durchgehend falsch als "Lydia Helly" verschriftet — in dieser Zusammenfassung anhand der Frames (X-Profil mit Namen sichtbar) korrigiert.
- **Der "Don't be a meat proxy"-Blogpost:** per WebSearch bestätigt real (gruhn.me/blog/2026-08-03/, Autor laut Suchergebnissen Niklas Gruhn), erreichte laut Suchergebnissen hohe Popularität auf Hacker News (über 1.000 Punkte). Ob der Autor tatsächlich aus Köln stammt (Aussage des Hosts), wurde nicht einzeln verifiziert.
- **Output-Styles als reales Claude-Code-Feature** (inkl. Default/Explanatory/Learning-Styles, `/output-style:new`, projektweite Konfiguration): per WebSearch anhand offizieller Anthropic-Dokumentation (code.claude.com/docs/en/output-styles) bestätigt.
- **`/rewind` und `Branch`** als Claude-Code-Funktionen wurden im Video live demonstriert, aber nicht zusätzlich unabhängig gegengecheckt.
- Keine inhaltlichen Widersprüche zu bestehenden Repo-Notizen gefunden. Thematische Nähe besteht zum bereits dokumentierten "Over-Engineering"-Fehlermuster in [karpathy-claude-md-guidelines.md](../karpathy-claude-md-guidelines.md) (dort: Code wird unnötig komplex) — dieses Video zeigt dieselbe Tendenz bei Text-/Konfigurationsausgaben, was die bestehende Beobachtung ergänzt statt ihr zu widersprechen.
- Die Werbe-Zahlen zum "AI Engineering Accelerator" (Launch-Datum, Modulzahl, Preis) sind reine Selbstauskunft des Hosts und wurden nicht verifiziert.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; die Zusammenfassung basiert auf dem Whisper-Fallback (Replicate, in 2 Chunks, 87 Segmente) plus allen 80 extrahierten Frames.
