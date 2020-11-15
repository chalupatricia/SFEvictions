"""
Is the decrease in eviction notices since the SF eviction moratorium statistically significant?
I use bootstrapping to run a hypothesis test to find out.
"""
import math
import numpy as np
from numpy.random import rand

NUM_EVICTIONS_MORATORIUM = float(293.0)
NUM_EVICTIONS_NO_MORATORIUM = float(691.0)
TOTAL = NUM_EVICTIONS_MORATORIUM + NUM_EVICTIONS_NO_MORATORIUM
SAMPLE_SIZE = 100

def simulate_bernoulli(p):
    if rand() < p:
        return 1
    return 0


def create_sample(p):
    sample = []
    for i in range(SAMPLE_SIZE):
        sample.append(simulate_bernoulli(p))
    return sample


def compute_p_val(sample1, sample2, niters = 10000):
    universal_sample = sample1 + sample2
    count = 0.0
    observed_diff = abs(np.mean(sample1) - np.mean(sample2))
    for i in range(niters):
        # 1. resample
        print(count)
        resample1 = np.random.choice(universal_sample, len(sample1), replace=True)
        resample2 = np.random.choice(universal_sample, len(sample2), replace=True)

        resample_diff = np.abs(np.mean(resample1) - np.mean(resample2))

        if resample_diff > observed_diff:
            count += 1

    return count / niters

def main():

    #Create the sample for evictions during the moratorium
    p_evictions_moratorium = float(NUM_EVICTIONS_MORATORIUM / TOTAL)
    sample_moratorium = create_sample(p_evictions_moratorium)
    #print(sample_moratorium)
    #Create the sample for evictions during the non-moratorium time
    p_evictions_non_moratorium = float(NUM_EVICTIONS_NO_MORATORIUM / TOTAL)
    sample_no_moratorium = create_sample(p_evictions_non_moratorium)
    #print(sample_no_moratorium)
    pval = compute_p_val(np.array(sample_moratorium), np.array(sample_no_moratorium), 10000)
    print("main: ", pval)


if __name__ == '__main__':
    main()

