# -*- coding: utf-8 -*-
"""
Activity 6.7.4: IPv4 Address Subnetting Part 2
Learning Objectives
Upon completion of this activity, you will be able to determine subnet information for a given IP address
and subnetwork mask.
Scenario
When given an IP address, network mask, and subnetwork mask, you will be able to determine other
information about the IP address such as:
• The subnet address of this subnet
• The broadcast address of this subnet
• The range of host addresses for this subnet
• The maximum number of subnets for this subnet mask
• The number of hosts for each subnet
• The number of subnet bits
• The number of this subnet
Task 1: For a Given IP Address and Subnet Mask, Determine Subnet Information.

"""

from networking import *
# lab 6.7.4
print("Activity 6.7.4 - Task 1: For a given IP address/netmask, Determine Network Information")
a = input("Please, input IP address: ")  #"192.168.3.219"
n = input("Kindly, input netwok mask: ")  #"255.255.255.224"
s = input("A subnet mask is also required: ") #"255.255.255.192"

net = get_network_address(a, s)
broad = get_broadcast(net, s)
print("\n", "="*30)
print("Host IP Address: ", a)
print(f"Major Network Netmask: {n} (/{get_prefix(n)})")
print(f"Subnet Netmask: {s} (/{get_prefix(s)})")
print("Major (Base) Network Address:", get_network_address(a, n))
print("Major Network Broadcast Address:",  get_broadcast(net, n))
print("Number of Subnet Bits:",  get_prefix(s)- get_prefix(n))
print("Number of Subnets:", 2 ** (get_prefix(s)- get_prefix(n)))
print("Number of Host Bits per Subnet:", 32 - get_prefix(s))
print("Number of Usable Hosts per Subnet:", 2 ** (32 - get_prefix(s)) - 2)
print("Subnet Address for this IP Address:", net)
print("IP Address of First Host on this Subnet", get_first_IP(net))
print("IP Address of Last Host on this Subnet", get_last_IP(broad))
print("Broadcast Address for this Subnet:", broad)
print("\n", "Happy Networking!")