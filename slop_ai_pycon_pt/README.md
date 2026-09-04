# Most of Your AI Output Is Slop (and how to optimise it)

_PyCon Portugal 2026 · Laís Carvalho ([@lais_bsc](https://twitter.com/lais_bsc))_

## The talk

Slop is output that is **fluent, plausible, and untethered from intent**. Not necessarily wrong — just off. This talk walks through _why_ language models produce it, and what we can do about it as the people driving them.

The journey runs through four acts:

- **Why slop happens.** From a 15-line Markov chain that faked Guardian headlines in 2020, to Word2Vec vector spaces, to Hofstadter's three levels of a message — and why a model that never fails to decode still fails to decode _your_ intent.
- **What you can fix yourself.** Vocabulary, skills and plugins, `AGENTS.md`, connectors, and MCP. Practical unhobbling for the model you already have.
- **You stop pasting.** The same prompt run twice — same model, same words, only the reach changed. Slop isn't only a prompt problem; it's a system-around-the-prompt problem.
- **So what's our job?** Define the problem, set the constraints, define good, verify the results, take responsibility. You can only delegate as far as your verifier reaches.

## Slides

[Download the slides (PDF)](https://drive.google.com/file/d/1EdmlxRHPNw_mFwXsGGNjyIXyHyOPfJyL/view?usp=sharing)

## Demos

- **[laisbsc/news_faker](https://github.com/laisbsc/news_faker)** — the original Markov chain fake-headlines generator, first shown at Python Pizza NYE 2020. What a language model looks like when its entire model of the world is _one word of context_.
- **[laisbsc/demos](https://github.com/laisbsc/demos)** — "the same prompt, twice." Same model, same words; the only change is what it can reach. Used in Act 3 to show that slop travels with the harness, not just the prompt.
- **[`demo_word2vec/`](./demo_word2vec)** — a small cosine-similarity demo over GloVe vectors, used on stage to make "a word is a point in a vector space" concrete.

## About

Laís Carvalho is a developer advocate at Pydantic, a PSF Fellow and Community Service Award recipient, EuroPython Fellow, and long-time Python community organiser. She is currently running for the PSF board.

_Obrigada, PyCon PT!_
