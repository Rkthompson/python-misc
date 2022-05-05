import duckduckgo

"""
    Using duckduckgo module to perfom a duckduckgo search compared to urllib
    and requests.

    This method offers the most levels of abstraction.  Here most details of
    the inner workings of the search are hidden.

"""


def main():
    for r in duckduckgo.query('barcon').results:
        print(r.url + ' - ' + r.text)


if __name__ == '__main__':
    main()
