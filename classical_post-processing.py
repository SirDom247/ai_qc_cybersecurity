# Extract periodicity from Shor Experiment results

from math import gcd
from fractions import Fraction

# Function to find the period (r) from quantum results
def extract_period(counts, a, N):
    """
    Extracts the period 'r' from the measurement results.
    Arguments:
        counts (dict): Measurement results from the quantum circuit.
        a (int): Chosen co-prime base.
        N (int): Number to be factorized.
    Returns:
        int: The period 'r', or None if no valid period is found.
    """
    # Sort measurement results by frequency
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    measured_values = [int(key, 2) for key, _ in sorted_counts]

    for value in measured_values:
        # Normalize the measured value to a fraction of 2^num_qubits
        frac = Fraction(value, 2 ** num_qubits).limit_denominator()
        r_candidate = frac.denominator

        # Check if the candidate satisfies a^r ≡ 1 (mod N)
        if pow(a, r_candidate, N) == 1:
            return r_candidate

    return None  # If no valid period is found

# Function to find factors based on the period
def find_factors(N, r, a):
    """
    Finds the factors of N using the period 'r' and base 'a'.
    Arguments:
        N (int): Number to factorize.
        r (int): The period of a^x mod N.
        a (int): The chosen co-prime base.
    Returns:
        tuple: A tuple of factors (factor1, factor2), or None if not found.
    """
    if r is None or r % 2 != 0:
        return None  # Period must be even to proceed

    # Compute potential factors
    factor1 = gcd(pow(a, r // 2) - 1, N)
    factor2 = gcd(pow(a, r // 2) + 1, N)

    if factor1 > 1 and factor2 > 1 and factor1 * factor2 == N:
        return factor1, factor2
    return None

# Classical Post-Processing
r = extract_period(counts, a, N)
if r:
    factors = find_factors(N, r, a)
    if factors:
        print(f"Factors of {N}: {factors[0]} and {factors[1]}")
    else:
        print("Failed to find factors. Try another value of 'a'.")
else:
    print("Failed to extract a valid period.")

