# "Anthropic vs. OpenAI! Wer hat die bessere KI?"

**Kanal:** Christoph Magnussen
**URL:** https://www.youtube.com/watch?v=K5KI6qfj1Do
**Länge:** 14:31
**Zusammenfassung erstellt:** 2026-09-22

---

*Siehe auch: [ki-modellvergleich-kosten.md](../ki-modellvergleich-kosten.md) (thematischer Cluster Modell-/Tarifvergleich), [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md), [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md), [fable-5-modell-sperre.md](../fable-5-modell-sperre.md), [video-summary-zQcatAdqjko.md](video-summary-zQcatAdqjko.md) (derselbe Host zum Astra-Launch), [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) (derselbe Host, KI-Marktüberblick 2026), [video-summary-889tcWGEnP0.md](video-summary-889tcWGEnP0.md) (Zero Data Retention bei Claude im Detail).*

**Hinweis zum Ablauf:** Native YouTube-Untertitel lagen nicht vor, und der automatische Whisper-Fallback in `watch.py` lieferte kein Transkript. Die Audiospur wurde daher manuell in drei Stücke à 5 Minuten geteilt und einzeln über Replicate-Whisper transkribiert (286 Segmente, zeitlich wieder zusammengesetzt). Die Qualität ist gut, es gibt typische Verhörer ("Chachepiti" = ChatGPT, "Cloud" = Claude, "Kapathi" = Karpathy, "Blackboard" = Blackboat). Alle 80 Frames wurden gesichtet (Upload: 21.09.2026). Format: Talking-Head (Magnussen in seinem Loft-Büro) mit eingeblendeten Webseiten-Screenshots samt Quellenangabe: SPIEGEL-Artikel "Claude wird immer populärer, ich hänge noch bei ChatGPT. Sollte ich wechseln?" (21.07.2026), ChatGPT- und Claude-Preisseiten, Anthropics Modellvergleichstabelle (Fable 5.1 / Opus 5 / Sonnet 5 / Haiku 4.5), OpenAIs Übersicht "Flagship models" (GPT-6 Astra, GPT-5.6 Sol/Terra/Luna), Guardian-Artikel zum Musk-vs.-Altman-Prozess, ein AI-Business-Artikel "Eleven OpenAI Employees Break Off to Establish Anthropic", OpenAIs RLHF-Methodengrafik, Anthropics "Claude's Constitution", OpenAIs Seite "Die Option Keine Datenaufbewahrung (ZDR) für Frontier-Modelle" und Anthropics Hilfeseite "Datenspeicherungspraktiken für abgedeckte Modelle". Bei ca. 4:10 ist kurz zu sehen, wie Magnussen die Videobeschreibung in Claude (Modellwahl Opus 5, Effort-Menü) schreiben lässt. Ab ca. 10:00 folgt ein als "Werbung" markierter Block für die Academy seiner eigenen Firma Blackboat.

## Produkte und Preise: an der Oberfläche fast gleich (0:00–2:58)

- **OpenAI:** ChatGPT (bekannt aus dem Privatkundenbereich), dazu **ChatGPT Work** und **Codex** als inzwischen etablierte Business-/Coding-Werkzeuge.
- **Anthropic:** Claude lange nur als Chatbot-Konkurrenz, lange ohne Spracheingabe. Dann der "Claude-Code-Moment" (Durchbruch der Coding-Agents), daraus **Claude Cowork** als Arbeitsoberfläche.
- **Preise vergleichbar:** privat ca. 20 bis 100/200 $ bzw. € pro Monat, im Business-Bereich Abrechnung per API oder pro Platz. OpenAI habe inzwischen auch Premium-Einzelplätze mit mehr Nutzung, Anthropic schon länger. Claude Code gebe es erst ab dem ca. 20-$-Tarif.
- **Profil-Unterschiede laut Magnussen:**
  - Anthropic: stark bei Sprache und Design ("Claude schreibt schöner", "agenturiger"), mit **Claude Design** jetzt Konkurrenz zu klassischen Agentur-Tools.
  - OpenAI: Produktpalette "smoother" abgestimmt, sehr gute Spracheingabe und Apps, dazu Bildgenerierung, die bei Anthropic fehlt.
  - Im Profibereich nähern sich beide stark an.

