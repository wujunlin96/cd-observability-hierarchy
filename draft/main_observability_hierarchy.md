# Observability of Hidden-Sector Limiting Speed Scales: No-Go Results and Interface Phenomenology

Prepared: 1 July 2026

Keywords: hidden sectors; limiting speeds; Lorentz symmetry; observability; interface phenomenology; Standard-Model Extension

## Abstract

Can a hidden sector with limiting speed scale \(D\) leave an invariant imprint on a visible sector with speed scale \(C\)? We treat this as a calibration problem. Under exact local Lorentz equivariance, ordinary spacetime point maps, and flat relative calibration, \(D/C\) has no local invariant visible content: Lorentz-commuting linear maps are scale maps, smooth equivariant point maps preserve null rays, and flat relative connections have no contractible holonomy. Observable C-D physics must therefore identify the failed assumption: a preferred hidden field, relative curvature or topology, an interface or defect, or a portal-projected effective coefficient. The paper's contribution is a no-go hierarchy and a morphology criterion \({\cal M}_{CD}\) that tests linked delay, conversion strength, coherence cutoff, and possible clock holonomy rather than fitting a lone speed. A one-dimensional interface example shows how finite wall thickness filters conversion through \(k_C-k_D\). The result is a classification and forecast framework, not evidence for a hidden D-sector spacetime.

## 1. Introduction

The phrase "a second light speed" is ambiguous. If two decoupled sectors each define their own clocks and rods, a numerical difference between their internal light speeds can be removed by calibration. If the sectors interact, however, a visible observer may ask whether hidden null propagation can appear as a distinct causal cone, a delayed or advanced echo, a closed-loop phase, or a portal-induced effective-field-theory coefficient.

This paper formulates that question as an observability problem. We call the visible-sector speed scale \(C\) and the hidden-sector speed scale \(D\). The symbols \(C\) and \(D\) are not coordinates or manifold labels, and they do not by themselves denote two visible signal speeds. They denote sectoral calibration data whose physical status depends on the inter-sector map, the existence of portals, and the global structure of the relative calibration.

The main result is negative but useful: exact local relativity erases a local C-D speed ratio. A hidden speed constant becomes visible only when at least one of the assumptions behind this erasure fails. This viewpoint protects the construction from a common mistake: promoting a coordinate or unit convention into new physics.

The work is deliberately narrower than a general Lorentz-violation or bimetric-gravity program. The idea that different sectors may carry different limiting speeds is not new; it appears in Lorentz-violating field-theory and superluminal-particle discussions [@Redigolo2012LorentzViolatingSUSY; @ChashchinaSilagadze2012LightSpeedBarrier]. Local visible-sector Lorentz violation is already systematically parameterized and tightly constrained by the Standard-Model Extension (SME) [@ColladayKostelecky1998SME; @KosteleckyRussell2011DataTablesSME]. Disformal metrics and preferred timelike fields have a long history [@Bekenstein1993DisformalGeometry; @Jacobson2008EinsteinAetherStatus]. Photon velocity oscillations and active-sterile altered-dispersion models already cover important portal phenomenology [@Glashow1998PhotonVelocityOscillations; @DeAngelisPain2002PhotonVelocityOscillations; @KosteleckyMewes2004Neutrinos; @PaesPakvasaWeiler2005ShortcutSterile; @HollenbergPaes2009ADRResonance; @Barenboim2019SterileADRRevisited]. Our goal is not to rename these fields. Our goal is to state what the C-D hypothesis adds before it enters them.

The contribution is an observability hierarchy with three local no-go layers and one diagnostic object. Constant local maps fail to produce a second cone; smooth nonlinear point maps still fail if they remain Lorentz equivariant and lack background tensors; flat relative calibration connections are pure gauge on simply connected regions. Once one of these assumptions is broken, the proposed signal must be tested through the joint morphology vector \({\cal M}_{CD}\), not through a single fitted speed parameter.

### Contribution and Scope

| This paper claims | This paper does not claim |
|---|---|
| \(D/C\) is locally unobservable under exact common Lorentz equivariance, smooth sector maps, and flat relative calibration | Multiple limiting speeds are new |
| C-D observability requires a named failure mode and a constrained morphology vector \({\cal M}_{CD}\) | A visible observer can directly measure a large second photon speed |
| The escape classes are constrained by known SME, disformal, aether, clock, portal, and multimetric literatures | Disformal metrics, SME coefficients, Weyl effects, hidden photons, or multimetric gravity are new by themselves |
| A finite interface gives a calculable coherence filter for one controlled escape route | The toy interface is already a realistic cosmological or laboratory detection proposal |

Throughout the paper, "breaking relativity" means particle or background Lorentz breaking in a sector, not a failure of observer covariance. Equations may still be written covariantly even when a background field such as \(u^\mu\) selects a physical frame.

This distinction is essential. A theory that abandons observer covariance has lost the common language in which different laboratories compare measurements. The C-D route considered here instead relaxes narrower assumptions: exact hidden-sector Lorentz symmetry, smooth global inter-sector calibration, flat relative connection, or exact decoupling from portal-induced effective coefficients.

| Result | Assumptions | Conclusion | Escape |
|---|---|---|---|
| Proposition 1 | constant linear Lorentz-compatible map | only \(A=\kappa I\) | nonlinear, nonlocal, internal, defect |
| Proposition 2 | smooth Lorentz-equivariant point map \(F:V\to V\) | radial map, null rays preserved | preferred tensors, topology, discontinuity, path dependence |
| Observation 3 | flat Abelian relative calibration on simply connected region | pure gauge, no holonomy | curvature, topology, defect/interface |

## 2. C-D Observability

Let \(V\simeq\mathbb{R}^{1,3}\) be a local inertial tangent space equipped with Lorentz metric \(\eta_{\mu\nu}\). We use signature \((-+++)\) and write \(x^2=\eta_{\mu\nu}x^\mu x^\nu\). A C-sector observer uses the visible metric \(g_{\mu\nu}\), locally equivalent to \(\eta_{\mu\nu}\). A D-sector field may use its own internal calibration or effective metric. We ask when that difference becomes visible as more than a field label.

### Notation and Conventions

The letters \(C\) and \(D\) denote sectoral speed scales. They are not spacetime coordinates. We keep \(C\) and \(D\) explicit rather than setting the visible light speed to one. In wave calculations we use phase convention \(e^{-i\omega t}\), with right-moving spatial dependence \(e^{+ikz}\) and \(k_i=\omega/v_i\). The delta-interface coupling is denoted \(\lambda\), while a finite wall uses the integrated coupling \(\lambda_{\rm int}=\int dz\,\lambda(z)\) and \(\alpha_{\rm int}=\lambda_{\rm int}/(2\omega\sqrt{CD})\). In the delta limit, \(\lambda_{\rm int}\to\lambda\) and \(\alpha_{\rm int}\to\alpha\).

