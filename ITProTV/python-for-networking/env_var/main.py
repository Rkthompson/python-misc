import os


def main():
    # lookup an environment variable
    # user = os.environ['USER']
    # user = os.getenv('USER')
    # user = os.environ.get('USER')
    # slug a default value if USER not found
    user = os.environ.get('USER', 'Some Default User Value')

    # print the value of user
    print(user)


if __name__ == '__main__':
    main()