## Modelle (2:58–5:32)

- Monatelang sei Anthropic bei den Modellen klar führend gewesen. Die neue Modellfamilie **Mythos** heiße im Endkundensegment **Fable** (aktuell Fable 5.1). Mythos selbst bekomme man als Endkunde nicht.
- OpenAI habe "vor ein paar Tagen" **GPT-6 Astra** veröffentlicht, laut Magnussen momentan "das stärkste Modell überhaupt".
- Darunter bei Anthropic **Opus** (Opus 5; "Claude-Code-Moment" mit Opus 4.5 im letzten Jahr), dann **Sonnet** und **Haiku**. Bei OpenAI die GPT-5.6-Reihe **Sol, Terra, Luna** (im Ton versprochen "Sol, Opus, Terra", die Einblendung zeigt Sol/Terra/Luna).
- Beide bieten abgestufte Modellgrößen und Reasoning-/Effort-Stufen.
- **Flaggschiff-Preise praktisch identisch:** rund 10 $ pro 1 Mio. Input-Tokens und 50 $ pro 1 Mio. Output-Tokens (Fable 5.1 und Astra).
- Entscheidend sei nicht der Token-Preis, sondern "wie viel und welche Arbeit ich damit erledigt bekomme". Fable 5.1 gehe durch knifflige Aufgaben in großen Codebasen "wie Butter", auch mit großem Kontextfenster, und antworte besser (weniger informationsdicht) als Fable 5. Astra sei ein "Brett", das nun fast gleichauf liege. Codex mit den 5.6- und jetzt 6er-Modellen sei ein "Allzweck-Workhorse".

## Philosophie und Herkunft der Firmen (5:32–8:17)

- OpenAI wurde u. a. von Elon Musk mitgegründet (Einblendung: Guardian-Bericht zum Prozess Musk vs. Altman).
- Anthropic: "sieben Co-Founder", die von OpenAI weggegangen sind (die Einblendung spricht von elf OpenAI-Mitarbeitern).
- Talente wechseln zwischen den Labs, z. B. **Andrej Karpathy** zu Anthropic.
- **Training, stark vereinfacht:** OpenAI habe anfangs auf **RLHF** gesetzt (viele Menschen trainieren ein Rohmodell per Feedback nach), Anthropic von Beginn an auf **Constitutional AI** (Modell verbessert sich anhand einer "Verfassung" weitgehend selbst). Heute nutzen beide beides. Anthropic setze aber besonders darauf, dass Modelle sich selbst verbessern und andere Modelle trainieren. Das ist für Magnussen die "Wildcard", die man nicht unterschätzen sollte.
- **Compute:** OpenAI habe von Anfang an auf Rechenleistung und eigene Infrastruktur gesetzt, die Anthropic teuer einkaufen müsse. Als Randnotiz nennt er 1,25 Mrd. pro Monat an Google und 1,2 Mrd. pro Monat an SpaceX (siehe Zu prüfen, die Zahlen sind so nicht korrekt).

## Welches Tool nehmen? (8:17–10:28)

- **Magnussens persönliches Workhorse ist Codex/OpenAI** (laut seiner Nutzungsstatistik), jetzt verstärkt durch Astra. Claude und Claude Code nutze er "für bestimmte Themen".
- Empfehlung für Profis: **beide nutzen**, die eigene Nutzung beobachten und schauen, was sich besser anfühlt. Als Firma "ein Auge auf beide haben".
- **Compliance-Unterschied:** OpenAI habe "glaube ich" Zero Retention bei allen Modellen, Anthropic "meines Wissens" nicht bei allen, jedenfalls nicht bei Fable. Eingeblendet werden dazu OpenAIs ZDR-Seite ("für berechtigte API-Kunden") und Anthropics Seite zu "abgedeckten Modellen": Für Mythos-Klasse-Modelle speichert Anthropic Ein- und Ausgaben 30 Tage für Sicherheitsprüfungen, gültig ab 9. Juni 2026.
- Mit einem Max-Account für 100–200 $ komme man als Einzelnutzer weit, habe aber **nicht dieselben Datenschutzverträge** wie ein Firmenkunde.
- **Kein FOMO bei Features:** Beide Firmen rüsten sehr schnell nach (OpenAI teils mehrfach täglich). Der Anthropic-Leak im April habe gezeigt, wie viel schon in der Pipeline steckt.