The recurring terms are used as follows. \(G_{\rm common}=O(g)\cap O(f)\) is the common local symmetry group of the visible and hidden cones. A relative calibration connection is the bookkeeping connection that compares sectoral clocks, rods, or phases along paths. An escape class is classified by the first no-go assumption it breaks. The morphology vector \({\cal M}_{CD}\) is the minimal observable pattern that a proposed C-D signal must fit jointly.

We define C-D observability as at least one of the following:

1. A D-sector null ray is mapped into a C-sector non-null ray by an invariant inter-sector map.
2. A C-sector observer can measure a second causal cone not removable by units, clocks, or field redefinitions.
3. A closed path or defect produces a gauge-invariant relative calibration holonomy.
4. A portal projects hidden-sector geometry into visible EFT coefficients with a constrained origin.

This definition intentionally excludes weak statements such as "there exists a hidden massive particle." Hidden particles can be observable without making \(D/C\) an observable spacetime property.

## 3. Local No-Go Hierarchy

The local no-go results use a shared set of hypotheses. The calculation is performed in one local tangent vector space \(V\), the visible and hidden calibration data are compared through the same proper orthochronous Lorentz action, and the inter-sector map acts on the ordinary vector representation without extra background tensors, defects, path dependence, or enlarged internal spaces. These hypotheses are deliberately strong. They identify when \(D/C\) is only calibration data; the escape classes in Section 5 are exactly the ways to relax them.

### 3.1 Proposition 1: Linear Scale-Map No-Go

Let \(A:V\to V\) be a constant real linear inter-sector map. Exact relativity of the local calibration requires

\[
A\Lambda=\Lambda A,\qquad \forall \Lambda\in SO^+(1,3).
\]

This is a Schur-type commutant statement for the real four-vector representation. Since the representation is real irreducible, any endomorphism commuting with the full proper Lorentz group must lie in its commutant; the elementary block calculation below shows that this commutant is just the real scalars.

Write \(A\) in time-space block form:

\[
A=
\begin{pmatrix}
a&r^T\\
s&B
\end{pmatrix}.
\]

Commutation with all spatial rotations forces \(r=s=0\) and \(B=bI_3\). Commutation with any nonzero boost then forces \(a=b\). Therefore

\[
A=\kappa I .
\]

Thus a Lorentz-compatible constant map preserves the null cone:

\[
x^2=0 \quad\Rightarrow\quad (Ax)^2=\kappa^2x^2=0 .
\]

The ratio \(D/C\), if represented only by such a constant local calibration, cannot become a visible second light cone.

### 3.2 Proposition 2: Nonlinear Point-Map No-Go

One might try to evade the previous result with a nonlinear map. Let \(F:V\to V\) be a smooth finite point map on each Lorentz orbit and assume exact Lorentz equivariance:

\[
F(\Lambda x)=\Lambda F(x),\qquad \forall \Lambda\in SO^+(1,3).
\]

For any nonzero \(x\), the little group \(G_x\) fixes \(x\). Equivariance gives

\[
F(x)=F(hx)=hF(x),\qquad h\in G_x.
\]

Therefore \(F(x)\) must lie in the fixed subspace of the little group. For timelike, spacelike, and null orbits, this fixed subspace is the line spanned by \(x\). The scalar multiplier can depend only on Lorentz invariants and branch labels. Hence

\[
F^\mu(x)=\alpha_b(x^2)x^\mu .
\]

In particular, null rays are mapped into the same null rays or to zero:

\[
x^2=0\quad\Rightarrow\quad F(x)^2=0 .
\]

Nonlinearity alone therefore does not make \(D/C\) observable. The proposition should not be read as a theorem about deformed special relativity or relative locality, where momentum-space geometry, composition laws, or locality itself may be modified. It applies only to ordinary spacetime point maps \(F:V\to V\). Nonlocal maps, momentum-space deformations, defects, discontinuities, preferred tensors, and maps into enlarged internal spaces are outside the proposition and are precisely escape classes.

For analytic \(F\), the Taylor expansion makes the same point. Lorentz equivariance requires the first coefficients to be intertwiners:

\[
F^\mu(x)=A^\mu{}_\nu x^\nu
+B^\mu{}_{\nu\rho}x^\nu x^\rho
+C^\mu{}_{\nu\rho\sigma}x^\nu x^\rho x^\sigma+\cdots .
\]

The symbolic-intertwiner check in the public repository finds

\[
\dim\operatorname{Hom}_{SO^+(1,3)}(V,V)=1,\qquad
\dim\operatorname{Hom}_{SO^+(1,3)}(\mathrm{Sym}^2V,V)=0,
\]

and the cubic correction is proportional to \(x^2x^\mu\). Again it cannot change the null cone.

### 3.3 Scope: Spin and Internal Degrees

The no-go statements above are spacetime-calibration statements, not claims about every Lorentz-covariant field representation. A Standard-Model field carries spin, gauge, flavor, and other internal labels. If a map acts on a larger space such as \(S\otimes W\), where \(S\) is a spin representation and \(W\) is an internal space, its Lorentz commutant can contain chiral or internal matrices. That extra freedom can mix species, masses, or couplings, and it is exactly why portal models must be analyzed as field theories rather than as bare point maps.

This freedom does not by itself create a second visible spacetime cone. The causal cone of a local field equation is controlled by its principal symbol. With exact local Lorentz covariance and no background tensor, the principal symbol of a first-order spinor equation has the form \(\gamma^\mu n_\mu\) times internal data up to field redefinitions; for a second-order wave equation it is proportional to \(\eta^{\mu\nu}n_\mu n_\nu\) times internal data. Species mixing can split masses or amplitudes, but a new characteristic cone requires a preferred tensor, nonlocal propagation, boundary condition, modified momentum-space structure, or portal-induced EFT coefficient in the principal symbol. Spin and internal labels are therefore not counterexamples to the hierarchy; they are the point at which the problem becomes an explicit EFT-matching problem.

### 3.4 Observation 3: Flat Relative-Connection Calibration

The previous results concern point maps. A more global formulation treats C-D calibration as a relative connection. In the simplest Abelian clock-scale case,

\[
d\tau_D=\kappa(d\tau_C+qB_\mu dx^\mu),
\]

with gauge transformation

\[
B\to B+d\varphi .
\]

The closed-path observable is

\[
H[\gamma]=\exp\left(q\oint_\gamma B\right).
\]

For the Abelian scale connection, if \(U\) is simply connected and

\[
F=dB=0,
\]

then by the Poincare lemma \(B=d\varphi\) on \(U\), and \(B\) can be gauged away. Every contractible closed-loop holonomy is trivial.

For a non-Abelian relative connection,

\[
{\cal F}=d{\cal A}+{\cal A}\wedge{\cal A}.
\]

