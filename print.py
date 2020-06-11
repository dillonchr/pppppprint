import sys
import math

MAX_PRINT_LEN = 32

def repeat(s, n):
    return "".join([s for _ in range(n)])

def line_of(s = "="):
    return repeat(s, MAX_PRINT_LEN)

def center(s):
    s_len = len(s)
    if s_len <= MAX_PRINT_LEN:
        start = math.floor((MAX_PRINT_LEN - s_len) / 2)
        return repeat(" ", start) + s
    return s

def print_ln(l):
    l = l.strip()
    if len(l) <= MAX_PRINT_LEN:
        return l

    new_l = ""
    current_len = 0
    for w in l.split(" "):
        if current_len + len(w) + 1 < 32:
            new_l = w if len(new_l) < 1 else new_l + " {}".format(w)
            current_len += len(w) + 1
        else:
            new_l += "\n{}".format(w)
            current_len = len(w)
    return new_l


for line in sys.stdin:
    print(print_ln(line))

