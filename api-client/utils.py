import sys
from collections import defaultdict
import xml.etree.ElementTree as ET


def api_from_xml(xml_filename):
    tree = ET.parse(xml_filename)
    api = dict()

    for child in tree.getroot():
        route = child.attrib['route']
        route = route.split('=')[1].split('.')
        if len(route) == 1:
            route1 = 'misc'
            route2 = route[0]
        elif len(route) == 2:
            route1 = route[0]
            route2 = route[1]
        else:
            raise NotImplementedError

        if not route1 in api:
            api[route1] = dict()

        credential = child.attrib['credential'].split('|')

        for type in child.attrib['type'].split('|'):
            api[route1][route2] = {'type:': type,
                                   'credential': credential}

    return api


# source : https://stackoverflow.com/questions/7684333/converting-xml-to-dictionary-using-elementtree
def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


# source : https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")