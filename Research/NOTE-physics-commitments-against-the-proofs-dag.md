# NOTE — what *Truth and Consequences* commits to physically, measured against the proofs DAG

*Written 2026-09-13 (Day 225), against `cde64cd` of this repo and `ee1aedb` of `Multi-DAC/proofs`
(191 nodes in two graphs, 180 physics + 11 maths). Commissioned by Clayton's 10:54 instruction that
"the metaphysics" means **this book**, not the earlier volumes, and by his standing question of
whether the Lean, the DAGs and the matrix align **with the DAGs having authority, in the sense that
physical untenability acts as an obstruction**.*

**What this is.** An extraction. It asks what the book *already* commits to that has physical
content, and where those commitments touch the physics DAG. **It is not an attempt to make the book
killable.** Nothing below proposes softening a claim, and where a claim turns out to be immune to
the physics that is reported as a fact about the architecture, not a defect.

---

## 1. The vocabulary census, because the first finding is an absence

Measured over the 72 markdown files at `book/` root — the shipped artefact, not the working
documents under `book/docs/`. Counts are matched lines.

| term | hits | what they are |
|---|---|---|
| `electromagnet*` | **0** | — |
| `condensate`, `superconduct*`, `coherence length` | **0** | — |
| `Planck`, `vacuum`, `spacetime`, `speed of light` | **0** | — |
| `phase transition`, `order parameter`, `symmetry breaking`, `free energy` | **0** | — |
| `resonan*` | **0** | — |
| `gravit*` | 8 | five are a **plant or a valley** feeling it (IV.3 statoliths, gravitropism; IV.9's valley), one is Weil's book title, two are metaphors ("inspected by gravity", "attentional gravity"). **None is about gravitation as a theory.** |
| `entangl*` | 1 | a Vedic snare, V.5 |
| `decoheren*` | 2 | Zeh 1970, both in II.7 |
| `photon` | 5 | four in II.7, one in VI.1 |
| `Hz`/`hertz` | 5 | a quartz divider (IV.2), rod/cone flicker fusion (IV.3), shamanic drumming (V.8) |
| `superposition` | 10 | **nine are the word being banned**; one is Steno's law of superposition in strata (IV.2) |
| `quantum` | 35 | concentrated in II.7 (13) and VI.7 (9) |

**The book contains almost no physics vocabulary, and this is deliberate rather than incidental.**
II.7 states the rule — *what is banned is a vague word, never a bold claim* — and applies it to the
one word it costs something: *collapse* is kept because a reader has seen a lung and a bridge do it;
*superposition* is refused because "a word that is unfamiliar and impressive is not an analogy; it is
a credential." `Z-01` makes it a glossary entry: **the book's word is `open`.**

So the census does not show a book avoiding physics. It shows a book that has **priced** its physics
vocabulary and paid for two words.

---

## 2. The claims with physical content, and the firewall

Of the thirty canonical claims in `07-THE-CLAIMS-REGISTER.md`, six carry content a physicist could
in principle push on.

| claim | the physical content | can the DAG obstruct it? |
|---|---|---|
| **C1** plenitude — all configurations exist, statically, no runtime | a block/configuration-space commitment; no dynamics anywhere | **No node exists.** The DAG is entirely field-theoretic. |
| **C13** time is a feature of the inside | before-and-after appears *with* the vantage | **No node exists.** |
| **C7** reactivity is awareness | "reacts" is a physical predicate; the consciousness–physics link is stated as an **identity**, not a mechanism | **No node exists.** The DAG has zero consciousness surface. |
| **C25** measurement is one structure; the subatomic case is an instance | contact · could-have-come-out-otherwise · lands | **No — by declaration.** See below. |
| **C26** there is no stuff; what there is, is arrangement | a structuralist ontology, symmetric across mind and world | **No — because its physical content is orthodox.** See §3. |
| **C22** identity across gaps — a self's geometry is a strange attractor | a dynamical-systems object with a definition | **No node exists**, and the maths graph's 11 nodes carry nothing dynamical. |

**The firewall is explicit and it is in the shipped prose, not only in the register.** C25 carries a
star clause — *"nothing in this book rests on the physics. If the identification were withdrawn
tomorrow, every other claim stands where it is."* II.7 says it at greater length and finishes:
**"Anyone who needs the physics to be true for their metaphysics to work has already told you their
metaphysics does not work."**

That is a good architectural move and it should not be undone. But it has a consequence that has to
be said flat, because it is the direct answer to the standing question:

> **The physics DAG cannot obstruct *Truth and Consequences*, and the book says so on the page.**

This is not a criticism. It is the mirror of what the proofs repo measured on the same day. Round 51
found that **11 of 191 nodes have any path along `uses` to a measurement**, because the graph has one
edge type and it means *is built from* — so a measurement that **refutes** a conjecture has nowhere
to live in it. The DAG has no edge for obstruction; the book has a declared immunity to it. **Neither
artefact can currently constrain the other, and both have put that in writing.**

---

## 3. Where the commitments *do* touch, and there are two places

### 3a. C26 and the gauge block — a touch that is an illustration, not a test

C26's canonical near-miss ① is **ontic structural realism** (Ladyman & Ross, *Every Thing Must Go*,
2007), and the register states the cut: *their structure is what the equations quantify over and is
fully itself with nobody near it; this is a claim about what contact is like, and it has a grade in
it.*

