import sys
from typing import List


def test(did_pass : bool):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)

def count_words(ls: List[str]) -> int:
    count = 0
    for word in ls:
        count += 1
        if word == "sam":
            break
            
    return count

test(count_words(["oi", "sam", "como", "vai"]) == 2)
test(count_words(["oi", "san", "como", "vai"]) == 4)
test(count_words(["sam", "vai", "bem"]) == 1)