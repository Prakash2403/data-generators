from pprint import pprint
import time
import numpy
import math


def get_seed():
    """
    Generates a seed value. Uses number of seconds elapsed from January 1, 1970.
    """
    curr_time = time.time()
    float_time = curr_time - int(curr_time)
    seed = int(time.time()) + int(10*float_time)
    return seed


def uniform_generator():
    """
    Uses linear congruential generator to generate a random variable between 0 and 1
    from uniform distribution.
    Basic Equation for generator is
        X_(n+1) = (a * X_n + b) mod m
    where a, b and m are large numbers.
    However, to allow large periods between states, a separate variable is maintained.
    """
    b = 3123135
    a = 1010012
    seed = get_seed()
    temp_num = seed
    while True:
        temp_num = (temp_num * a + b) % 109297270343
        random_number = temp_num % limit
        yield random_number/limit


limit = 10001
if __name__ == '__main__':
    output_list = []
    print("Generating 10000 random numbers from uniform distribution")
    start = time.time()
    norm_gen = uniform_generator()
    for i in range(10000):
       op1 = next(norm_gen)
       output_list.append(op1)
    end = time.time()
    print("Time taken " + str(end - start))
    print("Mean is: " + str(numpy.mean(output_list)))
    print("Standard Deviation: " + str(numpy.std(output_list)))