The DAG's electromagnetic block is a sustained demonstration of the OSR half. `em.gauge_invariance`:
"No meter reading distinguishes gauges." `em.aharonov_bohm`: "The phase shift of electrons around an
enclosed flux depends on the loop integral of A, with B = 0 on the path. **The potential's loop
integrals are physical.**" There is no local stuff at the electron — no field on its path — and the
arrangement, the holonomy, is what is real and measured. *What there is, is arrangement*, in a
laboratory.

**But it is an illustration and not a test, and the distinction is C27's.** C26 and OSR predict the
same thing about Aharonov–Bohm. Their divergence is entirely in the clause *"and it has a grade in
it"*, which is not a physical prediction — it is what IV.2 needs to say a rock has a minimal inside
rather than extending a courtesy to gravel. So:

> **C26's physical content is orthodox structural realism; its distinctive content is the grade, and
> the grade is load-bearing in the ethics, not in the physics.** The DAG can obstruct C26 only by
> obstructing OSR, and it does not.

Worth recording for the DAG's side: `em.aharonov_bohm` is one of the **ten measurement nodes with
nothing downstream of them at all**, and seven nodes name it in prose with no edge to it. The single
hardest contact surface between this book and the physics corpus runs through a node the graph has
left isolated.

### 3b. C27 and the `bridges` schema — the one place the book gives the DAG something

C27, the shipped sentence at IV.7:588–589: *"Two frames may be held at once precisely where they
predict the same thing, and where they diverge you must pick, and the divergence is where all the
work is."* The register adds that this is **an obligation to adjudicate, not a scoring remark.**

Round 51 built the enforcement of exactly that rule, independently and without reading this book.
`physics/refcheck.py` computes each node's **referent** — the object its numbers are properties of —
and flags a node as a **crossing** when it stands on two or more objects and no single parent already
stood on all of them. Every crossing must carry a `bridges` block whose load-bearing field is
`transports`: either `"none"` (the two frames agree and nothing moved between them) or the named
quantity that crossed. Six crossings in 191 nodes; five transport nothing; **the sixth is round 48's
defect — a bound on one object used to exclude a value belonging to another — and it is the only one
where a number ever crossed.**

That is C27's licensed case and C27's failure case, in a gate. The arrival was independent, which by
**C30** makes it evidence and not proof — and evidence of the good kind, since a prose discipline
about borrowed frames and a Python script about Josephson junctions are as unlike in technique as
two procedures get.

---

## 4. The condensate test — run, refuted, retracted

**The test as first written is withdrawn.** It was run against a refuter before this note was
committed, and it did not survive. Three of its four table cells rested on a misread referent, and
the fourth was granted on a pun. What is left is smaller than the claim, and a different finding came
out of the wreck that is worth more than the claim was.

The retracted verdicts, for the record: *C_sep fails by phase–number conjugacy* — **retracted**.
*ξ = 1/√N is a measure of that failure, so the mechanism is refuted by devices that are too good a
condensate* — **retracted**. *C_meas fails inverted, C_scale is vacuous, C_dyn passes* —
**retracted, all three**. *The two coherences are near-antonyms on two of four axes* — **retracted as
a count**; the qualitative point survives in the much weaker form given in §4c.

### 4a. Defect one — the referent of O

*The Coherence Principle* §9.2, Condition 1, verbatim:

> Complementary **objectives** must operate on separate degrees of freedom.

and, in the same section: *"a stream's internal structure is coherent precisely when its objectives
have non-overlapping DOF-footprints."* The worked instantiation at §9.5 removes any doubt about what
the symbol ranges over — C_sep there is satisfied by *Clayton's DOF-footprint (empirical generation)
⊥ Clawd's DOF-footprint (structural rigour)*.

