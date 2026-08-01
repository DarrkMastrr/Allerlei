# "KI & Datenschutz für Unternehmen: Der komplette DSGVO- & AI-Act-Guide (2026)"

**Kanal:** Chris Marvin Atsu
**URL:** https://www.youtube.com/watch?v=889tcWGEnP0
**Länge:** 34:18
**Zusammenfassung erstellt:** 2026-07-04, überarbeitet 2026-08-01 (echtes Transkript nachgereicht, siehe Hinweis am Ende)

---

## Das eine Bild, das alles erklärt

Kernmetapher des Videos: Ein KI/Cloud-Tool ist wie ein externer Mitarbeiter, der nicht im eigenen Büro sitzt. Bei einem Menschen würde man sich automatisch fragen: Was darf er sehen? Was darf er speichern? Darf er es weitergeben? Was passiert damit, wenn er geht? Genau diese Fragen — nur für Software — sind der rote Faden des ganzen Videos.

## Wann wird es rechtlich kritisch

- "Personenbezogene Daten" ist weiter gefasst als Name/Adresse — auch E-Mail, Telefonnummer, Kundennummer, Stimme, Foto, Standort, Gesprächstranskripte oder CRM-Notizen zählen dazu
- Demo im Video: "Schreib mir 5 Ideen für einen Newsletter über Immobilien" (unkritisch) vs. "Hier ist die Mail von Familie Müller mit Adresse und Telefonnummer, fass das zusammen" (überschreitet die Schwelle)
- **Wichtigster Irrtum, den das Video ausräumt:** Ein US-Tool ist nicht automatisch verboten. Entscheidend ist nicht das Herkunftsland allein, sondern: welche Daten gehen wohin, an wen, mit welchem Vertrag, wie lange, mit welchen Schutzmaßnahmen. Bei den meisten großen Anbietern gibt es einen sauberen und einen unsauberen Weg — selten ein klares "geht nicht"
- Drei Regelwerke merken: **DSGVO** (Schutz personenbezogener Daten), **AI Act** (fragt nicht *ob* KI genutzt wird, sondern *wofür* und wie stark das echte Menschen beeinflussen kann), **Vertragsebene** (AVV, Unterauftragnehmer, Zugriff, Logging, Speicherdauer)

## Account-Typ: der häufigste Fehler

Private und geschäftliche Accounts haben unterschiedliche Regeln — Demo am Beispiel Claude, Prinzip gilt laut Video ähnlich bei ChatGPT/Gemini:
- **Privat:** Standard-Aufbewahrung 30 Tage; wenn "Hilf uns, unsere KI-Modelle zu verbessern" aktiviert ist, dürfen Daten bis zu 5 Jahre gespeichert und zum Training verwendet werden — abschalten dauert 10 Sekunden (Einstellungen → Datenschutz)
- **Geschäftlich/Team:** ebenfalls 30 Tage Standard; "Nutzer-Feedback an Anthropic senden" (enthält vollständigen Prompt + Antwort) separat in den Organisationseinstellungen abschaltbar

## Die Vertragsebene: AVV/DPA

- Ohne Auftragsverarbeitungsvertrag (AVV, engl. DPA) fehlt die Rechtsgrundlage, dass ein Anbieter Daten überhaupt verarbeiten darf (DSGVO Art. 28 Abs. 3)
- Bei großen Anbietern ist der AVV im Geschäftstarif meist automatisch enthalten (bei Anthropic Teil der Commercial Terms, auffindbar über die Privacy-Seite von Anthropic) — man muss ihn nur einmal finden, speichern und ablagefähig machen
- **Datentransfer EU→USA:** zwei gängige Grundlagen — Data Privacy Framework (DPF, gilt nur wenn der konkrete Anbieter gelistet ist) und Standardvertragsklauseln (SCCs). Wichtige Einschränkung aus dem Video: das DPF ist vor dem höchsten EU-Gericht anfechtbar und sollte nicht als für immer feststehende Regel behandelt werden — es bleibt nutzbar, aber nicht als dauerhaft sicherer Selbstläufer

## Daten in der EU halten

