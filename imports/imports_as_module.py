import httplib


def run(num):
    if num % 2 == 0:
        print httplib.OK
    else:
        print httplib.ACCEPTED



if __name__ == '__main__':
    map(run, xrange(0, 100000))
