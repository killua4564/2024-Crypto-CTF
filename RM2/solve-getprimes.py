from functools import reduce
from time import time

from CTFLib.Crypto import *
from CTFLib.Utils import *


count = 0
p_list = []
p_prime_list = []

attempts = 0
start = time()
while True:
    prime_list = [2] + [fastGetPrime(16) for _ in range(63)]
    pp = reduce(lambda x, y: x * y, prime_list)
    while True:
        prime = fastGetPrime(1024 - (pp + 1).bit_length())
        if (pp * prime + 1).bit_length() == 1024:
            prime_list.append(prime)
            p = pp * prime + 1
            break

    attempts += 1
    if (attempts % 10000) == 0:
        info(f'Attempts : {attempts} , Time : {int(time() - start)}s')

    if fastIsPrime(p) and fastIsPrime(2 * p + 1):
        success('Find `p` satisfy `p - 1` is smooth && `2 * p + 1` is prime')
        p_list.append(p)
        p_prime_list.append(prime_list)
        count += 1

    if count == 2:
        print(p_list)
        print(p_prime_list)
        break

