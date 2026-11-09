# A Single Modular Character Is Complete for SYM∘LTF Counting

[![verify](https://github.com/Li-Hongmin/sym-ltf-modular-character/actions/workflows/verify.yml/badge.svg)](https://github.com/Li-Hongmin/sym-ltf-modular-character/actions/workflows/verify.yml) [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24054533-blue)](https://doi.org/10.5281/zenodo.24054533)

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo) · ORCID [0000-0003-0228-0600](https://orcid.org/0000-0003-0228-0600)

Main result of the manuscript: for SYM∘LTF circuits, estimating a single modular character of the bottom-gate sum is as hard as the general counting problem.

- Manuscript on rStation: <https://rstation.ai/problems/computer_science/papers/1/v2> (version 2)
- Archived on Zenodo: concept DOI [10.5281/zenodo.24054533](https://doi.org/10.5281/zenodo.24054533) (all versions); this repository mirrors version 2, DOI [10.5281/zenodo.24054538](https://doi.org/10.5281/zenodo.24054538)

## Contents

- `paper/paper.md`, `paper/sym-ltf-modular-character.pdf` — the manuscript (version 2).
- `verification/` — the supplement of that version, unpacked unchanged; its own README describes each file.
- `.github/workflows/verify.yml` — reruns every check below on each push.

## What the programs check

| Check | Command (run inside `verification/`) |
|---|---|
| Numerical check of identity (1) | `python verify_construction.py` |

The programs check the finite and exact computations used in the manuscript; the mathematical arguments are those written in the paper.

## Reproducing

```sh
cd verification
python verify_construction.py
```

Requirements: Python 3.9+. Run the commands from a copy if you want to keep the recorded outputs untouched.

## Cite

```bibtex
@misc{li2026symltfmodularcharacter,
  author    = {Li, Hongmin},
  title     = {A Single Modular Character Is Complete for SYM∘LTF Counting},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24054533},
  url       = {https://doi.org/10.5281/zenodo.24054533}
}
```

## License

Manuscript and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code: MIT (see `LICENSE`).
