"""
I first calculate joint probabilities and then use the Chow Liu Algorithm to create a
Bayesian network
"""

TOTAL = 34
def joint_probability_poc(filename):
    file = open(filename)

    count = 0
    poc_count = 0.0
    for line in file:
        line = line.strip()
        line = line.split(',')

        percent = float(line[0])
        income_status = int(line[1])

        if percent >= 0.5:
            poc_count += 1

        if percent >= 0.5 and income_status == 1:
            count += 1
    print("poc: ", poc_count/TOTAL)
    return count / TOTAL

def joint_probability_white(filename):
    file = open(filename)

    count = 0.0
    for line in file:
        line = line.strip()
        line = line.split(',')

        percent = float(line[0])
        income_status = int(line[1])

        if percent < 0.5 and income_status == 1:
            count += 1

    return count / TOTAL

def joint_income_covid(filename):
    file = open(filename)
    next(file)
    count = 0.0
    for line in file:
        line = line.strip()
        line = line.split(',')

        income = int(line[0])
        covid = int(line[1])
        if income == 0 and covid == 1:
            count += 1

    return count / TOTAL

def main():
    print(joint_probability_poc('poc_income.csv'))
    # print(joint_probability_poc('poc_covid.csv'))
    # print(joint_probability_poc('poc_eviction.csv'))
    #
    # print(joint_probability_white('white_income.csv'))
    # print(joint_probability_white('poc_income.csv'))
    print(joint_probability_white('poc_eviction.csv'))

    # print(joint_income_covid('income_covid.csv'))
    # print(joint_income_covid('income_evict.csv'))
    # print(joint_income_covid('covid_evictions.csv'))


if __name__ == '__main__':
    main()