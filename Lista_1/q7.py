import sys
from typing import List


def test(did_pass : bool):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)

def sum_of_squares(xs : List[int]) -> int:
    sum : int= 0
    for num in xs:
        sum += num**2
    return sum

test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([ ]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)