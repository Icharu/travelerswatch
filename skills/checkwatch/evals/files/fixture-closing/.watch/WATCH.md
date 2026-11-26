# Watch Logbook
<!-- travelers-watch logbook v1.2 · synthetic eval fixture -->

> The bearing for this project. The Checkpoint log and the Path log are append-only history.

## Status
- **Bearing:** confirmed
- **Checkpoint cadence:** every 10 commits or 5 sessions
- **Last checkpoint:** 2027-02-20 @ —

## Standard
- **Mode:** lens preset
- **Name:** Project Management lens
- **Criteria:**
  - **Objective anchor:** households in the two pilot districts divert 25% of organic waste by 2027-03-31
  - Scope changes are proposed, approved, and logged
- **Boundary notes:** No certification of municipal waste regulations.

## Context
- **Field / domain:** municipal composting pilot
- **Stakeholders:** city environment office (sponsor), two neighbourhood associations
- **Referenced works:** City waste report 2025
- **Current state:** pickup running in both districts since January; weekly weigh-ins recorded
- **Evidence scanned:** README, docs/weigh-ins.md

## Scope
The two-district pilot only — not the citywide rollout.

## Constraints
- Budget capped at 20k
- Two part-time staff
- Pilot ends 2027-03-31

## Problem
### Original problem
Organic waste fills 40% of the landfill and households have no separate pickup.

### Final objective
Households in the two pilot districts divert 25% of organic waste by 2027-03-31.

## Tools
- GitHub Projects — task tracking the team already uses
- Shared spreadsheet — weekly weigh-ins

## Relations
- Constraints ↔ Problem: two part-time staff may not cover weekly pickup in both districts. *Accepted risk (PM).*

## Checkpoint log
- 2026-12-10 @ — — On path — pickup routes planned within budget
- 2027-01-15 @ — — Drifting — two sessions spent on a citywide app mock-up
- 2027-02-20 @ — — On path — weigh-ins show 21% diversion, trend rising

## Path log
### 2026-11-25 — Bearing set
- **Trigger:** initial /checkwatch
- **Proposed by:** Claude
- **Change:** bearing established
- **Reason:** project kickoff
- **Impact:** Tools drafted from README; "only two part-time staff" moved from Context to Constraints
- **PM confirmation:** M.R., 2026-11-25

### 2027-01-16 — Pickup moved to fortnightly in district B
- **Trigger:** new information
- **Proposed by:** PM
- **Change:** Constraints — staff cover weekly pickup in district A only
- **Reason:** the accepted staffing risk materialized in January
- **Impact:** objective anchor kept; district B tracked separately
- **PM confirmation:** M.R., 2027-01-16
