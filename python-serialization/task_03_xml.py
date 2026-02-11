import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, str(key))
        element.text = str(value)

    tree = ET.ElementTree(root)

    try:
        ET.indent(tree, space="    ")
    except AttributeError:
        pass

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for element in root:
        key = element.tag
        value = element.text

        if value is not None:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    if value == "True":
                        value = True
                    elif value == "False":
                        value = False

        result[key] = value

    return result
