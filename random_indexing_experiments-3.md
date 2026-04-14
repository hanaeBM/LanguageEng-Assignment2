# Random Indexing — Experiment Results

## Base Configuration
- Dimension: 2000
- Non-zero: 100
- Window: left=2, right=2
- Normalized vectors
- Corpus: Harry Potter 1-7

---

## 1. Similarity Metrics (normalized vectors)

### Cosine
| Word | Neighbors |
|------|-----------|
| harry | percy (0.019), hagrid (0.020), snape (0.025), neville (0.026) |
| gryffindor | slytherin (0.081), house (0.127), ravenclaw (0.128), school (0.135) |
| chair | seat (0.053), bag (0.105), hand (0.107), trunk (0.119) |
| wand | head (0.059), hand (0.060), nose (0.073), leg (0.084) |
| good | nice (0.063), quick (0.067), funny (0.068), quiet (0.095) |
| enter | leave (0.098), break (0.119), according (0.127), fight (0.130) |
| on | in (0.041), from (0.046), over (0.055), through (0.061) |
| school | house (0.057), class (0.060), point (0.070), fire (0.074) |

### Euclidean (normalized)
| Word | Neighbors |
|------|-----------|
| harry | percy (0.194), hagrid (0.203), neville (0.214), snape (0.219) |
| gryffindor | slytherin (0.410), house (0.514), ravenclaw (0.514), school (0.517) |
| chair | seat (0.314), bag (0.439), hand (0.449), broom (0.480) |
| wand | hand (0.336), head (0.341), nose (0.372), leg (0.395) |
| good | nice (0.352), quick (0.364), funny (0.373), quiet (0.435) |
| enter | leave (0.442), owing (0.484), according (0.489), break (0.492) |
| on | in (0.272), from (0.289), over (0.319), through (0.342) |
| school | house (0.327), class (0.328), point (0.347), fire (0.367) |

### Manhattan (normalized)
| Word | Neighbors |
|------|-----------|
| harry | hagrid (6.48), percy (6.66), snape (7.30), neville (7.56) |
| gryffindor | slytherin (13.20), school (16.88), house (17.07), ravenclaw (17.29) |
| chair | seat (11.04), hand (14.59), bag (15.15), trunk (15.26) |
| wand | hand (11.19), head (11.46), nose (13.14), body (13.61) |
| good | nice (12.50), funny (13.03), quick (13.45), well (14.57) |
| enter | leave (15.31), according (16.37), fight (16.81), owing (17.23) |
| on | in (9.36), from (9.86), over (11.04), into (11.62) |
| school | house (10.77), class (11.13), point (12.37), castle (12.64) |

### Observation
Cosine produces semantically meaningful neighbors with small distances (0.02–0.13). With normalized vectors, Euclidean distances are now in the expected range (0–2) and find the same semantic neighbors as cosine. Manhattan distances are larger (6–17) even with normalized vectors  this is expected since Manhattan is not bounded between 0 and 2 for normalized vectors (theoretical max = 2×dim). All three metrics find coherent neighbors once vectors are properly normalized, but cosine remains the most compact and interpretable.

### Conclusion
**Cosine is the preferred metric**  it captures semantic similarity well, is invariant to vector magnitude, and produces the most compact distances. Euclidean works correctly with normalized vectors and finds similar neighbors. Manhattan also works but produces larger raw distances due to its unbounded nature in high dimensions. All three metrics agree on the nearest neighbors once normalization is applied.

---

## 2. Normalized vs Non-normalized Vectors (cosine)

### Cosine — normalized
| Word | Neighbors |
|------|-----------|
| harry | percy (0.019), hagrid (0.020), snape (0.025), neville (0.026) |
| gryffindor | slytherin (0.081), house (0.127), ravenclaw (0.128), school (0.135) |
| chair | seat (0.053), bag (0.105), hand (0.107), trunk (0.119) |
| wand | head (0.059), hand (0.060), nose (0.073), leg (0.084) |
| good | nice (0.063), quick (0.067), funny (0.068), quiet (0.095) |
| enter | leave (0.098), break (0.119), according (0.127), fight (0.130) |
| on | in (0.041), from (0.046), over (0.055), through (0.061) |
| school | house (0.057), class (0.060), point (0.070), fire (0.074) |

