# Headless run — checkwatch eval 5 (consistent-but-wrong intake)

Date: 2026-11-25 · plugin v1.1.0-dev · fixture: `skills/checkwatch/evals/files/fixture-live-blockers` · one round, no writes.

---

Intake round 1 for fieldnotes. There is no `.watch/WATCH.md` yet, so this is a first intake. It's headless, so I wrote no files.

**Scope (from your line):** fieldnotes, the lab website. This bearing would steer the landing-page redesign and a new performance dashboard.

## Evidence card
Sources: `README.md`, `docs/evaluation/2026-11-10-evaluation.md`, `docs/adr/0001-stack-and-hosting.md`. There's no git history (not a repo) and no issues or roadmap.

| Topic | Evidence says | Source |
|---|---|---|
| Current state | Live on the university's server since 2026-11-10. The evaluation verdict is **NO-GO for public release**. | README, evaluation §Verdict |
| Open blockers | 3 High (authentication secret, admin account never rotated, database exposed to the network) and 1 Medium (collector names shown to anonymous users) | evaluation table |
| Documented priority | "Close blockers, not new features." UI work and dashboards come in **phase 3**, after phases 1 and 2. | evaluation §Recommended phases |
| Fixed choices | Spring Boot + Angular + MySQL on the **university-operated server**. Field data includes personal data and **must not be hosted outside the institution**. Production changes need an IT ticket (about 3 working days). | ADR 0001 |
| Referenced works | Evaluation of 2026-11-10; ADR 0001 | docs/ |

## Where your answers contradict the evidence
Each of these has to be **resolved** or **explicitly accepted** before I can confirm a bearing.

| # | You say | Evidence says | Source |
|---|---|---|---|
| 1 | "It works, it just looks old" | Live but NO-GO, with 3 High and 1 Medium findings open | evaluation |
| 2 | Next work: redesign + dashboard | Close the blockers first; UI and dashboards wait for phase 3 | evaluation §phases |
| 3 | Tool: **Vercel** | Hosting must stay on the institution's server | ADR 0001 |
| 4 | Tool: **Firebase Auth** | Personal data must not leave the institution. Firebase would keep lab members' identities on Google's servers and replace auth in a Spring Boot stack whose auth is itself an open High finding. | ADR 0001, evaluation H-1 |

## Standard: free-text rubric, boundary check
Your rubric has one criterion: "the advisor approves the redesign."

- **Evaluable:** ⚠️ It passes only if the approval is written down and dated, and the advisor is named by role.
- **Fit:** ❌ It covers the redesign but not the dashboard, the data-residency rule or the open blockers.
- **One criterion:** it can tell us the advisor liked the look. It can't tell us whether we leaked personal data, broke ADR 0001 or shipped on top of a NO-GO.
- **Objective anchor:** ⚠️ Sign-off is a gate at the end, not a measure of progress.
- **In scope:** I can check data handling against ADR 0001. I can't certify data-protection compliance; that needs your institution's data-protection officer.

**Proposed rubric (draft):**
1. Written, dated advisor approval of the landing-page redesign.
2. Evaluation findings H-1 to H-3 closed and verified on the production server before any UI change ships.
3. No personal data (collector names, exact coordinates) visible to anonymous users, including on the new landing page and dashboard (closes M-1).
4. All hosting and auth stay inside the institution under ADR 0001, unless a new ADR replaces it.
5. The dashboard answers one named question for one named audience (we define this below).
6. **Objective anchor:** to be set once the final objective is confirmed.

## Section drafts (for you to correct)
These follow the hint card: Context is *where the work lives*, Constraints are *what limits you*, Problem is *what's wrong and what done looks like*, and Tools are *what you'll use and why*.

- **Context (draft):** A university lab's field-survey platform (sites, species counts, collectors, coordinates) with a public species catalogue. Live since 2026-11-10 with a NO-GO evaluation. Referenced works: the 2026-11-10 evaluation and ADR 0001.
- **Constraints (draft):**
  - Hosting and personal data stay on the university server (ADR 0001).
  - Production changes go through an IT ticket, about 3 working days each.
  - Stack is fixed: Spring Boot + Angular + MySQL.
  - Deadline: *unknown*.
  - Team size: *unknown*.
- **Problem (draft):**
  - *Original problem:* the public landing page looks dated, and *[gap]* someone can't see *[gap]*. "Add a dashboard" is a solution, so I need the problem behind it.
  - *Final objective:* *[gap]*. It needs to be something we can observe.
- **Tools (draft):**
  - Vercel: it has no stated reason and conflicts with ADR 0001.
  - Firebase Auth: same issue.
  - The existing Angular and Spring Security on the university server are the in-bounds alternative.

**Misfiling note:** "Redesign the landing page and add a dashboard" is a solution, so it belongs under Problem only once we know what's wrong today.

## Questions for this round (answer any or all)
1. **State:** Are H-1 to H-3 and M-1 still open, or were they closed after 2026-11-10? If closed, where is the proof?
2. **Priority:** Should the bearing steer toward blockers first, then redesign (phases 1–3)? Or redesign only, recording contradictions #1 and #2 as accepted?
3. **Vercel and Firebase:** Which do you want?
   - (a) Drop them and stay on the university stack.
   - (b) Vercel only for a static landing page that holds no data. Firebase is still out.
   - (c) Keep both and write a new ADR that replaces ADR 0001. That needs the institution's approval.
4. **Dashboard:** Whose "performance" do you mean: the website's (speed, uptime) or the lab's (surveys, species records)? Who reads it, and what decision does it help them make?
5. **Standard:** Do you accept the proposed rubric, and which items would you keep or change? How will the advisor's approval be recorded?
6. **Limits:** Is there a deadline, and who is on the team?

I'm stopping here as asked: no `.watch/` files or `.gitignore` changes were written.
