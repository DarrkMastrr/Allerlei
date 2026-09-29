# "Opus 5.5 und GPT-6 Sol getestet"

**Kanal:** AI mit Arnie
**URL:** https://www.youtube.com/watch?v=9EOqBiMR3z4
**Länge:** 15:37
**Zusammenfassung erstellt:** 2026-09-29

*Hinweis zum Ablauf: Native YouTube-Untertitel (maschinell ins Englische übersetzte Auto-Captions eines deutschen Videos, 402 Segmente) liefen über yt-dlp, kein Whisper-Fallback. Die Captions verstümmeln Modellnamen stark ("Kloto/Tropic" = Claude/Anthropic, "Soll" = Sol, "Loon" = Luna, "Mimoell" = MiMo, "Astra" teils als "Opus"); Zuordnungen wurden mit Frames (Anthropic-/OpenAI-Blogseiten, Artificial-Analysis-Diagramme) abgeglichen. 80 Frames bei 15 Minuten = grobe Abdeckung; Roboter-Demo nur in Stichproben sichtbar.*

---

## Aufhänger

Der Host (Arnie) gibt in einem bewusst kurzen Video vor seinem Spanien-Urlaub einen Überblick über die neueste Modell-Welle: **Claude Opus 5.5**, **GPT-6 Sol** und **GPT-6 Luna**, **Grok 4.7** sowie das chinesische **MiMo**. Neben Herstellerangaben zeigt er einen eigenen Praxistest (Roboter-Simulation) und Daten von Artificial Analysis. Sein persönliches Fazit: Opus 5.5 ist aktuell das beste getestete Modell, aber OpenAI-Nutzer müssen nicht wechseln.

## Claude Opus 5.5 (laut Anthropic-Blogpost)

- Erstes Modell nach Anthropics Artikel, in dem das Unternehmen zu einer Verlangsamung des KI-Fortschritts aufrief; laut Host bescheinigen externe Tests (u. a. METR, in das Anthropic investiert hat – Host weist ironisch darauf hin) Unbedenklichkeit.
- Ein Tester habe damit **680.000 Codezeilen in unter einem Tag migriert** (Aufgabe, die früher ein Team wochenlang beschäftigt hätte). Nur als Herstellerzitat, nicht belegt.
- Sicherheitsbremse bei Biologie- und Cyberfragen, da das Modell ähnlich stark wie Mythos sei.
- **Preise (im Frame lesbar):** Input 4 $ / Output 20 $ pro 1 Mio. Token (Opus 5: 5 $ / 25 $), Cache Reads 0,20 $ (vorher 0,50 $), Cache Writes 5 $. Anthropic: netto ca. **40 % geringere Kosten**, ca. 30 % schneller als Opus 5, Fast-Mode in Claude Code mit bis 2,5-facher Geschwindigkeit (8 $ / 40 $).
- Überarbeitet für angenehmere Gesprächsführung (Kritikpunkt an Opus 5; Opus 4.6 war wegen "Persönlichkeit" beliebt).
- Benchmarks laut Anthropic-Auswahl: Terminal-Bench 4.0 besser als GPT-6 Astra, teils bei deutlich geringeren Kosten; GDPval (wirtschaftlich relevante Wissensarbeit) deutlich verbessert.

## GPT-6 Sol und Luna (laut OpenAI)

- Neben Astra gibt es nun nur noch **Sol** und **Luna** als die weiterlaufenden Modelle (kein "Terra" mehr), die die gesamte Intelligenz-Kosten-Kurve abdecken sollen.
- API-Preise von Sol und Luna **halbiert** gegenüber GPT-5.6 (Input und Output).
- Computer Use: Astra bleibt das beste Modell. Laut OpenAI-Diagramm (Frame) erreicht Sol (High) auf OSWorld 2.0 offline 60,5 % gegenüber 60,3 % für Opus 5 (Medium) bei ca. 80 % niedrigeren Kosten; Luna (Max) übertrifft angeblich Sol 5.6 (Medium) bei einem Zehntel der Kosten.

## Praxistest: Roboter-Simulation (~04:10–09:40)

Der Host lässt Modelle einen Hexapod-/Rettungsroboter-Simulator ("ARES-6") mit Höhen-/Body-Roll-Steuerung, Autonomiemodus, Greifarm-Demo und Drohne mit Kamera-Feed bauen. Ergebnisse:

