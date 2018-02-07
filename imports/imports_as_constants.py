from httplib import OK, ACCEPTED


def run(num):
    if num % 2 == 0:
        print OK
    else:
        print ACCEPTED


if __name__ == '__main__':
    map(run, xrange(0, 100000))