On a simply connected region with a fixed global trivialization, a smooth flat connection has path-independent parallel transport and can be written as \({\cal A}=M^{-1}dM\). Conversely, for a smooth global sector map \(M\), the Maurer-Cartan identity gives \({\cal F}=0\). A smooth pure calibration therefore does not create relative curvature or a nontrivial contractible-loop holonomy.

The first macroscopic C-D invariant is therefore the conjugacy class of

\[
P\exp\oint_\gamma {\cal A},
\]

or, for small contractible loops, the relative curvature integrated over the spanning surface.

## 4. Visible Relativity Protection Principle

The C-D program does not assume large visible-sector relativity violation. The empirical posture is:

\[
\begin{aligned}
\text{protect visible relativity}
&\quad+\quad
\text{allow hidden or relative-sector calibration failure}
\\
&\quad+\quad
\text{make observability portal-suppressed or topological/interface-limited}.
\end{aligned}
\]

In practice the Standard Model is required to see

\[
{\cal L}_{SM}={\cal L}_{SM}[g,\psi,A,\ldots]+\delta{\cal L}_{SME},
\]

where \(\delta{\cal L}_{SME}\) remains below existing constraints. A hidden sector may instead see, for example,

\[
f_{\mu\nu}=\Omega^2(g_{\mu\nu}-\xi u_\mu u_\nu),
\]

but this does not automatically create a visible second cone. The background \(u^\mu\) is a controlled escape hatch rather than an unconstrained new ingredient; it places the model near disformal, SME, and Einstein-aether boundaries [@Bekenstein1993DisformalGeometry; @Jacobson2008EinsteinAetherStatus].

Relativity is therefore not treated as a binary switch. The useful question is which layer is preserved and which layer is relaxed:

| Layer | Status in this paper | Consequence |
|---|---|---|
| Observer covariance | Preserved | Equations remain tensorial and laboratories can compare invariant claims |
| Visible Standard-Model Lorentz symmetry | Protected | Any leakage is an SME-like coefficient below existing bounds |
| Hidden-sector metric Lorentz structure relative to \(g_{\mu\nu}\) | May differ from the visible one | A hidden cone, preferred field, or dispersion relation can exist but is not visible by itself |
| Inter-sector calibration | May be curved, discontinuous, or path dependent | C-D observables can appear as holonomy, conversion, echo, or transient structure |
| Portal decoupling | May be weakly broken | Hidden geometry can project into constrained visible EFT textures |

Here "hidden-sector Lorentz symmetry may be relaxed" means relaxed relative to the visible metric \(g_{\mu\nu}\). A D field may still have an exact local Lorentz structure with respect to its own effective metric \(f_{\mu\nu}\). What cannot remain exact, if \(f_{\mu\nu}\) is not conformal to \(g_{\mu\nu}\) and the two sectors interact, is a single common Lorentz group that simultaneously erases the C-D speed ratio.

This gives a useful constraint on any attempted small relativity-principle relaxation. Define the common local symmetry of two cones by

\[
G_{\rm common}=O(g)\cap O(f).
\]

If the full visible Lorentz group \(O(g)\) also preserves \(f\), then \(f\) is a Lorentz-invariant symmetric bilinear form. In a local frame with \(g=\eta\), invariance under spatial rotations makes \(f=\operatorname{diag}(a,b,b,b)\), and invariance under one nonzero boost forces \(a=-b\). Therefore, for some nonzero scalar \(\alpha\),

\[
f_{\mu\nu}=\alpha g_{\mu\nu}.
\]

A full common Lorentz principle thus permits only a conformal second metric, which has the same null cone. When the two metrics are required to have the same time and space orientation, one may write \(\alpha=\Omega^2>0\). A genuine \(D/C\neq1\) cone can still be logically consistent, but it requires one of three moves: independent sector Lorentz groups with no local comparison, a proper-subgroup common symmetry selected by a background field, or a nonlocal/global calibration failure such as holonomy or an interface. This is the sense in which the relativity principle is constrained rather than discarded.

The preferred-field representative makes the point explicit. Let \(u^\mu\) be a \(g\)-unit timelike vector, \(g_{\mu\nu}u^\mu u^\nu=-1\), and take \(\xi>-1\) so that the displayed metric is nondegenerate with Lorentzian signature in the local rest frame. In visible coordinates, choose

\[
g_{\mu\nu}dx^\mu dx^\nu=-C^2dt^2+d\mathbf{x}^2,
\qquad
u_\mu dx^\mu=-Cdt .
\]

Then the representative hidden metric

\[
f_{\mu\nu}=\Omega^2(g_{\mu\nu}-\xi u_\mu u_\nu)
\]

has null condition

\[
0=f_{\mu\nu}dx^\mu dx^\nu
=\Omega^2[-(1+\xi)C^2dt^2+d\mathbf{x}^2],
\qquad
D=C\sqrt{1+\xi}.
\]

Thus \(D/C=\sqrt{1+\xi}\) is a hidden-metric statement, not yet a visible observable. It becomes visible only through a portal or a nontrivial relative calibration; any local leakage into Standard-Model fields must then appear as constrained Lorentz-violating effective coefficients, schematically of order portal strength times \(\xi u^\mu u^\nu\).

This statement is a matching requirement, not a completed SME dictionary. A local portal would have to identify which visible operator is induced, whether it belongs to the minimal or nonminimal SME, and how its coefficient scales with \(D/C\), the portal coupling, and any background tensors. An interface or defect may instead behave as a boundary or nonlocal effective operator before any bulk SME limit is justified.

This gives a sharp constraint: exact local relativity plus smooth flat calibration makes \(D/C\) unobservable, while observable C-D physics must identify its controlled relaxation. A proposed signal that cannot name this relaxation is best treated as a choice of units or as an unconstrained Lorentz-violation parameterization.

The practical checklist is:

1. Which layer of relativity is preserved, and which no-go assumption is broken?
2. Does the visible Standard Model sector remain protected?
3. Which SME, aether, clock, domain-wall, or gravity bound applies?
4. Is the proposed observable invariant, or only a calibration artifact?
5. Is the portal technically natural or symmetry protected?

## 5. Escape Classes

| Primary broken assumption | Escape class | Typical observable | Required literature boundary |
|---|---|---|---|
| No background tensor | Hidden preferred-field cone | Portal-induced SME-like coefficient | SME, disformal, aether |
| Flat relative connection | Relative holonomy | Closed-loop clock or phase holonomy | Weyl/nonmetricity, clock networks |
| Smooth global calibration | Interface/defect | Conversion, echo, transient | Domain walls, defect searches |
| Exact decoupling | Portal-projected EFT texture | Low-rank SME/dark-sector coefficients | SME, sterile/ADR, dark-photon bounds |
| Ordinary locality/composition | Deformed momentum-space relativity | Modified conservation/boost kinematics | Relative locality / DSR [@AmelinoCamelia2011RelativeLocality] |
| Single visible metric | Dynamical multimetric gravity | Spin-2 mixing, GW propagation | Ghost-free bimetric, GW170817 [@HassanRosen2011Bimetric; @HassanRosen2011Secondary; @LIGO2017GW170817GRB] |

