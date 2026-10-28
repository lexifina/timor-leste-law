"""Prints an act, or one article of it, as it stood on a given day, from this repository's history.

    python tools/em_vigor.py 2020-01-01 lei-11-2009 5      # Art. 5 of Lei 11/2009 on 1 January 2020
    python tools/em_vigor.py 2024-01-01 lei-11-2009        # the whole law, in document order
    python tools/em_vigor.py 2024-01-01 constituicao 24

The act is named by its folder. The article is its number ("5", "4-A"), or "preambulo" / "estrutura". Every commit
carries the day its text took effect in its "In-force:" trailer; the day is read from the trailer, never from the
commit date. Standard library only.
"""
import datetime as dt
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def commit_on(day: str, path: str) -> str | None:
    """The last commit touching `path` whose In-force day is on or before `day` (history is in in-force order)."""
    out = git('log', '--format=%H%x00%(trailers:key=In-force,valueonly,separator=)%x01', 'main', '--', path)
    for rec in out.split('\x01'):
        rec = rec.strip()
        if not rec:
            continue
        h, d = rec.split('\x00')
        if d.strip() and d.strip() <= day:
            return h
    return None


def file_for(article: str) -> str:
    a = article.removesuffix('.md')
    if a in ('preambulo', 'estrutura') or a.startswith('artigo-'):
        return f'{a}.md'
    m = re.fullmatch(r'(\d+)(?:-([A-Za-z]))?', a)
    if not m:
        sys.exit(f'unknown article {article!r}')
    return f'artigo-{int(m.group(1)):03d}' + (f'-{m.group(2).upper()}' if m.group(2) else '') + '.md'


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, act = sys.argv[1], sys.argv[2].strip('/')
    dt.date.fromisoformat(day)
    commit = commit_on(day, act)
    if not commit:
        sys.exit(f'{act} is not in the record on {day}.')
    if len(sys.argv) > 3:
        name = file_for(sys.argv[3])
        try:
            text = git('show', f'{commit}:{act}/{name}')
        except subprocess.CalledProcessError:
            sys.exit(f'{act}/{name} was not in force on {day}.')
        print(text, end='')
        return
    order = git('show', f'{commit}:{act}/estrutura.md')
    for line in order.split('\n'):
        if line.startswith('- '):
            print(git('show', f'{commit}:{act}/{line[2:].strip()}'))
        elif line.startswith('## '):
            print(line + '\n')


if __name__ == '__main__':
    main()
