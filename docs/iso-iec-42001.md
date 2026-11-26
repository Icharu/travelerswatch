# ISO/IEC 42001 and The Traveler's Watch

> **Disclosure.** The Traveler's Watch (TTW) is **not certified** against ISO/IEC 42001 and makes
> **no claim of conformity** with it. It also **cannot** be certified on its own, because the
> standard certifies an *organization's* management system, not a tool. This page explains what the
> standard asks of an organization, then shows what TTW covers, what it covers only in part, and
> what it does not cover at all.

**How to read this page.** It is written from general knowledge of the published standard,
ISO/IEC 42001:2023. No text of the standard is reproduced; requirements are paraphrased and named by
clause or control group only. The standard is sold by ISO and national standards bodies. If you
need to rely on the details, read the standard itself and consult a qualified auditor.

## 1. What ISO/IEC 42001 is

ISO/IEC 42001 is the international standard for an **AI management system** (AIMS): the policies,
roles, processes, and records an organization uses to develop, provide, or use AI systems
responsibly. It follows the same high-level structure as other ISO management system standards
(such as ISO 9001 or ISO/IEC 27001), so it can be combined with them.

- **Who it is for:** any organization that develops, provides, or uses AI systems, of any size.
- **Who certifies:** an accredited third-party certification body, after auditing the
  organization's whole AIMS.
- **What gets certified:** the organization (within a defined scope), never a single product,
  plugin, or skill.

So the honest question for a tool like TTW is not "is it certified?" but "can it help an
organization meet some of the requirements, and which ones?"

## 2. What it asks of an organization

### Clauses 4–10: the management system

| Clause | In plain words, the organization must… |
|---|---|
| **4 Context** | Understand its situation, the interested parties and what they need, decide the scope of the AIMS, and decide its role with AI (developer, provider, user…). |
| **5 Leadership** | Have top management commit to the AIMS, set an **AI policy**, and assign roles, responsibilities, and authority. |
| **6 Planning** | Assess and treat **AI risks**, carry out **AI system impact assessments** (effects on people and society), set **AI objectives**, and plan changes. |
| **7 Support** | Provide resources and competent people, make people aware of the policy, plan communication, and control **documented information**. |
| **8 Operation** | Plan and control the processes, control planned changes, and carry out the risk assessment, risk treatment, and impact assessment in practice. |
| **9 Performance evaluation** | Monitor, measure, analyse, and evaluate; run **internal audits**; hold **management reviews**. |
| **10 Improvement** | Improve continually; handle nonconformities with corrective action. |

### Annex A: reference controls

Annex A lists controls the organization chooses from (and justifies its choices in a statement of
applicability). They are grouped by objective:

| Group | Topic |
|---|---|
| **A.2** | Policies related to AI |
| **A.3** | Internal organization: roles, responsibilities, and reporting concerns |
| **A.4** | Resources for AI systems: data, tooling, computing, people |
| **A.5** | Assessing the impacts of AI systems on individuals, groups, and society |
| **A.6** | The AI system life cycle: requirements, design, verification and validation, deployment, operation and monitoring, technical documentation, event logs |
| **A.7** | Data for AI systems: acquisition, quality, provenance, preparation |
| **A.8** | Information for interested parties: documentation for users, reporting, incidents |
| **A.9** | Use of AI systems: responsible use, objectives, intended use |
| **A.10** | Third-party and customer relationships: suppliers, customers, shared responsibilities |

Annex B gives implementation guidance for these controls; Annex C lists possible AI-related
objectives and risk sources (for example accountability, fairness, privacy, robustness, safety,
security, transparency and explainability); Annex D discusses use across domains and sectors.

## 3. TTW against the requirements

TTW is a method-driven evaluation skill for **one project**, used between a model and a person. It
is not an organization and not an AIMS. Each row below says what TTW covers and what it does not,
and links to where you can check it.

**Legend:** ✅ supports at project level · ◐ partial: helps, but far from what the standard asks ·
— not covered

### Clauses

