# Timor-Leste: law history

The law of Timor-Leste (TL) as a git history: one file per provision, one commit per law on the day it took effect,
with the law that made each change as the commit author. It follows the shared design of
[lexifina/global-law](https://github.com/lexifina/global-law), which places it at `tl/`.

Source: the official gazette, the **Jornal da República**, published by the Ministry of Justice at
<https://www.mj.gov.tl/jornal/>. Language: Portuguese (an official language with Tetum).

## What is in it

| Folder | Act | Versions |
|---|---|---|
| `constituicao/` | Constituição da República Democrática de Timor-Leste (2002) | one: never amended; in force 2002-05-20 |
| `lei-11-2009/` | Lei n.º 11/2009, de 7 de outubro, Divisão Administrativa do Território | the original (2009) and four amending laws: Lei 4/2016, Lei 14/2021, Lei 19/2023, Lei 14/2023 |

Each amending law of Lei n.º 11/2009 republished the whole law in an annex "da qual faz parte integrante", so every
version here is an official full text, not a reconstruction. Two dated quirks are kept visible:

- **Lei n.º 14/2021** entered into force on 2021-07-08 but "produz efeitos a partir do dia 1 de janeiro de 2022"; its
  commit is dated 2022-01-01 and carries `Entered-into-force: 2021-07-08`.
- **Lei n.º 14/2023** (published May 2023) takes effect only on 2024-01-01, after **Lei n.º 19/2023** (in force
  2023-12-06). The 19/2023 republication already prints the 14/2023 changes to Arts. 7 and 13; they are held back
  until 2024-01-01 (`Held-back:` trailers). Words that only the republications change, and that both laws' annexes
  print, are in a labelled commit authored by the Jornal da República with two `Candidate:` trailers.

Files: `<act>/artigo-NNN.md` (one paragraph per line block), `<act>/preambulo.md`, and `<act>/estrutura.md`, which
holds the chapter headings and the order of the files. `data/versions.json` lists every version with its source PDF
and sha256.

## Questions and commands

| Question | Command |
|---|---|
| Every change, oldest first | `git log --reverse --format="%ad %an: %s" --date=short` |
| Article 5 of Lei 11/2009 on 1 January 2020 | `python tools/em_vigor.py 2020-01-01 lei-11-2009 5` |
| Article 5 of Lei 11/2009 today | `python tools/em_vigor.py 2026-10-28 lei-11-2009 5` |
| Article 7 on 31 December 2023 and on 1 January 2024 | `python tools/em_vigor.py 2023-12-31 lei-11-2009 7` |
| Which law wrote each line of Art. 4 | `git blame lei-11-2009/artigo-004.md` |
| History of Art. 13 | `git log --follow --format="%ad %an" --date=short -- lei-11-2009/artigo-013.md` |
| What Lei 19/2023 changed | `git log --author="19/2023" --stat --format="%s"` |
| Word changes made by Lei 4/2016 | `git diff --word-diff lei-11-2009/2009-10-08 lei-11-2009/2016-05-26 -- lei-11-2009/artigo-005.md` |
| The tags (one per act and in-force day) | `git tag` |
| The labelled change and its candidates | `git log --author="Jornal" --format="%s%n%(trailers:key=Candidate)"` |
| The Constitution, Art. 24 | `python tools/em_vigor.py 2026-10-28 constituicao 24` |

Pick versions by the `In-force:` trailer (the tool does), not by `git rev-list --before`, which uses your local time
zone. Commits are dated noon in Díli (UTC+9). After a rebuild, run `git fetch --force --tags`.

## Notes

- The Constitution text is the Portuguese PDF that the Ministry of Justice serves with the Jornal
  (`public/docs/ConstituicaoRDTL_Portugues.pdf`); Tetum is also official.
- This repository is a research record and not legal advice. See [LICENSE](LICENSE) and [REPRODUCE.md](REPRODUCE.md).
