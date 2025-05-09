setup.sh - WiFi Evil Twin Emulator Setup Script

Author: Alungal Sinan

Description: Automates environment setup for the Evil Twin WiFi Emulator project.

#!/bin/bash

set -e

echo "[+] Starting setup for WiFi-EvilTwin-Emulator"

Check for root

if [ "$EUID" -ne 0 ]; then echo "[!] Please run as root (sudo ./setup.sh)" exit fi

Update and install dependencies

apt update && apt install -y python3 python3-pip aircrack-ng net-tools git

Install required Python packages

pip3 install -r requirements.txt

Set wireless interface to monitor mode (manual adjustment may be needed)

echo "[+] Available interfaces:" ip link show read -p "Enter your wireless interface (e.g., wlan0): " iface

Kill conflicting processes and enable monitor mode

airmon-ng check kill airmon-ng start $iface

echo "[+] Monitor mode enabled on ${iface}mon" echo "[+] Setup complete. To start the emulator, run:" echo "    python3 main.py"

exit 0

