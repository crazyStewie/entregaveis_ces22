import sys
from typing import List


def test(did_pass : bool):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)


def sum_list(ls : List[int]) -> int:
    sum : int= 0
    for num in ls:
        if num%2:
            sum += num
        else:
            break
    return sum

test(sum_list([1, 3, 5, 8, 7]) == 9)
test(sum_list([1, 3, 5, 7]) == 16)
test(sum_list([2, 3, 5, 7]) == 0)