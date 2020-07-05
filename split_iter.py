#
# Creates a generator version of split.
# https://stackoverflow.com/a/9770397/2650427
#
import re


def split_iter(string):
    return (x.group(0) for x in re.finditer(r"[A-Za-z']+", string))
