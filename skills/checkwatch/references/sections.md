# The four sections — hints and misfiling rules

## Hint card (show this to the user with the question)

| Section | Answer this | Belongs here | Does **not** belong here |
|---|---|---|---|
| **Context** | *Where does this work live?* | Field or domain, stakeholders, current state, **referenced works** (papers, prior projects, documents, decisions it builds on) | Limitations (→ Constraints), what you want to achieve (→ Problem) |
| **Constraints** | *What limits you?* | Time, budget, people, skills, technology already decided, regulation, data access, organizational rules | Background facts (→ Context), wishes (→ Problem), tool preferences without a limit behind them (→ Tools) |
| **Problem** | *What is wrong today, and what does done look like?* | **Original problem** (the situation before any solution) and **final objective** (observable end state) | Solutions or tools ("build an app" is a means, not a problem), constraints |
| **Tools** | *What will you use, and why does it fit?* | Software, methods, frameworks, services, techniques — each with a reason tied to Context or Constraints | The goal itself, mandatory platforms that are really constraints (record those in Constraints too) |

## Misfiling signals

| If the user writes… | It is probably… | Example |
|---|---|---|
| "only", "at most", "can't", "must use", "deadline", "budget", numbers of people/money/time | **Constraint** | "We only have two developers" written under Context |
| "we want to", "the goal is", "so that", success metrics | **Final objective** | "Increase retention by 10%" written under Context |
| "currently", "users complain", "it takes too long" | **Original problem** (or Context if it is just background) | "Reports take 3 days" written under Tools |
| a product, library, method, or service name | **Tool** | "Jira" written under Problem |
| "based on", "following", citations, links, prior projects | **Referenced works** in Context | "As in the 2024 pilot" written under Constraints |
| "build X", "implement Y" written as the problem | A **solution** — ask for the problem behind it | Problem: "build a dashboard" → "what decision is hard to make today without it?" |

Say each move in one line: *"'Budget is 20k' → Constraints: it limits what we can do."*

## Quality checks per section

- **Context:** names a field, and lists at least one referenced work or says explicitly "none yet".
- **Constraints:** each item is concrete (a number, a date, a named rule). Vague items ("limited
  time") get a follow-up question.
- **Problem:** the original problem does not mention a solution; the final objective is observable.
  If the objective cannot be checked, ask: *"How will you know you are done?"*
- **Tools:** every tool has a "why". A tool with no reason is a candidate for removal or a hidden
  constraint (e.g. "the company mandates it").

## When the user is unsure

Offer a draft based on what they already said, clearly marked as a draft, and ask them to correct it.
Never fill a section silently.
