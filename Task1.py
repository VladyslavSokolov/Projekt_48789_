import argparse

def prs_arguments():
    prse = argparse.ArgumentParser(description='Opis programu')

    prse.add_argument('pathFile1', type=str, help= r"C:\Users\Admin\PycharmProjects\projekt(48789)")
    prse.add_argument('pathFile2', type=str, help= r"C:\Users\Admin\PycharmProjects\projekt(48789)")
    prse.add_argument('-f', '--format', choices=['xml', 'json', 'yml'], help='Format pliku')

    args = prse.parse_args()
    return args
