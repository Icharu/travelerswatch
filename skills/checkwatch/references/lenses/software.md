# Lens: Software

For building or changing a software product, service, or library.

## How the sections read in this field

| Section | Ask it as |
|---|---|
| Context | Product and users, existing system and architecture, related specs/ADRs/issues, team and ownership |
| Constraints | Deadlines, team size and skills, fixed stack or platform, performance and security requirements, licences, backwards compatibility |
| Problem | The user or system problem today; final objective = behaviour that is shipped and verifiable (acceptance criteria) |
| Tools | Languages, frameworks, libraries, CI/CD, testing approach, hosting, AI tools used in development |

## Default criteria (keep, drop, or add)

1. **Acceptance criteria exist** for the final objective and are testable.
2. **Tests prove behaviour** — the changed behaviour is covered by automated tests that pass.
3. **Fits the architecture** — changes follow the existing patterns or an ADR explains the deviation.
4. **Security basics** — inputs validated, secrets not committed, dependencies reviewed.
5. **Scope per change is small** — work lands in reviewable increments.
6. **Docs match the code** — README / API docs updated where behaviour changed.

## Drift signals

- Refactors or "while I'm here" changes unrelated to the objective.
- New dependencies or frameworks not listed in *Tools*.
- The acceptance criteria are reinterpreted during implementation.
- An AI assistant keeps returning to an approach the team already rejected (the rewinding watch).

## Typical tools

Git and a forge (GitHub, GitLab), issue trackers, CI (GitHub Actions), test frameworks, linters,
containers, cloud platforms, coding assistants.
