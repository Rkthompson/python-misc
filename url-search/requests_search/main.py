import requests

"""
    Using requests to perfom a duckduckgo search compared to urllib.

    This method offers a level of abstraction where in more details of the
    inner workings of the search are hidden.

"""


def main():
    params = dict(q='bacon', format='json')
    parsed = requests.get('http://api.duckduckgo.com/', params=params).json()

    results = parsed['RelatedTopics']
    for r in results:
        if 'Text' in r:
            print(r['FirstURL'] + ' - ' + r['Text'])


if __name__ == '__main__':
    main()
