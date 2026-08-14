# "So lässt du Claude jedes Video für dich anschauen"

**Kanal:** Julian Ivanov | KI-Automatisierung
**URL:** https://www.youtube.com/watch?v=R403PGBArDY
**Länge:** 13:50
**Zusammenfassung erstellt:** 2026-08-08

---

*Meta-Hinweis: Dieses Video ist ein Tutorial/Showcase genau zu dem `/watch`-Skill (bradautomates/claude-video), den dieses Repo selbst unter `claude-skills/watch/` und `C:\Users\Admin\.claude\skills\watch\` einsetzt, um diese Video-Zusammenfassungen zu erstellen. Diese Zusammenfassung wurde also mit exakt dem Werkzeug erstellt, das im Video erklärt wird.*

## Kernidee

Claude kann von Haus aus kein Video "sehen" — nur einen Titel raten oder ein Transkript zusammenfassen, das laut Julian oft 90 % dessen verpasst, was visuell passiert (Diagramme, Textinserts, UI-Zustände). Der `/watch`-Skill schließt diese Lücke: Er lädt ein Video herunter, zieht Frame für Frame als Bilder sowie ein zeitgestempeltes Transkript, und Claude liest beides parallel — es "sieht und hört" das Video wirklich, nicht nur eine Textzusammenfassung davon.

## Demo 1: Langes Lernvideo als Obsidian-Notiz mit eingebetteten Abbildungen

Julian zeigt am Beispiel eines 3Blue1Brown-Erklärvideos zu Transformern (27 Min.), wie er einfach den Link kopiert, in Claude `/watch <Link>` eingibt und den Zusatzauftrag gibt: *"Fasse dieses Video zusammen und füge unter die wichtigsten Punkte direkt die passenden Abbildungen aus dem Video ein. Speichere das als Notiz in Obsidian."*

- Claude liest zunächst die Skill-Anleitung, lädt Video/Frames/Transkript, sichtet alle ~80 Frames in Batches, um die relevanten visuellen Stellen zu identifizieren
- Erkennt anhand des Transkripts, wo vermutlich etwas gezeigt wird, prüft den Frame, spult bei Bedarf vor/zurück, bis die passende Abbildung gefunden ist
- Kopiert die relevanten Frames in den Obsidian-Vault-Anhangsordner (im Video: 23 Abbildungen) und baut eine strukturierte Notiz mit Metadaten (Quelle, Datum, Länge, Ein-Satz-Zusammenfassung, dann Kapitel mit Text **und** eingebetteten Screenshots direkt an der passenden Stelle)
- Gesamtdauer laut Julian: ca. 5 Minuten für ein 27-minütiges Video; bei 2-3-stündigen Vorlesungen entsprechend länger, aber immer noch praktikabel

## Drei Haupt-Anwendungsfälle (im Video als Diagramm gezeigt)

1. **Stumme Videos** (z. B. Urlaubsaufnahmen ohne Sprache) — Transkript hilft nicht, aber Claude erkennt anhand der Frames, was passiert, und kann Fragen wie "ab welcher Stelle sind wir am Strand?" beantworten. Skaliert auch über mehrere Videos gleichzeitig (10-15 Clips durchsuchen lassen statt manuell).
2. **Bug-Aufnahmen** — statt 20 Screenshots plus Beschreibung einfach eine Bildschirmaufnahme geben; Claude sieht die komplette Oberfläche inkl. Optionen/Reiter/Fehlermeldung im Kontext, ähnlich wie ein menschlicher Tech-Supporter, der sich ein kurzes Video anschaut.
3. **Virale Videos analysieren** — Demo mit einem Ali-Abdaal-Short ("Rating self-help books"), der deutlich besser performt als seine anderen Shorts. Julian lässt Claude per `/watch` herausfinden, welche visuellen Hooks das Video nutzt. Claude identifiziert u. a.: animierten Titeltext im ersten Frame, sofort erkennbares Buchcover (Atomic Habits) als Wiedererkennungshook, große Wertungszahl in Sekunde 4, konsistentes 3-Schicht-Layout, hohe Schnittfrequenz (~10 Sekunden pro Buch) und leitet daraus konkrete Content-Empfehlungen ab. Julian bestätigt live im Video, dass Claudes Analyse mit dem übereinstimmt, was er selbst im Video sieht — als Beleg, dass reines Transkript-Lesen das nicht geleistet hätte.

## Installation (im Video gezeigt)

- GitHub-Repo `bradautomates/claude-video` (Open Source, MIT-Lizenz)
- In Claude Code: Link zum Repo einfügen und Claude bitten, "dieses Plugin und alles was dazugehört" zu installieren — Claude erkennt selbst die Marketplace-Installation
- Alternativ zeigt das im Frame sichtbare README explizit: `/plugin marketplace add bradautomates/claude-video` gefolgt von `/plugin install watch@claude-video`
- Setup-Skript prüft/installiert `yt-dlp`/`ffmpeg` automatisch und fragt danach nach einem Whisper-API-Key (nur nötig für Videos ohne native Untertitel)
- Empfehlung: **Groq** statt OpenAI — laut Julian der schnellste Transkriptionsservice, sehr günstig bis kostenlos im Free-Tier (im Frame sichtbar: Groq-Pricing-Seite zeigt Whisper V3 Large $0.111/h, Whisper Large v3 Turbo $0.04/h)

## Technische Pipeline (im Video als Diagramm erklärt)

Drei Tools im Hintergrund, alle Open Source/kostenfrei nutzbar:
1. **yt-dlp** lädt das Video (YouTube, 100+ Seiten, oder lokale Datei)
2. **ffmpeg** schneidet Frames heraus — max. ~100 Frames, gleichmäßig verteilt (bei langen Videos ~1 Bild alle 10-18 Sekunden je nach Länge), Tipp im Video: nur einen Abschnitt ansehen lassen für feinere Details und geringere Kosten
3. **Tonspur → Transkript** — native Untertitel wenn vorhanden (gratis), sonst Whisper via Groq (ein paar Cent)

Ergebnis: Claude bekommt Frames + Transkript gleichzeitig und "sieht und hört" das Video.

## Themen-Tags
Claude Skills, watch-Skill, claude-video, Video-Analyse, Obsidian/Second Brain, yt-dlp, ffmpeg, Whisper, Groq, Content-Analyse, Bug-Reporting, Produktivität

## Zu prüfen (falls zutreffend)
- Die im Video gezeigte Chat-Oberfläche (dunkles Theme, Seitenleiste mit "Sitzungen", ein Dashboard "Was steht als Nächstes an, Julian?" mit Sitzungen/Nachrichten/Token gesamt/Streak/bevorzugtes Modell, Tool-Chips "Lokal"/"second-brain") konnte anhand der Frames nicht sicher identifiziert werden — sieht nicht wie Standard-Claude-Desktop oder Claude-Code-CLI aus, sondern nach einem angepassten/Drittanbieter-Frontend oder Obsidian-Plugin mit MCP-Anbindung. Nicht unabhängig verifiziert.
- Sponsor-Zahlen zu Brevo ("über 600.000 Unternehmen nutzen Brevo") sind Werbeaussage im Video, nicht unabhängig gegengecheckt.
- Groq-Preise (Whisper V3 Large $0.111/h, Turbo $0.04/h) sind ein Screenshot-Stand aus dem Video, keine eigene Live-Prüfung der aktuellen Preisseite.
- Exakte Versionsnummer im gezeigten GitHub-Repo-Screenshot ("Release v0.1x") war auf dem 512px-Frame nicht zweifelsfrei lesbar.

## Hinweise für den Watch-Skill-Workflow dieses Repos (relevant für den täglichen Einsatz)

- **Neue, hier noch nicht genutzte Idee:** Der Prompt-Zusatz *"füge unter die wichtigsten Punkte direkt die passenden Abbildungen aus dem Video ein"* lässt Claude die relevanten Frames tatsächlich in die Notiz kopieren und einbetten. Die Zusammenfassungen in diesem Repo sind bisher rein textbasiert (keine eingebetteten Screenshots) — für Videos mit hohem visuellem Anteil (Diagramme, Benchmark-Folien wie in qZRftXozT3M) könnte das einen echten Mehrwert bringen, sofern gewünscht.
- **Kein neues Flag/keine neue Fähigkeit entdeckt:** Alles im Video gezeigte (Frame-Obergrenze ~100, Fokus-Modus für Abschnitte, Groq-Präferenz, Setup-Ablauf) deckt sich mit dem, was `C:\Users\Admin\.claude\skills\watch\SKILL.md` bereits dokumentiert. Auch die Plugin-Marketplace-Installation (`/plugin install watch@claude-video`) ist im Repo bereits in `claude-skills/watch/README.md` dokumentiert — keine Aktualisierung nötig.
- **Zu beachten:** Diese Maschine nutzt laut `whisper-replicate-rate-limit.md` eine lokal gepatchte Version des Skills mit Replicate-Whisper-Fallback statt des im Video gezeigten Groq-Standardpfads. Ein Update über `/plugin update watch@claude-video` würde diesen lokalen Patch vermutlich überschreiben — vor einem Update also den Replicate-Patch sichern bzw. bewusst gegen Groq/OpenAI tauschen.
