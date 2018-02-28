from pprint import pprint
import time
import numpy
import math
from normal_generator import normal_generator


def multivariate_standard_normal_generator(dimension):
    """
    Generates data from multivariate standard Gaussian distribution.
    """
    multivariate_vector = []
    norm_gen = normal_generator()
    while True:
        for _ in range(dimension):
            __, rand_norm = next(norm_gen)
            multivariate_vector.append(rand_norm)
        yield multivariate_vector
        multivariate_vector = []


if __name__ == '__main__':
    output_list = []
    print("Generating 2-D 10000 random numbers")
    start = time.time()
    multi_gen = multivariate_standard_normal_generator(2)
    for i in range(10000):
       op1 = next(multi_gen)
       output_list.append(op1)
    end = time.time()
    print("Time taken " + str(end - start))
    print("Mean is: " + str(numpy.mean(output_list, axis=0)))
    print("Standard Deviation: " + str(numpy.std(output_list, axis=0)))
