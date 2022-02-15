# secretary problem
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

n = 1000
samples = 1000

def main():
    # generate a random numpy matrix of n x samples numbers between 0 and max_score
    x = np.random.uniform(size=(n, samples))
    expected_score = np.zeros(x.shape)

    for s in tqdm(range(samples)):
        for i in range(n):
            # take the max of the first i dates
            nth_max = np.max(x[0:i+1, s])

            # date until you get a better score than the first i dates
            # take the last one if you didn't find a better score
            for j in range(i+1, n):
                current = x[j, s]
                if  current > nth_max:
                    break

            # set the result to the current score
            expected_score[i, s] = current

    # Average the results
    prob_success = np.average(expected_score == np.max(x, axis=0), axis=1)
    expected_score = np.average(expected_score, axis=1)

    plt.title("Success Rate")
    plt.xlabel("Heuristic Parameter")
    plt.ylabel("Probability of Success")
    plt.plot(prob_success)
    plt.savefig('success_rate.png')
    plt.close()

    plt.title("Expected Score")
    plt.xlabel("Heuristic Parameter")
    plt.ylabel("Expected Score")
    plt.plot(expected_score)
    plt.savefig('expected_score.png')
    plt.close()


if __name__ == "__main__":
    main()
