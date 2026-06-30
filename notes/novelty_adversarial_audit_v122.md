# Novelty adversarial audit v122

Date: 2026-06-30

Purpose:

Test whether the present manuscript is merely a review or an already-existing theory variant. The standard here is hostile: if a neighboring literature already contains the same conceptual package, the paper should not claim originality.

## Search method

Script:

```text
scripts/audit_novelty_literature_search.py
```

Outputs:

```text
results/novelty_literature_search.csv
results/novelty_literature_search.json
```

Databases queried:

1. arXiv API
2. OpenAlex API
3. CrossRef API
4. Semantic Scholar API

Semantic Scholar returned several HTTP 429 rate-limit errors, so it is treated as partial evidence only. The audit therefore relies mainly on arXiv, OpenAlex, and CrossRef.

Search themes:

1. exact title/framing collision;
2. hidden-sector speed observability;
3. multi-sector limiting speeds;
4. relative calibration and holonomy;
5. hidden cone and portal models;
6. interface/defect echo models;
7. disformal Lorentz-violation neighbors;
8. neutrino altered-dispersion neighbors.

The latest run returned:

```text
rows=167
high_or_medium_collision_candidates=6
exact_title_collision=9
observability_hidden_speed=25
multi_sector_limiting_speed=19
relative_calibration_holonomy=17
hidden_cone_portal=18
interface_echo_speed=25
disformal_lorentz_hidden=29
neutrino_altered_dispersion=25
```

## Manual screening of collision candidates

### Exact title/framing

No direct physics collision was found for the current title or package framing. CrossRef exact-title hits were false positives from unrelated fields, such as workplace observability, transport-sector hierarchy, pipeline detector speed control, or LLM observability.

Conclusion:

> No obvious existing paper was found that already frames "C-D observability hierarchy for multi-sector speed constants" as the central contribution.

This is not a proof of priority. It is evidence that the exact package is not trivially duplicated in indexed search.

### Multi-sector limiting speeds

This is not novel. The search repeatedly returns ordinary Lorentz-violation, SME, superluminal-particle, and multi-speed-sector neighborhoods. This supports the current manuscript's conservative claim that multiple speed parameters themselves are not a contribution.

Conclusion:

> Any novelty claim based only on "there may be two light speeds" should be rejected.

### Hidden-sector speed observability

The closest results are Lorentz-violating electrodynamics, VSL-like models, hidden-sector dark-matter portals, and photon-sector LIV bounds. These do not appear to package the C-D calibration no-go hierarchy, but they occupy the physical effects that a naive C-D model would try to claim.

Conclusion:

> The paper must keep the distinction between hidden speed as internal calibration data and hidden speed as a visible observable.

### Relative calibration and holonomy

Hits are mostly ordinary Lorentz-manifold holonomy, projective equivalence, navigation, or speculative nonstandard papers. They do not obviously treat C-D relative sector calibration as the observable object.

Conclusion:

> Relative holonomy remains a plausible C-D escape class, but it must be presented as adjacent to Weyl/nonmetricity and clock-effect literature, not as a completely new kind of geometry.

### Interface/defect echo

The search did not find a direct same-topic C-D interface result. Hits were mostly unrelated echo or speed/interface terms. The manuscript's finite-wall calculation is still a toy model and should not claim a new scattering formalism.

Conclusion:

> The interface example can serve as a controlled morphology example, not as a discovery channel.

### Disformal and aether-like neighbors

Disformal transformations, null-like disformal geometry, Einstein-aether, and Lorentz-violating gravity are mature neighbors. Search results include disformal geometry and Lorentz-violating gravity papers. This confirms that the representative hidden metric

```text
f_mu_nu = Omega^2 (g_mu_nu - xi u_mu u_nu)
```

cannot be claimed as new.

Conclusion:

> The novelty, if any, is the role of the disformal/aether representative inside a C-D observability hierarchy.

### Neutrino altered dispersion

This area is crowded. arXiv/OpenAlex/CrossRef recover sterile-neutrino altered dispersion and SME-like Lorentz-violating neutrino models. This supports the current decision not to make the neutrino portal the core first-paper claim.

Conclusion:

> A future neutrino paper would need a restrictive low-rank C-D texture and a real recast. It should not be folded into the current no-go/classification manuscript as a strong novelty claim.

## Overall verdict

The current manuscript is not a mere literature review if and only if it keeps the following claim:

> Under exact local Lorentz equivariance, smooth local sector maps, and flat relative calibration, a hidden speed ratio \(D/C\) has no local invariant visible content. Observable C-D physics must identify which no-go assumption fails, and each failure class maps to known constraint literatures.

The paper would become a weak or unpublishable variant if it claimed any of the following:

1. multiple limiting speeds are new;
2. disformal metrics are new;
3. SME-like Lorentz violation is new;
4. photon velocity oscillations are a new C-D prediction;
5. sterile altered dispersion is a new C-D prediction;
6. a finite scalar wall is a realistic detection model.

## Strength of evidence

Evidence for novelty is moderate, not conclusive:

1. No direct title/framing collision was found.
2. Known neighboring literatures cover most components.
3. The surviving contribution is a package: no-go hierarchy, observability definition, protection principle, escape-class map, and one controlled interface example.
4. The strongest original part remains the organization of the C-D idea as an observability theorem rather than a new particle or a new speed parameter.

## Go/no-go decision

Go, but only as a modest theory/classification paper.

Do not market it as:

```text
new light-speed physics
```

Market it as:

```text
a no-go and observability hierarchy for multi-sector speed constants
```

This keeps the work meaningful without overstating it.