The table is a primary-failure classification, not a claim that real models break only one assumption. If a model breaks several assumptions, it should be classified by the first local no-go layer that fails and then checked against the additional literature boundaries it enters.

## 6. Worked Example: A C-D Interface

We now give a minimal calculable escape. Consider two one-dimensional massless scalar channels coupled only at an interface:

\[
\left[\partial_t^2-C^2\partial_z^2\right]\phi_C+\lambda\delta(z)\phi_D=0,
\]

\[
\left[\partial_t^2-D^2\partial_z^2\right]\phi_D+\lambda\delta(z)\phi_C=0.
\]

For \(\phi_i=e^{-i\omega t}\psi_i(z)\), define

\[
k_C=\frac{\omega}{C},\qquad k_D=\frac{\omega}{D}.
\]

The interface imposes continuity of \(\psi_i\) and derivative jumps

\[
\psi_C'(0^+)-\psi_C'(0^-)= \frac{\lambda}{C^2}\psi_D(0),
\]

\[
\psi_D'(0^+)-\psi_D'(0^-)= \frac{\lambda}{D^2}\psi_C(0).
\]

For a C wave incident from the left and no incoming D wave, define

\[
\alpha=\frac{\lambda}{2\omega\sqrt{CD}} .
\]

The reflected, transmitted, and converted flux fractions are

\[
P_{\rm refl}=\frac{\alpha^4}{(1+\alpha^2)^2},
\]

\[
P_{C{\rm -trans}}=\frac{1}{(1+\alpha^2)^2},
\]

\[
P_{C\to D}^{\rm total}=\frac{2\alpha^2}{(1+\alpha^2)^2}.
\]

They sum to one. The forward C-to-D conversion probability is half the total:

\[
P_{C\to D}^{\rm forward}=\frac{\alpha^2}{(1+\alpha^2)^2}.
\]

Two such interfaces give the simplest echo scaling

\[
P_{\rm echo}\sim
\left[
\frac{\alpha^2}{(1+\alpha^2)^2}
\right]^2.
\]

The C-D-specific observable is the separation between conversion amplitude and hidden-path time shift:

\[
\Delta t=L_D\left(\frac{1}{D}-\frac{1}{C}\right).
\]

With this sign convention, \(D>C\) gives a negative \(\Delta t\), i.e. an apparent advance relative to visible propagation over the same path length. The scale estimates below use \(|\Delta t|\). Large \(D/C\) can change the delay or advance, while weak interface coupling suppresses the echo amplitude.

The sign of \(\Delta t\) is only a kinematic diagnostic. It is not a chronology-protection mechanism. A model with two or more separated interfaces must still specify a preferred wall foliation, a global time function for portal events, or another restriction that prevents the apparent advance from being assembled into a controllable closed causal curve.

A precise sufficient condition is as follows. Assume there exists a background time function \(T\) on the spacetime region containing the wall network such that every allowed C- or D-propagation segment has tangent \(v\) satisfying \(dT(v)>0\), and every interface conversion either preserves \(T\) or increases it. Then any admissible piecewise propagation-and-conversion curve has strictly increasing \(T\) along every nonzero propagation segment and nondecreasing \(T\) at conversions. Such a curve cannot be closed unless it has zero propagation length. This excludes controllable closed causal curves only inside this restricted model class; it is an added causal-ordering assumption, not a theorem derived from the scalar interface calculation.

### 6.1 Finite Wall Thickness

For a finite wall with profile \(\lambda(z)\), weak-coupling conversion is controlled by the Fourier transform of the wall:

\[
{\cal A}_{C\to D}^{\rm forward}\propto
\int dz\,\lambda(z)e^{i(k_C-k_D)z},
\]

\[
{\cal A}_{C\to D}^{\rm backward}\propto
\int dz\,\lambda(z)e^{i(k_C+k_D)z}.
\]

With fixed integrated coupling and normalized wall transform

\[
{\cal F}(q)=
\frac{1}{\lambda_{\rm int}}
\int dz\,\lambda(z)e^{iqz},
\]

the leading probabilities scale as

\[
P_{\rm forward}\simeq
\alpha_{\rm int}^2|{\cal F}(k_C-k_D)|^2,
\]

\[
P_{\rm backward}\simeq
\alpha_{\rm int}^2|{\cal F}(k_C+k_D)|^2.
\]

Finite wall thickness is therefore not merely a small correction; it acts as a momentum filter. Forward conversion is coherent only when

\[
|k_C-k_D|L_w\lesssim1,
\]

or

\[
L_w\lesssim
\frac{C}{\omega |1-C/D|}.
\]

This produces a real tension: large \(D/C\) helps create a distinctive time shift, but also increases phase mismatch and suppresses conversion through a thick wall. In a microscopic model, \(L_w\) cannot remain an arbitrary fitting length. It should be set by a wall field mass, defect tension, plasma or material response scale, or another dynamical mechanism that also controls the available energy range.

![Finite C-D interface momentum filter: wall thickness suppresses conversion once the phase mismatch \( |k_C-k_D|L_w \) exceeds unity](../figures/interface_wall_filter.svg)

Figure 1 shows the representative case \(D/C=2\), \(\alpha_{\rm int}=0.1\), and a small-splitting comparison \(D/C=\sqrt{1+10^{-3}}\). The horizontal axis is the dimensionless wall thickness \(\zeta=\omega L_w/C\), so the coherence scale is set by \(|k_C-k_D|L_w\simeq1\). This is a proof-of-principle diagnostic, not an exclusion plot. The transfer-matrix result tracks the Born Fourier-filter prediction in the weak-coupling regime. A smooth wall suppresses conversion more rapidly than a square wall, while the small-splitting curve remains coherent across the displayed range. Thus the wall profile and cone splitting are observable parts of the escape route rather than arbitrary modeling details.

The interface example is not claimed to be a new scattering formalism. Its role is to show how a C-D speed ratio becomes physical only when the smooth global calibration assumption fails.

A four-dimensional photon or fermion portal would not reuse this scalar model unchanged. Polarization, spin, angular incidence, and gauge constraints change the coupling coefficients and boundary data. The robust part of the toy calculation is narrower: conversion across a finite interface samples the momentum mismatch \(k_C-k_D\), so thickness acts as a coherence filter. A realistic channel must keep this filter while adding the appropriate spin or polarization structure.

It is also not a causal cosmology. If \(D>C\), a hidden segment may look like an advance in visible time. A consistent model must specify a wall frame, a global time orientation, or another causal-ordering condition that prevents controllable closed causal curves. The interface calculation only establishes flux-conserving conversion and coherence filtering in a fixed background.

