#!/usr/bin/env python3

#
# Script to collect host IP address and Hostname(local or remote) using module socket
#

import socket

def print_machine_info():
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print ("Hostname: %s"%(host_name))
        print ("IP Address: %s"%(ip_address))

def get_remote_machine_info(remote_host):
    try:
        print("IP address of remote host %s: %s"%(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))


if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info('www.python.org')