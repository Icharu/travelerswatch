# Concepts

## Agent Skills in one paragraph

A skill is a folder with a `SKILL.md` file (YAML frontmatter with `name` and `description`, then
instructions) and optional `references/`, `assets/`, and `scripts/`. Agents load skills by
**progressive disclosure**: only the name and description are always in context; the body is read
when a task matches the description; reference files are read only when the body points to them.
A skill does not change the model — it hands it a written method at the moment it is needed. The
format is an open standard ([agentskills.io](https://agentskills.io/)), so the three skills here work
in any agent that reads it. The **hook** is the one Claude Code–specific part.

## The pieces

| Piece | Type | Portable? | Job |
|---|---|---|---|
| `checkwatch` | Skill | Yes | Set the bearing from the PM's answers **and the project's evidence** (intake), or evaluate work and bearing against reality (checkpoint) |
| `fixwatch` | Skill | Yes | Propose → PM confirms → update bearing + append Path log; closes a bearing *under review* |
| `configwatch` | Skill | Yes | Show status; set the checkpoint cadence (`every N commits or M sessions`, or `off`) |
| `watchman.sh` | Hook (`UserPromptSubmit`) | Claude Code only | Inject a compact bearing on every prompt; flag drift in one line; nudge when a checkpoint is due |
| `.watch/WATCH.md` | File in *your* repo | Yes | The bearing, its status, and its history; committed so the team can review it |
| `.watch/.state` | Local file | — | Session counter for the cadence; git-ignored |

Without the hook (another agent, or the hook disabled), run `/checkwatch` at the start of each
working session for the same effect, by hand.

## The bearing

| Part | Question it answers |
|---|---|
| **Status** | Is the bearing confirmed or under review? How often should a checkpoint happen, and when was the last one? |
| **Scope** | What part of the project does this bearing steer — and what not? |
| **Standard** | What will the work be judged against? (lens preset, free-text rubric, or named external standard — always boundary-checked; one criterion must anchor the Final objective) |
| **Context** | Where does this work live? Field, stakeholders, current state *as the evidence shows it*, referenced works, evidence scanned |
| **Constraints** | What limits us? |
| **Problem** | What is wrong today (original problem), and what does done look like (final objective)? |
| **Tools** | What will we use, and why does each fit? |
| **Relations** | Where do the sections pull against each other or against the evidence — and which tensions and contradictions did the PM accept? |
| **Path log** | Every course change and settings change: trigger, who proposed it, what changed, why, impact, PM confirmation |

## Three layers against a wrong bearing

A bearing can be consistent with itself and still wrong about the project. No single check catches
that, so the design has three layers ([ADR 0003](adr/0003-evidence-grounded-bearing.md)):

| Layer | Mechanism |
|---|---|
| **Prevent** | Scope first; evidence scan; drafts from evidence; every contradiction resolved or explicitly accepted; objective anchor required |
| **Detect** | Checkpoints judge *work vs bearing* and *bearing vs reality*; shakedown cadence nudges for an early checkpoint |
| **Contain** | *Under review* status pauses drift flags until `/fixwatch` corrects or keeps the bearing |

## Verdicts

- **On path** — the work serves the final objective within the constraints, with the agreed tools,
  and the bearing still matches the evidence.
- **Drifting** — some work or discussion is moving away from a bearing that still holds.
- **Off path** — the work now serves a different objective, breaks a constraint, or depends on tools
  outside the bearing. Either come back or `/fixwatch`.
- **Bearing in question** — the evidence contradicts the bearing itself. Mark it *under review*
  (PM confirms) and correct it with `/fixwatch`.

## Who decides

Claude may **propose** a course change at any time, including when it realizes it misread the
context, and may **propose** marking the bearing under review. Only the **PM confirms**. Nothing in
the bearing changes without that confirmation, and the Path log is never rewritten.
