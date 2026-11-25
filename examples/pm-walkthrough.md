# Worked example — a municipal composting pilot

An abridged session showing intake, a drift flag, and a course change. Claude's replies are
shortened; the real ones include the hint cards from the skill.

---

## 1. Intake — `/checkwatch`

> **PM:** /checkwatch — we're launching a composting pilot for the city.

**Claude:** No logbook yet, so let's set the bearing. First, the **Standard** — what should this
work be judged against?
1. Lens preset (Project Management is the default)
2. Your own rubric
3. A named external standard

> **PM:** PM lens. Drop "progress is visible", add "residents in both districts were consulted".

**Claude:** Boundary check passed — all criteria can be checked against evidence. Now the four
sections. *(hint card shown)*

> **PM:** Context: city sustainability office, we have only two part-time staff. Problem: build a
> pickup app. Tools: GitHub Projects, Tableau.

**Claude:** A few things to move:
- "only two part-time staff" is a limitation → **Constraints**.
- "build a pickup app" is a solution → what is the **problem** behind it, and what does **done**
  look like?
- **Context** has no referenced works — is there a waste report or earlier pilot this builds on?

> **PM:** Problem: organic waste is ~40% of landfill. Done = divert 25% of household organic waste
> in two pilot districts within 12 months. Reference: City waste characterization report 2025.
> Budget is 20k, launch before March 2027.

**Claude:** How do you see these sections relating? … My view, most serious first:
- **Constraints ↔ Tools** — Tableau needs paid licences; with a 20k budget, is that intended?
- **Problem ↔ Tools** — nothing in Tools reaches residents. How will they sign up?

> **PM:** Drop Tableau. Residents have low internet access — use paper sign-up forms.

**Claude:** *(shows the full bearing)* Apply this bearing? → **PM:** yes.
Created `.watch/WATCH.md` with the first Path log entry. Suggest: `git add .watch && git commit -m "watch: bearing set"`.

---

## 2. Two weeks later — the watchman flags drift

> **PM:** Let's add a smartphone app with gamified recycling points for the whole city.

**Claude:** ⚠️ *Watch: this drifts from **Problem** (two pilot districts) and **Constraints**
(20k budget, two part-time staff) — continue, or `/fixwatch`?*
Here's what a citywide app would involve… *(continues the task)*

---

## 3. Course change — `/fixwatch`

> **PM:** /fixwatch — the sponsor approved moving launch to June 2027.

**Claude:** **Trigger:** new information.

```diff
 Constraints
- Launch before March 2027
+ Launch before June 2027 (sponsor approval, 2026-11-25)
```

**Ripple:** the 12-month objective window now ends June 2028; the PM-lens criterion "objective has a
metric and a date" is still met. No new tensions.

Apply this course change? → **PM:** apply.

Appended to Path log:

```markdown
### 2026-11-25 — Launch moved to June 2027
- **Trigger:** new information
- **Proposed by:** PM
- **Change:** Constraints — launch deadline March 2027 → June 2027
- **Reason:** sponsor approved delay
- **Impact:** objective window ends June 2028
- **PM confirmation:** A.M., 2026-11-25
```

New bearing: *divert 25% of household organic waste in two pilot districts within 12 months of a
June 2027 launch.*
