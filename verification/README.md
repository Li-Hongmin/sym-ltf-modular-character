Numerical check of identity (1) in "A Single Modular Character Is Complete for SYM∘LTF Counting" (version 2).

Run: python3 verify_construction.py (Python 3.8+, standard library only).

The script builds the threshold gates U_j exactly as in the proof of Theorem 1 for 30 random instances with h<=4 and q<=7, evaluates the character expectation by enumerating all inputs, and compares it with R^{-1} times the acceptance probability. The comparison is in floating point with tolerance 1e-9; it is a numerical check, not exact-arithmetic verification and not a proof. The general result rests on the proof in the paper.
