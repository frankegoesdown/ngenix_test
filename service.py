from collections import defaultdict
from functools import partial
import os.path
import random
import string


random_seq = lambda x: random.randint(1, x)

random_text = lambda x: ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(x))


def check_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def dicttree(nesting, leaf_type):
    """
    Returns tree-like structure made of defaultdicts of specified `nesting` with leafs of type `leaf_type`.
    """
    assert nesting > 0
    result = partial(defaultdict, leaf_type)
    for _i in range(nesting - 1):
        result = partial(defaultdict, result)
    return result()
