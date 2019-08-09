"""Reading keys for de script"""

from ast import literal_eval
FILE = './passwd.txt'


def get_pass(priv_pass):
    """return the key that was asked"""
    with open(FILE, mode='r') as f:
        lines_file = f.read()
        priv_pass = literal_eval(lines_file)[priv_pass]
    return priv_pass


if __name__ == '__main__':
    print(get_pass('cosumer_key'))
