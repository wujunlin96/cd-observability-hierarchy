# Paper self-review v108

Date: 2026-06-30

Target draft: `draft/main_observability_hierarchy.md`

## Overall verdict

The new draft is substantially healthier than the tower/disformal drafts because it has a clear negative theorem backbone. It is still not publication-ready. It is a defensible preprint skeleton for a short theoretical/classification paper.

## Major rejection risks

| Risk | Severity | Why it matters | Required response |
|---|---:|---|---|
| Contribution may be judged "obvious representation theory plus known escapes" | High | The linear theorem is elementary and the escape classes are known | Emphasize hierarchy, nonlinear point-map no-go, and flat-connection no-go as a package; avoid claiming each component is individually new |
| Nonlinear point-map theorem assumptions may be attacked | High | Smooth, local, finite, \(V\to V\), no background tensors are strong assumptions | State assumptions sharply and list excluded cases as escape hatches |
| Relative-connection route may collapse into Weyl/nonmetricity | High | Scale holonomy and second-clock effects are old | Keep it as relative hidden-sector calibration; require portal suppression and distinct morphology |
| Interface model is too toy-like | Medium-high | 1D scalar wall is not a real astrophysical model | Present it only as a worked escape example; add causality, wall-frame, and field-theory caveats |
| No direct experimental prediction yet | Medium-high | A theory paper can survive, but weaker without forecast | Add parameter-space figure and later choose FRB echo or clock-network as first forecast |
| Bibliographic boundary must be exact | Medium | Misstating neighboring literature would damage credibility | Keep claim-evidence audit; no novelty claim without citation or theorem |

## Five-dimension self-review

### 1. Contribution

Status: needs revision.

The contribution is not "two speeds exist." The contribution is the observability hierarchy. This is meaningful only if the draft makes the sequence of erasures and escape assumptions unmistakable.

Immediate fix:

- Add a concise theorem summary box or table in the paper.
- Keep "not evidence for D world" language.

### 2. Writing clarity

Status: pass with minor revision.

The draft now has a readable flow: definitions, no-go hierarchy, protection principle, escape table, interface example, literature boundary. It still needs tighter theorem numbering and more careful use of "exact relativity."

Immediate fix:

- Rename section headings to "Theorem 1/2/3" or add theorem labels.
- Add one sentence distinguishing observer covariance from particle/background Lorentz breaking.

### 3. Experimental strength

Status: weak by design.

The paper is not empirical. It has a calculable toy model and a new figure but no data recast or forecast. This is acceptable only for a short theory/classification preprint.

Immediate fix:

- Say explicitly that Figure 1 is a proof-of-principle calculational diagnostic, not an exclusion.

### 4. Evaluation completeness

Status: needs revision.

The no-go claims have symbolic checks and the interface has numerical checks, but the draft does not yet include a reproducibility appendix.

Immediate fix:

- Add an appendix or supplementary note listing scripts and outputs.
- Include the flux-conservation error for finite-wall scans.

### 5. Method design soundness

Status: pass with important caveats.

The logic is sound if the assumptions are kept narrow. It becomes unsound if the draft implies the interface toy model is a realistic cosmology or that hidden \(D>C\) propagation is automatically causal.

Immediate fix:

- Add a causality/model-status caveat to the interface section.
- State that \(D>C\) hidden segments require a preferred wall frame or global causal ordering condition.

## Claim-evidence map

| Major claim | Evidence in current work | Status |
|---|---|---|
| Constant Lorentz-compatible maps are scale maps | analytic proof; symbolic commutant dimension = 1 | supported |
| Smooth Lorentz-equivariant point maps preserve null rays | little-group proof; symbolic quadratic/cubic checks | supported with assumptions |
| Flat relative calibration is pure gauge | Poincare lemma / Maurer-Cartan argument | supported with topology assumption |
| Visible relativity must be protected | SME/Data Tables and known constraints | supported as modeling rule |
| Photon portal is constraint channel | Glashow and De Angelis--Pain literature | supported |
| Neutrino portal is crowded by SME/ADR/shortcut literature | cited SME and sterile ADR papers | supported |
| Interface finite wall acts as Fourier filter | transfer-matrix scan and Born formula | supported in toy model |
| The theory predicts real astrophysical echoes | not yet established | not claimed |

## Immediate edits recommended

1. Add theorem labels and a theorem summary table.
2. Add a short observer-covariance vs particle-Lorentz-breaking clarification.
3. Add interface causality/model-status caveat.
4. Add reproducibility paragraph with script paths and flux-conservation result.
5. Keep the observational forecast as future work, not current result.

## Decision

Continue. Do not claim publication-ready yet.

The paper now has a real spine. The next quality jump is not more speculation; it is tightening theorem statements, reproducibility, and limitations.
