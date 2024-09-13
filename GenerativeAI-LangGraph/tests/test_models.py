import unittest
from src.langgraph.models import LangGraph, Node, Edge

class TestModels(unittest.TestCase):

    def setUp(self):
        self.graph = LangGraph()

    def test_add_node(self):
        self.graph.add_node("A")
        self.assertIn("A", self.graph.nodes)
        self.assertIsInstance(self.graph.nodes["A"], Node)

    def test_add_edge(self):
        self.graph.add_edge("A", "B", 1)
        self.assertIn("A", self.graph.nodes)
        self.assertIn("B", self.graph.nodes)
        self.assertEqual(len(self.graph.nodes["A"].edges), 1)
        self.assertIsInstance(self.graph.nodes["A"].edges[0], Edge)
        self.assertEqual(self.graph.nodes["A"].edges[0].node, self.graph.nodes["B"])
        self.assertEqual(self.graph.nodes["A"].edges[0].weight, 1)

    def test_process_loan(self):
        result = self.graph.process_loan(10000, 12, 0.05)
        self.assertIn("Application", self.graph.nodes)
        self.assertIn("Evaluation", self.graph.nodes)
        self.assertIn("Decision", self.graph.nodes)
        self.assertIn("Funding", self.graph.nodes)
        self.assertIsInstance(result, str)
        self.assertIn("10000", result)
        self.assertIn("12", result)
        self.assertIn("5.0", result)

    def test_process_large_loan(self):
        result = self.graph.process_loan(150000, 36, 0.04)
        self.assertIn("High-Value Review", self.graph.nodes)
        self.assertIsInstance(result, str)
        self.assertIn("150000", result)
        self.assertIn("36", result)
        self.assertIn("4.0", result)

if __name__ == '__main__':
    unittest.main()
