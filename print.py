import sys
import math

MAX_PRINT_LEN = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 32

def repeat(s, n):
    return "".join([s for _ in range(int(n))])

def line_of(s = "="):
    return repeat(s, MAX_PRINT_LEN)[0:MAX_PRINT_LEN - 1]

def center(s):
    s_len = len(s)
    if s_len < MAX_PRINT_LEN:
        start = math.floor((MAX_PRINT_LEN - s_len) / 2)
        return repeat(" ", start) + s
    return s

def banner(s, banner_char = "="):
    s = " {} ".format(s)
    s_len = len(s)
    if s_len < MAX_PRINT_LEN:
        start = math.floor((MAX_PRINT_LEN - s_len) / 2)
        return repeat("=", start) + s + repeat(banner_char, MAX_PRINT_LEN - s_len - start)
    return s

def right_justify(s):
    if len(s) < MAX_PRINT_LEN:
        return repeat(" ", MAX_PRINT_LEN - len(s)) + s
    return s

def space_between(s):
    len_total = len("".join(s))
    if len(s) == 2 and len_total < MAX_PRINT_LEN:
        return repeat(" ", MAX_PRINT_LEN - len_total).join(s)
    elif len(s) == 3 and len_total < MAX_PRINT_LEN:
        first_spaces = round((MAX_PRINT_LEN - len_total) / 2)
        second_spaces = MAX_PRINT_LEN - len_total - first_spaces
        return "{}{}{}{}{}".format(
            s[0],
            repeat(" ", first_spaces),
            s[1],
            repeat(" ", second_spaces),
            s[2]
        )

    return " ".join(s)

def print_ln(l):
    if len(l) <= MAX_PRINT_LEN:
        return l.rstrip()

    has_checkbox = l.startswith("( ) ")
    new_l = ""
    current_len = 0
    for w in l.split(" "):
        if current_len + len(w) + 1 < 32:
            new_l = w if len(new_l) < 1 else new_l + " {}".format(w)
            current_len += len(w) + 1
        else:
            padding = "    " if has_checkbox else ""
            new_l += "\n{}{}".format(padding, w)
            current_len = len(w) + len(padding)
    return new_l.rstrip()

def process_line(l):
    if l.startswith("=>"):
        l = right_justify(l[2:].strip())
    elif l.startswith("<=>"):
        l = center(l[3:].strip())
    elif l.startswith("[=]"):
        l = banner(l[3:].strip())
    elif l.startswith("..."):
        l = line_of(l[3:].strip())
    elif "|=|" in l:
        l = space_between(l.strip().split("|=|"))
    return print_ln(l)


for line in sys.stdin:
    print(process_line(line))

