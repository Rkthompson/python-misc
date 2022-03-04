
# FTP is not secure.  For live production you should be using import FTP_TLS
from ftplib import FTP


def main():
    host = 'localhost'
    username = 'user_name'
    password = 'user_password'

    # connect to host, default port
    client = FTP(host)

    # user anonymous, passwd anonymous@
    # client.login()

    # login with cred
    client.login(username, password)

    # produce a directory listing as returned by the LIST command,
    # printing it to standard output.
    client.dir()

    # transfer a file as a binary (rb) to the FTP site
    with open('./foods.txt', 'rb') as fp:
        client.storlines("STOR foods.txt", fp)

    # check the directory after transfer
    client.dir()

    # close the connection
    client.quit()


if __name__ == '__main__':
    main()
