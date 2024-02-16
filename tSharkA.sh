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
#Step 2: Make the Script Executable

#chmod +x /path/to/your/script.sh
#Step 3: Setup Cronjob for Reboot Execution
#Edit the crontab file for your user with crontab -e and add the following line to execute the script at every reboot:
#@reboot /path/to/your/script.sh
#Important Notes:
#Running as root: The script requires sudo for airmon-ng and tshark. Running it as a cron job under the root user might be necessary.
#Security Concerns: Automatically executing this script at reboot with root privileges poses security risks. Ensure you understand the implications and secure your script accordingly.
#Interface Naming: After enabling monitor mode, the interface name might change (e.g., wlan1 to wlan1mon). You may need to adjust the script accordingly.
#Dependency on GUI: If you specifically need Wireshark's GUI, automating it to start at reboot with a specific task is more complex and may require a desktop environment to be loaded. Consider using tshark for headless setups.
