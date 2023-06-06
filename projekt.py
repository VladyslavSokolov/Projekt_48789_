import argparse
import json
import yaml
import xml.etree.ElementTree as ET


def install_components():
    components = [
        "komponent1",
        "komponent2",
        "komponent3",
    ]

    for component in components:
        from pip._internal.utils import subprocess
        subprocess.check_call(["pip", "install", component])


def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd w pliku JSON: {e}")
            return None

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Błąd w pliku YAML: {e}")
            return None

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd w pliku XML: {e}")
        return None

def save_xml(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)


def prs_arguments():
    prse = argparse.ArgumentParser(description='Opis programu')

    prse.add_argument('pathFile1', type=str, help= r"C:\Users\Admin\PycharmProjects\projekt(48789)")
    prse.add_argument('pathFile2', type=str, help= r"C:\Users\Admin\PycharmProjects\projekt(48789)")
    prse.add_argument('-f', '--format', choices=['xml', 'json', 'yml'], help='Format pliku')

    args = prse.parse_args()
    return args


def main():
    args = prs_arguments()
    path_file1 = args.pathFile1
    path_file2 = args.pathFile2
    file_format = args.format

    if file_format == 'json':
        data = load_json(path_file1)
        if data is not None:

            save_json(data, path_file2)

    elif file_format == 'yml':
        data = load_yaml(path_file1)
        if data is not None:

            save_yaml(data, path_file2)

    elif file_format == 'xml':
        root = load_xml(path_file1)
        if root is not None:

            save_xml(root, path_file2)

    else:
        print("Nieznany format pliku.")


if __name__ == '__main__':
    main()

