# -*- coding: utf-8 -*-
"""netmask_broadcast.ipynb
Activity 6.7.3: IPv4 Address Subnetting Part 1
Learning Objectives
Upon completion of this activity, you will be able to determine network information for a given IP address
and network mask.
Background
This activity is designed to teach how to compute network IP address information from a given IP
address.
Scenario
When given an IP address and network mask, you will be able to determine other information about the
IP address such as:
• Network address
• Network broadcast address
• Total number of host bits
• Number of hosts

Task 1: For a given IP address, Determine Network Information.

"""

from networking import *
# lab 6.7.3
print("Activity 6.7.3 - Task 1: For a given IP address/netmask, Determine Network Information")
a = input("Please, input IP address: ")  #"192.168.3.219"
n = input("Kindly, input netwok mask: ")  #"255.255.255.224"

net = get_network_address(a, n)
broad = get_broadcast(net, n)
number = get_number_of_hosts(get_prefix(n))
print("\n", "="*30)
print(f"{a} with netmask {n}/{get_prefix(n)}")
print("Network address:", net)
print("Broadcast address:", broad)
print("Total number of host bits:", 32 - get_prefix(n))
print("Number of hosts:", number)
print("\n", "Happy Networking!")
