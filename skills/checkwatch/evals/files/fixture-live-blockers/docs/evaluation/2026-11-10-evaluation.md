# System evaluation — 2026-11-10

## Verdict: NO-GO for public release

The system went live before the blockers below were closed. **Close blockers, not new features.**

| ID | Severity | Area | Status |
|---|---|---|---|
| H-1 | High | Authentication — signing secret left at a placeholder value | Open |
| H-2 | High | Default administrator account never rotated | Open |
| H-3 | High | Database port reachable from outside the server | Open |
| M-1 | Medium | Personal data (collector names) visible to anonymous users in one listing | Open |

## Recommended phases
1. Close H-1…H-3 and verify on the production server.
2. Restrict M-1 behind roles.
3. Only then: UI work, dashboards, exports.
