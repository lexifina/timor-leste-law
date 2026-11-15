# Timor-Leste: law history in git

The law of Timor-Leste as a git history: one file per article, one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Timor-Leste's national law, which global-law reads at `timor-leste/national/acts/`.

**What is in it now:** the Constitution (Constituição da República Democrática de Timor-Leste, 170 articles), in force from 20 May 2002 and never amended; and Lei n.º 11/2009, de 7 de outubro (Divisão Administrativa do Território) in five versions: as enacted, in force from 8 October 2009, and as republished by Lei n.º 4/2016 (from 26 May 2016), Lei n.º 14/2021 (from 1 January 2022), Lei n.º 19/2023 (from 6 December 2023) and Lei n.º 14/2023 (from 1 January 2024), now with 32 articles. Each act's folder has a `README.md` listing its versions; [`data/versions.json`](data/versions.json) lists every version with its source PDF and its sha256, and [`SOURCES.md`](SOURCES.md) every gazette issue read.

Each act is a folder, one file per article plus `preambulo.md` and `estrutura.md` (the chapter headings and the order of the files): `lei-11-2009/artigo-007.md` is Article 7 (Município de Baucau) of Lei n.º 11/2009, inserted articles are `artigo-004-A.md`, and the Constitution is in [`constituicao/`](constituicao/).

The text is in Portuguese, as the Jornal da República prints it; Tetum, also an official language, is not here. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 7 of Lei n.º 11/2009 (Município de Baucau) | `git log -p --word-diff -- lei-11-2009/artigo-007.md` |
| Which act wrote each paragraph of Article 7? | `git blame lei-11-2009/artigo-007.md` |
| Every version of Article 7, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- lei-11-2009/artigo-007.md` |
| Article 7 as in force on 31 December 2023 | `python tools/em_vigor.py 2023-12-31 lei-11-2009 7` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Timorese law](https://global-law.lexifina.com/v1/try_claude?country=timor-leste)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=timor-leste)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=liberdade+de+express%C3%A3o&jurisdictions=timor-leste)**: a search of Timorese law for "liberdade de expressão" (freedom of expression), returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Portuguese or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add timor-leste/national/acts
python3 tools/law.py show 2026-01-01 timor-leste/national/acts/lei-11-2009/artigo-007.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Dili (UTC+9), on the day the version took effect, and carries it in its `In-force:` trailer, with the law's `Approved:`, `Promulgated:` and `Published:` days:

- the day each law's own words give: the Constitution's Article 170 (20 May 2002), and for Lei n.º 11/2009 and its amending laws the day after publication in the Jornal da República, except Lei n.º 14/2023, which says 1 January 2024;
- Lei n.º 14/2021 entered into force on 8 July 2021 but "produz efeitos a partir do dia 1 de janeiro de 2022": its commit is dated 1 January 2022 and carries `Entered-into-force: 2021-07-08`;
- the republication by Lei n.º 19/2023 already prints the changes Lei n.º 14/2023 makes to Articles 7 and 13; they are held back to 1 January 2024 (`Held-back:` trailers). Ask for a date with `tools/em_vigor.py`, not `git log --before`, which uses your local time zone.

Each change is credited to the law that made it, including changes printed only in its republished annex. Ten articles whose new words both 2023 republications print, though neither law's operative articles name them, are in one labelled commit credited to the Jornal da República, with both laws as `Candidate:`. The committer is always Lexifina.

## How it is checked

- The builder's `check_repo.py` compares every file at every commit with the text read from the official PDF: 7 versions, 405 file checks, 0 mismatches; each full version's words were also found, in order, in a second, independent reading of the PDF (5 of 5). The results are in [`REPRODUCE.md`](REPRODUCE.md).
- The texts are read from the PDFs' own text layers (no OCR); each law's dates are read from its own words and checked against a table, and any difference stops the build.
- Two more builds from the cache gave identical hashes, and `test_repo.py` checks on a clone that blame names the amending laws and the dated tool gives the right text across amendments (11 of 11 passed).
- History is append-only: no merge commits, no rewriting, and every commit's trailers parse.

## What it does not show

- **Any other act.** Only the Constitution and Lei n.º 11/2009 are here; the Jornal da República's other laws and decrees, including the Government diplomas that set the areas of the postos administrativos, are not.
- **The Constitution as printed in a gazette issue.** The text here is the Portuguese PDF the Ministry of Justice serves with the Jornal; the Tetum text, also official, is not here.
- **Changes after 28 October 2026**, when the sources were last read; the last change here took effect on 1 January 2024.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Jornal da República](https://www.mj.gov.tl/jornal/) (Ministério da Justiça) | Official gazette, born-digital PDFs | yes, each amending law republishes Lei n.º 11/2009 in full | Lei n.º 11/2009 and its four amending laws, Série I |
| [Constituição da RDTL](https://www.mj.gov.tl/jornal/public/docs/ConstituicaoRDTL_Portugues.pdf), served with the Jornal | Official text, PDF | no, never amended | The Portuguese text of 2002 |

## Licence

See [`LICENSE`](LICENSE). No terms of use or licence were found on the Jornal da República's site, and none is granted here for the legal texts; when quoting, cite the Jornal da República issue (its series, number and date are in each commit's `Published:` and `Source:` trailers). The tools and documentation are MIT.

No AI wrote or edited legal text, and no model runs at build time; the research, the builder and the checks were written by Claude Code with Claude Opus 5.5, and commit messages are generated by code from the gazette text (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
