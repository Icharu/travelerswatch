# Benchmark — best vs worst case on a live project (v1.0.0 → v1.1.0)

- **Date:** 2026-11-25
- **Versions:** found on v1.0.0, fixed in v1.1.0
- **Run by:** the maintainer, with Claude Code (Opus 5.5)
- **Anonymized:** the project is a live academic data platform with open security findings. Its
  name, hostname, commit hashes, file paths, and finding details are withheld on purpose. Findings
  are described by severity and area only. The eval fixtures in `skills/*/evals/files/` are
  **synthetic** reconstructions of the same situation.

## Why this benchmark

The v1.0.0 evals only checked that each rule fires on a happy path. This benchmark asked a harder
question: **what happens when the PM gives a plausible but wrong account of the project?**

## Method (v1.0.0)

1. **Simulated PMs, real evidence.** Two fictional PMs answered the intake. The bearing was
   backdated to the day an evaluation of the real project was written, so the checkpoint is judged
   against the **real** commits made in the next five days (11 commits) and the real code state.
2. **Seeded defects.** The worst-case answers contained planted misfilings, gaps, boundary failures,
   and tensions; the best case had a few mild ones. Detection is counted against the seeds.
3. **Hook measured, not simulated.** `hooks/watchman.sh` was run on both logbooks.
4. **Drift probes.** Four prompts with a known correct call were judged under each bearing.

> **Bias warning.** In the v1.0.0 run the same model played the PM and the skill, and planted the
> defects it then found. Seed-detection rates are an upper bound. The informative results are what
> the procedure *cannot* catch by construction, the checkpoint verdicts on real git evidence, and
> the hook measurements. See *Protocol for future benchmarks* below.

## Results on v1.0.0

### Intake

| Metric | Best case | Worst case |
|---|---|---|
| Question rounds to a confirmed bearing | ~4 | ~11 |
| Boundary failures caught / seeded | 0 / 0 | 4 / 4 (in scope, evaluable, consistent, ethics) |
| Misfilings caught / seeded | 1 / 1 | 7 / 7 |
| Tensions surfaced / seeded | 2 / 2 | **5 / 6** |
| Criteria · evaluable · tied to objective | 5 · 5 · yes | 2 · 1 · weakly |
| Accepted risks carried into the bearing | 1 | 4 |

**The miss that matters.** The worst-case PM described the system as "working, just looking old".
The project's own evaluation said it was live with a **NO-GO verdict and open critical/high security
findings**. v1.0.0 built the bearing only from the conversation, so this contradiction was never
seen. The bearing was **internally consistent but wrong about the project**, and it passed every
intake check.

### Checkpoint on real evidence (5 days, 11 commits later)

| | Best case | Worst case |
|---|---|---|
| Verdict | Drifting — correct (≈4 of 11 commits were features outside a remediation bearing) | Drifting — **right verdict, inverted reason**: the work moved *toward* the real problem and *away from* a wrong bearing |
| ⚠️/❌ rows with concrete evidence | 6 / 6 | 4 / 4 |

### Per-prompt drift probes

| Probe (generalized) | Correct call | Best bearing | Worst bearing |
|---|---|---|---|
| Upgrade a dependency with a published CVE | on path | silent ✅ | **flags as drift ❌** (false positive) |
| Restyle dashboard cards | drift during blocker work | flags ✅ | silent ❌ |
| Add an optional data-export format | drift (optional later phase) | flags ✅ | flags ✅ |
| Move uploads to an external cloud host | breaks data rules | flags ✅ | **silent ❌** — the data risk sat in Relations / Boundary notes, which v1.0.0 did not inject |

**Score:** best 4/4, worst **1/4**. Under a wrong bearing the watchman was a liability until the
first checkpoint, 5 days later.

### Findings from the real intake (not simulated)

1. **Fit needs the scope first.** A lens was picked before the scope was known, so the Fit check
   had nothing to check against.
2. **No floor on criteria.** The PM kept 1 of 4 criteria; nothing required one to measure the
   objective, so checkpoints could not measure progress.
3. **Friction.** Three question rounds were spent on the Standard alone.

## What changed in v1.1.0

Three layers, because no single check can catch a bearing that is wrong only in someone's head.

| Layer | Change | Fixes |
|---|---|---|
| Prevent | **Scope line + evidence scan** before the Standard; drafts from evidence; every PM-vs-evidence contradiction resolved or explicitly accepted | The structural miss; Fit without scope; friction |
| Prevent | **Objective anchor required** (explicit opt-out recorded) | Criteria with no floor |
| Detect | Checkpoint evaluates **work vs bearing** *and* **bearing vs reality**; new verdict **Bearing in question** | "Right verdict, inverted reason" |
| Detect | **Shakedown cadence** (default every 3 commits or 2 sessions; `/configwatch` to change) | 5-day detection lag |
| Contain | Status **under review** pauses drift flags until `/fixwatch` | The liability window |
| Hook | Injects Scope + **limits & accepted risks**; strips intake annotations | The silent external-host probe; noise |