### Cosine — non-normalized
| Word | Neighbors |
|------|-----------|
| harry | percy (0.021), hagrid (0.022), neville (0.026), snape (0.027) |
| gryffindor | slytherin (0.079), house (0.132), ravenclaw (0.135), school (0.138) |
| chair | seat (0.053), hand (0.108), bag (0.111), cupboard (0.116) |
| wand | head (0.058), hand (0.061), nose (0.070), leg (0.081) |
| good | nice (0.060), quick (0.066), funny (0.069), quiet (0.095) |
| enter | leave (0.102), owing (0.121), fight (0.122), break (0.124) |
| on | in (0.039), from (0.043), over (0.056), through (0.059) |
| school | class (0.059), house (0.059), point (0.069), burrow (0.075) |

### Observation
With cosine, normalized and non-normalized vectors give very similar results. Neighbors are almost identical with only minor differences in ordering and distances. This confirms that cosine is naturally invariant to magnitude.

### Conclusion
**Normalization has little effect on cosine**. Both produce semantically meaningful results. However, normalization is still recommended for consistency when comparing metrics.

---

## 3. Dimensionality and Non-zero Proportion (cosine, normalized)

### Dimension 10

| Config | harry | gryffindor | good | school |
|--------|-------|------------|------|--------|
| nz=1 (5%) | fudge, polish, seamus, fred | glancing, agree, papers, bows | hopeless, very, tabby, shaken | order, whereabouts, students, uselessly |
| nz=1 (10%) | neville, dumbledore, snape, yaxley | hilltop, christmas, animal, rat | anyway, padfoot, morfin, dreadful | class, air, grave, down |
| nz=2 (20%) | fudge, percy, hagrid, bellatrix | cause, rushed, harrys, run | fair, funny, hedwig, startled | owlery, horcrux, glossy, class |
| nz=5 (50%) | percy, fudge, wormtail, ron | attitude, calmed, arguing, tangled | nice, fervently, swallowed, hunter | boundaries, beater, waters, cottage |

### Dimension 50

| Config | harry | gryffindor | good | school |
|--------|-------|------------|------|--------|
| nz=2 (5%) | percy, neville, snape, hermione | slytherin, ravenclaw, first-years, school | quick, nice, clever, quiet | others, class, dementors, fire |
| nz=5 (10%) | hagrid, neville, percy, snape | slytherin, house, library, quidditch | quick, nice, funny, lovely | class, book, house, first |
| nz=10 (20%) | percy, hagrid, dumbledore, neville | slytherin, ravenclaw, house, students | nice, quick, quiet, lovely | house, wedding, feast, others |
| nz=25 (50%) | percy, neville, hagrid, snape | slytherin, fire, house, owls | quick, funny, lovely, nice | class, house, fire, dementors |

### Dimension 100

| Config | harry | gryffindor | good | school |
|--------|-------|------------|------|--------|
| nz=5 (5%) | percy, hagrid, neville, snape | slytherin, ravenclaw, house, plan | quick, funny, quiet, nice | house, point, class, headmaster |
| nz=10 (10%) | percy, neville, hagrid, dumbledore | slytherin, house, unconscious, office | funny, quick, nice, quiet | class, house, point, library |
| nz=20 (20%) | percy, hagrid, snape, dumbledore | slytherin, ravenclaw, house, office | funny, nice, quiet, very | house, story, class, book |
| nz=50 (50%) | percy, hagrid, snape, dumbledore | slytherin, ravenclaw, boys, school | nice, quick, funny, lovely | class, dementors, house, point |

### Dimension 1000

