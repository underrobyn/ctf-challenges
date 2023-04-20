import sys
import time
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from ping3 import exceptions


def custom_ping(target_ip, payload_size, timeout):
    packet = IP(dst=target_ip) / ICMP() / ('A' * payload_size)
    response = sr1(packet, timeout=timeout, verbose=0)
    return response


def icmp_string_sender(target_ip, message):
    for char in message:
        try:
            # Convert the character to its ASCII value
            ascii_value = ord(char)
            # Send an ICMP ping with the ASCII value as the payload size
            response = custom_ping(target_ip, payload_size=ascii_value, timeout=2)
            if response is not None:
                print(f"Sent '{char}' with payload size {ascii_value}")
            else:
                print(f"Error sending '{char}': Request timed out")
            time.sleep(0.5)  # Add a small delay between pings to avoid flooding
        except (exceptions.PingError, RuntimeError) as e:
            print(f"Error sending '{char}': {e}")


if __name__ == "__main__":
    target_ip = "172.28.65.217"
    message = "Clam Corp is going down. The flag is: flag{35ca4p1ng_v14_p1ng}.."
    icmp_string_sender(target_ip, message)
