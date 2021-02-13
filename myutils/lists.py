import random
import re
from typing import Sequence

import numpy as np


def is_iterable(val):
    """
    Checks if `val` is iterable.


    This method calls `iter(val)`. If an exception is raised, it's not an iterable. 

    This is the 'correct' way, to account for the mess types are in Python.

    For details, see https://stackoverflow.com/a/1952655
    """
    try:
        iter(val)
    except TypeError:
        return False
    return True


def chunks(lst: list, n: int) -> list:
    """
    Splits lst into n chunks.
    
    Taken from Jason Mitchell at https://stackoverflow.com/a/29679492.
    """
    return [list(x) for x in np.array_split(lst, n)]


def scramble(lst: list) -> list:
    """
    Scrambles a list.

    Taken from koffein at https://stackoverflow.com/a/19836008.
    """
    return sorted(lst, key=lambda _: random.random())


def chunks_n(lst: list, n: int) -> list:
    """
    Yield successive n-sized chunks from lst.
    
    Taken from Ned Batchelder at https://stackoverflow.com/a/312464.
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def flatten(list_of_lists: list, exclude: Sequence = (str)) -> list:
    """
    Flatten a list of lists.

    This will also flatten items that are list like, such as strings.

    To exclude them, pass a list of types to `exclude`.

    By default, strings are excluded.

    Taken from Alex Martelli at https://stackoverflow.com/a/952952.
    """
    needs_flattening = lambda item: is_iterable(item) and not isinstance(item, exclude)

    while any(map(needs_flattening, list_of_lists)):
        list_of_lists = flatten_one_level(list_of_lists, exclude=exclude)

    return list_of_lists


def flatten_one_level(list_of_lists: list, exclude: Sequence = (str)) -> list:
    """
    Flatten a list of lists.

    Will only flatten a single level, so entries in output can also be lists.

    This will also flatten items that are list like, such as strings.

    To exclude them, pass a list of types to `exclude`.

    By default, strings are excluded.

    Taken from Alex Martelli at https://stackoverflow.com/a/952952.
    """
    #  Wrap non sequences in list, so we don't have problems later.
    need_wrap = lambda item: isinstance(item, exclude) or not is_iterable(item)
    list_of_lists = [[item] if need_wrap(item) else item for item in list_of_lists]
    return [item for sublist in list_of_lists for item in sublist]

