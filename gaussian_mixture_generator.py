from uniform_generator import uniform_generator
from multivariate_gaussian_generator import multivariate_gaussian_generator
import numpy
from pprint import pprint


def gaussian_mixture_generator(pi, mu, sigma, size, dimension):
    """
    Assumption: values in pi are in ascending order.
    
    pi: Weights of the Gaussian in mixture. 
    mu: Mean of each Gaussian.
    sigma: Covariance of each Gaussian.
    size: Number of examples to be generated.
    dimension: Dimension of each Gaussian.

    Algorithm:
        1. Construct a cdf using pi vector.
        2. Generate a random number.
        3. Pick the distribution from pi vector using the random number.
        4. Call multivariate_gaussian_generator function with corresponding mean and covariance.
    """
    pi_cdf = []
    uni_gen = uniform_generator()
    _sum = 0
    for val in pi:
        _sum = _sum + val
        pi_cdf.append(_sum)
    multi_gens = []
    for i in range(len(pi)):
        multi_gens.append(multivariate_gaussian_generator(mu[i], sigma[i], dimension))
    while True:       
        rand_num = next(uni_gen)
        for i in range(len(pi_cdf)):
            if rand_num <= pi_cdf[i]:
                yield next(multi_gens[i])
                break


if __name__ == '__main__':
    pi = [0.1, 0.2, 0.3, 0.4]
    mu = [[4, 0], [0, 3], [4, 4], [0, 0]]
    sigma_1 = [[0.25, 0], [0, 0.35]]
    sigma_2 = [[0.5, 0.1], [0.1, 1]]
    sigma_3 = [[1, 0.25], [0.25, 0.5]]
    sigma_4 = [[1, 0.7], [0.7, 1]]
    sigma = [sigma_1, sigma_2, sigma_3, sigma_4]
    size = 100000
    dimension = 2
    gmm_gen = gaussian_mixture_generator(pi, mu, sigma, size, dimension)
    op = []
    for _ in range(size):
        op.append(next(gmm_gen))
    pprint(numpy.mean(op, axis = 0))

