"""Inject the presentation-mode shim into the deck's bundled template.

The bundle carries the real document as a JSON string in a
<script type="__bundler/template"> tag; the loader parses it, substitutes
blob URLs for asset UUIDs and swaps it in as the live document. Editing that
string is the only way to reach the deck without rebuilding the bundle.

The shim goes in <head>, immediately after the opening tag. The loader
re-creates every script in document order so the inert parsed copies execute,
awaiting each src script's load — but the dc runtime detaches the <helmet>
scripts while the loader is still walking the list, so their replacements
never connect, never fire load, and the walk never reaches <body>. Anything
appended at the end of the document is therefore dead code.
"""
import json, pathlib, re, shutil, sys

DECK = pathlib.Path("/Users/stinsonrecon/work/EVNGENCO1/Projects/claude-code/Claude Code EVNGENCO1 - Trinh chieu.html")
SHIM = pathlib.Path(__file__).resolve().parent / "present-shim.html"
MARK = "<!-- ak:present-mode -->"


def encode(html: str) -> str:
    # The JSON lives inside a <script>, so a literal </ would close the tag
    # early. The bundler escapes exactly those; match it byte for byte.
    return json.dumps(html, ensure_ascii=False).replace("</", "<\\u002F")


def main() -> None:
    text = DECK.read_text(encoding="utf-8")
    lines = text.split("\n")
    i = next(i for i, l in enumerate(lines)
             if "__bundler/template" in l and l.strip().startswith("<script"))
    html = json.loads(lines[i + 1])

    # Idempotent: drop any previous injection before adding the current one.
    before = html
    # Exact inverse of the insertion below, so a re-run neither duplicates
    # the shim nor drifts the surrounding whitespace.
    html = re.sub(r"\n" + re.escape(MARK) + r".*?</script>", "", html, flags=re.S)
    replaced = html != before

    shim = SHIM.read_text(encoding="utf-8").strip("\n")
    head = re.search(r"<head[^>]*>", html, re.I)
    if not head:
        sys.exit("ERROR: template has no <head> to inject into")
    cut = head.end()
    html = html[:cut] + "\n" + shim + html[cut:]

    if not DECK.with_suffix(".html.orig").exists():
        shutil.copy2(DECK, DECK.with_suffix(".html.orig"))
        print(f"backup -> {DECK.with_suffix('.html.orig').name}")

    lines[i + 1] = encode(html)
    DECK.write_text("\n".join(lines), encoding="utf-8")
    print(f"{'re-injected' if replaced else 'injected'} shim ({len(shim)} chars) "
          f"into <head>; bundle now {DECK.stat().st_size / 1024:.0f} KB")


main()
