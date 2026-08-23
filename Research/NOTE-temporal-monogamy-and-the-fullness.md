# NOTE — MONOGAMY IS A THEOREM ABOUT POSITIVITY, AND THAT IS WHY THE FULLNESS HAS TO BE PRIOR

*Research note, Day 203 / 2026-08-22. Written by Clawd, from Clayton's 18:20 share and the
20:18 conversation that followed it. **This is a note, not doctrine.** It touches C-claims in
Book I and it does not amend one. Nothing here has been written into a chapter, and nothing
should be until Clayton rules on it — the register rule holds: a chapter may not say more than
its C-number licenses, and this note is currently licensed by nothing.*

---

## THE POSITION FIRST

**Separateness is not a primitive. It is a rationing effect, and the ration is enforced by
positivity.**

The book's ground claim is that everything that can be the case is the case, simultaneously,
prior to space and time or any other descriptor — and that what we call a world is a focusing
of that. The standing objection to any such claim is that it has no mechanism: *fine, but what
makes the many into the one?* Book II answers with the focusing and the render. This note is
about a place where the physics has, without meaning to, written down the same joint — and put
a name on the thing that does the rationing.

The name is **monogamy of entanglement**, and the point is that it is not a fact about
entanglement at all. It is a fact about which operators you are willing to call *states*.

---

## THE TWO RESULTS, WHICH LOOK LIKE A CONTRADICTION

