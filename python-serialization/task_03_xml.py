#!/usr/bin/python3
"""
  Let's import the XML module to apply
  the ser. and des. processes
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        First we should create the root element
        the we will iterate through our own dict
        each element we add as a child of the root
    """
    root = ET.Element("data")
    for k, v in dictionary.items():
        key = ET.Element(k)
        key.text = v
        root.append(key)
    """ Lastly we just create the tree itself """
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
        Here we take the data from XML file
        the we iterate throught this object
        to do that we need to loop into the root
        then simply we get the key and value:
        key -> k.tag
        value -> k.text
    """
    data = ET.parse(filename)
    dict = {}
    for k in data.getroot():
        dict[k.tag] = k.text
    return dict
