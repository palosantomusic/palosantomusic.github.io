#!/usr/bin/env python3
"""Build the Spanish pages (es/index.html, es/our-rhythms.html) from the English ones.

The English pages are the source of truth. Every element with a data-i18n key gets its
Spanish text from the `es:{...}` dictionary in that page's script, so Google can index real
Spanish HTML instead of text swapped in by JavaScript.

Run after any change to index.html or our-rhythms.html:

    python3 tools/build_es.py
"""
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://palosantomusic.github.io/"

PAGES = {
    "index.html": {
        "out": "es/index.html",
        "en_url": BASE,
        "es_url": BASE + "es/",
        "title": "Palo Santo · Banda del Caribe colombiano en Berlín | Bullerengue · Afrocolombiano · Folclor",
        "description": "Palo Santo es una banda del Caribe colombiano en Berlín que toca bullerengue, cumbia y folclor afrocolombiano: puya, mapalé y los ritmos de la costa Caribe de Colombia.",
        "social": "Banda del Caribe colombiano en Berlín · Bullerengue · Afrocolombiano · Folclor",
        "keywords": "Palo Santo, banda colombiana Berlín, banda del Caribe colombiano, bullerengue, afrocolombiano, folclor colombiano, cumbia, puya, mapalé, música colombiana, Berlín",
        "group": "Banda del Caribe colombiano con sede en Berlín que toca bullerengue, cumbia, puya, mapalé y folclor afrocolombiano.",
    },
    "our-rhythms.html": {
        "out": "es/our-rhythms.html",
        "en_url": BASE + "our-rhythms.html",
        "es_url": BASE + "es/our-rhythms.html",
        "title": "Cumbia y bullerengue explicados: ritmos afrocolombianos | Palo Santo",
        "description": "¿Qué es el bullerengue? ¿Cuáles son sus tres aires? Una guía de la cumbia y el bullerengue, los ritmos afrocolombianos detrás del sonido de Palo Santo.",
        "social": "¿Qué es el bullerengue? Una guía de la cumbia y el bullerengue, los ritmos afrocolombianos de Palo Santo.",
        "keywords": "bullerengue, bullerengue Berlín, qué es el bullerengue, cumbia colombiana, origen de la cumbia, banda afrocolombiana Berlín, folclor colombiano, mapalé, puya, Palo Santo, banda colombiana Berlín, música del Caribe",
        "group": "Banda colombiana con sede en Berlín que toca cumbia, bullerengue, puya, mapalé y otros ritmos afrocolombianos de la costa Caribe.",
    },
}

PAIR = re.compile(r"'([\w-]+)'\s*:\s*'((?:\\.|[^'\\])*)'")


def es_dict(src: str) -> dict:
    start = src.index("  es:{")
    end = src.index("\n};", start)
    return {k: v.replace("\\'", "'") for k, v in PAIR.findall(src[start:end])}


def to_parent(url: str) -> str:
    """Relative asset/page URLs need ../ once the page lives in /es/."""
    if url.startswith("assets/"):
        return "../" + url
    return url


def text(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text()


def build(name: str, cfg: dict) -> None:
    src = (ROOT / name).read_text(encoding="utf-8")
    es = es_dict(src)
    soup = BeautifulSoup(src, "html.parser")

    soup.html["lang"] = "es"

    # Translate every data-i18n element.
    for el in soup.select("[data-i18n]"):
        val = es.get(el["data-i18n"])
        if val is not None:
            el.clear()
            el.append(BeautifulSoup(val, "html.parser"))

    # Head: title, description, social, canonical, locale.
    soup.title.string = cfg["title"]
    for sel, attr, val in [
        ('meta[name="description"]', "content", cfg["description"]),
        ('meta[name="keywords"]', "content", cfg["keywords"]),
        ('meta[property="og:title"]', "content", cfg["title"]),
        ('meta[name="twitter:title"]', "content", cfg["title"]),
        ('meta[property="og:description"]', "content", cfg["social"]),
        ('meta[name="twitter:description"]', "content", cfg["social"]),
        ('meta[property="og:locale"]', "content", "es_ES"),
        ('meta[property="og:locale:alternate"]', "content", "en_GB"),
        ('link[rel="canonical"]', "href", cfg["es_url"]),
    ]:
        tag = soup.select_one(sel)
        if tag:
            tag[attr] = val

    # Relative URLs -> one level up.
    for tag in soup.find_all(True):
        for attr in ("src", "href", "poster"):
            if tag.has_attr(attr):
                tag[attr] = to_parent(tag[attr])
    for style in soup.find_all("style"):
        style.string = style.string.replace("url('assets/", "url('../assets/")

    # Language switch points back to English.
    btn = soup.select_one("#lang-btn")
    btn["href"] = "../" if name == "index.html" else "../our-rhythms.html"
    btn["hreflang"] = "en"
    btn["lang"] = "en"
    btn["aria-label"] = "View in English"
    btn.string = "EN"

    # Structured data in Spanish.
    for script in soup.find_all("script", type="application/ld+json"):
        data = json.loads(script.string)
        if data.get("@type") == "MusicGroup":
            data["description"] = cfg["group"]
        if data.get("@type") == "FAQPage":
            for i, item in enumerate(data["mainEntity"], start=1):
                if f"faq{i}-q" in es:
                    item["name"] = text(es[f"faq{i}-q"])
                    item["acceptedAnswer"]["text"] = text(es[f"faq{i}-a"])
        script.string = "\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    out = ROOT / cfg["out"]
    out.parent.mkdir(exist_ok=True)
    html = str(soup)
    html = html.replace(
        "<!DOCTYPE html>",
        "<!DOCTYPE html>\n<!-- GENERATED by tools/build_es.py from ../" + name + " — edit the English page and re-run. -->",
        1,
    )
    out.write_text(html, encoding="utf-8")
    print("wrote", cfg["out"], f"({len(es)} strings)")


if __name__ == "__main__":
    for name, cfg in PAGES.items():
        build(name, cfg)
