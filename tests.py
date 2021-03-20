import unittest
from collections import defaultdict

from calculateCostTransaction import calculate_loss


class TestCostTransaction(unittest.TestCase):

    def test_base_case(self):
        some_graph = defaultdict(list)

        edges = [
            (1, 2),
            (1, 10),
            (1, 4),
            (2, 3),
            (3, 4),
            (4, 5),
            (4, 6),
            (6, 7),
            (7, 8),
            (8, 9),
            (9, 10),
            (10, 11),
            (10, 8),
        ]

        num_nodes = 11

        for i, j in edges:
            some_graph[i].append(j)

        loss = [0.2, 0.2, 0.8, 0.3, 0.5, 0.38, 0.12, 0.11, 0.18, 0.13, 0.80]

        self.assertEqual(calculate_loss(num_nodes, some_graph, loss, (2, 3, 1.1)), "APPROVED")
        self.assertEqual(calculate_loss(num_nodes, some_graph, loss, (8, 10, 1.30)), "REJECTED")
        self.assertEqual(calculate_loss(num_nodes, some_graph, loss, (4, 10, 0.40)), "REJECTED")