The public repository, `https://github.com/wujunlin96/cd-observability-hierarchy`, contains the delta-interface, finite-wall, and plotting scripts. In the recorded finite-wall scan, the maximum flux-conservation error is below \(5\times10^{-14}\).

### 6.2 Echo Morphology as a Test Program

The interface calculation suggests a conservative observational program without claiming a detected signal. A viable C-D interface or defect echo should link three quantities that are independent in a generic transient model:

| Quantity | C-D interface scaling | Diagnostic role |
|---|---|---|
| Time offset | \(\Delta t=L_D(1/D-1/C)\) | fixes hidden-path length once \(D/C\) is chosen |
| Conversion strength | \(P_{\rm echo}\sim P_{C\to D}^{(1)}P_{D\to C}^{(2)}\) | separates weak portal coupling from large hidden speed mismatch |
| Coherence filter | \(|{\cal F}[\omega(1/C-1/D)]|^2\) | makes wall thickness and observing frequency part of the signal morphology |

Equivalently,

\[
L_D=\frac{C|\Delta t|}{|1-C/D|}.
\]

For the representative hidden-metric parameterization \(D/C=\sqrt{1+\xi}\), the repository scale table gives the following order-of-magnitude targets:

| Target offset | \(\xi\) | \(D/C\) | Required hidden segment |
|---|---:|---:|---:|
| \(1\,{\rm ns}\) | \(1\) | \(1.414\) | \(1.0\,{\rm m}\) |
| \(1\,{\rm ns}\) | \(10^{-3}\) | \(1.0005\) | \(6.0\times10^2\,{\rm m}\) |
| \(1\,{\rm ms}\) | \(1\) | \(1.414\) | \(1.0\times10^3\,{\rm km}\) |
| \(1\,{\rm ms}\) | \(10^{-3}\) | \(1.0005\) | \(6.0\times10^5\,{\rm km}\) |

These numbers are not exclusions. They are a scale sanity check. Small cone splitting demands macroscopic hidden path length, while large cone splitting must still overcome interface phase mismatch and portal suppression.

The frequency dependence gives an additional morphology test. A companion scan compares simple phenomenological couplings \(\alpha(\omega)=\alpha_{\rm ref}(\omega/\omega_{\rm ref})^p\). For \(p=-1\), high-frequency echoes rapidly disappear; for \(p=0\), the thin-wall echo probability is approximately achromatic before finite-wall filtering; for \(p=1\), strong reflection can appear at intermediate frequencies rather than monotonic conversion. A real forecast should therefore specify the wall profile and coupling dimension before fitting any event.

For photon-like portals, high-energy propagation constraints are a major obstacle. If the same mechanism induces an unsuppressed local photon speed shift over cosmological distances, gamma-ray burst and other distant-source timing bounds would strongly constrain it. The interface toy model avoids making that claim only because conversion is localized and filtered by \({\cal F}[\omega(1/C-1/D)]\). A photon implementation would still need an explicit time-of-flight and spectral recast before it could be treated as viable.

This is a falsifiability gate for the interface route: an alleged C-D echo should not be judged only by the existence of a delayed copy. It should show the linked time-offset, conversion-strength, and coherence-filter pattern implied by the same controlled failure of smooth calibration.

### 6.3 Interface-Holonomy Forecast Gate

The interface and holonomy routes give a pre-fit forecast gate. Before any event or clock-network data are interpreted as C-D evidence, the proposed signal must specify three morphology scales:

\[
L_D=\frac{C|\Delta t|}{|1-C/D|},
\]

\[
f_{\rm coh}\simeq \frac{C}{2\pi L_w |1-C/D|},
\]

and, for a clock of frequency \(\nu\),

\[
\Delta\phi=2\pi\nu\,\delta\tau_{CD}.
\]

The first equation fixes the hidden path length needed for a visible time offset. The second gives the frequency above which a wall of thickness \(L_w\) suppresses conversion by phase mismatch. The third turns a relative calibration holonomy into a clock phase step. These three relations are independent enough to be useful: a model can fit one by hand, but it is harder to fit all three without specifying the same wall, cone split, and relative connection.

For a non-Abelian relative calibration, the scalar loop integral is replaced by the conjugacy class of the holonomy

\[
U_\gamma={\cal P}\exp\oint_\gamma {\cal A}.
\]

The gauge-invariant small-loop data are the eigenphases of \(U_\gamma\); for weak curvature, \(U_\gamma\simeq I+{\cal F}_{\mu\nu}\Sigma^{\mu\nu}\). A clock or interferometer coupled with effective charge \(q_{\rm eff}\) would see a phase scale \(q_{\rm eff}\Theta_\gamma\), where \(\Theta_\gamma\) is an eigenphase norm. This is not yet an experimental bound, but it identifies the quantity a clock-network or interferometric recast would have to constrain.

It is useful to package the prediction as a morphology vector rather than as a single anomaly:

\[
{\cal M}_{CD}=
\left(
\Delta t,\,
P_{\rm echo}(\nu),\,
f_{\rm coh},\,
\Delta\phi_{\rm clock}
\right),
\]

with leading dependencies

\[
\Delta t\propto L_D |1-C/D|,
\qquad
f_{\rm coh}\propto \frac{1}{L_w |1-C/D|},
\]

\[
P_{\rm echo}(\nu)\propto
\alpha(\nu)^4
\left|{\cal F}\!\left[2\pi\nu(1/C-1/D)\right]\right|^4,
\qquad
\Delta\phi_{\rm clock}\propto\nu\oint_\gamma B .
\]

This morphology vector is the minimal phenomenological object for the interface/holonomy route. A delayed echo alone is not enough; a C-D interpretation must also specify how the echo probability changes with observing frequency, where finite-wall coherence is lost, and whether any closed-loop clock or phase observable follows from the same relative calibration structure.

The same idea extends to other escape classes. For a preferred-field SME route, the vector would replace echo probability by a low-rank coefficient texture and energy dependence. For multimetric gravity, it would include spin-2 mixing and multimessenger propagation. For deformed momentum-space relativity, it would include modified conservation or boost-composition data. The point is unchanged: a C-D interpretation should be a linked pattern, not a one-parameter anomaly.

The public forecast table gives conservative representative scales:

