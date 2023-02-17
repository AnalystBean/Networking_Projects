from scapy.all import *

def packet_sniffer(packet):
    if packet.haslayer(TCP):
        print("[TCP] From: ", packet[IP].src, " to: ", packet[IP].dst)
        print("[TCP] Source Port: ", packet[TCP].sport)
        print("[TCP] Destination Port: ", packet[TCP].dport)
        print("[TCP] Sequence: ", packet[TCP].seq)
        print("[TCP] Acknowledge: ", packet[TCP].ack)
        print("[TCP] Flags: ", packet[TCP].flags)
    elif packet.haslayer(UDP):
        print("[UDP] From: ", packet[IP].src, " to: ", packet[IP].dst)
        print("[UDP] Source Port: ", packet[UDP].sport)
        print("[UDP] Destination Port: ", packet[UDP].dport)
    elif packet.haslayer(ICMP):
        print("[ICMP] From: ", packet[IP].src, " to: ", packet[IP].dst)
    else:
        print("[Other] From: ", packet[IP].src, " to: ", packet[IP].dst)


sniff(filter="ip", prn=packet_sniffer)