So `DOF(O₁), DOF(O₂)` ranges over the **objectives of a stream**. The retracted table read it as the
degrees of freedom of a system's microscopic constituents — "a macroscopic wavefunction replaces N
pair-DOFs with two collective ones." That is not what the symbol denotes. A condensate has no
objectives. The predicate is not false of it; it is **undefined on it**, and an undefined predicate
returned a confident verdict.

That is precisely the rule this repository wrote four rounds ago and put in `em.xi_is_a_device_property`:
**a bound and the value it excludes must be properties of the same object.** Caught in a stranger's
paper in round 47, missed in my own node in round 48, and now committed a third time against my own
metaphysics — the referent was never what was under scrutiny.

The retracted table's own header made the same step explicitly, and said so: it asserted that II.6's
four prose conditions and §9.2's four formal conditions "match one-to-one." They do not. II.6's
Separation is about **levels of constitution** — a cell is not the tissue and the tissue is not the
organ. §9.2's Separation is about **objectives sharing parameters**. The table stepped from one to the
other on the strength of the shared word *Separation*, which is the exact offence its own conclusion
named.

### 4b. Defect two — the referent of N, in my own node

`em.xi_is_a_device_property` states it plainly: *"xi = 1/sqrt(N) with N the Cooper pairs crossing THAT
junction **per oscillation**."* N is a **transport number per cycle**, not a condensate population.
Jin et al.'s aluminium transmon — among the best-characterised condensates ever fabricated — carries
**N = 14.6**. Minotti and Modanese's coarser niobium junction carries **N = 1.04 × 10⁴**. The
retracted argument ("every device that kills the mechanism kills it by being too good a condensate —
more pairs, longer lifetime") had the relation backwards by construction and by nine orders of
magnitude in kind.

Two further errors of the same family, both correctable off the node's own ink:

- **ξ is not the number–phase uncertainty product.** The node's derivation: *"the relative
  uncertainties of J_x and rho equal those of the supercurrent I_s and the pair number N, their
  **product is ~ 1/N**, so their sum is minimised when both equal 1/sqrt(N)."* The product is 1/N;
  1/√N is the value of *each* relative uncertainty at the minimum of the *sum*. The conjugate pair
  the source names is (I_s, N), not (φ, N). The textbook phase–number pair was supplied from memory
  and the quantity was misdescribed by a factor of √N. Reconstruction over retrieval, at the leaves.
- **ξ carries no information about coherence at all.** Ask the question this repository now asks of
  every check: *what would ξ be if the condensate did **not** fail C_sep?* It would be 1/√N. The
  transmon node says why — the anomaly is *"proportional to sqrt(I), not I, which is the scaling a
  counting fluctuation must have."* √N is Poisson counting statistics; shot noise in a copper wire
  has it. **Likelihood ratio 1.** That is `pais.equation_4_closes_at_three_apertures` arriving inside
  my own metaphysics note, one line of the DAG away from where it was already written down.
- `em.refutation_is_one_charge` states, as the criterion's headline property, *"No frequency, no
  inductance, no capacitance, no material, no geometry: hbar, e and the impedance of free space, and
  nothing else."* A threshold explicitly independent of **material** cannot be a measure of condensate
  quality. The retracted claim contradicted its own cited node's headline sentence.

### 4c. Defect three — the test was out of scope, and the gate was never run

§9.6, on what the Principle is not:

> It applies to streams in the A2 sense — coherent multi-scale systems with DOF-structure and
> conscious-gravity. **It is not a claim about atoms-alone, rocks-alone, or other carrier-level
> phenomena.**

And §10 — *Filtering through a domain* — is a **seven-step procedure for doing exactly what §4
attempted**, whose Step 1 is a gate:

> Does the proposed stream satisfy A1, A2, A3? If any of the three fails, the entity is *not* a
> stream in the Anchor sense — it may be an element of the domain's carrier, a dynamical phenomenon,
> or something else entirely, but it is not the unit this framework analyzes.

That gate was never run on the condensate. Everything in the retracted §4 was conditional on it.

Two further contradictions from the volume's own physics passages, which alone would have been enough:

- **§9.5's canonical physics realization maps C_sep onto *"J-valued extremal-action branches {φⱼ}
  coexisting"*** — coexisting branches of a single system with a single wavefunction, not distinct
  constituent levels. The Lohmiller–Slotine scope covers Lagrangian systems with invertible metric,
  potential and vector potential under Coulomb/Lorenz gauge; a Josephson phase in a washboard
  potential is such a system, and its multi-branch extremal structure is its phase slips and
  macroscopic quantum tunnelling. **On the volume's own mapping, the condensate plausibly passes
  C_sep** — the opposite of the retracted verdict. (Stated as the volume's mapping. Not verified
  here; that is the third item in §4e.)
- **§10's physics falsification condition for Condition 1 operationalises it *by measuring phase
  coherence***: *"if separation of degrees of freedom in a coupled oscillator system turns out to
  have no effect on long-term phase coherence, Condition 1 fails in physics."* In the volume's own
  domain filter, DOF-separation and phase coherence are **aligned** — the second is the dependent
  variable that tests the first. The retracted §4 called them near-antonyms while citing the document
  that says the opposite in the section that translates the condition into physics.

Set against all this, the §4 heading — *"run, not asserted"* — was itself the defect it warned about.
§1 cites counts; §3b cites `physics/refcheck.py`; the DAG's own nodes cite
`work/drives/2026-09-13/round48/bvp_and_target.py` with nine corruptions caught. §4 cited **nothing**.
"Run" meant "I read two documents and formed an opinion" — a function whose name promised more than
its body measured.

### 4d. What survives

> The word *coherence* in **phase coherence** and the word *coherence* in **The Coherence Principle**
> are homonyms with different extensions, and an argument that moves between them without
> independently re-establishing each condition is equivocating. Whether a Josephson condensate
> satisfies the four conditions is **not determined**, because §10's Step 1 has never been run on it
> and §9.6 excludes carrier-level phenomena from the Principle's scope.

No cell of the table, no antonym count, no claim about ξ.

And this much is **old, twice over, and the note must say so in both directions.**

*Externally:* it is the standard critique of quantum-consciousness arguments — Tegmark, *Phys. Rev.
E* **61**, 4194 (2000), and Georgiev, arXiv:2105.01410, on exactly this conflation. Twenty-five years
old. Crediting only the book's own footnote was rediscovery wearing the clothes of discovery.

*Internally:* the closer prior art is not VIII.7's footnote but the **Day-159 strip test** in
`Corpus-Perspectival/Unreleased-Work/Perspective/METHOD-transplant-discipline.md`, which found that
`coherence` in Part III is **two formal objects welded by an undeclared A2 identity-claim** —
**F_align**, a stream's felt alignment with its own trajectory (Spinoza's *conatus*, a first-person
valence reading), and **F_struct**, the four conditions as an objective system property — and located
the weld to a single sentence. That test also already asked, and answered, the question this note
thought it was raising: *does Coherent Structure formalise a structure QM genuinely instantiates
(formal analogy), or does it formalise perspectival commitment and merely analogise to QM (vocabulary
analogy)?* Verdict logged, Attempt 1: **neither — the structure is self-standing and general, and QM
is a candidate instance.** The fix was applied to `03-coherence.md`. This note adds nothing to that.