- **Vorgänger (GPT-5.6):** Höhe und Drehung schwach, Autonomiemodus tut nichts.
- **GPT-6 Sol:** deutlich besser (Höhe, Rotation, Body Roll), Autonomiemodus weiterhin ohne Bewegung, Kamera-Feed friert Drohne ein; schneller und billiger als 5.6.
- **GPT-6 Astra:** läuft "auf ganz anderem Niveau": Bewegung, Kollisionen, Drohne, Kamera-Feed.
- **Opus 5.5 (laut Host "Opus 5"):** klar bestes Ergebnis: sehr detailliert, Staubwolken, überzeugende Physik, Greifdemo, Drohne mit Survivor-Scan und Autonomiemodus. Aber: Laufzeit **ca. 5 Stunden**, gelegentlich verklemmte Beine mit Fehlermeldungen. Der Host betont, der Test prüfe 3D-Verständnis und Physik; es handle sich um seinen ersten Kurztest.

## Grok 4.7 und MiMo

- **Grok 4.7:** günstig und relativ schnell, nach Aussage von Elon Musk ähnlich Opus 5, aber nicht auf Niveau von Fable/Astra/Opus. Host hat erst zwei Prompts getestet.
- **MiMo (China):** erst kürzlich aufgefallen, in Artificial-Analysis-Kosten/Leistung-Diagramm attraktiv; nicht selbst getestet, Host fragt nach Erfahrungen.

## Artificial Analysis (~10:35–14:15)

- Intelligence Index: **Opus 5.5 vorn (58 Punkte)**, gefolgt von Fable 5.1 und GPT-6 Astra (etwa gleichauf). Artificial Analysis hat neue Benchmarks eingeführt (u. a. Terminal-Bench 4.0), nachdem veraltete Tests kritisiert wurden.
- **Kosten pro Aufgabe:** Opus 5.5 ist auf dem "Cost to run"-Index *nicht* 40 % günstiger als Opus 5, sondern etwa gleich teuer, weil es viele Token verbrauche (Host bestätigt: dauert lange, verbraucht viel). GPT-Modelle waren in seinem Robotertest deutlich schneller.
- Sol: kleine Verbesserung ggü. 5.6 bei halben Kosten; Luna ähnlich. Sol/Luna waren im AA-Live-Diagramm noch nicht gelistet, Host zeigt Screenshot; Luna liegt extrem weit links (günstig).

## Praxistipps des Hosts

- Kein Zwang zum Wechsel: Astra sei ein "geniales Modell"; Opus 5.5 vielleicht "ein paar Prozent" besser.
- **Thinking Effort:** Opus 5.5 auf *Medium* wirkt stark und kostengünstig; auf *Max* verbrennt man Token schnell. Niedrige Stufen nicht unterschätzen.
- Für sehr günstige, ausreichend gute Modelle: Luna oder MiMo testen. Nutzung in agentischen Harnesses (Claude Code, Codex).

## Für Hardware-Entwickler und Team-Lead

- **Kostensteuerung im Team:** Listenpreis ≠ Aufgabenkosten. Opus 5.5 hat 20 % niedrigere Token-Preise, aber laut Artificial Analysis kaum niedrigere Kosten pro Aufgabe (Token-Verbrauch). Vor Modellwechsel eigene Referenzaufgabe messen (Kosten, Laufzeit).
- **Effort-Stufe als Stellschraube:** Medium als Standard, Max nur gezielt – direkt in Team-Richtlinien übernehmbar (vgl. [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md)).
- **Cache-Reads 0,20 $:** Lange, wiederverwendete Kontexte (z. B. Datenblatt-/Spezifikations-Prompts, CLAUDE.md) werden billiger.
- **Simulations-/Physiktest als Bewertungsidee:** Ein Roboter-Simulator als Modelltest ist für Hardware-Leute anschaulich, aber ein einzelner, nicht reproduzierbarer Web-App-Test; Ausdauer (5 h Laufzeit) und Fehler (verklemmte Beine) sind Warnzeichen für Physik-nahe Aufgaben. Kein Beleg für Tauglichkeit bei echter Schaltungs-/Hardwareauslegung.
- Team schreibt keine Software: Relevanz eher für Skripting, Auswertung und Dokumentation; der Modellstreit Claude vs. GPT ist für diesen Einsatz zweitrangig.

---

