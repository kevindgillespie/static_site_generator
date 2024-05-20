import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_init_no_children(self):
        with self.assertRaises(TypeError):
            under_test = ParentNode()

    #Parent
    #|
    #--Leaf
    def test_to_html_one_parent_one_child(self):
        under_test = ParentNode(
            children=[LeafNode(value="This is a test", tag="b")],
            tag="div",
            props=None
        )
        test_string = "<div><b>This is a test</b></div>"
        self.assertEqual(under_test.to_html(), test_string)

    #Parent
    #|
    #--Leaf
    #--Leaf
    def test_to_html_one_parent_two_children(self):
        under_test = ParentNode(
            children=[LeafNode(value="This is a test", tag="b"),
                        LeafNode(value="This is another test", tag="i")],
            tag="div",
            props=None
        )
        test_string = "<div><b>This is a test</b><i>This is another test</i></div>"
        self.assertEqual(under_test.to_html(), test_string)

       

    #Parent
    #|
    #--Parent
    #   |
    #   --Leaf
    def test_to_html_one_parent_one_parent_one_child(self):
        under_test = ParentNode(children=[ParentNode(
            children=[LeafNode(value="This is a test", tag="b")],
            tag="div",
            props=None
        )],
        tag="block"
        )
        test_string = "<block><div><b>This is a test</b></div></block>"
        self.assertEqual(under_test.to_html(), test_string)


    #Parent
    #|
    #--Parent
    #   |
    #   --Leaf
    #   --Leaf
    #--Parent
    #   |
    #   --Leaf
    #   --Leaf
    def test_to_html_one_parent_two_parents_two_children_each(self):
        under_test = ParentNode(children=[ParentNode(
            children=[LeafNode(value="This is a test", tag="b"), LeafNode(value="This is a test", tag="b")],
            tag="div",
            props=None
        ), ParentNode(
            children=[LeafNode(value="This is a test", tag="b"), LeafNode(value="This is a test", tag="b")],
            tag="div",
            props=None
        )],
        tag="block"
        )
        test_string = "<block><div><b>This is a test</b><b>This is a test</b></div><div><b>This is a test</b><b>This is a test</b></div></block>"
        self.assertEqual(under_test.to_html(), test_string)



if __name__ == "__main__":
    unittest.main()