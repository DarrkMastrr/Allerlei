# Lokale KI: Auslagerung von Rechercheschritten (Kontext für Claude Code)

## Hinweise für Claude Code
- Sprache: Deutsch. Direkt, technisch präzise, keine unnötigen Ausführungen.
- Andreas braucht für jeden Umsetzungsschritt eine Schritt-für-Schritt-Anleitung.
- Er hat noch nie einen MCP-Server aufgesetzt und bisher nur ein Modell in Ollama eingerichtet und wenig genutzt.
- Befehle bitte so geben, dass sie unter Windows (PowerShell) laufen.
- Nichts als gesichert behaupten, was nicht getestet wurde. Modellempfehlungen vor der Verwendung gegen die aktuelle Ollama-Bibliothek prüfen.

## Ziel
Tokens in der Cloud sparen. Das Cloud-Modell (Claude) soll nie Rohmaterial sehen (Transkripte, Webseiten, Frames), sondern nur strukturierte, lokal erzeugte Destillate. Recherche-Vorarbeit und Verdichtung laufen lokal, Urteil und Planung bleiben in der Cloud.

## Hardware (der Rechner, auf dem gearbeitet wird)
- CPU: Intel Core Ultra 9 285K, 24 Kerne
- RAM: 64 GB (Windows zeigt 63)
- GPU: NVIDIA GeForce RTX 4070 (Name in nvidia-smi abgeschnitten), 16 GB VRAM, 285 W Limit, Treiber 617.42, CUDA 13.4
- Im Leerlauf belegen Desktop, Firefox, Claude-App usw. rund 1,9 GB VRAM, nutzbar sind also etwa 14 GB.
- Ollama 0.40.2, vorhandenes Modell: `qwen3:14b` (9,3 GB)
- NPU im Prozessor (ca. 13 TOPS): wird nie genutzt, für dieses Vorhaben irrelevant. Ollama, llama.cpp und die übliche Whisper-Variante laufen über GPU/CPU.
- Über Nacht laufende Stapelverarbeitung ist möglich, Geschwindigkeit ist bei Nachtläufen also zweitrangig.

## Bestehende Pipeline (Projekt "Allerlei", Watch-Skill)
1. YouTube-Video herunterladen
2. In Chunks zerlegen
3. Audio an Whisper zum Transkribieren
4. Bilder aus dem Video samplen
5. Informationen aus Transkript und Bildern gewinnen
6. Prüfer untersuchen die Informationen auf Plausibilität gegen Quellen im WWW
7. Recherche-Agent läuft erneut, um gefundene Fehler zu korrigieren
8. Orchestrator macht bis zu 3 Korrekturschleifen
9. PDFs mit dem korrigierten Content werden erzeugt (eigener Skill)

Die lokale KI kann auf das WWW zugreifen und recherchieren.

## Aufteilung: was lokal, was in der Cloud

### Lokal (hoher Spareffekt, geringes Risiko)
- Download, Chunking: reine Skriptarbeit
- Whisper (faster-whisper oder whisper.cpp): braucht kein LLM, läuft lokal sehr gut
- Frame-Sampling per ffmpeg, ggf. mit Szenenwechsel-Erkennung statt festem Intervall, um Duplikate zu sparen
- Bildbeschreibung und OCR der Frames mit lokalem Vision-Modell (z. B. Qwen-VL, Gemma 3, Llama 3.2 Vision, 7B bis 12B). Hier ist der Token-Hebel am größten, weil Bilder in der Cloud viele Tokens kosten.
- Transkript-Bereinigung und Verdichtung pro Chunk (Füllwörter raus, Zusammenfassung)
- Extraktion der überprüfbaren Einzelbehauptungen als Liste

### Lokal mit Vorbehalt
- Claim-Extraktion: Was hier fehlt, wird nie geprüft. Stichprobenartig gegenprüfen, ggf. größeres Modell (ca. 30B) nehmen.
- Quellensuche und Abruf: Seiten suchen, laden und relevante Passagen herausziehen kann lokal laufen. Die Bewertung, ob eine Quelle die Behauptung stützt, bleibt in der Cloud.

### Cloud (nicht auslagern)
- Plausibilitätsprüfung selbst (Urteil Behauptung gegen Quelle). Das ist die Qualitätsschranke der Pipeline. Kleine Modelle neigen dazu, Behauptungen durchzuwinken oder Quellen falsch zu lesen.
- Orchestrator-Entscheidungen (Fehler real? Korrektur ausreichend? Schleife beenden?)
- Endredaktion des Contents für die PDFs

## Architekturprinzip
Die Cloud bekommt nur Destillate, zum Beispiel pro Chunk ein JSON mit `claims[]`, `zeitstempel`, `bildtext`, plus lokal vorgefilterte Quellenauszüge. Für Korrekturschleifen recherchiert die lokale KI Quellen zu genau der als fehlerhaft markierten Behauptung und liefert Auszüge, die Cloud entscheidet, ob die Korrektur passt.