## Kernbotschaft
Opus 5.5 gilt zum Zeitpunkt des Videos in Benchmarks und im Kurztest des Hosts als bestes Modell, aber der Vorsprung ist klein, die tatsächlichen Kosten pro Aufgabe sinken kaum (hohe Token-Nutzung), und OpenAIs günstige Sol/Luna-Modelle sind bei Preis-Leistung interessant. Empfehlung: bei bestehender Zufriedenheit nicht wechseln, Opus 5.5 auf Medium testen, Luna/MiMo für Billigaufgaben prüfen.

## Themen-Tags
Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, GPT-6 Astra, Grok 4.7, MiMo, Artificial Analysis, Intelligence Index, Terminal-Bench 4.0, OSWorld 2.0, Thinking Effort, Token-Effizienz, Cache-Preise, Roboter-Simulation, Modellvergleich

## Zu prüfen
- **Per WebSearch bestätigt:** Opus 5.5 Release 22.09.2026, Preise 4 $ / 20 $, Cache Reads 0,20 $, Cache Writes 5 $, Fast-Mode 8 $ / 40 $, "ca. 40 % billiger bei typischen Workloads" (Anthropic-Seite, Claude-Docs, mehrere Blogs). Video-Angabe stimmt.
- **Nicht geprüft:** 680.000-Zeilen-Migration (Herstellerzitat), "30 % schneller", OSWorld-2.0-Zahlen von Sol/Luna, Artificial-Analysis-Werte (58 Punkte, Kostenindex), MiMo, Grok-4.7-Aussagen, METR-Investitionsbehauptung. Roboter-Ergebnisse sind ein einziger subjektiver Kurztest des Hosts. Nicht unabhängig verifiziert wurde zudem, ob die Captions-Übersetzung Details (z. B. "5 Stunden") korrekt wiedergibt.
- **Widerspruch/Spannung im Video selbst:** Anthropic wirbt mit 40 % geringeren Kosten, Artificial Analysis zeigt laut Host ähnliche Kosten pro Aufgabe; beides kann stimmen (Token-Preis vs. Verbrauch), Auflösung offen.
- **Querverweise (nicht editiert):** [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md) nennt Astra mit 10 $ / 50 $ pro 1 Mio. Token und Sol 5.6 als Vorgänger; dort fehlen GPT-6 Sol/Luna sowie Opus 5.5 noch. Dort dokumentierte OSWorld-2.0-Werte (Astra 72,6 %) passen zur Aussage "Astra beste Computer-Use-Wahl". [ki-modellvergleich-kosten.md](../ki-modellvergleich-kosten.md) und [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) (Opus 5 mit Medium-Effort teils besser) stützen den Effort-Tipp; Opus 5.5 selbst ist im Repo bisher nicht behandelt. Grok 4.7 auch in [video-summary-aTaKM8FSy2k.md](video-summary-aTaKM8FSy2k.md) (angekündigt für ca. 11./12. September).

## Nachtrag Faktencheck (2026-09-29)

Unabhängiger Faktencheck (Recherche-Agents plus skeptische Prüf-Agents, Primärquellen per WebFetch). Der bisherige Text oben bleibt unverändert; Abweichungen und Bestätigungen stehen hier. Konfidenz jeweils in Klammern.

- **Opus 5.5 (hoch):** Release 22.09.2026, 4 $/20 $, Cache Read 0,20 $. Anthropic: "40 % less to run than Opus 5" bei typischen Workloads und Standardeinstellungen. Artificial Analysis (Max-Effort): pro Aufgabe gleichauf mit Opus 5, weil ca. 119k statt 73k Output-Tokens anfallen. Die genauen Dollarwerte 5,98 $ vs. 5,86 $ konnte der Prüfer nicht bestätigen; belegt ist "gleichauf".
- **GPT-6 Sol/Luna (mittel):** Nur Sekundärquellen (OpenAI-Seite lieferte 403): Sol 2 $/10 $, Luna 0,10 $/0,50 $; Release 22.09.
- **Terminal-Bench 4.0 (mittel):** Anthropic nennt für Opus 5.5 66,4 % (laut zwei Prüfern bei xhigh, laut einem bei max; nicht abschließend geklärt) gegen GPT-6 Astra 57,9 % (high); Vals AI (Stand 29.09.2026): Opus 5.5 65,15 %, Astra 59,60 %. Nicht effort-gleich; Quelle und Datum immer mitnennen.
- **Nicht geprüft:** 680.000-Zeilen-Migration, MiMo, Roboter-Simulator-Test (subjektiver Einzelfall).
