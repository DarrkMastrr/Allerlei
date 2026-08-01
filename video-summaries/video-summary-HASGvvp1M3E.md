# "LOOPS statt PROMPTS? SO arbeiten deine Agents richtig!"

**Kanal:** Christoph Magnussen
**URL:** https://www.youtube.com/watch?v=HASGvvp1M3E
**Länge:** 11:36
**Zusammenfassung erstellt:** 2026-07-04

---

## Loops statt Prompts – worum geht's?
- Boris Cherny, Erfinder von Claude Code, sagt, er schreibe gar keine Prompts mehr, sondern nur noch "Loops"
- Ein Loop ist konzeptionell aus der Entwicklerwelt bekannt (`while`-Loop), kombiniert mit einem LLM wird daraus eine sich selbst prüfende, autonome Wiederholschleife
- Unterschied zum Prompt: Ein Prompt ist ein Hin-und-Her, ein Loop läuft komplett autonom, bis eine Bedingung erfüllt ist
- Codex und Claude Code arbeiten dabei mit Sub-Agents: ein Haupt-Agent mit einem Goal beauftragt weitere Sub-Agents, die zurückmelden

## Wo findet man das in der Praxis?
- Direkt per `/goal`-Befehl starten
- Dauerhaft/wiederkehrend: bei Codex unter "Automations", bei Claude Code unter "Schedule" (früher "Routines")
- Beispiel: eine Automation, die läuft, bis der Kalender für den nächsten Monat aufgeräumt ist
- Laut Roman (Head of Codex) kann ein Agent mit GPT-5.5 an einem ambitionierten Ziel tage- bis mehrtagelang autonom weiterarbeiten, bevor er "fertig" zurückmeldet

## Gute Goals formulieren
- Ein Goal sollte kurz, konkret und messbar sein
- Gutes Beispiel: eine Liste offener Pull Requests/Bugs abarbeiten lassen
- Schlechtes Beispiel: zu vage Ziele wie "hilf mir, mein Leben in den Griff zu kriegen"
- Eigener Test des Autors: "Baue mir meine Website neu" — nach 20 Stunden gab es eine fertige, aber nicht die gewünschte Website. Lehre: große Ziele in kleinere Teilziele zerlegen
- Tipp: den Agent selbst fragen, welche sinnvollen Goals für den eigenen Arbeitsbereich infrage kommen

## Was menschlich bleibt
- Judgment, Taste und Richtung bleiben zentrale menschliche Aufgaben
- Zwei Varianten: klare, durchcheckbare Kriterien vorgeben, oder die Bewertung einem LLM als "Judge" überlassen

## Ausblick
- OpenAI habe ein Feature "Record and Replay" für Codex vorgestellt: Codex beobachtet manuelle Arbeitsschritte und lernt daraus, wie sich diese als Loop automatisieren lassen
- Matthew Berman habe eine eigene Website mit seinen genutzten Loops veröffentlicht

## Kosten
- Autonome Agenten-Loops sind "Token-Burner" — Kosten hängen vom Tokenverbrauch ab; Wortspiel des Autors: "learn to burn"

---

## Kernbotschaft
Agentische Coding-Tools verschieben sich von einzelnen Prompts hin zu autonomen "Loops"/Goals, bei denen Agenten-Netzwerke selbstständig über längere Zeit an einem Ziel arbeiten. Der Mensch bleibt für Zieldefinition, Bewertungsmaßstäbe und die Zerlegung großer Vorhaben in überprüfbare Teilziele verantwortlich.

## Themen-Tags
Agentic Coding, Claude Code, Codex, Automatisierung/Loops, Prompting, KI-Agenten

## Zu prüfen
- Aussage, Boris Cherny schreibe keine Prompts mehr, nur noch Loops
- OpenAI-Feature "Record and Replay" für Codex
- Aussage von Roman (Head of Codex) zu tage-/mehrtagelanger autonomer Arbeit mit GPT-5.5
- Claude Codes Funktion "Schedule" hieß vorher "Routines"
- Matthew Bermans öffentliche Loop-Liste-Website

**Hinweis:** Whisper-Transkription lief über Replicate-Fallback (nativer Untertitel-Abruf scheiterte mit HTTP 429), beim zweiten Versuch erfolgreich. Ein kurzer Abschnitt (~08:56–09:26) war akustisch unklar und teils fehlerhaft transkribiert.
