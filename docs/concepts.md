# Concepts

## Agent Skills in one paragraph

A skill is a folder with a `SKILL.md` file (YAML frontmatter with `name` and `description`, then
instructions) and optional `references/`, `assets/`, and `scripts/`. Agents load skills by
**progressive disclosure**: only the name and description are always in context; the body is read
when a task matches the description; reference files are read only when the body points to them.
A skill does not change the model — it hands it a written method at the moment it is needed. The
format is an open standard ([agentskills.io](https://agentskills.io/)), so the two skills here work
in any agent that reads it. The **hook** is the one Claude Code–specific part.

## The pieces

| Piece | Type | Portable? | Job |
|---|---|---|---|
| `checkwatch` | Skill | Yes | Set the bearing (intake) or evaluate against it (checkpoint) |
| `fixwatch` | Skill | Yes | Propose → PM confirms → update bearing + append Path log |
| `watchman.sh` | Hook (`UserPromptSubmit`) | Claude Code only | Inject a compact bearing on every prompt so drift is flagged in one line |
| `.watch/WATCH.md` | File in *your* repo | Yes | The bearing and its history; committed so the team can review it |

Without the hook (another agent, or the hook disabled), run `/checkwatch` at the start of each
working session for the same effect, by hand.

## The bearing

| Part | Question it answers |
|---|---|
| **Standard** | What will the work be judged against? (lens preset, free-text rubric, or named external standard — always boundary-checked) |
| **Context** | Where does this work live? Field, stakeholders, current state, referenced works |
| **Constraints** | What limits us? |
| **Problem** | What is wrong today (original problem), and what does done look like (final objective)? |
| **Tools** | What will we use, and why does each fit? |
| **Relations** | Where do the sections pull against each other, and which tensions did we accept? |
| **Path log** | Every course change: trigger, who proposed it, what changed, why, impact, PM confirmation |

## Verdicts

- **On path** — the work serves the final objective within the constraints, with the agreed tools.
- **Drifting** — some work or discussion is moving away from the bearing; nothing decided yet.
- **Off path** — the work now serves a different objective, breaks a constraint, or depends on tools
  outside the bearing. Either come back or `/fixwatch`.

## Who decides

Claude may **propose** a course change at any time, including when it realizes it misread the
context. Only the **PM confirms**. Nothing in the bearing changes without that confirmation, and the
Path log is never rewritten.
