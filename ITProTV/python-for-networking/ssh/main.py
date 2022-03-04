from paramiko import SSHClient
from paramiko.client import AutoAddPolicy


def main():
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())

        # connect to IP address and authorize via username and password
        client.connect('IP_address_here',
                       username='username_here',
                       password='password_here')

        """
        execute a command on the remote server

        stdin, stdout, and stderr are three data
        streams created in a Linux command

        Streams in Linux—like almost everything else
        —are treated as though they were files
        """

        stdin, stdout, stderr = client.exec_command('ls -l /')

        # read the output of the remote server
        output = stdout.read()

        # display that output
        print(output.decode())


if __name__ == '__main__':
    main()
