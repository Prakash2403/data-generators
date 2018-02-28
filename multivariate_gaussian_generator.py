from pprint import pprint
import numpy
from multivariate_standard_gaussian_generator import multivariate_standard_normal_generator


def get_eigenvalues(x):
    pass


def get_eigenvectors(x):
    pass


def get_transform_matrix(eigen_vectors):
    pass


def get_diagonal_matrix(eigen_values):
    pass


def multivariate_gaussian_generator(mean, cov, dimension):
    """

    @param: mean: Mean of target Gaussian.
    @param: cov: Covariance of target Gaussian.
    @param: dimensiom: Dimension of target Gaussian.
    Algorithm:
        1. Generate N-Dimensional vector where each value in vector is randomly chosen from standard Gaussian distribution.
        2. This data can be assumed to be coming from  N-dimensional Gaussian distribution.
        3. Using y = p * sqrt(lambda) * x, convert standard Gaussian data to correlated Gaussian data.
        4. Add mean to correlated Gaussian data.
        5. Return the data obtained in step 4.

        Mathematical details will be given in report.
    """
    multi_gen = multivariate_standard_normal_generator(dimension)
    eigen_values, eigen_vectors  = numpy.linalg.eig(cov)
    transform_matrix = eigen_vectors
    diagonal_matrix = numpy.diag(eigen_values)
    while True:
        standard_data = next(multi_gen)
        standard_data = numpy.asarray(standard_data)
        gaussian_data = numpy.matmul(numpy.matmul(transform_matrix, numpy.sqrt(diagonal_matrix)), standard_data)
        gaussian_data = gaussian_data + mean
        yield gaussian_data


if __name__ == '__main__':
    mu = [1, 2]
    sigma = [[1, 1], [1, 1]]
    dimension = 2
    op = []
    multivariate_data = multivariate_gaussian_generator(mu, sigma, dimension)
    for _ in range(100000):
        op.append(next(multivariate_data))
    pprint(numpy.mean(op, axis = 0))