## Google und Microsoft (10:28–14:31)

- **Google-Modelle:** schwächer beim Tool-Use, dafür sehr schnell, günstig und stark multimodal. Sie seien weniger "gelenkt" durch Prompts, fühlten sich also nicht wie ein "Co-Buddy" an. Claude dagegen fühle sich an "wie ein Mensch, mit dem man arbeitet" (Magnussen: "so lala").
- **Microsoft:** viel Legacy, Copilot wolle niemand "anbiedernd" als Buddy haben, "acht Wege für denselben Knopf".
- Die beiden Labs, die vorne liegen, seien Anthropic und OpenAI. **Das Geld verdienen aber momentan Google und Microsoft.**
- **Innovator's Dilemma:** Google beschäftige "gefühlt jeden zweiten Researcher" bei DeepMind, trage aber mehr Verantwortung beim Veröffentlichen und müsse seine Cloud-Infrastruktur für Kunden freihalten. Anthropic und OpenAI dagegen *müssen* das Rennen gewinnen.
- **Offene Frage:** Welche Firmen- und Team-Organisation wird der neue Standard? AI-native Startups hätten einen deutlich höheren Umsatz pro Kopf. Manches davon sei Blase, manches real. Die Margen liegen (noch) unter den 80–90 % klassischer SaaS-Firmen, weil Modelle teuer sind, doch die Effizienz steige.
- Schluss: Egal, wer gewinnt, man gewinne nur, wenn man die agentische Arbeitsweise lernt, statt KI "nur als Chatbot wie Google" zu nutzen. Dazu eine Umfrage in den Kommentaren: Team ChatGPT/Codex oder Team Claude/Claude Code?

## Einordnung

Der Titel verspricht ein Urteil, das Video liefert bewusst keines. Es ist ein Meinungs- und Orientierungsstück eines Beraters/Unternehmers, kein Test: Es gibt keine eigenen Benchmarks und keine Vergleichsaufgaben. Die Aussagen zu Modellqualität ("Astra stärkstes Modell überhaupt", "Fable geht durch wie Butter") sind persönliche Eindrücke. Der Host legt seine Präferenz (Codex) offen. Die Preis- und Produktangaben stimmen mit dem überein, was im Repo bereits dokumentiert und bestätigt ist. Schwachstellen sind die Firmengeschichte und die Compute-Zahlen: RLHF vs. Constitutional AI ist stark verkürzt, und die Monatsbeträge sind falsch zugeordnet (siehe Zu prüfen). Die Werbung für die eigene Academy ist gekennzeichnet.

## Für den technischen Team-Lead

- **Datenschutz ist der eigentlich entscheidungsrelevante Unterschied, nicht die Modellqualität.** Die beiden eingeblendeten Primärquellen sind für die Tool-Freigabe im Team direkt nutzbar: OpenAI bietet ZDR für Frontier-Modelle an, aber nur für *berechtigte API-Kunden*. Anthropic speichert bei Mythos-Klasse-Modellen (Fable) Ein- und Ausgaben 30 Tage, auch für Enterprise. Wer vertrauliche Schaltpläne, Firmware oder Kundendaten verarbeitet, muss je Modell prüfen, welche Aufbewahrungsregel gilt. Das passt zu den Detailregeln in [video-summary-889tcWGEnP0.md](video-summary-889tcWGEnP0.md) und zu [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md).
- **Private Accounts sind kein Ersatz für Firmenverträge.** Ein Mitarbeiter mit eigenem Max-Account für 200 $ hat nicht die Datenschutzverträge der Firma. Das ist ein klares Argument gegen "Schatten-KI" und für zentral beschaffte Business-Plätze.
- **Nicht jedem Feature hinterherrennen:** Beide Anbieter liefern Features binnen Wochen nach. Für die Tool-Strategie heißt das: Entscheidung nach Compliance, Integration und Kosten pro erledigter Aufgabe treffen, nicht nach der Feature-Liste der Woche.
- **Kosten pro Aufgabe statt Kosten pro Token:** Die Flaggschiffe kosten gleich viel pro Token. Der Unterschied liegt im Token-Verbrauch und in der Erfolgsquote. Für Budgetplanung lohnt ein kleiner interner Vergleich an echten Team-Aufgaben (z. B. Code-Review einer Firmware-Codebasis, Datenblatt-Auswertung).
- **Organisationsfrage:** Magnussens These vom "AI-native"-Unternehmen mit höherem Umsatz pro Kopf ist spekulativ. Für einen Gruppenleiter bleibt der Kern: Die Arbeitsweise mit agentischen Tools muss im Team aktiv gelernt werden, egal welcher Anbieter.

