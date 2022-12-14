import xml.etree.ElementTree as ET


class Xml2Json:
    def __init__(self, split_key: str, skip_keys: list = None):
        self.results = []
        self.split_key = split_key
        self.skip_keys = skip_keys or []

    def parse(self, xml_string: str):
        self.xml_element_to_json(ET.fromstring(xml_string))
        return self.results

    def xml_element_to_json(self, xml_element, result=None):
        result = {} if result is None else result
        if len(xml_element) == 0:
            result["text"] = xml_element.text
        else:
            for child in xml_element:
                if child.tag == self.split_key:
                    result = {}
                    self.results.append(result)
                child_result = child.attrib
                key = child.tag
                if key in self.skip_keys:
                    continue
                if key in result:
                    if isinstance(result[key], list):
                        result[key].append(child_result)
                    else:
                        result[key] = [result[key], child_result]
                else:
                    result[key] = child_result
                self.xml_element_to_json(child, child_result)
