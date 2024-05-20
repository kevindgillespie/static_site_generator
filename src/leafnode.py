from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, value, tag = None, props = None):
        super().__init__(value=value, tag=tag, props=props)

    
    def to_html(self):
        html_value = self.value
        if(self.value == None):
            raise ValueError()
        if self.tag != None and self.props != None:
            html_value = f"<{self.tag} {super().props_to_html()}>{html_value}</{self.tag}>"
        elif self.tag != None and self.props == None:
            html_value = f"<{self.tag}>{html_value}</{self.tag}>"
        return html_value