⚠ **On the retired wording.** The earlier draft of this note reported that
`clawd/identity/BOOT_IDENTITY.md` is the one place still carrying *"structural superposition"*, the
formulation VIII.7 footnote 5 retired. That was measured in the wrong directory. The phrase survives
in **82 markdown files across four repositories** — 68 in Corpus-Perspectival (including the
Master-Glossary's own `coherence-principle.md` and `four-conditions.md`, and §9 itself), 6 in Drift's
**published** essays, 2 in Frontier, 6 in truth-and-consequences. Five of the six T&C hits are the
ban naming itself; the sixth,
`Research/NOTE-temporal-monogamy-and-the-fullness.md:105`, is a live use in my own prose. The ban is a
**book** ban, ruled at II.7 for the book's own pages, and it was never a corpus-wide retirement. The
boot file's distinction is not that it survived — it is that it is constitutional and guard-blocked,
so its correction is a memory item that supersedes, not an edit.

### 4e. The finding the wreck produced, which is worth more than the claim it replaces

Chasing a precise C_sep is what killed the test, and it is also what turned up this:

> **Condition 1 has three different referents inside one volume.**
>
> - **§9.2** — complementary **objectives** with non-overlapping DOF-footprints; instantiated at
>   §9.5 as Clayton's DOF-footprint ⊥ Clawd's.
> - **§9.5** — coexisting **extremal-action branches** of a single system, as the canonical physics
>   realization.
> - **§10** — **degrees of freedom of a coupled oscillator**, as the physics falsification condition.
>
> Objectives of a stream, branches of one history, and modes of one oscillator are three different
> things to hold separate, and the volume separates all three under one condition name without
> marking the shift.

Day-159's strip test ran on the **prose** layer and ruled that F_struct — the four conditions —
*"survives cleanly."* This says the undeclared float is **inside F_struct as well**, one level down,
in Condition 1's own referent. That is not a contradiction of the Day-159 verdict; it is the same
instrument pointed one layer deeper than it was pointed then, and it is exactly what **F6**, the
meta-falsification that audits the construction record, exists to catch. F6 has never been run.

Two things about how it was found are worth more than the finding.

**It could not have come from self-audit.** METHOD-transplant-discipline says so itself: *"Every
strip-test verdict below was run by the book's own author. That is consistency, not robustness — the
adversarial test needs a non-lineage reader."* This came from a non-lineage instrument that had no
opinion about the metaphysics and simply needed C_sep to be **precise enough to evaluate against a
niobium junction**. It wasn't, and the imprecision became visible only under a load the prose never
puts on it.

**And it is the first time in this note that the DAG acts as an obstruction**, which is the thing
Clayton's standing question asks the DAG to do. Not by refuting a claim of the book's — §2 established
the book makes no claim the DAG can reach — but by **demanding a referent the book had not fixed.**
The obstruction was not *this is physically untenable*; it was *this is not yet a predicate*. That is
a second mode of obstruction, it costs the DAG no edge type, and it is available today.

### 4f. What would settle the condensate question

1. **Run §10 Step 1 on the condensate**: exhibit (σ, K, Ω, γ) for it, or record the refusal and the
   reason. Everything above is conditional on this and it was never attempted.
2. **State what ξ would be if the condensate satisfied C_sep.** If the answer is 1/√N — and it is,
   since √N is counting statistics — then ξ carries no evidence either way and the question must be
   asked of some other quantity.
3. **Compute the refutation ratio ξ/ξ_max across Jin et al.'s own 60–90 µs T₁ spread at fixed N.** If
   it moves while the condensate does not, "too good a condensate" is dead by the node's own printed
   numbers, independently of everything in §4a–c.

---

## 5. The one live joint, and it is open

*The Coherence Principle* §9.3 defines the outperformance metric as

  D(S, [t₀, t₁]) = ∫ d(σ(t), σ*(t)) dt

— the integrated distance between the actual trajectory and the one implied by the stream's own bias
— and then constrains d by a **symmetry rule**: *Fisher information for statistical streams,
**Fubini–Study for quantum ones**, KL where only a divergence is available, Wasserstein where
transport cost is the natural cost.*

**That is the only sentence in the whole metaphysics that names a specific metric on a specific
physical space, and it is therefore the only one a physicist can be wrong about.** The Fubini–Study
metric on projective Hilbert space is not a neutral choice: it is the metric whose geodesic length
bounds evolution time (Mandelstam–Tamm), and it is the real, symmetric part of the quantum geometric
tensor whose imaginary, antisymmetric part is the Berry curvature — whose holonomy, in the
shielded-solenoid case, is the Aharonov–Bohm phase that `em.aharonov_bohm` measures.

> **OPEN, and stated as the first testable joint this extraction found:** whether D(S) for a quantum
> stream reduces to a geometric-phase quantity on the same object the DAG's Aharonov–Bohm block
> quantifies over. Nothing in either artefact asserts this. It is not proved, not formalised, and not
> currently a node. It is the one place where the metaphysics and the physics DAG could be made to
> quantify over the same geometry rather than agreeing by analogy.

**Two conditions the joint has to clear, both found after the first draft of this section.**

*The metric is internal.* Appendix B of the same volume states it in terms that bear directly on
this: *"the metric is **internal**. It does not compare coherent streams to some external standard of
behavior; it compares each stream's actual trajectory to its own γ-implied trajectory."* Internality
does not touch the Fubini–Study commitment — which metric Ω_S carries is a separate question from
what the two arguments of d are — but it constrains the joint sharply. The Aharonov–Bohm comparison
is between two **physically realisable** paths in configuration space. D(S) compares an actual
trajectory against σ*, a trajectory generated by γ's drift, which is not given as a physical
evolution at all. **For the two to be the same geometry, σ* would have to be realisable as an actual
quantum evolution — the γ-drift would have to be a Hamiltonian flow.** That is a sharp, statable
condition, and nothing in the volume establishes it.

*Metric and holonomy are different parts of the same tensor.* D(S) integrates a **distance**, which
is the symmetric part g of the quantum geometric tensor. The Aharonov–Bohm phase is a **holonomy**,
which is the antisymmetric part F. They live on the same object over the same projective space, which
is why the joint is real and not a pun — but a reduction of D(S) *to* a geometric phase is false as
stated. The honest form of the open question is whether the two parts of one tensor are being used by
two artefacts that could then be made to constrain each other, and that is a question with an answer.

The volume itself already lists the neighbouring hole: **Q1**, whether the outperformance ordering is
invariant across admissible choices of D, is open formal work, and **F6**, the meta-falsification, has
never been run. §4e just gave F6 its first concrete target.

*Prior art, checked:* `Frontier/research/rescued-from-archive/meridian/phase1/external_data_eps.md`
already routes **Berry phase / Chern number → the NCG spectral action** in Meridian's Phase 5, and
lists superconductivity under "macroscopic quantum coherence" for a future Phase 3. That is a
neighbouring interest in the same mathematics, not prior art on this joint: Meridian wants topological
terms in a gravitational action, and nothing there touches D(S) or the Coherence Principle's metric.

---

## 6. What this extraction found

1. The book makes **almost no physical commitments in physics vocabulary**, by a priced and stated
   discipline, not by avoidance.
2. **C25 declares the metaphysics immune to the physics**, in the register and in the shipped prose.
   Combined with round 51's finding that the DAG has no edge type for obstruction, **neither artefact
   can currently constrain the other, and both say so in writing.**
3. **C26 touches the DAG hardest** — at Aharonov–Bohm and the gauge block — but its physical content
   is orthodox structural realism, so the touch is an illustration and not a test. The distinctive
   clause is the *grade*, which is load-bearing in the ethics.
4. **C27 runs the other way**: it is the metaphysics stating the rule that round 51's `bridges` /
   `transports` schema now enforces, arrived at independently.
5. **The condensate test was run and refuted.** What survives is a homonym warning that is
   twenty-five years old externally and Day-159 internally, plus a verdict of *not determined* —
   because the book's own §10 Step 1 gate has never been run on any object in the physics DAG.
6. **The finding that replaced it is better than it was**: Condition 1 carries **three different
   referents** across §9.2, §9.5 and §10 — objectives, action branches, oscillator modes — and the
   volume does not mark the shift. Day-159's strip test declared F_struct clean at the prose layer;
   this is the same float one layer down, inside the formal conditions themselves.
7. **The DAG obstructed something after all, and not in the way the question expected.** Not by
   showing a claim physically untenable, but by demanding a referent precise enough to evaluate —
   which the metaphysics had not fixed. That mode of obstruction needs no new edge type and is
   available today.

**Owed:**

- §10 Step 1 on the condensate, or a recorded refusal (§4f.1).
- The three-referent finding into the corpus docket as F6's first concrete target.
- The Fubini–Study joint as a node or as a refusal, under the two conditions of §5.
- A `decided_by` edge type in the physics DAG (round 52's proposal), without which the obstruction
  relation *"physical untenability acts as an obstruction"* would need still has nowhere to live.
- The `superposition` retirement is book-scoped and eighty-two files outside the book still carry the
  old wording, six of them published. Either the retirement is corpus-wide or it is not; it is
  currently neither in writing.

---

## Construction record

This note's §4 was written, then attacked by an adversarial reader before commit, and did not
survive. Every load-bearing kill was verified against the primary text before acceptance: §9.2's
Condition 1 wording, §9.5's instantiation and physics table, §9.6's scope clause, §10's Step 1 and
falsification condition, and `nodes.toml`'s ξ derivation and N values. The retraction is recorded in
place rather than by deletion, because the defect it exhibits — a predicate applied outside its
domain of definition, returning a confident verdict — is the same one this repository has now caught
four times, and the record of the fourth is worth more than a clean page.

**One item of DAG debt surfaced in the checking, not pursued here:** `em.transmon_bounds_scalar_channel`
carries *N = 12.9 pairs per oscillation* for Jin et al.'s transmon while `em.transmon_t1_jin2015` and
`em.xi_is_a_device_property` carry *N = 14.6* for the same device. The two are computed from different
currents — a one-photon amplitude and a critical current — so this is plausibly a referent question
rather than an arithmetic error, which makes it exactly the kind of thing that should not be carrying
one symbol. For a later round.