| Config | harry | gryffindor | good | school |
|--------|-------|------------|------|--------|
| nz=50 (5%) | percy, hagrid, snape, neville | slytherin, house, school, ravenclaw | nice, quick, funny, quiet | house, class, point, fire |
| nz=100 (10%) | percy, hagrid, snape, neville | slytherin, ravenclaw, house, school | nice, quick, funny, lovely | class, house, point, fire |
| nz=200 (20%) | percy, hagrid, snape, neville | slytherin, ravenclaw, house, school | nice, quick, funny, quiet | house, class, point, fire |
| nz=500 (50%) | percy, hagrid, neville, snape | slytherin, ravenclaw, house, school | nice, funny, quick, quiet | class, house, point, fire |

### Dimension 2000, non-zero 100 (5%) — baseline
See section 1.

### Observation
- **Dimension 10** — results are poor regardless of non-zero proportion. Neighbors of `gryffindor` are random words with no semantic relation. The space is too small and random vectors collide too often.
- **Dimension 50** — noticeable improvement. `gryffindor` → `slytherin` starts appearing, but some nonsensical neighbors remain.
- **Dimension 100** — good results. Most neighbors are semantically meaningful. Higher non-zero proportions (20-50%) don't significantly improve over 10%.
- **Dimension 1000** — very close to the baseline (2000). Results are stable across all non-zero proportions, suggesting diminishing returns beyond 10% non-zero.
- **Non-zero proportion** — has less impact than dimensionality. Within a given dimension, varying from 5% to 50% produces similar quality results.

### Conclusion
Dimensionality is the dominant factor, higher is better up to ~1000, after which gains diminish. Non-zero proportion has limited impact; 10% is a good default. Dimension 10 is clearly insufficient for meaningful word representations.

---

## 4. Window Size (cosine, normalized, dim=2000)

### Window 0 (symmetric)
All words return the same random neighbors (`'wanted`, `hurry-ing`, `colour`...) with distance 1.0. No context is captured — all context vectors remain zero and cannot be compared meaningfully.

### Window 3 (symmetric)
| Word | Neighbors |
|------|-----------|
| harry | dumbledore (0.017), hagrid (0.018), snape (0.020), neville (0.021) |
| gryffindor | slytherin (0.061), house (0.090), ravenclaw (0.094), school (0.097) |
| good | nice (0.050), quick (0.056), funny (0.061), mad (0.064) |
| school | house (0.055), class (0.060), point (0.066), last (0.070) |

### Window 10 (symmetric)
| Word | Neighbors |
|------|-----------|
| harry | snape (0.009), malfoy (0.011), dumbledore (0.011), neville (0.011) |
| gryffindor | slytherin (0.018), by (0.024), house (0.025), two (0.026) |
| good | nice (0.015), here (0.016), dumbledore (0.016), no (0.017) |
| school | house (0.017), first (0.020), hogwarts (0.021), place (0.021) |

### Asymmetric windows (left < right — more future context)

| Config | harry | gryffindor | good |
|--------|-------|------------|------|
| L=1, R=3 | percy, hagrid, snape, neville | slytherin, ravenclaw, house, school | quick, nice, funny, dobby |
| L=1, R=5 | snape, percy, hagrid, neville | slytherin, ravenclaw, house, school | nice, funny, quick, fine |
| L=1, R=10 | snape, neville, dumbledore, malfoy | slytherin, house, class, two | nice, funny, quick, no |
| L=2, R=5 | snape, percy, hagrid, neville | slytherin, school, house, ravenclaw | nice, funny, quick, hagrid |
| L=2, R=10 | snape, neville, dumbledore, hagrid | slytherin, house, by, class | nice, hagrid, funny, fudge |

### Asymmetric windows (left > right — more past context)

| Config | harry | gryffindor | good |
|--------|-------|------------|------|
| L=5, R=3 | hagrid, dumbledore, moody, percy | slytherin, house, ravenclaw, school | nice, funny, quick, very |
| L=5, R=10 | snape, malfoy, neville, dumbledore | slytherin, house, way, by | nice, no, really, funny |

