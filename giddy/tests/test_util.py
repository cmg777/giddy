import unittest
from .. import util
import numpy as np


class ShuffleMatrix_Tester(unittest.TestCase):
    def setUp(self):
        self.X = np.arange(16)
        self.X.shape = (4, 4)

    def test_shuffle_matrix(self):
        np.random.seed(10)
        obs = util.shuffle_matrix(self.X, list(range(4))).flatten().tolist()
        exp = [10, 8, 11, 9, 2, 0, 3, 1, 14, 12, 15, 13, 6, 4, 7, 5]
        for i in range(16):
            self.assertEqual(exp[i], obs[i])


class GetLower_Tester(unittest.TestCase):
    def setUp(self):
        self.X = np.arange(16)
        self.X.shape = (4, 4)

    def test_get_lower(self):
        np.random.seed(10)
        obs = util.get_lower(self.X).flatten().tolist()
        exp = [4, 8, 9, 12, 13, 14]
        for i in range(6):
            self.assertEqual(exp[i], obs[i])

class FillDiagonal_Tester(unittest.TestCase):
    def setUp(self):
        self.p3 = np.array([[.5, .5, 0], [.3, .7, 0], [0, 0, 0]])
        self.p23 =np.array([[[.5, .5, 0], [.3, .7, 0], [0, 0, 0]],
                            [[0, 0, 0], [.3, .7, 0], [0, 0, 0]]])


    # def test_fill_diag2(self):
    #     obs = util.fill_empty_diagonal_2d(self.p3)
    #     exp = np.array([[0.5, 0.5, 0. ], [0.3, 0.7, 0. ], [0. , 0. , 1. ]])
    #     np.testing.assert_array_almost_equal(exp, obs)
    #
    #     with self.assertRaises(ValueError):
    #         obs = util.fill_empty_diagonal_2d(self.p23)
    #
    # def test_fill_diag3(self):
    #     obs = util.fill_empty_diagonal_3d(self.p23)
    #     exp = np.array([[[0.5, 0.5, 0. ], [0.3, 0.7, 0. ], [0. , 0. , 1. ]],
    #                     [[1. , 0. , 0. ], [0.3, 0.7, 0. ], [0. , 0. , 1. ]]])
    #     np.testing.assert_array_almost_equal(exp, obs)
    #
    #     with self.assertRaises(ValueError):
    #         obs = util.fill_empty_diagonal_3d(self.p3)

    def test_fill_diag(self):
        obs = util.fill_empty_diagonals(self.p3)
        exp = np.array([[0.5, 0.5, 0.], [0.3, 0.7, 0.], [0., 0., 1.]])
        np.testing.assert_array_almost_equal(exp, obs)

        obs = util.fill_empty_diagonals(self.p23)
        exp = np.array([[[0.5, 0.5, 0. ], [0.3, 0.7, 0. ], [0. , 0. , 1. ]],
                        [[1. , 0. , 0. ], [0.3, 0.7, 0. ], [0. , 0. , 1. ]]])
        np.testing.assert_array_almost_equal(exp, obs)


suite = unittest.TestSuite()
test_classes = [ShuffleMatrix_Tester, GetLower_Tester]
for i in test_classes:
    a = unittest.TestLoader().loadTestsFromTestCase(i)
    suite.addTest(a)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