| Route | Input | Derived scale | Meaning |
|---|---|---|---|
| delay | \(\Delta t=1\,{\rm ns}\), \(\xi=1\) | \(L_D\simeq1.0\,{\rm m}\) | large cone split can give laboratory-scale offsets |
| delay | \(\Delta t=1\,{\rm ns}\), \(\xi=10^{-6}\) | \(L_D\simeq6.0\times10^5\,{\rm m}\) | tiny cone split needs macroscopic hidden paths |
| delay | \(\Delta t=1\,{\rm ms}\), \(\xi=10^{-3}\) | \(L_D\simeq6.0\times10^8\,{\rm m}\) | millisecond offsets with small split become astronomical |
| coherence | \(L_w=1\,{\rm km}\), \(\xi=1\) | \(f_{\rm coh}\simeq1.6\times10^5\,{\rm Hz}\) | thick walls suppress high-frequency conversion for large split |
| coherence | \(L_w=1\,{\rm km}\), \(\xi=10^{-3}\) | \(f_{\rm coh}\simeq9.5\times10^7\,{\rm Hz}\) | smaller split keeps radio-scale coherence |
| holonomy | \(4\times10^{14}\,{\rm Hz}\) clock, \(0.01\) rad, \(1\,{\rm s}\) event | \(\delta\tau\simeq4.0\times10^{-18}\,{\rm s}\), \(y\sim4.0\times10^{-18}\) | optical clocks convert tiny time steps into measurable phase targets |

The table is not a proposal to search exactly these numbers. It states consistency requirements. A C-D interface interpretation should name the wall thickness, the cone split, and the coupling frequency dependence; a C-D holonomy interpretation should name the loop, the relative connection, and the clock response. Otherwise the signal is not yet distinguishable from a generic transient, ordinary propagation delay, or unconstrained clock perturbation.

This gives immediate null tests:

| Candidate observation | Why it is not yet C-D evidence |
|---|---|
| A delayed copy with no frequency-dependent conversion law | Could be ordinary propagation, scattering, lensing, or source repetition |
| A frequency cutoff with no tied time offset | Could be an ordinary material/plasma/filtering effect |
| A clock-network transient with no closed-loop or defect geometry | Could be a generic correlated clock perturbation |
| A fitted speed ratio with no named failure of the no-go assumptions | Likely a calibration convention or an unconstrained Lorentz-violation parameter |

The positive target is therefore not "any anomalous delay." It is a co-constrained pattern: the same \(D/C\), wall scale \(L_w\), interface coupling \(\alpha(\nu)\), and relative connection must explain the delay, conversion strength, coherence cutoff, and possible clock phase response.

## 7. Discussion: Literature Boundary and Next Routes

Multi-speed sector models already exist. For example, Lorentz-violating supersymmetric field theories can contain sectors with different limiting speeds, and broader superluminal-particle discussions have explored particles whose critical speed differs from the visible speed of light [@Redigolo2012LorentzViolatingSUSY; @ChashchinaSilagadze2012LightSpeedBarrier]. The C-D hierarchy does not claim priority for the existence of multiple speed parameters. Its claim is narrower: before such parameters become new spacetime physics for a visible observer, one must identify the map, holonomy, defect, portal, or background field that prevents \(D/C\) from being removed by calibration.

Varying-speed-of-light cosmologies change the status of the visible light speed or introduce bimetric/cosmological mechanisms to address early-universe puzzles [@AlbrechtMagueijo1999VSL; @Magueijo2003VSLReview; @Moffat2002VSLTheories; @Magueijo2008BimetricVSL]. The C-D question treated here is different. We do not assume that the visible-sector speed \(C\) varies in spacetime, nor do we use a varying visible \(c\) to solve horizon or flatness problems. We instead ask whether a hidden-sector speed ratio \(D/C\) has invariant observable content under exact local relativity and controlled inter-sector calibration.

Local visible-sector Lorentz breaking belongs to the SME program [@ColladayKostelecky1998SME; @KosteleckyRussell2011DataTablesSME]. The C-D hierarchy does not replace the SME. It says that any visible local breaking generated by a C-D portal must land in an SME-like coefficient or justify why it does not. The living Data Tables are the proper entry point for current coefficient bounds. The present paper gives a matching requirement and a tree-level sketch, not a full numerical coefficient map.

Disformal hidden metrics and preferred vectors sit near Bekenstein-type physical/gravitational metric relations and Einstein-aether models [@Bekenstein1993DisformalGeometry; @Jacobson2008EinsteinAetherStatus]. In this paper they are escape classes, not novelty claims.

Photon portals are particularly constrained. Photon/paraphoton velocity oscillation models already show that mixing a visible photon with a second velocity eigenstate is strongly bounded by CMB and distant-source propagation [@Glashow1998PhotonVelocityOscillations; @DeAngelisPain2002PhotonVelocityOscillations]. A C-D photon portal is therefore a constraint channel, not the preferred discovery channel.

Neutrino portals are less immediately fatal but still crowded. SME neutrino Hamiltonians and active-sterile altered-dispersion or shortcut models already contain unconventional energy dependence and resonant structures [@KosteleckyMewes2004Neutrinos; @PaesPakvasaWeiler2005ShortcutSterile; @HollenbergPaes2009ADRResonance; @Barenboim2019SterileADRRevisited]. A C-D neutrino model would need to prove a restrictive low-rank geometric texture and then perform a real recast.

Relative holonomy must be separated from ordinary Weyl second-clock effects and metric-affine/nonmetricity phenomenology. Existing clock-network searches for topological dark matter already look for transient correlated frequency shifts [@LoboRomero2018SecondClockConstraints; @HobsonLasenby2020WeylNoSecondClock; @HobsonLasenby2021SecondClockNote; @DereviankoPospelov2013TopologicalDMClocks; @Wcislo2016OpticalClocksTopologicalDM; @Roberts2017GPSDomainWallDM; @Wcislo2018GlobalClockNetworkDM]. A C-D holonomy model is distinctive only if it is relative-sector, portal-suppressed, and morphologically constrained.

Finally, full multimetric gravity is outside this work. Generic interacting spin-2 sectors face the usual ghost and consistency issues unless special structures are imposed, and visible gravity-light speed differences are tightly constrained by GW170817/GRB170817A [@HassanRosen2011Bimetric; @HassanRosen2011Secondary; @LIGO2017GW170817GRB].

The practical link to existing data is therefore a recast dictionary, not a new universal bound. The table below gives the minimal quantity that must be computed before a C-D escape route can use existing constraints.

| Escape route | Quantity to compute | Existing boundary |
|---|---|---|
| Preferred-field SME texture | low-rank coefficients such as \(c_{\mu\nu}^{(\psi)}\sim \zeta_\psi\xi u_\mu u_\nu\) | SME coefficient tables |
| Photon portal/interface | conversion probability and coherence filter \(P_{\gamma\to D}(\nu)\) | photon/paraphoton velocity oscillation and distant-source bounds |
| Relative holonomy | loop phase \(U_\gamma={\cal P}\exp\oint_\gamma B\) or \(\Delta\phi=2\pi\nu\delta\tau_{CD}\) | second-clock and clock-network searches |
| Visible multimetric leakage | visible \(v_g-C\), spin-2 mixing, or multimessenger delay | GW170817/GRB170817A and bimetric consistency |

Two routes are most natural after this classification paper. The interface/holonomy route should turn \({\cal M}_{CD}\) into a data-facing forecast with wall-scale priors. The SME route should choose a UV portal and replace the sketch in Appendix D by an operator-level coefficient map and loop-stability calculation.

