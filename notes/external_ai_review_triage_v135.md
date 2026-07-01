# External AI review triage v135

Date: 2026-07-01

Scope: triage the fifth external review batch after the first public GitHub push.
The review correctly identified several remaining arXiv-facing risks, but also
included a few format suggestions that should not be followed mechanically.

## Addressed now

1. Retitled the manuscript to `Observability of Hidden-Sector Limiting Speed
   Scales: No-Go Results and Interface Phenomenology`, which is clearer than
   the internal C-D working title.
2. Replaced the draft-date title block by `Prepared: 1 July 2026` and added
   a concise keyword line.
3. Compressed the abstract to 158 words and moved example detail out of the
   abstract.
4. Added a dedicated discussion of spin and internal degrees of freedom. The
   no-go hierarchy is now explicitly a spacetime-calibration statement; spinor
   and internal-sector maps require principal-symbol/EFT matching.
5. Rewrote the causal-ordering paragraph as a sufficient global-time condition:
   if every allowed propagation segment increases \(T\) and every conversion
   preserves or increases \(T\), controllable closed causal curves are excluded
   inside that model class.
6. Added a non-Abelian holonomy diagnostic based on the conjugacy class of
   \(U_\gamma={\cal P}\exp\oint_\gamma{\cal A}\).
7. Added a compact recast dictionary linking C-D escape routes to SME,
   photon/paraphoton, clock-network, and GW170817-style constraint channels.
8. Strengthened Appendix D with a visible-sector naturalness inequality
   \(g^2|\xi|/(16\pi^2)\lesssim c_{\rm max}\), with explicit caveats.
9. Moved the public repository URL into the interface discussion and shortened
   the declaration block.
10. Adjusted LaTeX margins to keep the strengthened manuscript at 20 pages
    without creating a nearly blank final page.

## Not adopted as stated

1. PACS numbers were not added. PACS is not an arXiv-required metadata field,
   and forcing it into the manuscript would add outdated clutter.
2. The paper does not add several new figures. The requested heat maps and
   phase-offset figures would require a real data-facing model; adding toy
   plots now would overstate the phenomenology.
3. The reference style was not manually rewritten to force journal
   abbreviations or arXiv identifiers into every bibliography item. The source
   BibTeX contains arXiv identifiers and passes the reference audit.

## Still journal-level work

1. A full four-dimensional photon or fermion portal calculation with spin,
   polarization, angular incidence, gauge constraints, and multichannel
   unitarity.
2. A portal-specific SME dictionary and numerical bound table, rather than
   the present schematic matching.
3. A technically natural UV completion or a clear sequestering/symmetry
   mechanism.
4. A data-facing recast using real clock, photon, multimessenger, or SME
   datasets with nuisance modeling.
5. A curved-spacetime/tetrad version of the hierarchy, including relative
   transport and causal structure.
