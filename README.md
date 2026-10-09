# project-kickoff

A portable AI-agent skill for initializing local projects: gather context, prepare
Git, check optional Engram memory and create useful project documentation.

## Features

- Ask for **English or Spanish** document output and reuse prepared templates.
- Interview users about purpose, deliverables, scope, tools and conventions.
- Check Git; request permission to install it when missing.
- Detect optional Engram; install only with consent and skip if declined.
- Preserve existing repositories, documents and staged changes.
- Create README.md/AGENTS.md; offer BRAND_IDENTITY.md/DESIGN.md with confirmation.
- Proactively request permission to record created files in a local commit.

Also supports non-code projects. No automatic feature implementation, publication
or visual style. Repository documentation is English; generated documents use the
user's chosen language. Filenames and machine-readable keys remain stable.

## Install manually from a release

Download `project-kickoff-vX.Y.Z.zip` and its `.sha256` file from this repository's
GitHub Releases page. Verify the checksum, then extract into the skills parent
directory recognized by your agent. The archive already contains **project-kickoff/**;
do not add a second nested folder.

For clients supporting shared user skills, this is commonly `~/.agents/skills/`
(`%USERPROFILE%\.agents\skills\` on Windows). Other clients may use another directory;
consult their configuration. No path guarantees automatic discovery by every agent.
Any local agent with file access can read the installed SKILL.md directly.

```text
<skills-directory>/project-kickoff/
├── SKILL.md
├── INSTALL.md
├── LICENSE
├── agents/openai.yaml
├── references/dependencies.md
└── assets/
    ├── en/  # Four English templates
    └── es/  # Four Spanish templates
```

No Python, Node.js or package installation is needed to load the skill. Git is
required in the project being initialized; Engram is optional. Preserve customizations
before replacing an installed version. Reload the client's skill catalog if necessary.

## Install from the repository

Ask your agent to inspect this repository and install the runtime files listed in
`release-manifest.txt` into `project-kickoff` under its skills directory. Copy both
locales and references, not only SKILL.md. Runtime files do not depend on the author's
environment or the checkout's absolute path.

## Use

From the target project, invoke `$project-kickoff` if supported or ask the agent to
follow its installed SKILL.md. Explain the goal/scope and answer **English** or
**Spanish** when asked which document language you prefer. Installations, optional
branding/design and commits each require their own scope of consent.

## Development and validation

Edit repository sources, not installed copies. Python 3.11+ and PyYAML are development
dependencies only:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/build_release.py --version v1.0.0
```

The builder creates `dist/project-kickoff-v1.0.0.zip` and a checksum from an explicit
allowlist. Checks cover runtime resources, both locales, YAML, portable documentation
and clean ZIP extraction. They do not prove conversational behavior or real dependency
installation. `dist/` is generated and intentionally ignored by Git.

## Release on GitHub

Publish this repository with GitHub Actions enabled, then push a version tag:

```sh
git tag v1.0.0
git push origin v1.0.0
```

The [release workflow](.github/workflows/release.yml) validates, tests, builds and
publishes the ZIP/checksum using an existing tag and `GITHUB_TOKEN` with `contents: write`.
No personal token or external release service is needed. CI validates pull requests
and branch pushes. Local builds do not publish releases; the skill creates no remote/tag.
