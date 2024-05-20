from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, children, tag=None, props=None):
        super().__init__(children=children, tag=tag, props=props, value=None)

    def to_html(self):
        if (self.tag == None):
            raise ValueError("No tag found for Parent Node")
        if (self.children == None or len(self.children) < 1):
            raise ValueError("No Children found for Parent Node")
        full_html = f"<{self.tag}>"
        for child in self.children:
            full_html += child.to_html()
        return full_html + f"</{self.tag}>"