## 8. Limitations

This manuscript is a local no-go and classification note, not a complete theory of a D sector. It does not prove the existence of a hidden spacetime, derive a UV completion, or provide a technically natural portal. The interface calculation is a one-dimensional classical scalar toy model. Its value is narrower: it preserves flux, exposes the coherence condition, and gives a concrete failure mode of smooth calibration.

The most serious missing dynamical question is radiative stability. In an ordinary local quantum field theory, a portal connecting visible fields to a hidden Lorentz-breaking cone can radiatively feed Lorentz-violating operators back into the visible sector. A realistic model must therefore invoke a symmetry, sequestering mechanism, emergent low-energy protection, or fine tuning, and then compute the induced coefficients rather than merely assuming visible relativity is protected.

The program would lose its independent content if every proposed C-D signal reduced to an unconstrained SME coefficient, an ordinary Weyl/nonmetricity effect, or a generic dark-sector portal with no restricted C-D morphology. Conversely, it gains content only when the same relaxation that makes \(D/C\) observable also predicts a constrained pattern, such as a low-rank coefficient texture, a holonomy class, or an interface coherence filter.

The following limitations identify the precise boundary of the present argument.

1. EFT matching. The paper states that visible leakage must enter SME-like coefficients and gives only a tree-level matching sketch. A complete model must choose a portal and compute Wilson coefficients in terms of \(D/C\), background fields, and coupling strengths.
2. Quantum consistency. The present treatment stays at classical geometry and scalar scattering level. A complete model must analyze loop corrections, radiative Lorentz breaking, technical naturalness, and possible tachyonic or ghost instabilities.
3. Causal ordering. Apparent advances are treated only as kinematic diagnostics. A complete model must specify a preferred foliation, global time function, or other condition preventing controllable closed causal curves.
4. Four-dimensional channels. The local no-go statements are four-vector statements, but the interface calculation is one-dimensional and scalar. A complete channel must include spin, polarization, angular incidence, multiparticle thresholds, and multichannel unitarity when relevant.
5. Curved spacetime. The hierarchy is formulated in one local tangent space. A curved-background version must use tetrads, relative connections, global causal ordering, and gravitational constraints.
6. Quantitative phenomenology. The scale and morphology gates are not exclusions. A data-facing version must choose a data class and produce a forecast or exclusion workflow with detector statistics, nuisance models, high-energy propagation bounds, and wall-scale priors.

This scope also clarifies the novelty claim. The paper is not original because it mentions multiple speeds, bimetric ideas, SME coefficients, or hidden portals. Those ingredients are already established. The proposed contribution is the ordered test: if a C-D speed ratio is claimed to be physical, one must identify which local no-go assumption fails and then supply the corresponding morphology or EFT texture.

The cleanest next step is to choose one escape class and close this table for that case, rather than to expand all escape classes superficially. The interface/holonomy route is the closest to the present calculation because it already links a broken calibration assumption to a morphology vector. A different route, such as a low-rank SME texture, would require less new observational language but a more explicit EFT matching calculation.

## 9. Conclusion

A hidden sector assigned a speed scale \(D\) is not automatically a hidden second light cone for a visible observer. Under exact local Lorentz equivariance, smooth Lorentz-equivariant maps, and flat relative calibration, \(D/C\) has no local invariant observable content. This is not a failure of the idea; it is the organizing principle.

The C-D hypothesis becomes physical only at controlled failure modes: preferred hidden fields, relative holonomy, defects/interfaces, or portal-projected EFT textures. Those failure modes are constrained by mature literatures, so the correct first paper is not a discovery claim. It is a no-go and observability hierarchy with a carefully bounded worked example. Its distinctive output is the morphology vector \({\cal M}_{CD}\), which forces any future model to fit delay, conversion, coherence, and clock/holonomy information together.

## Appendix A. Formal Assumptions Behind the No-Go Results

This appendix collects the assumptions that prevent the no-go hierarchy from being misread as a universal statement about all possible hidden sectors.

### Formal Proposition Statements

Let \(V\) denote the real four-vector representation of \(SO^+(1,3)\), with Lorentz metric \(\eta\). All statements below are local statements in one tangent space unless a connection is explicitly introduced.

**Proposition A.1 (linear local calibration).** If a constant real linear map \(A:V\to V\) satisfies

\[
A\Lambda=\Lambda A,\qquad \forall \Lambda\in SO^+(1,3),
\]

then \(A=\kappa I\). Consequently \(A\) maps the visible null cone to itself and cannot represent a second visible signal cone.

Equivalently, complexify the vector representation. The \((1/2,1/2)\) representation of \(SL(2,\mathbb C)\) is irreducible, so Schur's lemma makes every complex intertwiner a scalar. A real Lorentz-commuting endomorphism is therefore the real scalar multiple \(A=\kappa I\). The block-matrix calculation in Appendix B is only a component check of this representation-theoretic statement.

**Proposition A.2 (smooth point-map calibration).** Let \(F:V\to V\) be smooth and finite on each nonzero Lorentz orbit, and suppose

\[
F(\Lambda x)=\Lambda F(x),\qquad \forall \Lambda\in SO^+(1,3).
\]

Then on each orbit branch

\[
F^\mu(x)=\alpha_b(x^2)x^\mu,
\]

so null rays are mapped to null rays or to zero. Nonlinearity alone therefore does not make \(D/C\) visible.

**Proposition A.3 (flat relative calibration).** In a simply connected region, an Abelian relative calibration connection \(B\) with \(dB=0\) is pure gauge, so every contractible closed-loop holonomy is trivial. In the non-Abelian case, the same conclusion holds for a smooth flat connection in a fixed global trivialization on a simply connected region; equivalently, \({\cal A}=M^{-1}dM\) for a smooth global sector map, and the Maurer-Cartan identity gives \({\cal F}=0\). Topology, curvature, singular support, and boundary jumps are therefore the routes to nontrivial relative holonomy.

**Proposition A.4 (common-cone constraint).** Let \(g\) and \(f\) be two symmetric nondegenerate bilinear forms on \(V\). If the full visible Lorentz group \(O(g)\) also preserves \(f\), then \(f=\alpha g\) for a nonzero scalar \(\alpha\). Thus a full common Lorentz group permits only conformally related bilinear forms and hence a shared null cone.

This is a tangent-space statement. In curved spacetime the same algebra can be repeated in a local tetrad at one point, but global cone comparison also depends on tetrad transport, relative connections, curvature, topology, and boundary data. A curved-background extension must therefore redo the argument with those structures specified.

These propositions are conditional. They do not apply to maps with extra internal indices, spacetime-dependent backgrounds, singular defects, nonlocal propagation, momentum-space deformations, topology, or portal-induced effective coefficients. Those are not afterthought loopholes; they are the controlled C-D observability routes.

