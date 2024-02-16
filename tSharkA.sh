#!/bin/bash

# Set wlan1 to monitor mode
sudo airmon-ng start wlan1

# The interface might be renamed after enabling monitor mode
# Check the new interface name with airmon-ng or iwconfig, assuming wlan1mon for this example

# Define a variable for the capture file location
CAPTURE_DIR="/var/log/wireshark"
CAPTURE_FILE="$CAPTURE_DIR/$(date +'%Y-%m-%d_%H-%M-%S').pcap"

# Ensure the capture directory exists
mkdir -p "$CAPTURE_DIR"

# Start capturing packets
sudo tshark -i wlan1mon -w "$CAPTURE_FILE" -F pcap
