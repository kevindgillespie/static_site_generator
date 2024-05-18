import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is another test node", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        test_text = 'TextNode(This is a test node, bold, test.com)'
        node = TextNode("This is a test node", "bold", "test.com")
        self.assertEqual(repr(node), test_text)

if __name__ == "__main__":
    unittest.main()
