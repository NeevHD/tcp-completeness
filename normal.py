from scapy.all import *
import time

target = "google.com"
port = 80

total = 10
success = 0

for i in range(total):
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    reply = sr1(pkt, timeout=2, verbose=0)

    if reply and reply.haslayer(TCP) and reply[TCP].flags == "SA":
        success += 1

    time.sleep(0.5)   # delay (no flooding)

print("Normal Traffic TCP Completeness:", (success/total)*100, "%")