- **Azure-Praxisbeispiel:** Bei der Ressourcen-Erstellung explizit die Region "Germany West Central" wählen — das ist der Unterschied zwischen "wir hoffen, dass es passt" und "wir können vertraglich und konfigurativ zeigen, dass es passt"
- **Zero Data Retention (ZDR) bei Claude — mit wichtigen Einschränkungen, die im Video sehr konkret gezeigt werden:**
  - Kein Schalter, sondern ein Antrag, der vorher gestellt werden muss (Organisationseinstellungen → Datenschutz → Support kontaktieren → Formular)
  - Gilt **nur** für Nutzung über die Claude API unter einer Commercial Organization oder Claude Enterprise
  - Claude Free/Pro/Max werden dafür zu 100 % abgelehnt; auch Claude Teams/Enterprise ohne API-Nutzung sind ausgeschlossen
  - Einzige gezeigte Ausnahme: Claude Code zählt auch unter Enterprise
  - Auch mit ZDR dürfen Anbieter Daten ausnahmsweise länger behalten (Regelverstoß, gesetzliche Pflicht) — ZDR ersetzt nicht das Prinzip "so wenig Daten wie möglich"
- **Azure-Äquivalent "Modified Abuse Monitoring":** speichert Eingaben standardmäßig bis zu 30 Tage zur Missbrauchserkennung, im Ausnahmefall mit menschlicher Prüfung. Beides (automatisiert + menschlich) lässt sich vorab per Antrag bei Microsoft abschalten — **muss vor** dem Einspielen echter Kundendaten passieren, nicht danach

## Organisatorische Pflichten

- Subprozessoren (die Dienstleister der eigenen Dienstleister) grob kennen
- Interne KI-Policy mit klaren Antworten: welche Tools sind erlaubt, welche Daten dürfen rein und welche nie, wer prüft neue Anwendungsfälle
- **AI Literacy:** seit Februar 2025 Pflicht — bedeutet nicht, dass alle Informatik studieren müssen, sondern dass wer mit KI arbeitet Halluzinationen erkennen, keine sensiblen Daten blind einkopieren, Ergebnisse prüfen und wissen muss, wann ein Mensch statt der Maschine entscheiden muss. Laut Video derzeit Ziel einer Gesetzesvereinfachung, aber noch nicht abgeschwächt — gilt also bis auf Weiteres unverändert

## Der EU AI Act

- **Rollen:** Provider (baut/vertreibt ein KI-System unter eigenem Namen) vs. Deployer (nutzt es beruflich) — die meisten normalen Unternehmen sind Deployer, nicht Provider
- **Risikoklassen:** verboten (z. B. Social Scoring, manipulative Systeme), Hochrisiko (z. B. Bewerbungen, Kreditwürdigkeit, kritische Infrastruktur), Transparenzpflicht (Chatbots/Deepfakes müssen als KI erkennbar sein), minimales Risiko (normale Schreib-/Brainstorming-Tools)
- **Fristen:** Gesetz seit August 2024 in Kraft, Verbote + Literacy-Pflicht seit Februar 2025. Laut Video hat sich die EU im Mai 2026 darauf geeinigt, die strengen Hochrisiko-Regeln auf Dezember 2027 zu verschieben (in manchen Fällen August 2028)
- **Bußgelder:** bei verbotenen Praktiken bis 35 Mio. € oder 7 % des weltweiten Jahresumsatzes; bei anderen Verstößen bis 15 Mio. € oder 3 %; mit Staffelungen für kleinere Unternehmen
- **DSFA (Datenschutz-Folgenabschätzung):** Risikoanalyse vor "heiklen" KI-Einsätzen — nicht nötig für Brainstorming/anonyme Texte, aber z. B. bei Bewerber-Bewertung, Mitarbeiterüberwachung, Scoring/Profiling, automatisierten Entscheidungen, großen Kundendatenmengen, Gesundheits-/Finanzdaten oder einem Chatbot mit Zugriff auf echte Kundendaten. Faustregel: je näher an echten Menschen und echten Konsequenzen, desto eher nötig

## Zwei DACH-Spezifika, die laut Video oft übersehen werden

1. **Betriebsrat:** Wenn ein System Verhalten oder Leistung von Mitarbeitenden messbar machen kann, hat der Betriebsrat oft ein eigenes Mitbestimmungsrecht — unabhängig von der DSGVO. In der Praxis laut Video oft der eigentliche Showstopper, an den vorher niemand denkt
2. **Berufsgeheimnisträger** (Ärzte, Anwälte, Steuerberater, Psychotherapeuten): Hier reicht die normale Datenschutz-/AI-Act-Prüfung nicht — Mandanten-/Patientendaten in einem Cloud-/KI-Tool berühren zusätzlich die strafbewehrte Schweigepflicht, Dienstleister müssen besonders sauber vertraglich zur Geheimhaltung verpflichtet werden

