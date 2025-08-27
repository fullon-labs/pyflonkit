from pyflonkit import _pyflonkit
from .common import check_result

def create_key(old_format=True):
    ret = _pyflonkit.crypto_create_key(old_format)
    return check_result(ret)
