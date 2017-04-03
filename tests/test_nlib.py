import unittest

import nlib


class TestNLib(unittest.TestCase):
    def test_fib(self):
        result0 = nlib.fib(0)
        expected0 = 0
        self.assertEqual(expected0, result0)

        result1 = nlib.fib(1)
        expected1 = 1
        self.assertEqual(expected1, result1)

        result2 = nlib.fib(2)
        expected2 = 1
        self.assertEqual(expected2, result2)

        result10 = nlib.fib(10)
        expected10 = 55
        self.assertEqual(expected10, result10)

    def test086(self):
        pat = [[[0, 0], [0]],
               [[0, 1], [1]],
               [[1, 0], [1]],
               [[1, 1], [0]]]
        n = nlib.NeuralNetwork(2, 2, 1)
        n.train(pat)

        for input_list, expected_list in pat:
            result_list = n.update(input_list)
            for expected_member, result_member in zip(expected_list, result_list):
                self.assertAlmostEqual(expected_member, result_member, places=1)

    def test084(self):
        bases = 'ATGC'
        from random import choice
        genes = [''.join(choice(bases) for k in range(10)) for i in range(20)]
        chromosome1 = ''.join(choice(genes) for i in range(10))
        chromosome2 = ''.join(choice(genes) for i in range(10))
        z = nlib.needleman_wunsch(chromosome1, chromosome2)
        nlib.Canvas(title='Needleman-Wunsch').imshow(z).save('images/needleman.png')


if __name__ == '__main__':
    unittest.main()
