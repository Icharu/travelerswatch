# Headless run — checkwatch eval 8 (checkpoint on a wrong bearing)

Date: 2026-11-25 · plugin v1.1.0-dev · fixture: `skills/checkwatch/evals/files/fixture-wrong-bearing` · no writes.

---

## Watch report — 2026-11-25 — Bearing in question

**Standard:** free-text rubric · 2 criteria (objective anchor: advisor approves the redesign in a recorded meeting; admins see API response times on a dashboard)

| Criterion / section | Status | Evidence |
|---|---|---|
| Objective anchor: advisor approves the redesign | ⚠️ | No meeting record in the repo and no git history to show any redesign work. `docs/evaluation/2026-11-10-evaluation.md` puts UI work in phase 3, after the blockers are closed |
| Admin performance dashboard | ⚠️ | No work evidence. The same evaluation says: "Only then: UI work, **dashboards**, exports" |
| Context · Current state ("works, looks old") | ❌ | The evaluation's verdict is **NO-GO for public release**, with 3 High findings open (H-1 placeholder signing secret, H-2 default admin never rotated, H-3 database port exposed) and M-1 open. `README.md` says the site is in production |
| Context · Evidence scanned ("none found") | ❌ | `README.md`, `docs/adr/0001-stack-and-hosting.md` and the 2026-11-10 evaluation are in the project, and the evaluation is dated the same day the bearing was set |
| Tools · Vercel (free hosting) | ❌ | ADR 0001 (Accepted) says the site is deployed on the **university-operated server** and that field data "must not be hosted outside the institution" |
| Tools · Firebase Auth (simpler login) | ❌ | The ADR stack is Spring Boot + Angular + MySQL, kept in-house. The real auth problem is H-1, which means fixing a secret, not changing provider. Moving to Firebase would also put user identities with an outside service |
| Constraints | ⚠️ | Missing: production changes need a university IT ticket (about 3 working days, ADR 0001). "End of semester" has no date |
| Relations · Vercel vs university server (*Accepted risk (PM)*) | ❌ | This was accepted when the logbook says no evidence had been scanned. ADR 0001 treats it as a data-residency rule, not a trade-off a PM can take on alone |
| Boundary · data protection not evaluated | ⚠️ | Leaving out compliance certification is fine. But the project's own evaluation names M-1 (collector names visible to anonymous users). The boundary note can't be used to set that finding aside |
| Problem · Final objective | ⚠️ | The evaluation says "**Close blockers, not new features.**" Both parts of the objective are in its last phase |

**Work vs bearing:** I can't assess this. The project isn't a git repo, there are no commits or changed files since 2026-11-10, and `.watch/.state` records only that day's session. I found no work drifting from the bearing. The problem is the bearing itself.

**Bearing vs reality:** It doesn't hold. The watch was set wrong at the start: the bearing was built on "Evidence scanned: none found", but the project's own documents from that same day contradict it.
- The current state is a NO-GO system in production with High security findings open, not just a site that looks old.
- Both Tools conflict with an accepted ADR on hosting and on where data may live.
- The objective is to build features the project's evaluation says should wait.

**Tensions:**
- The Vercel risk was accepted without its evidence, so it needs to be re-decided.
- M-1 (personal data visible to anonymous users) and the ADR's data-residency rule go beyond what I can rule on. A qualified person, such as the university's data-protection officer or IT, should review them. I'm not certifying compliance either way.

**Next step:** Mark the bearing under review, then run `/fixwatch` with the trigger *misinterpretation* (the evidence existed at intake but wasn't scanned). Likely changes:
- Current state reflects the NO-GO.
- Tools follow ADR 0001.
- The 3-working-day IT-ticket lead time becomes a Constraint, and the semester deadline gets a date.
- The objective is re-sequenced, or a "blockers H-1 to H-3 closed and verified on production" criterion goes ahead of the redesign and dashboard.

---

**Stopped before writing, as asked.** No files were changed. A normal run would make two Status edits in `.watch/WATCH.md`:
1. `Last checkpoint: 2026-11-25 @ —` (no git, so no SHA).
2. Only if you confirm: `Bearing: under review since 2026-11-25 — bearing set without scanning README, ADR 0001 and the 2026-11-10 evaluation; Current state and Tools contradict them`. This pauses drift flags until `/fixwatch` resolves it.

Do you want me to mark the bearing under review?
