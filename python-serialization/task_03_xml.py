#!/usr/bin/python3
"""
XML serialization and deserialization module
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=str(key))
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for item in root.findall("item"):
        key = item.attrib.get("key")
        value = item.text

        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except (ValueError, TypeError):
                pass

        result[key] = value

    return result
