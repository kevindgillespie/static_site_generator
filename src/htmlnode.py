
class HTMLNode:

    #An HTMLNode without a tag will just render as raw text
    #An HTMLNode without a value will be assumed to have children
    #An HTMLNode without children will be assumed to have a value
    #An HTMLNode without props simply won't have any attributes
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
