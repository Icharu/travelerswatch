<!-- lang-bar -->
**English** · [Português (Brasil)](i18n/pt-BR/QUICKSTART.md) · [Español](i18n/es/QUICKSTART.md) · [繁體中文](i18n/zh-Hant/QUICKSTART.md) · [简体中文](i18n/zh-Hans/QUICKSTART.md) · [日本語](i18n/ja/QUICKSTART.md) · [العربية](i18n/ar/QUICKSTART.md)

# Quick start

Install The Traveler's Watch (TTW), set your project's bearing on day one, and use it every day
after that. Back to the [README](README.md).

**TTW is daily-led.** You lead each day's work. The watchman keeps the bearing in view at every
prompt, and the logbook keeps the history, so each day starts from where the project really is, not
from what the model remembers.

## 1. Install

Pick one.

| Option | Commands | You get |
|---|---|---|
| **Claude Code plugin** (recommended) | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | Skills + the automatic watchman. Commands: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch` |
| **Skills only** (Claude Code or any [Agent Skills](https://agentskills.io/) agent) | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | Skills, no watchman. Commands: `/checkwatch`, `/fixwatch`, `/configwatch`. Run `/checkwatch` at the start of each session by hand. |
| **Try without installing** | `claude --plugin-dir ./travelerswatch` | Everything, for this session only |

Requirements: Claude Code for the watchman; `bash` and `awk` (macOS and Linux have both); `git` is
optional but enables commit counting and the full post-project review.

## 2. Day one: set the bearing

1. Open Claude Code in your project's root folder.
2. Run **`/checkwatch`**. Answer one line: what the project is and which part this bearing steers.
3. Claude reads your README, `docs/`, and recent git history, then shows an **evidence card** and
   **drafts** of each section. You correct them; it asks about gaps, misfiled items, and any place
   where your answers contradict the evidence. Expect about five rounds.
4. Confirm the bearing. Claude writes `.watch/WATCH.md` and adds `.watch/.state` to `.gitignore`.
5. **Commit the logbook**: `git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`.

From now on, nothing in the bearing changes unless you confirm it.

## 3. Every day

| When | What you do | What TTW does |
|---|---|---|
| **Start of the day** | Open Claude Code and work as usual. | The watchman re-reads `.watch/WATCH.md` on your first prompt, so yesterday's confirmed changes are already in effect. |
| **While working** | Ask for what you need: code, reviews, drafts. | Repetitive work is done inside the bearing. If a request drifts, Claude says so in **one line** and carries on. |
| **A drift flag appears** | Decide: was it a detour, or is the path really changing? | Detour: just continue. Real change: run **`/fixwatch`**, review the diff and its ripple, and confirm or cancel. |
| **"A checkpoint is due"** | Run **`/checkwatch`** when you have a minute. | Reports *On path / Drifting / Off path / Bearing in question* with evidence, and adds one line to the Checkpoint log. |
| **End of the day** | Commit `.watch/WATCH.md` together with your work if it changed. | Nothing else. TTW keeps no data outside your repository. |
| **End of a phase or of the project** | Tell Claude: "the phase is ending, let's do the post-project review." | Drafts a review from the Checkpoint log, Path log, and git history. You choose **review and close** or **review only**. |

### What TTW knows, and when

TTW is aware of your project's daily changes through the logbook and git, not by watching your
files. To be precise:

| Moment | What is read | What is **not** read |
|---|---|---|
| **Every prompt** (watchman) | The bearing and Status in `.watch/WATCH.md`; the number of commits and sessions since the last checkpoint. | Your code, diffs, or other files. |
| **Checkpoint** (`/checkwatch`) | The conversation, `git log` since the last checkpoint, changed files, the documents listed under *Evidence scanned*. | Anything outside the project folder. |
| **Post-project review** | The whole logbook (Checkpoint log + Path log) and the git history of `.watch/WATCH.md`. | Anything outside the project folder. |

## 4. Commands at a glance

| Command | Use it to |
|---|---|
| `/checkwatch` | Set the bearing (first time) · run a checkpoint · run a post-project review |
| `/fixwatch` | Change course on purpose · close a review · reopen a closed project |
| `/configwatch` | See the status · set the checkpoint cadence: shakedown `every 3 commits or 2 sessions` (default), steady `every 10 commits or 5 sessions`, custom, or `off` |

## 5. What TTW will not do for you

TTW will not confirm a change, accept a contradiction, or close the project on your behalf, even if
you ask it to. It will draft the diff, check the ripple, and gather the evidence so that each
decision takes you one look. That is by design: see
[What it is, and what it is not](README.md#what-it-is-and-what-it-is-not).

## 6. Turn it off or pause it

- For this shell: `export TRAVELERSWATCH_DISABLE=1`
- For good: `/plugin` → travelerswatch → disable (the skills still work by hand).
- Fewer checkpoint reminders: `/configwatch` → steady or `off`.

## Next

[Concepts](docs/concepts.md) · [Worked example](examples/pm-walkthrough.md) ·
[Methods](docs/methods.md) · [Contributing](CONTRIBUTING.md)
