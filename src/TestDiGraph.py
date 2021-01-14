import unittest

from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_get_mc(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)
        self.assertEqual(50, g.get_mc())
        g.remove_node(51)
        self.assertEqual(50, g.get_mc())
        g.remove_node(49)
        self.assertEqual(51, g.get_mc())
        g.remove_node(22)
        g.add_edge(0, 10, 12)
        g.add_edge(0, 5, 5)
        g.add_edge(0, 7, 9)
        g.remove_node(10)

        self.assertEqual(57, g.get_mc())

    def test_v_size(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)
        g.remove_node(55)
        self.assertEqual(50, g.v_size())
        g.remove_node(22)
        self.assertEqual(49, g.v_size())
        g.add_node(50)
        self.assertEqual(50, g.v_size())

    def test_e_size(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)

        self.assertEqual(0, g.e_size())
        g.add_edge(0, 10, 2)
        self.assertEqual(1, g.e_size())
        g.add_edge(0, 10, 2)
        self.assertEqual(1, g.e_size())
        g.add_edge(0, 7, 5)
        self.assertEqual(2, g.e_size())
        g.remove_edge(0, 10)
        self.assertEqual(1, g.e_size())
        g.add_edge(0, 9, 10)
        g.add_edge(0, 8, 5)
        self.assertEqual(3, g.e_size())

    def test_add_node(self):
        g = DiGraph()
        g.add_node(40)
        g.add_node(100)
        g.add_node(50)
        g.add_node(25)
        g.add_node(80)
        self.assertEqual(5, g.v_size())
        g.add_node(50)
        self.assertEqual(5, g.v_size())

    def test_get_all_v(self):
        g = DiGraph()
        self.assertEqual(0, len(g.get_all_v()))  # No nodes
        for i in range(50):
            g.add_node(i)
        self.assertEqual(50, len(g.get_all_v()))
        g.add_node(51)
        self.assertEqual(51, len(g.get_all_v()))

        self.assertIsNotNone(g.get_all_v().get(25))
        self.assertIsNone(g.get_all_v().get(800))

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)

        g.add_edge(0, 45, 10)
        g.add_edge(10, 45, 10)
        g.add_edge(2, 50, 10)
        g.add_edge(4, 45, 8)
        self.assertEqual(3, len(g.all_in_edges_of_node(45)))
        g.add_edge(6, 45, 5)
        self.assertEqual(4, len(g.all_in_edges_of_node(45)))
        g.remove_edge(10, 45)
        self.assertEqual(3, len(g.all_in_edges_of_node(45)))
        self.assertIsNone(g.all_in_edges_of_node(45).get(800))

        self.assertIsNotNone(g.all_in_edges_of_node(45).get(6))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)
        g.add_edge(2, 5, 10)
        g.add_edge(2, 10, 10)
        g.add_edge(2, 30, 10)
        g.add_edge(4, 40, 2)
        self.assertEqual(3, len(g.all_out_edges_of_node(2)))
        g.add_edge(2, 55, 10)
        self.assertEqual(3, len(g.all_out_edges_of_node(2)))
        g.add_edge(2, 48, 7)
        self.assertEqual(4, len(g.all_out_edges_of_node(2)))

        self.assertIsNotNone(g.all_out_edges_of_node(2).get(10))
        g.remove_edge(2, 10)
        self.assertEqual(3, len(g.all_out_edges_of_node(2)))

        self.assertIsNone(g.all_out_edges_of_node(2).get(10))
        self.assertIsNotNone(g.all_out_edges_of_node(2).get(5))
        self.assertIsNone(g.all_out_edges_of_node(2).get(900))

    def test_remove_node(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)
        self.assertEqual(50, g.v_size())
        g.remove_node(2)
        g.remove_node(6)
        g.remove_node(10)
        g.remove_node(15)
        self.assertEqual(46, g.v_size())
        g.remove_node(4)
        g.remove_node(33)
        g.remove_node(51)
        self.assertEqual(44, g.v_size())

    def test_add_edge(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
        g.add_edge(0, 10, 2)
        g.add_edge(1, 4, 6)
        g.add_edge(2, 2, 1)
        self.assertEqual(2, g.e_size())
        g.add_edge(1, 4, 6)
        g.add_edge(3, 6, 2)
        self.assertEqual(3, g.e_size())
        self.assertIsNotNone(g.all_out_edges_of_node(0).get(10))
        self.assertIsNone(g.all_out_edges_of_node(0).get(50))

    def test_remove_edge(self):
        g = DiGraph()
        for i in range(50):
            g.add_node(i)
        g.add_edge(2, 6, 2)
        g.add_edge(4, 8, 5)
        g.add_edge(6, 6, 3)
        g.add_edge(3, 4, 4)
        self.assertEqual(3, g.e_size())
        g.remove_edge(0, 1)
        self.assertEqual(3, g.e_size())
        g.remove_edge(3, 4)
        self.assertEqual(2, g.e_size())


if __name__ == '_main_':
    unittest.main()
