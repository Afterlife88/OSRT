from __future__ import division

# Series module


max_n = 10000


def get_nth(n):
    return pow(n / (n + 1), pow(n, 2))


def check_limit(e):
    i = 1
    n = e + 1.0
    limits_on = -1

    while abs(n) >= e and i <= max_n:
        n = get_nth(i)
        i += 1

    if abs(n) < e:
        limits_on = i - 1

    return limits_on


def ratio_test(e):
    def divide(i):
        return get_nth(i + 1) / get_nth(i)

    i = 2

    q_n = divide(1)
    q_n_1 = divide(2)

    while abs(q_n_1 - q_n) >= e and abs(1 - q_n_1) >= e and i <= max_n:
        q_n = q_n_1
        q_n_1 = divide(i)
        i +=1

    if i > max_n or abs(1 - q_n_1) < e:
        return 1
    else:
        return q_n_1
