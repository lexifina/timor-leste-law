# Sources

All from the Jornal da República, the official gazette of Timor-Leste, published by the Ministry of Justice.
robots.txt (checked 2026-10-28) allows `/jornal/` with `Crawl-delay: 10`; the builder waits 10 seconds between
requests. Index of laws: <https://www.mj.gov.tl/jornal/?q=node/12>.

From 2026-11-26 the acts filed by kind and year come from the Série I indexes of the Jornal: Leis
(`?q=node/12`), Decretos-Leis (`?q=node/13`), Decretos do Governo (`?q=node/18`), Resoluções do Parlamento Nacional
(`?q=node/19`), Resoluções do Governo (`?q=node/20`), and the issue PDFs they link under
`https://www.mj.gov.tl/jornal/public/docs/<ano>/serie_1/`; the source URL and sha256 of each are in each commit's
`Source:` and `Source-sha256:` trailers.

| Act | Issue | URL |
|---|---|---|
| Constituição da RDTL (2002) | text served with the Jornal | https://www.mj.gov.tl/jornal/public/docs/ConstituicaoRDTL_Portugues.pdf |
| Lei n.º 11/2009, de 7 de outubro | Série I, N.º 35 (2009-10-07) | https://www.mj.gov.tl/jornal/public/docs/2009/serie_1/serie1_no35.pdf |
| Lei n.º 4/2016, de 25 de maio (with republication) | Série I, N.º 20 (2016-05-25) | https://www.mj.gov.tl/jornal/public/docs/2016/serie_1/SERIE_I_NO_20.pdf |
| Lei n.º 14/2021, de 7 de julho (with republication) | Série I, N.º 28 (2021-07-07) | https://www.mj.gov.tl/jornal/public/docs/2021/serie_1/SERIE_I_NO_28_NORMAL.pdf |
| Lei n.º 14/2023, de 24 de maio (with republication) | Série I, N.º 19, Suplemento I (2023-05-24) | https://www.mj.gov.tl/jornal/public/docs/2023/serie_1/SERIE_I_NO_19_SUPLEMENTO_I.pdf |
| Lei n.º 19/2023, de 5 de dezembro (with republication) | Série I, N.º 45 D (2023-12-05) | https://www.mj.gov.tl/jornal/public/docs/2023/serie_1/SERIE_I_NO_45_D.pdf |

The sha256 of every file read is in `data/versions.json` and REPRODUCE.md.
