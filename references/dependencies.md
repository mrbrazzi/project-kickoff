# Dependency checks and installation

## Git

| Environment | Locate | Verify |
| --- | --- | --- |
| PowerShell | `Get-Command git -ErrorAction SilentlyContinue` | `git --version` |
| macOS / Linux / WSL | `command -v git` | `git --version` |

Git outside PATH may require a fresh session or a known executable path. Diagnose
execution failures before installing duplicates. Windows and WSL are separate
environments: install only where the project needs it.

If absent, explain versioning/recovery and propose a concrete method before asking
permission. Consult [official instructions](https://git-scm.com/install/). Windows
may use winget's exact `Git.Git` package, macOS an existing manager/system tools and
Linux its distribution manager. Do not install another manager or elevate without
approval. Review remote scripts before execution and verify Git's exit status/version.

## Engram

- [Official repository](https://github.com/Gentleman-Programming/engram).
- [Installation](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md).
- [Agent setup](https://github.com/Gentleman-Programming/engram/blob/main/docs/AGENT-SETUP.md).

Consult current sources for installation/client setup, rather than remembered versions,
Go module paths or release assets. Prefer a compatible stable release. Binary install
and MCP setup are separate changes; explain components and required reloads.

1. Discover Engram MCP tools. A successful identification read, such as
   `mem_current_project` using the live schema, proves backend access. Verify the
   project mapping before writing.
2. Without a connection, locate `engram` in the active environment; check
   `engram version` or `engram --help`.
3. Where existing WSL/container/service integration is evidenced, inspect relevant
   status/launcher only. Do not inspect credentials, persistent volumes or unrelated
   environments. A stopped on-demand backend may still be installed.
4. Configuration without execution means detected/unverified access. If another
   environment cannot be checked, report uncertainty and ask its location.

Engram complements Git/documents with cross-session context. An Engram skill alone
does not prove backend availability. After authorization, use an official method,
verify available checksums and preserve installations/configuration; no automatic
data migration. A specialized skill may help but is not required. Verify backend
and agent access separately; document data location/reconnection without secrets.
On failure, report and continue independent tasks without blind repairs.
