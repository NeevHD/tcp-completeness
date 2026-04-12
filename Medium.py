from scapy.all import *
import time

# Target details
target = "google.com"   # You can replace with local IP if needed
port = 80

# Medium traffic settings
total = 50              # Number of packets
success = 0             # Successful handshakes counter

print("Starting Medium Traffic Test...")
print("Sending", total, "TCP SYN packets...\n")

for i in range(total):
    
    # Create TCP SYN packet
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    
    # Send packet and receive reply
    reply = sr1(pkt, timeout=2, verbose=0)
    
    # Check if SYN-ACK is received
    if reply and reply.haslayer(TCP) and reply[TCP].flags == "SA":
        success += 1
    
    # Delay to avoid flooding (Medium Traffic)
    time.sleep(0.05)   # 50 milliseconds


# Calculate TCP Completeness
tcp_completeness = (success / total) * 100

print("----------------------------------")
print("Medium Traffic Results")
print("----------------------------------")
print("Total Packets Sent     :", total)
print("Successful Handshakes  :", success)
print("TCP Completeness       :", tcp_completeness, "%")
print("----------------------------------")
