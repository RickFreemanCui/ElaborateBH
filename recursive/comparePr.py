from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 2 ** 27
    M = 2 ** 22
    delta = 100
    p = M / N
    for i in range(1, delta, 1):
        Pr1 = H(delta, N, M, i)
        Pr2 = F(delta, N, M, i)
        print('hypergeo:\t%0.8f, p:\t%0.8f' % (Pr1, Pr2))

# return a fraction
def H(n, N, M, k):
    return comb(M, k) * comb(N-M, n-k) / comb(N, n)

# return a fraction
def F(n, N, M, k):
    result = Fraction(1, 1)
    for i in range(k):
        result *= Fraction(M, N)
    for i in range(n-k):
        result *= Fraction(N-M, N)
    return result

# return a fraction
def comb(n, m):
    result = Fraction(1,1)
    for i in range(m):
        result *= Fraction((n - i), (m - i))
    return result

        
if __name__ == '__main__':
    main()
