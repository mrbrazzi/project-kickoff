# Install project-kickoff

Verify the release ZIP against its accompanying SHA256 file, then extract into the
skills parent directory recognized by your agent. The ZIP already contains
`project-kickoff/`: SKILL.md must be directly inside it, beside assets/en, assets/es,
references and agents. Keep both locales and all resources together.

Common shared-user directories, when supported, are `~/.agents/skills/` or
`%USERPROFILE%\.agents\skills\` on Windows. Other clients use their configured
skills directory; check their instructions. No location guarantees universal
auto-discovery. Agents with local file access can follow SKILL.md directly.
Reload the client/catalog if needed. Preserve customizations before replacing versions.

Invoke `$project-kickoff` from the project to initialize and choose English or Spanish
when asked. No runtime package installation is needed for the skill. Git is needed
for project versioning; Engram is optional. Installations and commits require consent
as described in SKILL.md. Repository development files are not included in this ZIP.
