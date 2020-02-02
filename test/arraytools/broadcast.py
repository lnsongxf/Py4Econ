'''
Created on Jan 7, 2018
python "C:/Users/fan/PyFan/ProjectSupport/Support/arraytools/broadcast.py"
@author: fan
'''

# python "C:/Users/fan/Py4Econ/test/arraytools/broadcast.py"

'''
Numpy can broadcast, use that for states and choices
'''
import logging
logger = logging.getLogger(__name__)

import unittest

import numpy as np
import sys
# sys.path.append("C:/Users/fan/PyFan/ProjectSupport/Support/")
import Support.Timer as Timer

class TestBroadcast(unittest.TestCase):

    def test_broadcast_func(self):
        array1d = np.random.rand(3)
        logger.debug('array1d:%s',array1d)

        array1d_broadcast = array1d[:,None]
        logger.debug('array1d_broadcast:%s', array1d_broadcast)

        array2d = np.random.rand(3, 4)
        logger.debug('array2d:%s', array2d)

        array_sum = array1d_broadcast + array2d
        logger.debug('array_sum:%s', array_sum)

    def test_add_state_scalar_choice_1d(self):
        """ 1 * [1,2,3]
        """
        a_array1d = 1
        b_array1d = np.random.rand(3)

        ab_sum = a_array1d + b_array1d
        logger.debug('ab_sum:%s', ab_sum)

    def test_add_state_1d_choice_1d(self):
        """ [4,4,4,6,6,6] * [1,2,3,1,2,3]
        """
        "States Shocks Already Expanded"
        a_array1d = np.random.rand(2*3)
        b_array1d = np.random.rand(2*3)

        ab_sum = a_array1d + b_array1d
        logger.debug('ab_sum:%s', ab_sum)

    def test_add_state_1d_choice_1d_broadcast(self):
        """ [[4],[6]] * [1,2,3]
        """
        a_array_1d = np.random.rand(2)
        a_array_col_2d = a_array_1d[:, None]

        b_array_1d = np.random.rand(3)

        logger.debug('a_array_col_2d:%s', a_array_col_2d)
        logger.debug('b_array_1d:%s', b_array_1d)

        ab_sum = a_array_col_2d + b_array_1d
        logger.debug('ab_sum:%s', ab_sum)
        ab_mul = a_array_col_2d*b_array_1d
        logger.debug('ab_mul:%s', ab_mul)
        ab_cobb_doug = np.exp(a_array_col_2d)*a_array_col_2d*b_array_1d
        logger.debug('ab_cobb_doug:%s', ab_cobb_doug)

    def test_add_state_1d_choice_2d_broadcast(self):
        """ [[4],[6]] * [[1,2,3],[1,2,3]]
        """
        a_array_1d = np.random.rand(2)
        a_array_col_2d = a_array_1d[:, None]

        b_array_2d = np.random.rand(2, 3)

        logger.debug('a_array_col_2d:%s', a_array_col_2d)
        logger.debug('b_array_1d:%s', b_array_2d)

        ab_sum = a_array_col_2d + b_array_2d
        logger.debug('ab_sum:%s', ab_sum)
        ab_mul = a_array_col_2d*b_array_2d
        logger.debug('ab_mul:%s', ab_mul)

def broadcast_add1d1d(state_count, choice_count, rounds_bound):
    state = np.random.rand(state_count)
    choice = np.random.rand(choice_count)
    rounds = 0
    while (rounds <= rounds_bound):
        rounds += 1
#         logger.debug('rounds:%s',rounds)
        sum1d2d = state[:,None] + choice
    return sum1d2d

def broadcast_add1d2d(state_count, choice_count, rounds_bound):
    state = np.random.rand(state_count)
    choice = np.random.rand(state_count, choice_count)
    rounds = 0
    while (rounds <= rounds_bound):
        rounds += 1
#         logger.debug('rounds:%s',rounds)
        sum1d2d = state[:,None] + choice
    return sum1d2d

def tile_add1d2d(state_count, choice_count, rounds_bound):
    state = np.random.rand(state_count,1)
    state = np.repeat(state, choice_count, axis=1)
    choice = np.random.rand(state_count, choice_count)
    rounds = 0
    while (rounds <= rounds_bound):
        rounds += 1
#         logger.debug('rounds:%s',rounds)
        sum1d2d = state + choice
    return sum1d2d

def test_speed(rounds_bound = 0,
               rounds_bound_inner = 100,
               state_count = 10000,
               choice_count = 10000):

    with Timer.Timer('broadcast_add1d1d'):
        rounds = 0
        while (rounds <= rounds_bound):
            rounds += 1
            logger.debug('rounds:%s',rounds)
            broadcast_add1d2d(state_count=state_count,
                              choice_count=choice_count,
                              rounds_bound=rounds_bound_inner)

    with Timer.Timer('broadcast_add1d2d'):
        rounds = 0
        while (rounds <= rounds_bound):
            rounds += 1
            logger.debug('rounds:%s',rounds)
            broadcast_add1d2d(state_count=state_count,
                              choice_count=choice_count,
                              rounds_bound=rounds_bound_inner)

    with Timer.Timer('tile_add1d2d'):
        rounds = 0
        while (rounds <= rounds_bound):
            rounds += 1
            logger.debug('rounds:%s',rounds)
            tile_add1d2d(state_count=state_count,
                         choice_count=choice_count,
                         rounds_bound=rounds_bound_inner)

'States Today'
y = np.array([100, 120])
y_mat = np.repeat(y[:, None], 3, 1)
np.reshape(y_mat, (1,-1))

'Choices'
k_tp = np.array([1,2,3])
k_tp_mat = np.repeat(k_tp[None,:], 2, 0)
np.reshape(k_tp_mat, (1,-1))

if __name__ == '__main__':
    FORMAT = '%(filename)s - %(funcName)s - %(lineno)d -  %(asctime)s - %(levelname)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
#     unittest.main()
    test_speed()
