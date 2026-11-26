# Estrutura / Structure

Um ficheiro por artigo, uma pasta por ato, as pastas por tipo de ato e por ano (no máximo 1 000 entradas por pasta).
One file per article, one folder per act, folders by kind of act and year (at most 1,000 entries per folder).

```
constituicao/                               Constituição da República (2002)
codigos/<codigo>/                           a code: its articles here, the act that approves it in diploma/
    artigo-001.md ... estrutura.md README.md
    diploma/artigo-001.md preambulo.md
leis/<ano>/<número>-<assunto>/              Leis do Parlamento Nacional
decretos-leis/<ano>/<número>-<assunto>/     Decretos-Leis do Governo
decretos-governo/<ano>/<número>-<assunto>/  Decretos do Governo
resolucoes-parlamento/<ano>/...             Resoluções do Parlamento Nacional
resolucoes-governo/<ano>/...                Resoluções do Governo
diplomas-ministeriais/<ano>/...             Diplomas Ministeriais
```

Inside an act's folder:

- `artigo-007.md` is Article 7; an inserted article is `artigo-004-A.md`;
- `preambulo.md` is the text before Article 1 (name, date, title, preamble, enacting formula);
- `estrutura.md` lists the chapter and section headings and the order of the files;
- `anexo/artigo-001.md` ... is an annex numbered again from Article 1 (for example a republication);
- `texto.md` holds an act without numbered articles (many resolutions), whole;
- `README.md` gives the act's kind, publication, entry into force and source PDF.

`<ano>` is the year in the act's number (Lei n.º 4/2012 is in `leis/2012/`), `<número>` its number, `<assunto>` its
title in lower case without accents, cut at about 60 characters.

## Dates

Each act is one commit, dated noon in Dili (UTC+9) on the day it entered into force under its own rule
("entra em vigor no dia seguinte ao da sua publicação", "... 120 dias após a sua publicação", "... em 1 de janeiro
de 2027"), counted from its publication in the Jornal da República. Trailers: `Published:`, `In-force:`,
`In-force-basis:`, `Evidence:` (the rule, quoted), `Source:`, `Source-sha256:`. An act whose rule could not be read,
which fixes no day (Lei n.º 1/2002, artigo 16.º: then the tenth working day), or which is not yet in force, is held
back, not guessed.
