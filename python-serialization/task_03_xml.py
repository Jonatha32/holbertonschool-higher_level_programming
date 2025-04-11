import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """"
    Serialize a python dic
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        ch = ET.SubElement(root, key)
        ch.text = str(value)
    
    tr = ET.ElementTree(root)
    tr.write(filename, xml_declaration=True)
    
def deserialize_from_xml(filename):
    """
    Deserialize a python dic
    """
    
    tr = ET.parse(filename)
    root = tr.getroot()
    
    res = {}
    for ch in root:
        res[ch.tag] = ch.text
    
    return res