## Praxisfall: Chatbot/RAG-System auf echten Firmendaten

Sobald ein Chatbot an CRM, E-Mails, Kundendatenbank oder interne Dokumente angebunden wird, ist er kein "Chatbot mit ein paar Dokumenten" mehr, sondern Infrastruktur, die echte Kundendaten verarbeitet. Dann greift alles zusammen: saubere Datenquellen, Berechtigungskonzept, Löschkonzept, klare Regeln für Halluzinationsfälle, eine saubere Vertragskette und je nach Datenlage eine DSFA.

## 10-Schritte-Startplan

1. Liste aller tatsächlich genutzten KI-Tools erstellen (auch die "heimlichen")
2. Private Accounts für alles mit echten Daten stoppen
3. Auf Geschäftsversionen wechseln (Business/Team/Enterprise/API)
4. Für jedes Tool den AVV besorgen und die Transfergrundlage dokumentieren
5. Training/Speicherung prüfen und entsprechend einstellen
6. Einfache interne KI-Regel schreiben, Team kurz schulen
7. Anwendungsfälle nach Risiko sortieren
8. Für heikle Fälle eine DSFA prüfen
9. So wenig echte Kundendaten wie möglich verwenden, minimieren/anonymisieren
10. Eine verantwortliche Person benennen, die das Thema wirklich besitzt

---

## Kernbotschaft
KI-Tools im Unternehmen einzusetzen ist rechtlich möglich, aber nicht automatisch compliant — es braucht bewusste Entscheidungen zu Account-Typ, Vertrag (AVV), Datenstandort/-transfer, Speicherfristen sowie in Deutschland zusätzlich Betriebsrats-Mitbestimmung und ggf. Berufsgeheimnis. Compliance bedeutet nachweisbar zu wissen, was mit den eigenen Daten passiert — das macht laut Video nicht langsamer, sondern professioneller, und wird zunehmend zur Voraussetzung für größere Kunden.

## Themen-Tags
KI & Datenschutz, DSGVO, EU AI Act, Cloud-Compliance, Claude/Anthropic, Azure, Zero Data Retention, Betriebsrat, Berufsgeheimnis, Unternehmensrecht

## Zu prüfen (falls zutreffend)
- Speicherfristen bei Claude: 30 Tage Standard / bis zu 5 Jahre bei aktiviertem Modell-Training (privat) — gegen aktuelle Anthropic-Datenschutzdokumentation abgleichen
- Genaue ZDR-Zugangsvoraussetzungen (nur Commercial Organization/Enterprise + API, Claude Code als Ausnahme) — Stand zum Aufnahmezeitpunkt, kann sich ändern
- "AI Literacy seit Februar 2025 Pflicht" sowie die im Video erwähnte laufende Abschwächung durch eine Gesetzesvereinfachung — Gesetzesstand direkt prüfen, da in Bewegung
- Verschiebung der Hochrisiko-Fristen auf Dezember 2027/August 2028 durch EU-Einigung im Mai 2026 — gegen offizielle EU-Quellen verifizieren
- Konkrete Bußgeldrahmen (35 Mio. €/7 % bzw. 15 Mio. €/3 %) — gegen AI-Act-Text prüfen
- Alle Rechtsaussagen sind wie im Video selbst betont **keine Rechtsberatung**

**Hinweis zum Ablauf:** Beim ersten Watch-Versuch scheiterten sowohl native YouTube-Untertitel (HTTP 429) als auch der Replicate-Whisper-Fallback am festen 6-Minuten-Timeout des Skripts (siehe [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md)) — auch nach Aufladen des Replicate-Guthabens, da das diesmal kein Kontostand-, sondern ein reines Verarbeitungszeit-Problem bei diesem 34-minütigen Video war. Lösung: Video lokal in 6 Häppchen à ca. 5:43 Min. zerlegt und jeweils einzeln transkribiert (469 Segmente gesamt) — dieser Ansatz ist jetzt in [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md) als Workaround für lange Videos dokumentiert. Die obige Zusammenfassung basiert auf diesem vollständigen Transkript statt nur auf Frames.
