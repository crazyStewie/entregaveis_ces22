import sys

def test(did_pass : bool):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} OK.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)

def is_prime(value : int) -> bool:
    for i in range(2, value):
        if not value%i:
            return False
    return True

test(is_prime(11))
test(not is_prime(35))
test(not is_prime(19980912)) # not a prime number (even)