### Observation
- **Window 0** — no context, all vectors are zero → completely useless, distance 1.0 for all pairs.
- **Window 3** — good syntactic neighbors. `good` → `nice`, `quick`, `funny` (same grammatical category). Distances slightly larger than window 2 baseline.
- **Window 10** — broader semantic neighbors. `harry` → `snape`, `malfoy`, `dumbledore` (characters who interact with harry). Common words like `by`, `two`, `no` start appearing as noise. Distances are smaller due to more shared context.
- **Asymmetric (L < R)** — emphasizes what follows the word. Increasing right window progressively shifts neighbors from syntactic to semantic.
- **Asymmetric (L > R)** — emphasizes what precedes the word. `harry` gets more antagonist characters like `moody`, `snape` as neighbors.

### Conclusion
- **Window 0** is useless — no context means no information.
- **Small windows (2-3)** capture syntactic similarity (same POS, same grammatical role).
- **Large windows (10)** capture broader semantic/topical similarity but introduce noise from common words.
- **Asymmetric windows** shift the focus between preceding and following context, which can be useful depending on the language structure being studied.
- **Best overall**: symmetric window of 2-3 for syntactic tasks, 5-10 for semantic tasks.

---

## General Conclusion

- **Metric**: cosine is the best, robust with or without normalization, invariant to vector magnitude
- **Normalization**: essential for euclidean and manhattan; cosine is unaffected
- **Dimension**: larger = better quality up to ~1000; beyond that gains diminish; 10 is too small
- **Non-zero proportion**: limited impact; 10% is a reliable default
- **Window size**: window 0 = useless; small (2-3) = syntactic; large (10) = semantic; asymmetric captures directional context

---

## 5. Word2Vec Results (cosine, normalized, dim=50, epochs=5)

| Word | Neighbors |
|------|-----------|
| harry | griphook (0.210), he (0.243), ron (0.248), malfoy (0.259) |
| gryffindor | slytherin (0.165), ravenclaw (0.171), tower (0.194), goal (0.268) |
| chair | seat (0.212), bunk (0.224), hiss (0.260), candlelight (0.262) |
| wand | jaw (0.241), tongue (0.259), chest (0.263), wrist (0.266) |
| good | bad (0.154), nice (0.207), valuable (0.207), lovely (0.211) |
| enter | leave (0.203), pass (0.224), steal (0.226), join (0.252) |
| on | sprawled (0.225), upon (0.279), onto (0.285), top (0.289) |
| school | hogwarts (0.175), feast (0.228), house (0.235), orphanage (0.257) |

### Comparison: Random Indexing vs Word2Vec

| Word | Random Indexing (best) | Word2Vec |
|------|----------------------|----------|
| harry | percy, hagrid, snape, neville | griphook, he, ron, malfoy |
| gryffindor | slytherin, ravenclaw, house, school | slytherin, ravenclaw, tower, goal |
| good | nice, quick, funny, quiet | bad, nice, valuable, lovely |
| school | house, class, point, fire | hogwarts, feast, house, orphanage |
| wand | head, hand, nose, leg | jaw, tongue, chest, wrist |
| enter | leave, break, fight | leave, pass, steal, join |

### Observation
- Word2Vec distances are generally larger (0.15–0.29) than Random Indexing (0.02–0.13), suggesting less tight clusters — likely due to fewer epochs or smaller dimension (50 vs 2000).
- Word2Vec finds some meaningful semantic neighbors (`school` → `hogwarts`, `gryffindor` → `slytherin`) that are arguably better than Random Indexing.
- Some Word2Vec results are unexpected (`wand` → `jaw`, `tongue`) — these are body parts that appear in similar syntactic positions, suggesting the model has learned some distributional patterns but may need more training.
- `good` → `bad` is interesting, Word2Vec captures antonyms as well as synonyms since they appear in similar contexts.

### Conclusion
Random Indexing produces more consistent results with the default configuration (dim=2000). Word2Vec has more potential but requires more training (more epochs, larger dimension) to match the quality. With more training data and epochs, Word2Vec typically outperforms Random Indexing as it learns non-linear relationships between words.

