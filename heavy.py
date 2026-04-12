from scapy.all import *
import time

# Target details
target = "google.com"   # You can change to local IP if needed
port = 80

# Heavy traffic settings (NO FLOODING)
total = 200             # Number of packets
success = 0             # Successful handshakes counter

print("Starting Heavy Traffic Test...")
print("Sending", total, "TCP SYN packets...\n")

for i in range(total):
    
    # Create TCP SYN packet
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    
    # Send packet and receive reply
    reply = sr1(pkt, timeout=2, verbose=0)
    
    # Check if SYN-ACK is received
    if reply and reply.haslayer(TCP) and reply[TCP].flags == "SA":
        success += 1
    
    # Small delay to avoid flooding (Heavy Traffic)
    time.sleep(0.01)   # 10 milliseconds


# Calculate TCP Completeness
tcp_completeness = (success / total) * 100

print("----------------------------------")
print("Heavy Traffic Results")
print("----------------------------------")
print("Total Packets Sent     :", total)
print("Successful Handshakes  :", success)
print("TCP Completeness       :", tcp_completeness, "%")
print("----------------------------------")
