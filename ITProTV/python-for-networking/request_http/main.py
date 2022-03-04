
import requests
# import json


def main():
    """
    response = requests.get('https://httpbin.org/get')
    # return <Response [200]>
    print(response)

    # check for an error code on response.  return None
    print(response.raise_for_status())

    # return 200
    print(response.status_code)

    # return the full json response
    print(response.json())
    """
    data = dict(username='JohnDev')
    # application/json "/json" is the content type
    headers = {'Content-Type': 'application/json'}
    response = (
        # requests.post('https://httpbin.org/post', json.dumps(data))
        requests.post('https://httpbin.org/post', data, headers=headers)
    )
    print(response.json())


if __name__ == '__main__':
    main()
