import time
import numpy as np
from operator import attrgetter
import logging
from scipy.special import lambertw
import math

class Complexity:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def get_log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger


def estimate_complexity_manager(times, numbers, given_time, given_n):

    get_log().info("Module estimation")

    n = np.array(numbers)
    t = np.array(times)

    result = find_smaller(t, n)

    a = count_a(result, n[0], t[0])

    if given_time:
        n_counted =check_max_size_n(result, a, given_time)
        print("size of n: ", n_counted)

    if given_n:

        s = check_time(result, a, given_n)
        print("Time: ", s)


def count_a(result, n, time):
    if result == 'n':
        return time / n

    if result == 'n^2':
        return time / (n * n)

    elif result == 'nlogn':
        return time / (n * np.log(n))

    else:
        return None

def check_time(result, n, a):
    if result == 'n':
        return a*n

    if result == 'n^2':
        return a*(n**2)

    elif result == 'nlogn':
        return a*np.log(n)

    else:
        return None



def check_max_size_n(result, a, given_time):

    if result == 'n':
        return math.floor(given_time / a)

    if result == 'n^2':
        return math.floor(np.sqrt(given_time / a))

    elif result == 'nlogn':
        x = a/given_time
        return math.floor(x/lambertw(x))

    else:
        return None


def print_complexity(function):

    def wrapper(*args, **kwargs):
        res =  function(*args, **kwargs)
        if(res == 'n'):
            get_log().info("This function is probably O(n)")
        elif(res == 'nlogn'):
            get_log().info("This function is probably O(n*logn)")
        elif (res == 'n^2'):
            get_log().info("This function is probably O(n^2)")
        else:
            get_log().info("Something went wrong when estimating cmplexity")
        return res

    return wrapper


@print_complexity
def find_smaller(t, n):

    com = []

    n_val = np.var(np.log(t/n))
    n_com = Complexity('n', n_val)

    com.append(n_com)

    nlogn_val = np.var(np.log(t/(n*np.log(n))))
    nlogn_com = Complexity('nlogn', nlogn_val)

    com.append(nlogn_com)

    n2_val = np.var(np.log(t/(n*n)))
    n2_com = Complexity('n^2', n2_val)

    com.append(n2_com)

    mini_comp = min(com, key=attrgetter('value'))
    return mini_comp.name
