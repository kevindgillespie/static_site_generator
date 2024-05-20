import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init_no_value_arg(self):
        with self.assertRaises(TypeError):
           under_test = LeafNode()

    def test_to_html_no_value(self):
        under_test = LeafNode("test")
        under_test.value = None
        with self.assertRaises(ValueError):
           test_html = under_test.to_html()

    def test_to_html_raw_text(self):
        test_value = "This is a test"
        under_test = LeafNode(test_value)
        self.assertEqual(under_test.to_html(), test_value)
        
    def test_to_html_paragraph_text(self):
        test_tag = "p"
        test_value = "This is a test"
        under_test = LeafNode(test_value, tag=test_tag)
        self.assertEqual(under_test.to_html(), f"<{test_tag}>{test_value}</{test_tag}>")

    def test_to_html_link_text(self):
        test_tag = "a"
        test_value = "This is a test"
        test_props = {"href": "https://github.com/kevindgillespie"}
        under_test = LeafNode(value=test_value, tag=test_tag, props=test_props)
        full_test_string = f'<{test_tag} href="{test_props["href"]}">{test_value}</{test_tag}>'
        self.assertEqual(under_test.to_html(), full_test_string)

if __name__ == "__main__":
    unittest.main()