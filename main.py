# secretary problem
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def show_plot(x):
    # plot the data
    plt.xlabel("Woman where I start to look for the highest one")
    plt.ylabel("Expected Score")
    plt.plot(x)

    # # show the plot
    # plt.show()

n_dates = 100
max_score = 10000
samples = 1000

def main():
    # generate a random numpy matrix of n x samples numbers between 0 and max_score
    x = np.random.randint(0, max_score, (n_dates, samples))
    y = np.zeros(x.shape)

    for s in tqdm(range(samples)):
        for i in range(n_dates):
            # take the max of the first i dates
            nth_max = np.max(x[0:i+1, s])

            # get the next best score
            current = x[i, s]

            # if the current score is not the maximum
            if current != nth_max:
                # date until you get a better score than the first i dates
                # take the last one if you didn't find a better score
                for j in range(i, n_dates):
                    current = x[j, s]
                    if x[j, s] > nth_max:
                        break
                    
            # set the result to the current score
            y[i, s] = current

    y = np.average(y, axis=1)

    show_plot(y)
    plt.savefig('result.png')


if __name__ == "__main__":
    main()
