"""
Cosine similarity between word vectors — live demo.
Dependencies: numpy + the Python standard library. Nothing else.

SETUP:

    curl -O https://nlp.stanford.edu/data/glove.6B.zip     # 822 MB, one time
    unzip glove.6B.zip glove.6B.100d.txt                   # keep just this one
    python3 cosine_demo.py --check                         # confirm it loads

The file is plain text: one line per word, the word then 100 numbers.
Lines are ordered by how often the word appeared in the training corpus,
so reading the first N lines gives you the N most common words.

These vectors are GloVe (Pennington, Socher & Manning, EMNLP 2014), trained on
Wikipedia + Gigaword. Not word2vec — a different training objective, the same
resulting idea: a word is a point, similarity is an angle.
"""

import argparse
import math

import numpy as np

VECTOR_FILE = "glove.6B.100d.txt"
VOCAB_LIMIT = 50_000          # how many lines to read; None = all 400k

PAIRS = [
    ("lisbon", "rome"),     # same kind of thing: two cities
    ("lisbon", "portugal"),        # related, different kind of thing
    ("lisbon", "potato"),       # unrelated
]

NEIGHBOURS_OF = "lisbon"


def load_vectors(path, limit=None):
    """Read a GloVe text file into {word: numpy array}."""
    vectors = {}
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if limit is not None and i >= limit:
                break
            word, *numbers = line.rstrip().split(" ")
            vectors[word] = np.asarray(numbers, dtype=np.float32)
    return vectors


def cosine(u, v):
    """Cosine of the angle between two vectors. Magnitude divides out."""
    return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))


def nearest(vectors, word, topn=5):
    """The words at the smallest angle to `word`."""
    target = vectors[word]
    scored = ((w, cosine(target, v)) for w, v in vectors.items() if w != word)
    return sorted(scored, key=lambda pair: pair[1], reverse=True)[:topn]


def main(check=False):
    print(f"reading {VECTOR_FILE} ...")
    vectors = load_vectors(VECTOR_FILE, VOCAB_LIMIT)
    dims = len(next(iter(vectors.values())))
    print(f"{len(vectors):,} words, {dims} dimensions\n")

    if check:
        missing = [w for pair in PAIRS for w in pair if w not in vectors]
        print("missing words:", missing or "none — ready for the talk")
        return

    print(f"{'word A':<10} {'word B':<10} {'cosine':>8} {'angle':>8}")
    print("-" * 40)
    for a, b in PAIRS:
        if a not in vectors or b not in vectors:
            print(f"{a:<10} {b:<10}   not in vocabulary")
            continue
        sim = cosine(vectors[a], vectors[b])
        angle = math.degrees(math.acos(max(-1.0, min(1.0, sim))))
        print(f"{a:<10} {b:<10} {sim:>8.3f} {angle:>7.1f}°")

    print(f"\nclosest to '{NEIGHBOURS_OF}':")
    for word, sim in nearest(vectors, NEIGHBOURS_OF):
        print(f"  {word:<14} {sim:.3f}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true",
                   help="verify the file loads and the demo words exist")
    main(**vars(p.parse_args()))
