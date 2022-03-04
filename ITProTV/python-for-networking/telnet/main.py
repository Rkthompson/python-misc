from telnetlib import Telnet
from getpass import getpass


def main():
    host = input('Please enter the host: ')  # IP address
    user = input('Please enter the username: ')  # username
    password = getpass()  # password

    client = Telnet(host)
    client.read_until(b'login: ')
    client.write(user.encode() + b'\n')
    if password:
        client.read_until(b'Password: ')
        client.write(password.encode() + b'\n')

    client.write(b'ls -lah / \n')
    client.write(b'uname -a \n')
    client.write(b'exit \n')
    print(client.read_all().decode())


if __name__ == '__main__':
    main()
