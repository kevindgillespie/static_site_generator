
class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_list = []
        for prop in self.props:
            props_list.append(f'{prop}="{self.props[prop]}"')
        return " ".join(props_list)

    def __repr__(self):
        return f"HTMLNode(tag={tag}, value={value}, children={children}, props={props})"
