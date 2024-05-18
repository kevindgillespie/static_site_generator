import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HTMLNode(props = { "someKey": "someValue"})
        expected_str = 'someKey="someValue"'
        self.assertEqual(html_node.props_to_html(), expected_str)

if __name__ == "__main__":
    unittest.main()
