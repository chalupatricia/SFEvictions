import math
import numpy as np
from numpy.random import rand

from analysis import *

NUM_EVICTIONS_MORATORIUM = float(293.0)
BAYVIEW_P = 15/NUM_EVICTIONS_MORATORIUM
MISSION_P = 62/NUM_EVICTIONS_MORATORIUM
NOE_VALLEY_P = 4/NUM_EVICTIONS_MORATORIUM
CHINATOWN_P = 4/NUM_EVICTIONS_MORATORIUM
TENDERLOIN_P = 33/NUM_EVICTIONS_MORATORIUM
P_HILL = 4/NUM_EVICTIONS_MORATORIUM
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
        resample1 = np.random.choice(universal_sample, len(sample1), replace=True)
        resample2 = np.random.choice(universal_sample, len(sample2), replace=True)

        resample_diff = np.abs(np.mean(resample1) - np.mean(resample2))

        if resample_diff > observed_diff:
            count += 1

    return count / niters


def main():

    #white, affluent neighborhood
    noe_valley_sample = create_sample(NOE_VALLEY_P)

    #Black neighborhood
    bayview_sample = create_sample(BAYVIEW_P)
    pval = compute_p_val(np.array(noe_valley_sample), np.array(bayview_sample))
    print("Black vs White p: ", pval)

    #Latinx neighborhood
    mission_sample = create_sample(MISSION_P)
    pval = compute_p_val(np.array(noe_valley_sample), np.array(mission_sample))
    print("Latinx vs White p: ", pval)

    #Asian neighborhood
    ctown_sample = create_sample(CHINATOWN_P)
    pval = compute_p_val(np.array(noe_valley_sample), np.array(ctown_sample))
    print("Asian vs White p: ", pval)

    #Black vs Latinx
    pval = compute_p_val(np.array(bayview_sample), np.array(mission_sample))
    print("Black vs Latinx p: ", pval)

    #high income vs low income
    tl_sample = create_sample(TENDERLOIN_P)
    pval = compute_p_val(np.array(noe_valley_sample), np.array(tl_sample))
    print("High Income vs Low Income p: ", pval)

    #White vs white
    potrero_sample = create_sample(P_HILL)
    pval = compute_p_val(np.array(noe_valley_sample), np.array(potrero_sample))
    print("White vs White p: ", pval)


if __name__ == '__main__':
    main()