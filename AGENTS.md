# Agent instructions

Maintain a portable local-project kickoff skill. Preserve the context interview,
Git checks, optional Engram, confirmation for branding/design and proactive local
commit permission requests. Do not expand kickoff into application implementation.

## Conventions

- Common repository documentation and instructions are English.
- Maintain all four templates in both `assets/en/` and `assets/es/`.
- Ask explicitly for project-document language and reuse that locale, without
  translating another template at runtime.
- Keep filenames, YAML keys and token roles stable across locales.
- No author-specific paths, personal data, source-brand choices or local service
  state in reusable documentation.
- Edit this canonical repository; installed copies are release artifacts.
- Preserve manually maintained files, existing approvals and unrelated Git changes.

## Packaging and validation

SKILL.md is the entrypoint, references/dependencies.md contains diagnostics and locale
templates define documents. agents/openai.yaml is optional metadata. release-manifest.txt
defines runtime files; INSTALL.md ships inside the ZIP. Development scripts, CI and
tests are excluded. Update the manifest when runtime resources change.

Run `python scripts/validate_skill.py`, `python -m unittest discover -s tests -v`
and the release builder. Inspect a clean extraction. Offline checks do not prove
conversational decisions or actual Git/Engram installation.

## Git and continuity

Review status/diffs and commit authorized changes. An explicit request to commit
is sufficient authorization; no implicit push, remote creation or global identity
changes. The skill requests permission after reviewing files unless already authorized.
Verify Engram project identity before saving context; never assume a developer's
backend or configuration. Keep documentation current and exclude secrets.