| Clause | TTW | What it covers | What it does not cover | Check it |
|---|---|---|---|---|
| 4 Context | ◐ | The bearing records Scope, Context, stakeholders, and current state **for one project**, grounded in the project's evidence. | Organization-wide context, the AIMS scope, the organization's role with AI. | [checkwatch](../skills/checkwatch/SKILL.md) Part A |
| 5 Leadership | — | A human-in-the-loop principle for TTW's own use. | An AI policy, management commitment, organizational roles. | [ADR 0004](adr/0004-human-in-the-loop.md) |
| 6 Planning | ◐ | Project risks and accepted risks (Relations), limits (Boundary notes), a measurable Final objective with an objective anchor. | An AI risk assessment method, risk treatment plans, **AI system impact assessments**, AI objectives for the organization. | [relations](../skills/checkwatch/references/relations.md), [standards](../skills/checkwatch/references/standards.md) |
| 7 Support | ◐ | **Documented information**: the logbook is versioned in git, its history is append-only, and every change has a reason and a PM confirmation. | Resources, competence, awareness, a communication plan. | [logbook template](../skills/checkwatch/assets/WATCH.md), [ADR 0002](adr/0002-committed-logbook.md) |
| 8 Operation | ◐ | **Control of planned changes**: every course change is proposed as a diff, its ripple is shown, and the PM confirms it before it is applied. | Operational control of AI systems; carrying out AI risk and impact assessments. | [fixwatch](../skills/fixwatch/SKILL.md) |
| 9 Performance evaluation | ◐ | **Monitoring** at project level: the watchman on every prompt, two-direction checkpoints, a Checkpoint log, and a post-project review. | Internal audit (TTW's reviews are self-assessments, not independent audits); management review. | [checkwatch](../skills/checkwatch/SKILL.md) Parts B–C |
| 10 Improvement | ◐ | *Bearing in question* → `/fixwatch` with the *misinterpretation* or *evidence contradiction* trigger; lessons tied to evidence in the post-project review. | A nonconformity and corrective-action process for an organization; continual improvement of an AIMS. | [ADR 0005](adr/0005-post-project-review.md) |

### Annex A control groups

| Group | TTW | What it covers | What it does not cover |
|---|---|---|---|
| A.2 Policies | — | — | Any AI policy. |
| A.3 Organization | ◐ | One clear allocation of authority: the model proposes, the PM confirms. A private channel to report concerns about TTW itself ([SECURITY.md](../SECURITY.md)). | Organizational roles and a channel for reporting concerns about your AI systems. |
| A.4 Resources | ◐ | The *Tools* section names each tool and why it fits. | Inventories of data, computing resources, and people for AI systems. |
| A.5 Impact assessment | — | — | Impact on individuals, groups, and society. TTW does not assess this. |
| A.6 Life cycle | ◐ | For **TTW itself**: design decisions (ADRs), tests, evals, and a benchmark with its bias stated. In your project: a record of decisions (Path log) and checkpoint verdicts (Checkpoint log). | Life-cycle processes for *your* AI systems. TTW's logs record human decisions, not an AI system's event logs. |
| A.7 Data | — | TTW stores no data of its own and copies no secrets or personal data into the logbook. | Data quality, provenance, and preparation for AI systems. |
| A.8 Information for interested parties | ✅ | For **TTW itself**: what it is and is not, limits, methods, benchmark, data handling, prohibited uses, governance. | Information about *your* AI systems for *your* users. |
| A.9 Use of AI systems | ◐ | Intended use, human-in-the-loop by principle, prohibited uses, and a refusal to run the bearing in a fully automated session. | Your organization's processes and objectives for responsible AI use. |
| A.10 Third parties | ◐ | Discloses that TTW runs inside Claude Code and sends its output to the model provider as part of the prompt. | Supplier management, contracts, shared responsibilities. |

## 4. The three principles behind this page

| Principle | How this page applies it |
|---|---|
| **Transparency** | It starts with what TTW is *not*. A row is marked ✅ only where TTW has a concrete mechanism you can open and read; everything else is ◐ or —. |
| **Verifiability** | Every "covers" claim links to a file in this repository. The hook's behaviour is covered by `tests/watchman.test.sh`; the skills' behaviour by `skills/*/evals/`. Neither is a controlled study of drift reduction ([methods: limits](methods.md#limits-of-this-evidence)). |
| **Feasibility** | It claims only what a solo-maintained, open project can do: support one project's records and decisions. It does not promise what only an organization can do: policy, audits, impact assessments, certification. |

## 5. If your organization is pursuing ISO/IEC 42001

TTW can be one small piece of evidence inside a larger system, for example:

- the logbook as **documented information** on a project's objectives, constraints, and decisions;
- the Path log as a record of **controlled changes**, each with a reason and a named approver;
- the Checkpoint log and post-project reviews as **monitoring** records for that project.

You would still need everything marked — above, and most of what is marked ◐: an AI policy, roles,
risk and impact assessment methods, internal audits, management reviews, supplier controls, and a
certification body. Do not present TTW output as evidence of conformity on its own; TTW's skills are
written to refuse to certify compliance ([checkwatch rules](../skills/checkwatch/SKILL.md#rules)).

---

*Last reviewed: 2026-11-25, against the TTW version in this repository. If ISO/IEC 42001 is revised,
this page must be reviewed again.*