## Technischer Weg
Empfohlen: **MCP-Server vor dem lokalen Ollama** mit zwei bis drei eng geschnittenen Tools, z. B.:
- `seite_holen_und_verdichten(url, frage)`
- `dokument_zusammenfassen(text)`
- `transkript_extrahieren(video)` bzw. `claims_extrahieren(chunk)`

Alternativen (weniger kontrolliert): Claude Code per `ANTHROPIC_BASE_URL` auf einen Anthropic-kompatiblen lokalen Endpoint (Ollama oder LiteLLM) umleiten und als Subprozess starten (`claude -p`); Router-Proxy (claude-code-router, LiteLLM); Hooks und Skripte für Vorverarbeitung.

Grenzen lokaler Modelle: Tool-Calling und lange Agent-Schleifen sind deutlich schwächer. Gut geeignet: Zusammenfassen, Extrahieren, Klassifizieren, Vorfiltern. Fehler der lokalen Stufe wandern ungeprüft nach oben, deshalb nur Aufgaben auslagern, deren Ergebnis stichprobenartig verifizierbar ist.

## Modellplanung (16 GB VRAM, 64 GB RAM)
- `qwen3:14b` (9,3 GB) passt mit 8k bis 16k Kontext in die GPU. Ollamas Standardkontext ist klein und muss für lange Chunks per `num_ctx` hochgesetzt werden.
- Vision-Modell 7B bis 12B (ca. 6 bis 9 GB) und Whisper (large-v3, ca. 3 bis 5 GB) laufen nacheinander, nicht parallel zum LLM. Ollama entlädt Modelle über `keep_alive`.
- MoE-Modelle der 30B-Klasse (z. B. Qwen3-30B-A3B, ca. 19 GB quantisiert) laufen mit Auslagerung ins RAM noch brauchbar. Qualitätssprung gegenüber 14B für die Claim-Extraktion möglich.
- Dichte Modelle ab ca. 30B laufen mit Auslagerung langsam (RAM-Bandbreite), für Nachtläufe okay.
- Offen: Ob es in der Ollama-Bibliothek inzwischen bessere Modelle als `qwen3:14b` gibt, vor der Auswahl prüfen.

## Plan
1. **Test mit echtem Chunk** (siehe unten): `qwen3:14b`, Claim-Extraktion, Qualität und Dauer beurteilen.
2. Falls Qualität nicht reicht: MoE-30B oder dichtes 30B-32B für Nachtläufe testen, denselben Chunk nochmal laufen lassen.
3. Vision-Stufe für Frames testen (Modell wählen, Frames einer Beispiel-Folie beschreiben lassen).
4. Whisper lokal einbinden, falls noch nicht geschehen.
5. Erst danach MCP-Server bauen, wenn klar ist, welche Modelle dahinterhängen. Schritt-für-Schritt-Anleitung nötig.
6. Pipeline-Skill so umbauen, dass die Cloud-Stufen nur noch die Destillate sehen.

## Testskript (Schritt 1)
Echten Transkript-Chunk (ca. 5 bis 10 Minuten Sprechzeit) als `chunk.txt` (UTF-8) in den Ordner legen, von dem aus PowerShell gestartet wird:

```powershell
$chunk = Get-Content .\chunk.txt -Raw -Encoding UTF8
$prompt = @"
Extrahiere aus dem folgenden Transkript-Abschnitt alle überprüfbaren Tatsachenbehauptungen (Zahlen, Namen, Daten, technische Aussagen). Meinungen und Füllwörter ignorieren. Antworte nur als JSON in dieser Form: {"claims":[{"claim":"...","zitat":"wörtliche Stelle aus dem Text"}]}

TRANSKRIPT:
$chunk
"@
$body = @{
  model   = "qwen3:14b"
  prompt  = $prompt
  stream  = $false
  think   = $false
  format  = "json"
  options = @{ num_ctx = 16384; temperature = 0 }
} | ConvertTo-Json -Depth 5
$r = Invoke-RestMethod -Uri http://localhost:11434/api/generate -Method Post -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -ContentType "application/json; charset=utf-8"
$r.response
"Dauer (s): " + [math]::Round($r.total_duration/1e9,1)
```

Danach prüfen, ob alles auf der GPU lief:

```powershell
ollama ps
```

In der Spalte `PROCESSOR` sollte `100% GPU` stehen. Ein CPU/GPU-Mix bedeutet, dass der Kontext zu groß fürs VRAM war.

Auswerten: JSON-Ausgabe, Dauer, `ollama ps` und den Chunk vergleichen. Fehlen relevante Behauptungen oder wurden welche erfunden? Danach entscheiden, ob 14B reicht.

## Offene Punkte
- Pfad des Allerlei-Projekts und Struktur des Watch-Skills (für die Umbauplanung nötig)
- Welche Whisper-Variante aktuell lokal läuft, falls überhaupt
- Ergebnis des Tests mit `qwen3:14b`
