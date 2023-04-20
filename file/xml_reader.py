import xml.etree.ElementTree as ET
from typing import Union

class XmlReader:
    output = []

    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def read_child(self, child, elements, attributes=[], required_elements=[]):
        self.validate_xml(child, required_elements)

        child_arr = self.root.findall(child)

        for child_ in child_arr:
            self.output.append(self.__parse_node_to_dict(child_, elements=elements, attributes=attributes))

        return self.output

    def __parse_node_to_dict(self, node, elements, attributes):
        node_ = {
            "attributes": {},
        }

        attributes_ = self.__find_attributes(node, attributes)
        elements_ = self.__find_elements(node, elements)

        [node_['attributes'].update(attribute) for attribute in attributes_]
        [node_.update(element) for element in elements_]

        return node_

    def __find_attributes(self, tag, attributes):
        return [{attribute: tag.get(attribute)} for attribute in attributes]
    
    def __find_elements(self, tag, elements):
        return [{element: self.__get_element_value(tag.find(element))} for element in elements]
    
    def validate_xml(self, tag, elements):
        for child in self.root.findall(tag):
            if child is None:
                raise Exception("Invalid XML, tag <{}> not found".format(tag))
            
            if elements is not None:
                for element in elements:
                    el_ = child.find(str(element))
                    if el_ is None:
                        raise Exception("Invalid XML, tag <{}> not found".format(element))

        pass

    def __get_element_value(self, element) -> Union[str,None]:
        if element is None or element.text is None:
            return None
            
        return element.text