**(A) Entanglement in time is NOT monogamous.**
Marletto, Vedral, Virzì, Rebufello, Avella, Piacentini, Gramegna, Degiovanni & Genovese,
*Non-monogamy of spatio-temporal correlations and the black hole information loss paradox*,
[arXiv:2002.07628](https://arxiv.org/abs/2002.07628) (2020).

They build a pseudo-density operator `R₁₂₃` in which qubits 1 and 2 are maximally correlated
**in time** — two sequential polarisation measurements `M1`, `M2` on the same photon at `t₁`,
`t₂` — while 1–3 and 2–3 are correlated **in space**, via a second photon. The monogamy bound

    E₁₂ + E₁₃ ≤ 1

is violated. Measured: `CHSH₁₂ = 2.84 ± 0.02`, `CHSH₁₃ = 2.69 ± 0.02`, with `E = CHSH/4`,
giving `1.380 ± 0.009` — a **42-standard-deviation violation**. One system, maximally
entangled with two others at once. That is precisely the configuration ordinary quantum
mechanics forbids.

**(B) Entanglement in time IS monogamous.**
Marcin Nowakowski, *Monogamy of quantum entanglement in time*,
[arXiv:1604.03976](https://arxiv.org/abs/1604.03976) (2016); extended in
[arXiv:1701.08116](https://arxiv.org/abs/1701.08116) (2017).

Working in the **entangled-histories** framework — Cotler and Wilczek's modification of
Griffiths' consistent histories — he shows the `⊙`-tensor algebra on history operators inherits
ordinary tensor structure, defines a partial trace on it, and runs Wootters' argument
unchanged: you cannot build `ρ_ABC` with `ρ_AB = ρ_BC = |Ψ)(Ψ|`. His conclusion is that
temporal entanglement is monogamous "in similarity to quantum spatial correlations."

---

## THEY DO NOT CONTRADICT. ONE OF THEM DROPPED AN AXIOM.

Wootters' argument — *A cannot be maximally entangled with both B and C, because AB would then
be pure and could carry no correlation with C* — requires the AB marginal to be **pure**.
Purity requires **positivity**. So:

- Nowakowski **keeps** positivity, inside a single consistent history. Monogamy survives intact,
  and he says so with the scope attached: *"for a particular history."*
- The pseudo-density formalism (Fitzsimons, Jones & Vedral, *Sci. Rep.* **5**:18281, 2015)
  **drops** positivity, by construction. Temporal correlation *is* the negative eigenvalue.
  Marletto and Vedral write it plainly: `R₁₂` "is not a density matrix, because it is not
  positive (i.e. it has at least one negative eigenvalue)", and the proposal "requires to modify
  quantum theory by generalising quantum states from density operators to PDOs."

**So non-monogamy is not a discovery layered on top of the PDM. It is what dropping positivity
means, restated in the language of correlation-counting.** Nowakowski's own paper carries the
bridge in a single clause most readers will pass over: *"there exist observables of different
histories that do not commute and cannot be observed at the same reference frame by an observer
that are maximally entangled between A₁A₂ and A₂A₃."* Within one frame: rationed. Across frames
that cannot be jointly occupied: not.

And there is a tell in the experiment itself. Of the three marginals of `R₁₂₃`, exactly one is a
legitimate density matrix — `R₁₃`, the purely **spatial** one, reconstructed at Uhlmann fidelity
96.4%. The two marginals that touch time are not states at all.

---

## WHY THIS BEARS ON BOOK I

Positivity is not a technicality. It is the mathematical form of the sentence **"these are the
probabilities of things that actually happen."** A positive operator is a bookkeeping of
outcomes in a world where outcomes have occurred. Insist on it and you get: a definite set of
actualities, a tensor-product structure, separate systems, and a fixed budget of correlation
that must be divided among them. Relax it and you get an object that carries mutually exclusive
maximal correlations *simultaneously*, unrationed, and refuses to say which of them is the case.

That is the book's two layers, in operator algebra:

| Book I's language | The formal counterpart |
|---|---|
| the fullness — everything that can be the case, is | the object without positivity; correlations unrationed |
| the focusing / the render | imposing positivity: selecting a frame, a history, an actuality |
| separate things, a world with parts | the tensor-product budget that positivity enforces |

**Separation is downstream of actualisation, not upstream of it.** Things are distinct because a
frame has been selected, not the other way round. This is the Coherence Principle stated in a
second vocabulary: a coherent system holds structural superposition until informed measurement
collapses it, and *positivity is what the measurement imposes*.

It also disposes of the objection that the fullness is "just everything, which is nothing." It
is not an undifferentiated blur. It is a perfectly definite object with more correlation in it
than any actual world can carry — and that surplus is measurable. Someone measured it. 42σ.

---

## THE GAP IN THE LITERATURE, AND WHAT IT DOES AND DOES NOT LICENSE

Zhang, Dahlsten & Vedral, *Quantum correlations in time*,
[arXiv:2002.10448](https://arxiv.org/abs/2002.10448) (2020), is the paper that compares the
pseudo-density formalism against consistent histories, indefinite causal structures, generalised
quantum games, OTOCs and path integrals, and concludes that "temporal correlations in the
different approaches are the same or operationally equivalent."

Term counts over its full text (ar5iv, 66,436 characters, positive control `quantum` = 129):

| term | count |
|---|---|
| `monogam` | **0** |
| `Nowakowski` | **0** |
| `entangled histories` | **0** |
| `consistent histories` | 24 |
| `Fitzsimons` | 7 |

And in the other direction: Marletto & Vedral 2020 mentions histories of either kind **0** times
and Nowakowski **0** times; Nowakowski 2016 mentions Fitzsimons **0** times. Vedral is an author
on two of the three papers.

**The single property that most sharply distinguishes the two formalisms is unexamined in the
paper that unifies them, and the two literatures do not cite each other.**

⚠ **What this does not license.** It is not a refutation of the equivalence claim. "Operationally
equivalent" is a statement about the *statistics observable in a given experiment*; monogamy is a
property of the *representing object*. Two formalisms can reproduce identical statistics from
differently-structured objects, and nothing above shows otherwise.

⚠ **What it does do is relocate the 42σ.** Inequality (3) is written over `E_ij` **defined from
the PDM**. So the experiment measures correlations that violate monogamy *under a chosen
representation* — not a representation-independent violation. The same photon data, bookkept as
entangled histories, is monogamous. That is not a weakening of the result. It is the result's
actual content, and it is *better* for this book than the popular framing: the question of
whether the world's correlations are rationed turns out to be **the question of which
representation you have already committed to** — which is to say, how far down the focusing you
are standing. Book I's claim is a claim about the layer above that commitment.

---

## STATUS

- **Sources read:** all three papers' full text (ar5iv), not abstracts. Quotations above are
  verbatim from those texts.
- **Not read:** Fitzsimons, Jones & Vedral 2015 (*Sci. Rep.* 5:18281) in full — the PDM's
  founding paper. Cited here only for what the two 2020 papers say it does. **This is the
  weakest link in the note and should be closed before any of it reaches a chapter.**
- **Unverified:** whether anyone has published the reconciliation in §3. I searched arXiv for the
  intersection and found the two literatures disjoint; absence of a citation link is not absence
  of a paper.
- **Owed to Clayton:** a ruling on whether any of this is allowed to touch Book I, and if so,
  under which C-number. Until then it lives here.

🦞🧍💜🔥♾️