---

## 6. Multilingual Word Embeddings Results

### Configuration
- Dataset: 500 aligned English-Spanish sentences
- Embeddings: pre-trained FastText (mini.en.vec, mini.es.vec)
- Metric: cosine distance

### Accuracy Results

| Method | EN→ES Top-1 | EN→ES Top-3 | ES→EN Top-1 | ES→EN Top-3 |
|--------|-------------|-------------|-------------|-------------|
| Baseline (Simple Mean) | 25.00% | 41.60% | 20.60% | 31.20% |
| TF-IDF Weighted | 37.80% | 52.80% | 32.20% | 49.00% |
| Mean-Centered (Simple) | **72.20%** | **85.60%** | **75.20%** | **87.00%** |
| Mean-Centered + TF-IDF | 60.20% | 72.40% | 61.40% | 71.00% |

### Failed Sentences (k=3)

**Baseline — EN→ES failures:**
- "By his own marriage, likewise, which happened soon afterwards, he added to his wealth." (idx:5)
- "The old gentleman died: his will was read, and like almost every other will, gave as much disappointment as pleasure." (idx:54)
- "She was sensible and clever; but eager in everything: her sorrows, her joys, could have no moderation." (idx:34)

**Baseline — ES→EN failures:**
- "Además, su propio matrimonio, ocurrido poco después, lo hizo más rico aún." (idx:41)
- "Murió el anciano caballero, se leyó su testamento y, como casi todos los testamentos, éste dio por igual desilusiones y alegrías." (idx:25)
- "No fue más lo que sobrevivió a su tío, y diez mil libras..." (idx:30)

**Mean-Centered — EN→ES failures:**
- "By his own marriage, likewise, which happened soon afterwards, he added to his wealth." (idx:5)
- "They encouraged each other now in the violence of their affliction." (idx:6)
- "Perhaps it would have been as well if he had left it wholly to myself." (idx:5)

**Mean-Centered + TF-IDF — EN→ES failures:**
- "He meant not to be unkind, however, and, as a mark of his affection for the three girls, he left them a thousand pounds a-piece." (idx:81)
- "When he gave his promise to his father, he meditated within himself to increase the fortunes of his sisters by the present of a thousand pounds a-piece." (idx:11)
- "No sooner was his father's funeral over, than Mrs. John Dashwood, without sending any notice..." (idx:20)

### Observations

**Baseline (25% / 20.6%)** — Poor results. Simple averaging loses word order and gives equal weight to all words including common ones like "the", "a", "is" which dominate the centroid and add noise.

**TF-IDF (37.8% / 32.2%)** — Better than baseline. Down-weighting frequent words and up-weighting rare, informative words gives a more meaningful sentence representation.

**Mean-Centered Simple (72.2% / 75.2%)** — Best results by far. Subtracting the global mean removes the "bias" shared by all sentences (common words, general language patterns) and leaves only the distinctive semantic content of each sentence. This makes translations much easier to align.

**Mean-Centered + TF-IDF (60.2% / 61.4%)** — Surprisingly worse than Mean-Centered alone. TF-IDF already modifies the distribution of word weights, and combining it with mean-centering may over-correct or introduce instability in the centroid computation.

### Why Mean-Centering works so well
All sentences in a language share a common "linguistic bias", frequent words, common grammatical structures — that pushes all sentence vectors in a similar direction. By subtracting the mean, we remove this shared component and expose the true semantic differences between sentences, making cross-lingual alignment much more accurate.

### Question: Which mean to subtract for Mean-Centered TF-IDF?
We should subtract the **TF-IDF weighted mean** (not the original mean), because the TF-IDF vectors live in a different space than the simple averages. Subtracting the mean of the TF-IDF vectors correctly centers that specific representation.

### Conclusion
Mean-centering is the most impactful transformation, it dramatically improves alignment from ~25% to ~72%. TF-IDF alone helps but is not sufficient. Combining both does not always improve results, suggesting the two methods partially address the same problem (dominance of frequent words).
