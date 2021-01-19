import sys


def numbers_gen(start, stop):
    all_odd = True

    for a in range(start, stop):
        for b in str(a):
            if int(b) % 2 == 0:
                all_odd = False
        if all_odd:
            yield a
        all_odd = True


_start = int(sys.argv[1])
_stop = int(sys.argv[2])
print(list(numbers_gen(_start, _stop)))
