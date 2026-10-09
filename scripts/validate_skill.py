"""Validate the portable runtime and documentation; requires development PyYAML."""
from pathlib import Path, PurePosixPath
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = ('README', 'AGENTS', 'BRAND_IDENTITY', 'DESIGN')


def frontmatter(text):
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    result = yaml.safe_load(match.group(1))
    if not isinstance(result, dict):
        raise ValueError('Frontmatter must be a mapping')
    return result


def runtime_files(root=ROOT):
    entries = (root / 'release-manifest.txt').read_text(encoding='utf-8').splitlines()
    entries = [e.strip() for e in entries if e.strip() and not e.startswith('#')]
    if len(entries) != len(set(entries)):
        raise ValueError('Duplicate runtime manifest entry')
    for entry in entries:
        path = PurePosixPath(entry)
        if path.is_absolute() or '..' in path.parts or '\\' in entry or ':' in entry:
            raise ValueError(f'Unsafe runtime path: {entry}')
        target = root / entry
        if not target.is_file() or target.is_symlink() or not target.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Missing or unsafe runtime resource: {entry}')
    return entries


def validate(root=ROOT):
    root = root.resolve()
    entries = runtime_files(root)
    required = {'SKILL.md', 'INSTALL.md', 'agents/openai.yaml', 'references/dependencies.md'}
    required.update(f'assets/{locale}/{name}.template.md' for locale in ('en', 'es') for name in DOCUMENTS)
    if set(entries) != required:
        raise ValueError('Runtime manifest differs from the required installable package')
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    metadata = frontmatter(skill)
    if metadata.get('name') != 'project-kickoff' or not metadata.get('description'):
        raise ValueError('Invalid skill name or description')
    for link in re.findall(r'\]\(((?:assets|references)/[^)]+)\)', skill):
        if link not in entries:
            raise ValueError(f'Unpackaged resource link: {link}')
    for locale in ('en', 'es'):
        for name in DOCUMENTS:
            text = (root / f'assets/{locale}/{name}.template.md').read_text(encoding='utf-8')
            if not text.strip() or '{{' not in text:
                raise ValueError(f'Incomplete template: {locale}/{name}')
        design = frontmatter((root / f'assets/{locale}/DESIGN.template.md').read_text(encoding='utf-8'))
        if set(design) != {'name', 'category', 'surface', 'colors'}:
            raise ValueError(f'Invalid DESIGN metadata: {locale}')
        if not isinstance(design['colors'], dict) or any(v is not None for v in design['colors'].values()):
            raise ValueError(f'Design template must not impose a palette: {locale}')
    yaml.safe_load((root / 'agents/openai.yaml').read_text(encoding='utf-8'))
    for path in root.rglob('*.md'):
        if any(part in {'.git', 'dist', '.venv'} for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding='utf-8')
        if re.search(r'(?i)(?<![a-z])[a-z]:[\\/]|/mnt/[a-z]/|/home/[^\s/]+|C:\\Users|mrbrazzi|Alain Sánchez', text):
            raise ValueError(f'Author-specific environment or identity in {path.relative_to(root)}')
    print(f'Validated {len(entries)} runtime files and both template locales')
    return entries


if __name__ == '__main__':
    try:
        validate()
    except (ValueError, OSError, yaml.YAMLError) as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
