"""Dependency-free structural validation. Run from any working directory."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = []
        self.links = []
        self.h1_count = 0
        self.tags = []
        self.navigation = []
        self.in_main_nav = False
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'nav' and attrs.get('aria-label') == '主要導覽':
            self.in_main_nav = True
        if tag == 'a' and self.in_main_nav:
            self.navigation.append(attrs)
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_main_nav = False


def main():
    pages = {path.resolve(): Page(path) for path in ROOT.rglob('*.html')}
    errors = []
    checked_links = 0
    index = pages[(ROOT / 'index.html').resolve()]
    expected_nav = {unquote(urlsplit(link['href']).path) for link in index.navigation}
    for path, page in pages.items():
        label = str(path.relative_to(ROOT))
        source = path.read_text(encoding='utf-8')
        if page.h1_count != 1:
            errors.append(f'{label}: expected one h1, found {page.h1_count}')
        if len(page.ids) != len(set(page.ids)):
            errors.append(f'{label}: duplicate id')
        required = [('html', 'lang', 'zh-Hant'), ('meta', 'charset', 'utf-8'), ('meta', 'name', 'viewport'), ('meta', 'name', 'description')]
        for tag, key, value in required:
            if not any(t == tag and a.get(key) == value for t, a in page.tags):
                errors.append(f'{label}: missing {key}={value}')
        if '<title>' not in source:
            errors.append(f'{label}: missing title')
        is_template = path.parent.name == 'templates'
        if not is_template and re.search(r'\{\{.+?\}\}', source):
            errors.append(f'{label}: unresolved template text')
        normalized_nav = set()
        current_count = 0
        for link in page.navigation:
            target = (path.parent / urlsplit(link['href']).path).resolve()
            normalized_nav.add(target.relative_to(ROOT).as_posix())
            if link.get('aria-current') == 'page':
                current_count += 1
                if target != path:
                    errors.append(f'{label}: aria-current points to another page')
        if normalized_nav != expected_nav:
            errors.append(f'{label}: navigation differs from homepage')
        if not is_template and current_count != 1:
            errors.append(f'{label}: expected one active navigation link')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                errors.append(f'{label}: external runtime/link dependency {link}')
                continue
            if url.path.startswith('/'):
                errors.append(f'{label}: root-relative URL {link}')
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_file():
                errors.append(f'{label}: missing target {link}')
            elif url.fragment and not is_template:
                target_page = pages.get(target)
                if target_page and unquote(url.fragment) not in target_page.ids:
                    errors.append(f'{label}: missing fragment {link}')
            checked_links += 1
    catalog_source = (ROOT / 'assets/catalog.js').read_text(encoding='utf-8')
    catalog = json.loads(catalog_source.split('=', 1)[1].strip().rstrip(';'))
    ids = [entry['id'] for entry in catalog]
    if len(ids) != len(set(ids)):
        errors.append('catalog: duplicate ids')
    card_tags = [attrs for tag, attrs in index.tags if tag == 'article' and 'catalog-card' in attrs.get('class', '')]
    if {attrs['data-id'] for attrs in card_tags} != set(ids):
        errors.append('catalog: homepage and catalog entries differ')
    index_source = (ROOT / 'index.html').read_text(encoding='utf-8')
    for entry in catalog:
        if not (ROOT / entry['href']).is_file():
            errors.append(f'catalog: missing {entry["href"]}')
        if entry['summary'] not in index_source:
            errors.append(f'catalog: summary differs for {entry["id"]}')
    for required_file in ['AGENTS.md', 'README.md', 'CHANGELOG.md', '.nojekyll', 'templates/article-template.html']:
        if not (ROOT / required_file).is_file():
            errors.append(f'missing deliverable {required_file}')
    if errors:
        print('\n'.join('FAIL ' + error for error in errors))
        return 1
    print(f'PASS {len(pages)} HTML documents, {checked_links} local references, {len(catalog)} catalog entries. Metadata, navigation, fragments and relative paths verified.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
