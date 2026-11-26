# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 1.2.x | ✅ |
| 1.1.x | ⚠️ Critical fixes only — please upgrade |
| ≤ 1.0.x | ❌ |

## Reporting a vulnerability

**Please do not open a public issue, discussion, or pull request for a security problem.**

Report it privately through GitHub's **private vulnerability reporting**:

1. Go to the repository's **Security** tab.
2. Click **Report a vulnerability**, or go straight to
   <https://github.com/Icharu/travelerswatch/security/advisories/new>.
3. Fill in the summary, affected files and versions, steps to reproduce, and impact. Suggest a
   severity if you can; the maintainer confirms the final severity in the advisory.

Only you and the maintainer can see the report. If the fix warrants it, a GitHub Security Advisory
is published afterwards, and you are credited unless you ask not to be.

## What is in scope

- **`hooks/watchman.sh`**, which runs on every prompt in Claude Code: command injection (including
  through the session id or the checkpoint SHA it passes to `git`), path traversal, reading or
  writing files other than `.watch/WATCH.md` and `.watch/.state`, symlink tricks on the state file,
  crashes that block prompts, unbounded output.
- **The evidence scan** (`checkwatch` intake and checkpoints), which reads project documents: text in
  those documents that gets the model to act on it as instructions, or to copy secrets or personal
  data into the logbook.
- **Prompt injection through the logbook**: text in `.watch/WATCH.md` that escapes the `<bearing>`
  data block or gets the model to act on it as instructions.
- **Skill instructions** (`skills/*/SKILL.md`, `references/`) that could lead an agent to write
  outside `.watch/`, change the bearing without PM confirmation, or rewrite the Path log.
- **Manifests** (`.claude-plugin/`, `hooks/hooks.json`) that run unexpected commands.

Out of scope: vulnerabilities in Claude Code, the model, or third-party tools themselves (report those
to their vendors), and issues that require an attacker who already has write access to your
repository *and* bypasses your code review.

## Response times (best effort)

The Traveler's Watch is maintained by **one person in their spare time**. There is no SLA. These are
the targets I currently aim for, measured from the moment a report arrives, by the severity
confirmed in the GitHub advisory:

| GitHub severity | Acknowledge | Triage / assessment | Fix or mitigation target |
|---|---|---|---|
| **Critical** | ≤ 3 days | ≤ 7 days | ≤ 14 days |
| **High** | ≤ 7 days | ≤ 14 days | ≤ 30 days |
| **Moderate** | ≤ 14 days | ≤ 30 days | Next minor release |
| **Low** | ≤ 30 days | Best effort | Next release, as capacity allows |

If you have not heard back within the acknowledgement window, add a comment to the same private
advisory; please do not move the report to a public channel.

## While you wait

You do not have to stay exposed while a report is open:

1. **Turn off the watchman hook.** Set `export TRAVELERSWATCH_DISABLE=1`, or disable the plugin
   (`/plugin` → travelerswatch → disable). The three skills still work; run `/checkwatch` by hand at
   the start of each session.
2. **Review changes to `.watch/`** in pull requests like code, because anything in that file reaches
   the model when the hook is on.
3. **Track the bearing in established project-management tools** in the meantime. Any of these can
   hold the problem statement, constraints, and a change log:
   - [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
   - [OpenProject](https://www.openproject.org/) (open source)
   - [Taiga](https://taiga.io/) (open source)
   - [Plane](https://plane.so/) (open source)
4. **Read the methods behind the skill** to apply them by hand:
   - [docs/methods.md](docs/methods.md): the annotated literature
   - Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
   - Dongre et al. (2025), [*Drift No More?*](https://arxiv.org/abs/2510.07777), which covers how goal reminders reduce drift
   - PMI, [*Top five causes of scope creep*](https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675)

## For the maintainer

Private vulnerability reporting must be **enabled** for the link above to work:
repository **Settings → Advanced Security → Private vulnerability reporting → Enable**.
