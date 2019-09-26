from math import gcd
from functools import reduce
import random
import time

aperys_constant_20dec = 1.20205690315959428539

def estimate_aperys_constant(trials):
    """Estimate Apéry's constant, a constant used in quantum electrodynamics and the value of zeta(3).
       It is approximately equal to 1.20205 69031.
       You can estimate Apéry's constant by drawing three random numbers 100 times. Keep track of how many times
       the numbers are coprime (GCD == 1) Apéry's constant is roughly (# trials) / (# coprime)
    """
    times_coprime = 0
    for _ in range(trials):
        num1, num2, num3 = random.randint(1, 500), random.randint(1, 500), random.randint(1, 500)
        if reduce(gcd, (num1, num2, num3)) == 1:
            times_coprime += 1
    print(f"\n# Trials: {trials}\n# Coprime: {times_coprime}")
    return trials / times_coprime


if __name__ == "__main__":
    print("Apéry's Constant Estimator\n")
    trials = int(input("How many trials to do? "))

    start = time.time()
    estimation = estimate_aperys_constant(trials)
    print(f"Apéry's constant estimation: {estimation}")
    print(f"Difference: {abs(estimation - aperys_constant_20dec)}")
    print(f"\nTime taken: {time.time() - start} sec")