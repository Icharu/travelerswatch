# Standards — modes and boundary checks

The Standard is what the work will be judged against. It is set after the one-line **Scope** and
the evidence scan (step A0) and before the four sections: Fit can only be judged once you know what
the bearing will steer, and the Standard then decides what "good" means for every later evaluation.

## The three modes

| Mode | What to ask | What to record |
|---|---|---|
| **Lens preset** | "Which field fits best? Project management (default), research, software, data science — or none of these?" Then show the lens's default criteria and ask which to keep, drop, or add. | Lens name + final criteria list |
| **Free-text rubric** | "List the criteria you want the work judged by. Each should be something we could check." | The criteria as written, after the boundary check |
| **Named external standard** | "Which standard or framework? Which parts of it apply to this project?" | Name, version if known, the parts in scope, and the boundary notes |

A user may combine a lens with extra rubric items. Record the mode as `lens preset + rubric`.

## Boundary check — run on every standard

| # | Check | Passes when | Typical failure | What to say |
|---|---|---|---|---|
| 1 | **Fit** | The standard is meant for this kind of work, field, **and the Scope line** — checked against the evidence card, not the lens name alone. | A medical-device quality standard used for a marketing campaign; a Research lens when the Scope is "platform hardening only". | "This standard governs X; your scope is Y. The closest fit is Z." |
| 2 | **Evaluable** | Each criterion can be checked against evidence (a file, metric, decision, date). | "The project should be excellent." | "How would we see that? e.g. 'stakeholder sign-off on the scope document'." |
| 3 | **Consistent** | Criteria do not contradict each other or the Constraints. | "Ship in two weeks" + "full external audit before release" with a one-month audit lead time. | Name both criteria and ask which wins. |
| 4 | **In scope** | Judging it does not require a certified human role. | "Confirm we are GDPR-compliant." | "I can check this against the parts of the regulation you name, but I can't certify compliance — that needs a qualified reviewer." Record under *Boundary notes*. |
| 5 | **Rights** | Using it does not require reproducing protected text. | Asking Claude to paste a paid standard's clauses into the logbook. | Evaluate from general knowledge of the standard; reference clause numbers only; tell the user. |
| 6 | **Ethics & safety** | The criteria do not reward harm, deception, or discrimination. | "Maximize sign-ups by hiding the cancellation option." | Decline that criterion, say why in one line, and offer a legitimate alternative. |

### Handling a failure

1. Name the check that failed and the exact criterion.
2. Propose the closest standard or rewording that passes.
3. Continue only when the user accepts the fix, or accepts the limit — then write the limit under
   *Boundary notes* so later checkpoints do not evaluate beyond it.
4. Check 6 is not negotiable: the criterion is dropped, not recorded as a limit.

## The objective anchor (required)

At least one criterion must measure progress toward the **Final objective**. Mark it in the logbook
as `**Objective anchor:** …`. Without it, checkpoints can say whether the work is tidy but not
whether it is getting anywhere.

- The anchor is checked in step A3, once the Final objective is known. If no criterion anchors it,
  propose one built from the objective ("C-1 and H-1…H-7 closed and verified by 2026-12-15").
- The PM may **opt out explicitly**. Record `Anchor opt-out: progress toward the objective is not
  measured` in *Boundary notes*; every checkpoint report then says so.
- If the PM trims criteria to fewer than two, say what the remaining set can and cannot detect.

## Writing good criteria

- One idea per criterion.
- Start with what can be observed: "A written scope statement approved by the sponsor", not
  "Scope is clear".
- Three to eight criteria is usually enough; more becomes noise in every report.