## Results on v1.1.0

### Headless evals on synthetic fixtures

| Eval | Expectation met | Transcript |
|---|---|---|
| checkwatch #5 — consistent-but-wrong intake | 6 / 7 fully, 1 partly: scanned docs first, evidence card, 4 contradictions side by side, resolve-or-accept required, Fit failed for a one-criterion rubric; the objective anchor was left as a placeholder until the objective is confirmed (partial) | [run](runs/2026-11-25-checkwatch-eval5.md) |
| checkwatch #8 — checkpoint on a wrong bearing | 5 / 5: two-direction report, verdict *Bearing in question*, asked before marking under review, proposed `/fixwatch` without applying it | [run](runs/2026-11-25-checkwatch-eval8.md) |

### Drift probes re-run (real headless sessions)

| Probe | Bearing | v1.0.0 | v1.1.0 |
|---|---|---|---|
| Move uploads to an external cloud host | worst case | silent ❌ | **flags** — cites personal field data leaving the institution (from the injected accepted risks) ✅ |
| Upgrade a dependency with a published CVE | worst case, *under review* | false drift flag ❌ | **no false flag** ✅ |
| Restyle dashboard cards | worst case, *under review* | silent | silent — neutral: under review there is no trusted bearing to flag against |

Not re-run: the intake simulation and the full probe matrix under a corrected bearing. The two
headless evals above replace the simulated worst-case intake for the structural miss.

### Hook tests

`bash tests/watchman.test.sh`: **58 passed, 0 failed** (24 in v1.0.0), also under `LC_ALL=C`.

## Hook time per prompt

Measured with `tests/bench_hook.py`: wall time from process start to exit for one
`UserPromptSubmit` call, 300 runs per row, on an Intel Core i7-12650H, Linux 7.0, GNU bash 5.2.21,
mawk 1.3.4, git 2.43.0. Tokens ≈ characters / 4.

**Public fixtures** (reproducible from this repo):

| Logbook | Hook | Median (ms) | p95 (ms) | Injected chars | ≈ tokens |
|---|---|---|---|---|---|
| none | v1.0.0 | 1.8 | 2.4 | 0 | 0 |
| none | v1.1.0 | 2.7 | 4.9 | 0 | 0 |
| v1.0 format (composting) | v1.0.0 | 7.5 | 11.5 | 1,215 | 303 |
| v1.0 format (composting) | v1.1.0 | 7.7 | 12.0 | 1,432 | 358 |
| v1.1, no git | v1.0.0 | 7.5 | 10.5 | 1,034 | 258 |
| v1.1, no git | v1.1.0 | 10.2 | 18.0 | 1,296 | 324 |
| v1.1, git, 12 commits since checkpoint | v1.0.0 | 8.0 | 12.2 | 1,034 | 258 |
| v1.1, git, 12 commits since checkpoint | v1.1.0 | 11.1 | 21.3 | 1,296 | 324 |
| v1.1, under review | v1.1.0 | 6.9 | 11.6 | 493 | 123 |

**Benchmark logbooks** (private, anonymized):

| Logbook | Hook | Median (ms) | p95 (ms) | Injected chars | ≈ tokens |
|---|---|---|---|---|---|
| best case | v1.0.0 | 8.0 | 12.8 | 2,134 | 533 |
| worst case | v1.0.0 | 7.8 | 11.9 | 1,617 | 404 |
| best case + Status, git | v1.1.0 | 11.4 | 21.1 | 2,589 | 647 |
| worst case + Status, git | v1.1.0 | 10.7 | 17.0 | 2,236 | 559 |
| worst case, under review | v1.1.0 | 6.2 | 12.5 | 486 | 121 |

**Reading:** v1.1.0 adds about 3 ms per prompt (git count + session state) and ≈ 60–110 tokens
(Scope + limits digest). The first v1.1.0 draft took ≈ 25–29 ms because it forked ~20 helper
processes; merging the logbook parsing into one `awk` pass and using bash built-ins brought it to
the figures above. *Under review* is cheaper than normal operation because the bearing is not injected.

## Protocol for future benchmarks

To remove the self-grading bias of the v1.0.0 run:

1. **Fixtures with ground truth.** A small project folder per case, whose documents encode the
   truth (e.g. an evaluation with a NO-GO), plus a hidden `seeds.json` listing the defects.
2. **Separate roles.** One session plays the PM from a persona card and never sees the seeds; the
   skill under test runs in a fresh headless session (`claude -p --plugin-dir`); a third session
   grades the transcript against `evals.json` expectations and the seeds.
3. **Repeat.** At least 3 runs per case; report pass rates and variance, not single runs.
4. **Measure the hook** with `tests/bench_hook.py` on every release, on the public fixtures.
5. **Keep real-project runs private.** Publish only anonymized summaries.
