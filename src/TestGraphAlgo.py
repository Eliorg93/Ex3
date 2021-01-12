import unittest
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

class MyTestCase(unittest.TestCase):

    def test_something(self):
        algo = GraphAlgo()
        self.assertTrue(algo.load_from_json("../data/A5"))
        print(algo.connected_components())

if __name__ == '__main__':
    unittest.main()
