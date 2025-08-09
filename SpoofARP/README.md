# ARP Spoofer for Educational Purposes

This is a simple ARP spoofing tool written in Python using the Scapy library. It performs ARP cache poisoning to intercept network traffic between a target device and a gateway, designed for **educational purposes only** to demonstrate network protocol vulnerabilities on a Linux system. The script requires **root privileges** due to raw socket access and is intended for use in controlled, authorized environments.

> **⚠️ Legal Notice**: ARP spoofing and packet sniffing are illegal in many jurisdictions without explicit consent from all parties involved. This script is provided for **educational purposes only** to study network protocols and security. Ensure you have proper authorization before running this tool. The author is not responsible for any misuse of this software.

## Features
- Performs ARP spoofing to associate the attacker's MAC address with the IP addresses of a target and gateway.
- Uses Scapy to craft and send ARP packets (`is-at` operation).
- Configurable via command-line arguments for network interface, gateway IP, and target IP.
- Continuously sends spoofed ARP packets with a configurable interval (default: 0.2 seconds).
- Stops gracefully on user interrupt (Ctrl+C).

## Requirements
- **Python 3.x**
- **Scapy**: Install via `pip install scapy`
- **Root privileges**: Required for raw socket access to send ARP packets.
- **Linux system**: The script is designed for Linux environments.
- Network interface (e.g., `eth0`, `wlan0`) with connectivity to the target network.

## Installation
1. Clone this repository:
2. Install Scapy:
   ```bash
   pip install scapy
   ```
3. Ensure you have root privileges to run the script (use `sudo`).

## Setup
To enable packet forwarding (required for ARP spoofing to intercept traffic):
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```
This command allows your system to forward packets between the target and gateway, which is necessary for the spoofing to work effectively.

## Usage
Run the ARP spoofing script with root privileges, specifying the network interface, gateway IP, and target IP:
```bash
sudo python3 spoofarp.py -i <interface> <gateway_ip> <target_ip>
```
### Example
To spoof ARP packets between a gateway (`192.168.1.1`) and a target (`192.168.1.100`) on interface `eth0`:
```bash
sudo python3 spoofarp.py -i eth0 192.168.1.1 192.168.1.100
```
- The script will continuously send spoofed ARP packets every 0.2 seconds.
- Press `Ctrl+C` to stop the script.

### Customizing Interval
To adjust the frequency of ARP packets, modify the `time.sleep(0.2)` value in the script (e.g., `time.sleep(1.0)` for 1-second intervals).

## Code Overview
The script (`spoofarp.py`) performs the following:
1. Checks for root privileges to ensure proper execution.
2. Parses command-line arguments for the network interface, gateway IP, and target IP.
3. Crafts two ARP packets:
   - First packet: Associates the attacker's MAC address with the target's IP, sent to the gateway.
   - Second packet: Associates the attacker's MAC address with the gateway's IP, sent to the target.
4. Continuously sends these packets to poison the ARP caches of the target and gateway.
5. Stops on user interrupt (Ctrl+C) with a clean exit.

## Notes
- **Educational Use Only**: This tool is intended for learning about network protocols, ARP, and security vulnerabilities. Do not use it to intercept traffic without explicit permission.
- **Network Impact**: ARP spoofing can disrupt network traffic. Use in a controlled lab environment (e.g., a virtual network or testbed).
- **Customization**: Modify the script to add packet filters, logging, or additional protocols using Scapy’s capabilities.
- **Performance**: Adjust the `time.sleep()` interval to balance performance and reliability based on your network.

## License
This project is licensed under the **GNU General Public License v3.0**. You are free to use, modify, and distribute this software, provided any derivative works are also licensed under the GPL v3. See the [COPYING](COPYING) file for the full license text.

For more details, visit [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).

## Author
Written by Davit Jalagonia (an0n9m).

## Contributing
Contributions are welcome! Please submit a pull request or open an issue on GitHub.
