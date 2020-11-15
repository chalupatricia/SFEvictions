import math
import numpy as np

def process_data(filename):
    file = open(filename)
    next(file)
    district_counts = {}
    for line in file:
        line = line.strip()
        line = line.split(',')
        district = line[2]

        if district not in district_counts:
            district_counts[district] = 0
        district_counts[district] += 1

    print(district_counts)
    return district_counts


def sort_dict(district_counts):
    #print({k: v for k, v in sorted(district_counts.items(), key=lambda item: item[1])})
    return {k: v for k, v in sorted(district_counts.items(), key=lambda item: item[1])}


def parse_total(filename = 'TotalPop.csv'):
    file = open(filename)
    pop_dict = {}
    for line in file:
        line = line.strip()
        line = line.split(',')
        pop_dict[line[0]] = int(line[1])
    return pop_dict


def get_percents(district_dict):
    pop_dict = parse_total('TotalPop.csv')
    percent_dict = {}
    for district in district_dict:
        if district in pop_dict:
            percent_dict[district] = district_dict[district] / pop_dict[district]
    print(sort_dict(percent_dict))
    return sort_dict(percent_dict)



def main():
    district_dict = process_data('Eviction_Notices.csv')
    sort_dict(district_dict)
    #print(len(district_dict.keys()))
    parse_total('TotalPop.csv')
    get_percents(district_dict)


if __name__ == '__main__':
    main()