# ADR 0004 — Human in the loop by principle: no fully automated sessions

- **Status:** Accepted
- **Date:** 2026-11-25
- **Extends:** ADR 0001 (per-prompt watch), ADR 0003 (evidence-grounded bearing)
- **Erratum (2026-11-26, v1.2.3):** the Context below says "the literature". The support is one
  review, Adamantiadou & Tsironis (2025), as summarized by Koshman & Zubkova (2026); see
  [methods §5](../methods.md#5-why-a-human-stays-in-the-loop). "Automating it is where AI helps
  most" is the maintainer's judgement, not a cited finding. The decision is unchanged.

## Context

TTW already said "only the PM confirms" a course change. It did not say what to do when the PM
*asks* Claude to take that role: "decide for me", "auto-approve future changes", "run this without
asking". A user who has seen TTW automate a lot of work may reasonably think it is a fully automated
tool. It is not, and the skills must not drift into becoming one.

Two kinds of work happen in a TTW session:

- **Direction**: setting, changing, closing, or reopening the bearing; accepting a risk or a
  contradiction. This depends on judgement about a changing project, which the literature says
  AI models are not yet adaptable or validated enough to own (Koshman & Zubkova, 2026; see
  [methods §5](../methods.md#5-why-a-human-stays-in-the-loop)).
- **Execution inside the direction**: coding, evaluating texts against the Standard, gathering
  evidence, drafting reports and diffs. This is often repetitive, and automating it is where AI
  helps most.

## Decision

1. The skills **refuse, by principle, to run the bearing in a fully automated session.** They never
   set, change, close, or reopen the bearing, accept a contradiction, or write a PM confirmation the
   PM did not give, even when asked to. The refusal is one line, says why, and offers an
   alternative.
2. The skills **do automate repetitive work inside the bearing** and bring the result back for the
   PM's decision.
3. This rule is listed in [GOVERNANCE.md](../../GOVERNANCE.md) among the rules no proposal can
   remove.

## Consequences

- New rule in `checkwatch` and `fixwatch`; new eval case (fixwatch #7).
- TTW is slower than an autopilot for decisions about direction, on purpose.
- The rule lives in skill text, so it relies on the model following it. It is tested by evals, not
  enforced by code; the hook only re-states it ("Never edit the bearing sections … without explicit
  PM confirmation").
