import sys
from typing import Tuple

def test(did_pass : bool):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)

Complex = Tuple[int, int]

def sum_complex(a : Complex, b : Complex) -> Complex:
    return [a[0] + b[0], a[1] + b[1]]

x1 : Complex = [3, 2]
x2 : Complex = [1, 5]
test_sum : Complex = [4, 7]

test(test_sum == sum_complex(x1, x2))
