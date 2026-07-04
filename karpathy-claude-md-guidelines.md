# Die Karpathy-CLAUDE.md-Guidelines (Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution)

Quellen: [video-summary-x-Jqu_WlEI4.md](video-summary-x-Jqu_WlEI4.md) ("This Free File Makes Claude Code 10x Cleaner"), [video-summary-5DuHZrtmwoY.md](video-summary-5DuHZrtmwoY.md) ("Karpathys CLAUDE.md macht Claude Code 10x cleverer")

Zwei unabhängige Kanäle haben im selben Zeitraum Videos über dasselbe Repo gemacht — mit widersprüchlichen Angaben zu Autor und Sternezahl. Deshalb hier als eigenes Thema mit Fact-Check statt in zwei getrennten Einzel-Summaries.

## Die Kernidee (in beiden Videos gleich)

Ausgangspunkt ist ein viraler X-Thread von Andrej Karpathy über typische Fehlermuster von Coding-Agents:
- **Silent Assumptions** — der Agent trifft stillschweigend eine von mehreren möglichen Interpretationen und fragt nicht nach
- **Over-Engineering** — aus einer einfachen Funktion wird eine überkomplizierte Abstraktion
- **Scope Creep** — ein Bugfix wird von unnötigem Refactoring benachbarter Funktionen begleitet
- **Fehlende Verifikation** — der Agent meldet "fertig", ohne Edge Cases getestet zu haben

Daraus wurde eine ca. 50-zeilige `CLAUDE.md`-Datei mit vier Prinzipien destilliert:
1. **Think Before Coding** — Annahmen benennen, bei Unklarheit nachfragen statt raten
2. **Simplicity First** — nur so viel Code wie nötig
3. **Surgical Changes** — nur anfassen, was wirklich geändert werden muss
4. **Goal-Driven Execution** — Aufgaben in verifizierbare, überprüfbare Ziele umwandeln

Installation: `/plugin marketplace add forrestchang/andrej-karpathy-skills` gefolgt von `/plugin install andrej-karpathy-skills@karpathy-skills` (Claude Code Plugin), alternativ `CLAUDE.md` direkt per curl ins Projekt laden.

## Praxis-Belege aus beiden Videos

- **x-Jqu_WlEI4:** Demo an einem E-Commerce-Dashboard — mit aktivierten Guidelines fragt der Agent zuerst nach Scope (echte API vs. Hardcoded-Daten, responsive ja/nein), baut dann exakt das Angeforderte ohne ungefragte Zusatzfeatures.
- **5DuHZrtmwoY:** A/B-Test an einem Habit-Tracker mit zwei parallelen Claude-Code-Instanzen (identischer Prompt). Mit Guidelines: ~7,5 Min., ~0,70 $, sauberes Ergebnis. Ohne Guidelines: ~17 Min., ~1,42 $, unsauberer (Layout-Fehler, inkonsistente Logik, unerwünschte Extras).

## Fact-Check: Repo-Identität und Sternezahl (2026-07-04)

Beide Videos machen je eine falsche Angabe:

| | Video x-Jqu_WlEI4 | Video 5DuHZrtmwoY | Realität |
|---|---|---|---|
| Owner/Ersteller | forrestchang | "Herobrine19"/"ferrettechang" | **Forrest Chang** (27.01.2026 erstellt) |
| Repo-Pfad | `forrestchang/andrej-karpathy-skills` | `multica-ai/andrej-karpathy-skills` | Beide Pfade zeigen aufs selbe Repo — **`multica-ai/andrej-karpathy-skills`** ist die kanonische GitHub-URL, `forrestchang/...` ein Alias/Fork-Pfad |
| Sternezahl | "über 26.000" | "über 165.000" | **~165.000–187.000** (Stand Anfang Juli 2026) — Video 1 nennt einen veralteten Wert von vor Monaten |
| Install-Befehl | `forrestchang/andrej-karpathy-skills` | `ferrettechang/andrej-karpathy-skills` | **`forrestchang/andrej-karpathy-skills`** ist korrekt — "ferrettechang" existiert nicht, vermutlich Verhörer/Fehltranskription von "forrestchang" |

**Fazit:** Video x-Jqu_WlEI4 hat Owner-Name und Install-Befehl richtig, aber eine veraltete Sternezahl. Video 5DuHZrtmwoY hat die aktuellere Sternezahl, aber einen falschen Install-Befehl und unklare Autor-Zuschreibung. Für die eigene Installation gilt: `/plugin marketplace add forrestchang/andrej-karpathy-skills`.

Quellen: [GitHub: multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills), [ClaudePluginHub](https://www.claudepluginhub.com/plugins/forrestchang-andrej-karpathy-skills), [Medium/Joe Njenga](https://medium.com/@joe.njenga/i-tried-andrej-karpathy-claude-md-file-that-got-157k-github-stars-6f079f400ad9)

## Einordnung
Diese vier Prinzipien decken sich stark mit dem bereits bestehenden [ai-agent-workflow.md](ai-agent-workflow.md) (destilliert aus Peter Steinbergers Build-Talk) — insbesondere "Closing the Loop" (dort Punkt 1) entspricht "Goal-Driven Execution" hier, und beide Quellen betonen, Claude vor dem Loslegen erst Annahmen/Scope klären zu lassen. Wer bereits nach `ai-agent-workflow.md` arbeitet, bekommt mit dieser CLAUDE.md eine fertige, copy-paste-fähige Umsetzung der gleichen Grundidee.