Proposition A.1 assumes a constant real linear map \(A:V\to V\), no extra internal indices, and exact commutation with the proper orthochronous Lorentz group. If the map acts on a larger vector space \(V\otimes W\), mixes internal sectors, depends on spacetime, or is nonlocal, the conclusion \(A=\kappa I\) need not hold.

Proposition A.2 assumes a smooth finite point map \(F:V\to V\) on each Lorentz orbit, with no background vector, tensor, spinor, defect, boundary, or path dependence. The proof uses the fixed subspace of each orbit's little group. For a timelike representative the little group is \(SO(3)\), and the fixed vector is parallel to the time direction. For a spacelike representative the little group acts nontrivially on the orthogonal \(1+2\) subspace, leaving only the representative direction fixed. For a null representative the \(E(2)\)-like little group fixes only the null line. Therefore \(F^\mu(x)=\alpha_b(x^2)x^\mu\) on each orbit branch.

Proposition A.3 assumes a smooth relative connection on a simply connected region. If the region is not simply connected, a flat connection may still have global holonomy. If the connection has curvature, singular support, boundary jumps, or defect sources, the pure-gauge conclusion does not apply. These are not loopholes to hide; they are the physical escape classes listed in the main text.

## Appendix B. Symbolic Intertwiner Check

The analytic Taylor-expansion corollary in Section 3.2 is checked by the symbolic-intertwiner script in the public repository. In the recorded run it reports:

```text
linear_commutant_dim = 1
linear_basis_vector = Matrix([[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]])
quadratic_equivariant_dim = 0
cubic_equivariant_dim = 1
cubic_x2x_residual_zero = True
```

The first line confirms that the linear commutant is spanned by the identity. The second result confirms that no quadratic Lorentz-equivariant map \(\mathrm{Sym}^2(V)\to V\) exists in this representation check. The cubic result is the expected \(x^2x^\mu\) structure, which vanishes as a cone-changing correction on null vectors.

This symbolic check is not a substitute for the proposition. It is a reproducibility guard against algebraic mistakes in the lowest-order expansion.

## Appendix C. Interface Transfer-Matrix Calculation

The finite-wall calculation rewrites the coupled channel equations as a first-order transfer system:

\[
\frac{d}{dz}
\begin{pmatrix}
\psi_C\\
\psi_C'\\
\psi_D\\
\psi_D'
\end{pmatrix}
=
\begin{pmatrix}
0&1&0&0\\
-k_C^2&0&\lambda(z)/C^2&0\\
0&0&0&1\\
\lambda(z)/D^2&0&-k_D^2&0
\end{pmatrix}
\begin{pmatrix}
\psi_C\\
\psi_C'\\
\psi_D\\
\psi_D'
\end{pmatrix}.
\]

For a square wall, the transfer matrix is a single matrix exponential. For the smooth \(\mathrm{sech}^2\) wall, the script multiplies midpoint-step exponentials. The integrated coupling is fixed as

\[
\int dz\,\lambda(z)=2\alpha_{\rm int}\omega\sqrt{CD},
\]

so the thin-wall limit can be compared directly to the \(\delta\)-interface result.

The numerical output and plotting script are provided in the public repository. In the recorded scan the maximum flux-conservation error is \(4.852\times10^{-14}\).

The finite-wall result should be read only within its assumptions: one spatial dimension, scalar channels, a fixed wall background, no backreaction, no stochastic wall network, and no full cosmological causal model.

## Appendix D. Minimal Tree-Level SME Matching Sketch

This appendix records the minimal local matching logic behind the visible-relativity protection principle. It is not a UV completion and it does not replace a full SME recast.

Suppose a hidden cone splitting is represented locally by a \(g\)-unit timelike vector \(u^\mu\) and a small parameter \(\xi\), so that the hidden metric differs from the visible metric through a tensor proportional to \(\xi u_\mu u_\nu\). If a local portal induces a visible fermion derivative operator

\[
\Delta{\cal L}_\psi=
\frac{i}{2}\epsilon_\psi u_\mu u_\nu
\bar\psi\gamma^\mu\overleftrightarrow{\partial^\nu}\psi,
\qquad
\epsilon_\psi=\zeta_\psi\xi+O(\xi^2),
\]

then comparison with the usual SME fermion kinetic structure identifies, up to trace conventions and field redefinitions,

\[
c_{\mu\nu}^{(\psi)}\sim \epsilon_\psi u_\mu u_\nu .
\]

A vector-current portal instead gives the schematic operator

\[
\Delta{\cal L}_\psi=-a_\mu^{(\psi)}\bar\psi\gamma^\mu\psi,
\qquad
a_\mu^{(\psi)}\sim g_\psi U_\mu ,
\]

which is an SME-like \(a_\mu\) term. A constant species-universal \(a_\mu\) can be unobservable after field redefinition, while species-dependent or spacetime-dependent terms are constrained.

The loop problem is visible already at the level of dimensional analysis. For a dimensionless portal coupling \(g\) to a hidden Lorentz-breaking propagator, one generically expects

\[
\delta c_{\mu\nu}^{\rm loop}
\sim \frac{g^2}{16\pi^2}\xi u_\mu u_\nu
\]

unless a symmetry, sequestering mechanism, emergent low-energy structure, or fine tuning suppresses it. This estimate is the reason the visible-relativity protection principle is a quantitative naturalness requirement rather than a slogan.

If an experiment bounds a relevant visible coefficient by \(|c_{\mu\nu}^{(\psi)}|<c_{\rm max}\), the schematic loop estimate gives the necessary condition

\[
\frac{g^2}{16\pi^2}|\xi| \lesssim c_{\rm max}
\]

up to portal-dependent group factors, thresholds, and tensor projections. This inequality should not be read as a universal exclusion curve. It is a diagnostic: an unsuppressed portal with \(|\xi|\sim1\) generically needs very small \(g\), a symmetry cancellation, or genuine sectoral sequestering before the visible-relativity protection principle can be credible.

## Declarations

### Data and Code Availability

This manuscript uses analytic derivations and generated toy-model data. The public artifact repository is `https://github.com/wujunlin96/cd-observability-hierarchy`; a persistent archive can be minted for future versions if needed. The repository contains the LaTeX source package, bibliography, compiled PDF, generated figure, reproducibility scripts, audit outputs, and the 27-reference release bibliography used for this version.

### Ethics, Funding, and Conflicts of Interest

This theoretical work uses no human participants, animal subjects, or private datasets. No external funding was received for this work. The author declares no conflicts of interest.

### Author Contributions and AI Assistance

Junlin Wu supplied the motivating C-D question and research direction, reviewed the theoretical claims, and is responsible for the final interpretation and submission. AI assistance was used for mathematical organization, literature-search organization, code generation, reproducibility checks, literature-boundary auditing, and manuscript drafting support. The author is responsible for the final claims, interpretation, and submission.