---

## Kernbotschaft

Christoph Magnussen vergleicht Anthropic und OpenAI und kommt zu keinem Sieger: Produkte (ChatGPT/Codex vs. Claude/Claude Code/Cowork), Tarife und Flaggschiff-Preise (Fable 5.1 und GPT-6 Astra, je ca. 10 $/50 $ pro Mio. Tokens) seien sich im Profibereich sehr ähnlich, die Leistung liege nach Astras Launch fast gleichauf. Unterschiede sieht er im Profil (Anthropic stärker bei Sprache und Design, OpenAI mit runderer Produktpalette und Bildgenerierung), in der Firmenphilosophie (Constitutional AI und Selbstverbesserung als Anthropics "Wildcard", Compute-Fokus bei OpenAI) und vor allem beim Datenschutz (ZDR-Regeln je Modell). Sein eigenes Workhorse ist Codex, er empfiehlt Profis aber, beide zu nutzen, Features nicht aus FOMO hinterherzulaufen und vor allem die agentische Arbeitsweise zu lernen. Google und Microsoft verdienen derzeit das meiste Geld, liegen bei den Modellen aber hinten (Innovator's Dilemma). Die Aussagen zu Produkten und Preisen sind plausibel und decken sich mit dem Repo. Die Compute-Zahlen und die RLHF-Geschichte sind ungenau.

## Themen-Tags

Anthropic, OpenAI, Claude, ChatGPT, Codex, ChatGPT Work, Claude Code, Claude Cowork, Claude Design, Claude Fable 5.1, Mythos, Opus 5, Sonnet 5, Haiku 4.5, GPT-6 Astra, GPT-5.6 Sol/Terra/Luna, API-Preise, Tarife, Zero Data Retention, Datenschutz, Compliance, RLHF, Constitutional AI, Compute, SpaceX Colossus, Google TPU, Andrej Karpathy, Google Gemini, Microsoft Copilot, Innovator's Dilemma, AI-native Unternehmen, Tool-Auswahl, Christoph Magnussen, Blackboat

## Zu prüfen

- **Compute-Zahlen falsch zugeordnet (per WebSearch geprüft):** Das Video nennt "1,25 Mrd. pro Monat an Google und 1,2 Mrd. pro Monat an SpaceX", die Anthropic zahle. Laut Axios (20.05.2026) zahlt Anthropic **an SpaceX ca. 1,25 Mrd. $/Monat** (Colossus 1, bis Mai 2029). **Google** zahlt seinerseits ca. 920 Mio. $/Monat **an SpaceX** (TechCrunch, 05.06.2026). Anthropics Google-Vertrag liegt bei ca. 200 Mrd. $ über fünf Jahre (Computing.co.uk), also im Schnitt deutlich mehr als 1,25 Mrd./Monat, mit Hochlauf ab 2027. Die Größenordnung stimmt, die Zuordnung im Video nicht. Die Aussage, OpenAI habe "eigene Infrastruktur", ist ebenfalls verkürzt: Auch OpenAI mietet Rechenleistung in großem Stil (Microsoft Azure, Oracle/Stargate u. a.). Das ist Vorwissen und wurde hier nicht per Web geprüft.
- **Karpathy zu Anthropic, per WebSearch bestätigt:** Wechsel ins Pre-Training-Team, angekündigt am 19.05.2026 (TechCrunch, Axios, Karpathys X-Post). Damit ist der in [video-summary-6LVB3mpPvB4.md](video-summary-6LVB3mpPvB4.md) als "nicht gegengecheckt" markierte Punkt nun belegt.
- **Anthropic-Leak "im April", per WebSearch weitgehend bestätigt:** Gemeint ist der Claude-Code-Quellcode-Leak über ein npm-Paket (ca. 512.000 Zeilen; Fortune datiert ihn auf den 31.03.2026, andere Quellen auf den 01.04.2026). Er enthüllte unveröffentlichte Features (u. a. "Kairos", Coordinator Mode) und Modell-Codenamen.
- **ZDR-Aussagen, teils bestätigt:** OpenAI hat am 19.08.2026 ZDR für Frontier-Modelle (wieder) eingeführt, aber **nur für berechtigte API-Kunden** (OpenAI-Blog, Computerworld). "Zero Retention bei allen Modellen" ist also zu pauschal. Für Anthropic zeigt die im Video eingeblendete Hilfeseite 30 Tage Speicherung bei Mythos-Klasse-Modellen ab 9. Juni 2026. Die Seite wurde nur als Frame gesichtet, nicht selbst aufgerufen. Das passt zum Launchdatum von Fable 5 in [fable-5-modell-sperre.md](../fable-5-modell-sperre.md) und ergänzt [video-summary-889tcWGEnP0.md](video-summary-889tcWGEnP0.md) (ZDR bei Claude nur per Antrag, nur API/Enterprise). Dort ist die Mythos-Ausnahme noch nicht erwähnt.
- **RLHF vs. Constitutional AI (Vorwissen, nicht per Web geprüft):** Die Darstellung "RLHF ist bei Anthropic erst mittlerweile dazugekommen" ist eher umgekehrt: Anthropic hat schon 2022 RLHF-Arbeiten veröffentlicht ("Helpful and Harmless") und Constitutional AI (Dez. 2022) darauf aufgebaut (RL from AI Feedback). Die Grundrichtung (Anthropic setzt stärker auf KI-Feedback und eine Verfassung) stimmt.
- **"Sieben Co-Founder" vs. Einblendung "Eleven OpenAI Employees":** Kein echter Widerspruch. Anthropic hat sieben Mitgründer, die ursprüngliche Abspaltung von OpenAI umfasste mehr Personen (Vorwissen).
- **"Astra ist das stärkste Modell überhaupt"** ist eine persönliche Einschätzung. [video-summary-aTaKM8FSy2k.md](video-summary-aTaKM8FSy2k.md) berichtet, dass Astra im Artificial Analysis Index zunächst hinter Fable 5.1 lag und erst nach Korrekturen auf einen geteilten ersten Platz kam. Das ist ein gradueller Unterschied, kein harter Widerspruch.
- **Spannung zu früherer Aussage desselben Hosts:** In [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) empfiehlt Magnussen, *ein* Harness-Tool (Claude Code **oder** Codex) in voller Tiefe zu lernen, "nicht beide oberflächlich". Hier rät er Profis, beide zu nutzen. Das ist vereinbar (Tiefe in einem, Beobachtung des anderen), sollte in [ki-modellvergleich-kosten.md](../ki-modellvergleich-kosten.md) aber nicht als Widerspruch missverstanden werden. Die Präferenz für Codex ist in beiden Videos gleich.
- **Cross-Check mit bestehenden Notizen:** Preise (10 $/50 $) und das Astra-Rollout decken sich mit [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md) und [video-summary-zQcatAdqjko.md](video-summary-zQcatAdqjko.md). Die SpaceX-Compute-Beziehung ist auch in [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) bestätigt (dort ohne Monatsbeträge). Die Google-Einordnung (multimodal, weniger "Personality") deckt sich mit zNuynCOm5Mc. Claude Design ist in [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) noch als "nicht gegengecheckt" geführt; hier wird es nur erwähnt, nicht gezeigt. Thematisch passt das Video am besten in [ki-modellvergleich-kosten.md](../ki-modellvergleich-kosten.md).
- **Nicht geprüft:** Die Tarifdetails (Claude Code erst ab ca. 20 $, OpenAI-Premium-Einzelplätze), das Fehlen von Bildgenerierung bei Claude und die Aussage, SaaS-Margen lägen bei 80–90 %.
