# Carlo Pires <carlopires@gmail.com>
# from http://pypi.python.org/pypi/appfy.recipe.gae/0.9.3
# Ter 15 Mar 2011 18:03:35 BRT 

import hashlib
import os

TRUE_VALUES = ('yes', 'true', '1', 'on')

def get_bool_option(option):
    return option.strip().lower() in TRUE_VALUES

def get_checksum(path, hashtype='sha1'):
    if not os.path.isfile(path):
        return None

    func = getattr(hashlib, hashtype)
    checksum = func()

    f = open(path, 'rb')
    try:
        chunk = f.read(2**16)
        while chunk:
            checksum.update(chunk)
            chunk = f.read(2**16)

        return checksum.hexdigest()
    finally:
        f.close()
